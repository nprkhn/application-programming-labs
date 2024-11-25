import csv
import os

def Annotation(annotation: str, directory: str) -> None:
    """
    Создаем аннотацию.

    :annotation - путь, по которому будет записываться аннотация
    :directory - директория, в которой находятся изображения
    """
    with open(annotation, 'w', newline='', encoding = 'utf-8') as csvfile:
        fieldnames = ['Relative path', 'Absolute path']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        list_image = os.listdir(directory)
        for image in list_image:
            relative_path = os.path.join(directory, image)
            absolute_path = os.path.abspath(relative_path)
            writer.writerow({'Relative path': relative_path, 'Absolute path': absolute_path})
