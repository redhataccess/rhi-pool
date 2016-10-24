import re
import shutil
import tarfile


def get_system_id(machine_id_path, archive_location):
    """ Checking system id from archive """
    tar = tarfile.open(archive_location, 'r')
    tar.extractall()
    machine_id = tar.extractfile(machine_id_path)
    system_id = machine_id.read()
    tar.close()
    return system_id

def replace_bash_version(search_file_path, un_archive_file_location, bash_version, new_bash_version):
    """ For introducing rule, replacing bash version with new bashclea
    version in folder and making modified archive with updated bash version  """
    with open(search_file_path, "r") as search_file, open("tmp.txt", "w")as new_file:
        for line in search_file:
            if "bash" in line:
                line = re.sub(bash_version, new_bash_version, line)
            new_file.write(line)
        shutil.move('tmp.txt', search_file_path)
        with tarfile.open('tarfile_add.tar.gz', mode='w') as new_archive:
            new_archive.add(un_archive_file_location)
