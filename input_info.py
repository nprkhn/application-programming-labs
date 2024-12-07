import argparse

def InputInfo():
    """
    Вводим данные через консоль

    :image_path - путь к файлу с изображением
    :result-path - путь к файлу для сохранения результата работы функции FlipImage
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('image_path', type=str, help='image')
    parser.add_argument('result_path', type=str, help='result')
    args = parser.parse_args()

    return args
