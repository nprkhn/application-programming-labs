from annotation import Annotation
from download import Download
from image_iterator import ImageIterator
from input_info import InputInfo

def main():
    try:
        word = InputInfo().word
        count = InputInfo().count
        destination = InputInfo().destination
        annotation_file = InputInfo().annotation

        Download(word, count, destination)
        Annotation(annotation_file, destination)
        iterator = ImageIterator(destination)
        for image in iterator:
            print(image)
    except:
        print("Invalid parametres")

if __name__ == '__main__':
    main()
