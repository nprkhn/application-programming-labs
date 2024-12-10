import pandas as pd
import cv2

def Sizes(df: pd.DataFrame) -> None:
    """
    Функция, добавляющая столбцы с размерами изображения

    :df - исходный набор данных
    """
    for i, image in enumerate(df['Relative_path']):
        img = cv2.imread(image)
        sizes = img.shape
        df.at[i, 'Height'] = sizes[0]
        df.at[i, 'Width'] = sizes[1]
        df.at[i, 'Channels'] = sizes[2]

def StatisticalInfo(df: pd.DataFrame) -> None:
    """
    Функция для вывода статистических данных

    :df - исходный набор данных
    """
    print(df[['Height', 'Width', 'Channels']].describe())
