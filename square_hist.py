import matplotlib.pyplot as plt
import pandas as pd

def Histogram(df: pd.DataFrame) -> None:
    """
    Функция, создающая гистограмму по площади изображений

    :df - исходный набор данных
    """
    plt.figure(figsize=(15,5))
    plt.hist(df['Square'], bins=40, color='b', alpha=0.7)
    
    plt.title("Histogram")
    plt.xlabel("Square")
    plt.ylabel("Count of images")

    plt.show()
