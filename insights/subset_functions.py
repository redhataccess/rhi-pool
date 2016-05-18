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

# print json.dumps(create_subset_payload("a7f920d0-991f-11e5-aad6-001a4ac7a427 ",
#                                       [
#                                           "286ef64a-5d9f-49cb-a321-a0b88307dfffff",
#                                           "9186bf73-93c1-4855-9e04-2ce3c9f13125",
#                                           "e388e982-d4ee-43d3-9670-56051b23155b"
#                                       ]
#                                       ))
