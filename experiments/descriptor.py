import cv2

file_path_1 = "./data/peppers.png"
file_path_2 = "./data/peppers-copy.png"

image1 = cv2.imread(file_path_1, cv2.IMREAD_GRAYSCALE)
image2 = cv2.imread(file_path_2, cv2.IMREAD_GRAYSCALE)

sift = cv2.SIFT_create()
keypoints1, descriptors1 = sift.detectAndCompute(image1, None)
keypoints2, descriptors2 = sift.detectAndCompute(image2, None)

bf = cv2.BFMatcher()
matches = bf.knnMatch(descriptors2, descriptors2, k=2)

good = []
for m, n in matches:
    if m.distance < 0.75 * n.distance:
        good.append([m])

print(good)
