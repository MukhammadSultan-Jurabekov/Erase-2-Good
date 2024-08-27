import cv2
import torch
import numpy as np
from lama import Inpainting

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
inpainter = Inpainting(device=device)

def remove_object(image_path, mask_path, output_path):
    image = cv2.imread(image_path)

    mask = cv2.imread(mask_path, cv2.IMREAD_GRAYSCALE)

    inpainted_image = inpainter(image, mask)

    cv2.imwrite(output_path, inpainted_image)

remove_object('input_image.jpg', 'mask_image.png', 'output_image.jpg')
