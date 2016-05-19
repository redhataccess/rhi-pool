import hashlib

def create_subset_payload(branch_id, system_ids):
    """
    Create a dictionary representing payload for creating a subset
    :param branch_id:
    :param system_ids:
    :return:
    """
    payload = {
        "hash": get_subset_id(branch_id, system_ids),
        "branch_id": branch_id,
        "machine_ids": system_ids
    }
    return payload

def get_subset_id(branch_id, system_ids):
    """
    Create a subset id to uniquely identify a subset
    :param branch_id:
    :param system_ids:
    :return:
    """
    sha = hashlib.sha1()
    system_ids.sort()
    sha.update(''.join(system_ids))
    s_hash = sha.hexdigest()
    return branch_id + "__" + s_hash