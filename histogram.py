import cv2
import numpy as np
import matplotlib.pyplot as plt

def Histogram(image: np.ndarray) -> None:
    """
    Создаем гистограмму изображения

    :image - считанное изображение в виде многомерного массива
    """
    channels = ('b', 'g', 'r')

    plt.figure(figsize=(10,5))

    for i, color in enumerate(channels):
        hist = cv2.calcHist([image], [i], mask=None, histSize=[256], ranges=[0,256])
        plt.plot(hist, color=color)
    
    plt.title("Hystogram")
    plt.xlabel("Pixel intensity")
    plt.ylabel("Frequency")
    plt.show()
