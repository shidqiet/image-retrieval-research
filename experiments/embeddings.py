import torch
import torch.nn as nn
from PIL import Image
from scipy.spatial.distance import cosine
from torchvision import models

model = models.mobilenet_v3_small(weights=models.MobileNet_V3_Small_Weights.DEFAULT)
model.classifier = nn.Identity()
model.eval()
model.cpu()

transform = models.MobileNet_V3_Small_Weights.DEFAULT.transforms()


def get_embedding(image_path):
    image = Image.open(image_path).convert("RGB")
    image = transform(image).unsqueeze(0)
    with torch.no_grad():
        embedding = model(image.cpu())
    return embedding.squeeze().numpy()


image_path_1 = "./data/peppers.png"
image_path_2 = "./data/peppers.png"

embedding1 = get_embedding(image_path_1)
embedding2 = get_embedding(image_path_2)

print(1 - cosine(embedding1, embedding2))
