import cv2
import matplotlib.pyplot as plt
import numpy as np


def FlipImage(image: np.ndarray, param: int) -> np.ndarray:
    """
    Отображаем изображение относительно различных осей

    :image - считанное изображение в виде многомерного массива
    """
    flip_image = cv2.flip(image, param)

    return flip_image

def ShowFlipImage(flip_image: np.ndarray, original: np.ndarray) -> None:
    image_rgb = cv2.cvtColor(original, cv2.COLOR_BGR2RGB)
    flip_image_rgb = cv2.cvtColor(flip_image, cv2.COLOR_BGR2RGB)

    plt.figure(figsize=(12,8))

    plt.subplot(1,2,1)
    plt.imshow(image_rgb)
    plt.title("Original")
    plt.axis('off')
    
    plt.subplot(1,2,2)
    plt.imshow(flip_image_rgb)
    plt.title("Flipped image")
    plt.axis('off')

    plt.show()
