import cv2
import numpy as np
import matplotlib.pyplot as plt

def FlipImage(image: np.ndarray) -> tuple:
    """
    Отображаем изображение относительно различных осей

    :image - считанное изображение в виде многомерного массива
    """
    flip_horizontal = cv2.flip(image, 1)
    flip_vertical = cv2.flip(image, 0)
    flip_both = cv2.flip(image, -1)

    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    flip_horizontal_rgb = cv2.cvtColor(flip_horizontal, cv2.COLOR_BGR2RGB)
    flip_vertical_rgb = cv2.cvtColor(flip_vertical, cv2.COLOR_BGR2RGB)
    flip_both_rgb = cv2.cvtColor(flip_both, cv2.COLOR_BGR2RGB)

    plt.figure(figsize=(12,8))

    plt.subplot(2,2,1)
    plt.imshow(image_rgb)
    plt.title("Original")
    plt.axis('off')
    
    plt.subplot(2,2,2)
    plt.imshow(flip_horizontal_rgb)
    plt.title("Horizontal flip")
    plt.axis('off')

    plt.subplot(2,2,3)
    plt.imshow(flip_vertical_rgb)
    plt.title("Vertical flip")
    plt.axis('off')

    plt.subplot(2,2,4)
    plt.imshow(flip_both_rgb)
    plt.title("Both flip")
    plt.axis('off')

    plt.show()

    return [flip_horizontal, flip_vertical, flip_both]
