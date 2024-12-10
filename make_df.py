import pandas as pd

def MakeDataFrame(file: str) -> pd.DataFrame:
    """
    Функция, создающая набор данных(DataFrame)

    :file - путь к файлу, по которому будет создан DataFrame
    """
    df = pd.read_csv(file, header=0)
    df = df.rename(columns={'Relative path': 'Relative_path', 'Absolute path': 'Absolute_path'})
    df['Height'] = 0
    df['Width'] = 0
    df['Channels'] = 0

    return df
