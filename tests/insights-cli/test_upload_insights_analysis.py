import requests
import pytest
from insights.ssh import SSHConnection
from insights.configs import settings
import logging

LOGGER = logging.getLogger('insights_cli')

upload_url = settings.insights_cli.upload_url
archive_file1 = settings.insights_cli.archive_file1
archive_file2 = settings.insights_cli.archive_file2
archive_file3 = settings.insights_cli.archive_file3
archive_file4 = settings.insights_cli.archive_file4
hostname = settings.insights_cli.hostname
username = settings.insights_cli.username
rule_ids = []
ssh = SSHConnection()

@pytest.mark.parametrize("upload_file", [archive_file1,
                                               archive_file2,
                                               archive_file3,
                                               archive_file4])


def test_insights_analysis_upload(upload_file):
    """
    Test the response of /upload api end point from insights-
    analysis server
    :return:
    """
    with open(upload_file, "rb") as f1:
        result = requests.post(upload_url,
                               files = {"file": (upload_file, f1,
                            "application/octet-stream")}
                               )
    LOGGER.info("Status code: %s", result.status_code)
    assert result.status_code <= 201
    reports = result.json().get('reports')
    print len(reports)

    for report in reports:
        rule_ids.append(report['rule_id'])
    LOGGER.info(rule_ids)
