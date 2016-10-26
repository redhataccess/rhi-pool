import re
import shutil
import tarfile


def get_system_id(archive_location):
    """ Checking machine id Path from archive """
    tar = tarfile.open(archive_location, 'r')
    tar.extractall()
    names = tar.getnames()
    matchine_id_string = [s for s in names if "machine-id" in str(s)]
    machine_id_path = matchine_id_string[0]
    machine_id = tar.extractfile(machine_id_path)
    """ Checking system id from archive """
    system_id = machine_id.read()
    tar.close()
    return system_id


def get_file_path(archive_location):
    """ Checking file Path from archive """
    file_name = "rpm_-qa_--qf_NAME_-_VERSION_-_RELEASE_._ARCH_INSTALLTIME_date_BUILDTIME_" \
                "RSAHEADER_pgpsig_DSAHEADER_pgpsig"
    tar = tarfile.open(archive_location, 'r')
    tar.extractall()
    names = tar.getnames()
    search_path_in_archive = [s for s in names if file_name in str(s)]
    search_file_path = search_path_in_archive[0]
    tar.close()
    return search_file_path


def replace_bash_version(un_archive_file_location, new_bash_version, archive_location):
    """ For introducing rule, replacing bash version with new bash
    version in folder and making modified archive with updated bash version  """

    file_path = get_file_path(archive_location)
    with open(file_path, "r") as search_file, open("tmp.txt", "w")as new_file:
        for line in search_file:
            if "bash" in line:
                """ Checking bash_version from archive """
                bash_version = line.split()[0]
                line = re.sub(bash_version, new_bash_version, line)
            new_file.write(line)
        shutil.move('tmp.txt', file_path)
        with tarfile.open('tarfile_add.tar.gz', mode='w') as new_archive:
            new_archive.add(un_archive_file_location)
