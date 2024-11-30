import numpy as np

def Size(img: np.ndarray):
    """
    Функция вывода размеров изображения

    :img - считанное изображение в виде многомерного массива
    """
    size = img.shape
    print("Size of image:", size)
