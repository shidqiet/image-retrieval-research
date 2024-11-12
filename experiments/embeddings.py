import torch
import torch.nn as nn
import torchvision.transforms as transforms
from PIL import Image
from scipy.spatial.distance import cosine
from torchvision.models import mobilenet_v3_small

model = mobilenet_v3_small(pretrained=True)
model.classifier = nn.Identity()
model.eval()
model.cpu()

transform = transforms.Compose(
    [
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ]
)


def get_embedding(image_path):
    image = Image.open(image_path).convert("RGB")
    image = transform(image).unsqueeze(0)
    with torch.no_grad():
        embedding = model(image.cpu())
    return embedding.squeeze().numpy()


image_path_1 = "./data/peppers.jpg"
image_path_2 = "./data/peppers.jpg"

embedding1 = get_embedding(image_path_1)
embedding2 = get_embedding(image_path_2)

print(1 - cosine(embedding1, embedding2))
