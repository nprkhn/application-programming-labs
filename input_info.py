import argparse

def InputInfo():
    """
    Функция, считывающая данные, введенные через консоль
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('file', type=str, help='File')
    args = parser.parse_args()

    return args
