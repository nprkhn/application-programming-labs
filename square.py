import pandas as pd

def CreateSquare(df: pd.DataFrame) -> None:
    """
    Функция, добавляющая в набор данных столбец с площадью

    :df - исходный набор данных
    """
    df['Square'] = 0
    for i in range(len(df['Width'])):
        df.at[i, 'Square'] = df.at[i, 'Width'] * df.at[i, 'Height']

def SquareFilter(df: pd.DataFrame) -> pd.DataFrame:
    """
    Функция, фильтрующая набор данных по площади (от меньшего к большему)

    :df - исходный набор данных
    """
    filtered_df = df.sort_values(by='Square')

    return filtered_df
