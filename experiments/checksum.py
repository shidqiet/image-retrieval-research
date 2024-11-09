import hashlib


def hash_file_md5(file_path: str) -> str:
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


def hash_file_sha256(file_path: str) -> str:
    hash_sha256 = hashlib.sha256()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_sha256.update(chunk)
    return hash_sha256.hexdigest()


file_path_1 = "./data/peppers.png"
file_path_2 = "./data/peppers-copy.png"
file_path_3 = "./data/peppers-low-contrast.png"
file_path_4 = "./data/not-peppers.png"

print(hash_file_md5(file_path_1) == hash_file_md5(file_path_2))
print(hash_file_sha256(file_path_1) == hash_file_sha256(file_path_2))
print()

print(hash_file_md5(file_path_1) == hash_file_md5(file_path_3))
print(hash_file_sha256(file_path_1) == hash_file_sha256(file_path_3))
print()

print(hash_file_md5(file_path_1) == hash_file_md5(file_path_4))
print(hash_file_sha256(file_path_1) == hash_file_sha256(file_path_4))
