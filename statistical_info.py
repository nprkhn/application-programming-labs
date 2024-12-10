import pandas as pd
import cv2

def StatisticalInfo(df: pd.DataFrame) -> None:
    """
    Функция, добавляющая статистические данные в соответствующие столбцы

    :df - исходный набор данных
    """
    for i, image in enumerate(df['Relative path']):
        img = cv2.imread(image)
        sizes = img.shape
        df.at[i, 'Height'] = sizes[0]
        df.at[i, 'Width'] = sizes[1]
        df.at[i, 'Channels'] = sizes[2]
