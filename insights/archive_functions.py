import shutil
import tarfile
import tempfile


def get_system_id(archive_location):
    """ Checking machine id Path from archive """
    try:
        tmp_dir = tempfile.mkdtemp()
        tar = tarfile.open(archive_location, 'r')
        tar.extractall(tmp_dir)
        names = tar.getnames()
        matchine_id_string = [s for s in names if "machine-id" in str(s)]
        machine_id_path = matchine_id_string[0]
        machine_id = tar.extractfile(machine_id_path)
        """ Checking system id from archive """
        system_id = machine_id.read()
    finally:
        shutil.rmtree(tmp_dir)
    tar.close()
    return system_id


