import requests
import pytest
from insights.ssh import SSHConnection
from insights.configs import settings
import logging
import re
import unittest2

LOGGER = logging.getLogger('insights_cli')

upload_url = settings.insights_cli.upload_url
archive_file1 = settings.insights_cli.archive_file1
archive_file2 = settings.insights_cli.archive_file2
archive_file3 = settings.insights_cli.archive_file3
archive_file4 = settings.insights_cli.archive_file4
hostname = settings.insights_cli.hostname
username = settings.insights_cli.username
ssh = SSHConnection()
remote_dir_path = '/root/data/' #path for files onn remote machine

@pytest.mark.parametrize("upload_file", [archive_file1,
                                                 archive_file2,
                                                 archive_file3,
                                                 archive_file4
                                        ])

def test_insights_analysis_upload(upload_file):
    """
    Verify if the result count for /upload api end point matches with
    the result count from insights-cli

    """
    rule_ids = [] #rule_ids list will contain all rule_ids from the json response(/uplaod api)
    error_keys = [] #error_keys will contain all error keys from the json response(/upload api)

    with open(upload_file, "rb") as f:
        result = requests.post(upload_url,
                               files = {"file": (upload_file, f,
                            "application/octet-stream")}
                               )

    LOGGER.info("Status code for post request /upload: %s", result.status_code)
    assert result.status_code <= 201
    reports = result.json().get('reports')
    archives = result.json().get('archives')
    LOGGER.debug(type(reports))
    if reports is not None:
        for report in reports:
            rule_ids.append(report['rule_id'].split("|")[0])
            error_keys.append(report.get('details')['error_key'])
    LOGGER.info("Rule ids from 'reports': {0}".format(rule_ids))
    LOGGER.info("Error keys from reports: {0}".format(error_keys))

    # for multi-node sos reports, there are multiple reports under 'archives' whereas for
    # single node sos reports, 'archives' is empty and we require a counter(count =0) to get the total
    # count for rule hits.
    count = 0

    # 'archives' variable above is None for single-node archives
    # eg. test-single-node-archive.tar
    if archives is not None:
        for archive in archives:
            report = archive['reports']
            count += len(report)
            for archive_report in report:
                rule_ids.append(archive_report['rule_id'].split("|")[0])
                error_keys.append(archive_report.get('details')['error_key'])
        LOGGER.info("Result count of reports from 'archives': {0}".format(count))
    LOGGER.info("Result count of reports from 'reports': {0}".format(len(reports)))
    total_count_from_api = count + len(reports)
    LOGGER.info("Total result count: {0}".format(total_count_from_api))

    LOGGER.info("Rule ids from /upload: \n {0} \n".format(rule_ids))
    LOGGER.info("Error keys from /upload: \n {0} \n".format(error_keys))

    rule_ids_count = len(rule_ids)
    error_keys_count = len(error_keys)
    LOGGER.info("Rules ids count: {0}".format(rule_ids_count))
    LOGGER.info("Error keys count: {0}".format(error_keys_count))

    assert rule_ids_count == error_keys_count

    # ssh into the insights-analysis server to run 'insights-cli' command and verify the output
    # with json response from api call
    ssh.get_ssh_instance(hostname, username)
    LOGGER.info(ssh.ssh_client)
    LOGGER.info("Established ssh connection with {0}".format(hostname))

    remote_file = remote_dir_path + upload_file.split('/')[-1]

    ssh.copy_files(upload_file, remote_dir_path, remote_file)
    LOGGER.info("Copied the sos reports from base machine to {0}".format(hostname))
    cmd = 'insights-cli  --plugin-modules telemetry.rules.plugins ' \
          'diag_insights_rules -- {0}'.format(remote_file)
    output = ssh.run(cmd) #run the above cmd on host
    LOGGER.info(type(output))

    # parsing the cli output with regex
    result_count_regex = re.compile('Result count:.*') #regex to match the 'result count' string
    rule_id_regex = re.compile('\w+:\r\n$') #regex to match the rule ids on the cli
    error_key_regex = re.compile('\s+error_key\s+:.*') #regex to match the error key

    total_count = 0 # total number of results/rule hits from the cli output
    result_counts_cli = [] #contains the 'Result count: *' string matches from cli output
    rule_ids_cli = [] #contain the list of rule ids from cli output
    error_keys_cli = [] # contain the list of error keys from cli output

    for i in output:
        rule_id_match = re.match(rule_id_regex, i)
        error_key_match = re.match(error_key_regex, i)
        if rule_id_match is not None:
            rule_id = rule_id_match.group().replace(':\r\n','')
            LOGGER.debug(rule_id)
            rule_ids_cli.append(rule_id)
        if error_key_match is not None:
            error_key = error_key_match.group().split(":")[1].replace('"\r','').\
                replace('"','').replace(' ','')
            LOGGER.debug(error_key)
            error_keys_cli.append(error_key)

        result_count = re.match(result_count_regex, i)
        if result_count is not None:
            result_count = result_count.group()
            result_counts_cli.append(result_count)
            LOGGER.info(result_count)

            number = re.search('\d+', result_count)
            total_count += int(number.group())

    LOGGER.info(result_counts_cli)
    LOGGER.info("Rule hits from cli: {0} \n".format(total_count))
    LOGGER.info("Rule hits from /upload: {0} \n".format(total_count_from_api))
    LOGGER.info("Verifying that the rule hits response from cli matches the "
                "rule hit count from the /upload api response \n")
    assert total_count == total_count_from_api

    LOGGER.info("error key length {0}".format(len(error_keys_cli)))
    LOGGER.info("rules id length {0}".format(len(rule_ids_cli)))
    assert len(error_keys_cli) == len(rule_ids_cli)

    LOGGER.info("Rule ids: \n {0} \n ".format(rule_ids_cli))
    LOGGER.info("Error keys: \n {0} \n ".format(error_keys_cli))
    LOGGER.info("Verifying if the list of rule ids and error keys match from "
                "the api response and cli output")
    assert set(error_keys_cli) == set(error_keys)
    assert set(rule_ids_cli) == set(rule_ids)

    ssh.close()
