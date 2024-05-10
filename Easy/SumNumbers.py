import hashlib

file_path = 'C:/HSS/Ass2/assignment_2-24-1.pdf'


def compute_hashes(file_path):
    md5_hash = hashlib.md5()
    sha256_hash = hashlib.sha256()

    with open(file_path, "rb") as file:
        for byte_block in iter(lambda: file.read(4096), b""):
            md5_hash.update(byte_block)
            sha256_hash.update(byte_block)

    return md5_hash.hexdigest(), sha256_hash.hexdigest()


md5_result, sha256_result = compute_hashes(file_path)
print(md5_result)
print(sha256_result)

import hmac

shared_key = b"hsscomp716"

def compute_hmac(file_path, key):
    with open(file_path, "rb") as file:
        hmac_obj = hmac.new(key, digestmod=hashlib.sha256)
        for byte_block in iter(lambda: file.read(4096), b""):
            hmac_obj.update(byte_block)
    return hmac_obj.hexdigest()

hmac_result = compute_hmac(file_path, shared_key)
print(hmac_result)




