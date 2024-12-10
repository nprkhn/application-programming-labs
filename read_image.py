import cv2
import numpy as np

def ReadImage(file: str) -> np.ndarray:
    """
    Считываем изображение

    :file - путь к файлу с изображением
    """
    img = cv2.imread(file)

    return img
