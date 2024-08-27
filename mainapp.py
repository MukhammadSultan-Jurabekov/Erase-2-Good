import cv2
import torch
import numpy as np
from lama import Inpainting

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
inpainter = Inpainting(device=device)

