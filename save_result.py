import cv2
import numpy as np

def SaveResult(res: list[np.ndarray], file: str) -> None:
    """
    Сохраняем получившийся результат функции FlipImage

    :res - кортеж с отраженными относительно различных осей изображениями
    :file - путь к файлу для сохранения результата
    """
    if len(res) == 1:
        cv2.imwrite(file, res[0])
        return

    result = cv2.hconcat(res)

    cv2.imwrite(file, result)
