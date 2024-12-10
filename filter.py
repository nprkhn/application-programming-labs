import pandas as pd

def Filter(df: pd.DataFrame, max_width: int, max_height: int) -> pd.DataFrame:
    """
    Функция, фильтрующая набор данных по введенным значениям

    :df - исходный набор данных
    :max_width - максимальная ширина
    :max_height - максимальная высота
    """
    filtered_df = df[(df['Width'] <= max_width) & (df['Height'] <= max_height)]

    return filtered_df
