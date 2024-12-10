import cv2
import matplotlib.pyplot as plt
import numpy as np


def Histogram(image: np.ndarray) -> list:
    """
    Создаем гистограмму изображения

    :image - считанное изображение в виде многомерного массива
    """
    hist = []

    for i in range(3):
        hist.append(cv2.calcHist([image], [i], mask=None, histSize=[256], ranges=[0,256]))
    
    return hist
    
    

def ShowHistogram(hist) -> None:
    channels = ('b', 'g', 'r')

    plt.figure(figsize=(10,5))
    for i, color in enumerate(channels):
        plt.plot(hist[i], color=color)
    
    plt.title("Hystogram")
    plt.xlabel("Pixel intensity")
    plt.ylabel("Frequency")
    plt.show()
