import imagehash
from PIL import Image

file_path_1 = "./data/peppers.png"
file_path_2 = "./data/peppers-copy.png"
file_path_3 = "./data/peppers-low-contrast.png"
file_path_4 = "./data/not-peppers.png"

avg_hash_1 = imagehash.average_hash(Image.open(file_path_1))
avg_hash_2 = imagehash.average_hash(Image.open(file_path_2))
avg_hash_3 = imagehash.average_hash(Image.open(file_path_3))
avg_hash_4 = imagehash.average_hash(Image.open(file_path_4))

print(avg_hash_1 == avg_hash_2)
print(avg_hash_1 - avg_hash_2)  # hamming distance
print()

print(avg_hash_1 == avg_hash_3)
print(avg_hash_1 - avg_hash_3)  # hamming distance
print()

print(avg_hash_1 == avg_hash_4)
print(avg_hash_1 - avg_hash_4)  # hamming distance
