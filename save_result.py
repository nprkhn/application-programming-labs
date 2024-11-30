import cv2

def SaveResult(res: tuple, file: str) -> None:
    """
    Сохраняем получившийся результат функции FlipImage

    :res - кортеж с отраженными относительно различных осей изображениями
    :file - путь к файлу для сохранения результата
    """
    result = cv2.hconcat(res)

    cv2.imwrite(file, result)
