from read_image import ReadImage
from histogram import Histogram
from flip_image import FlipImage
from save_result import SaveResult
from input_info import InputInfo
from size import Size

def main() -> None:
    image_path = InputInfo().image_path
    result_path = InputInfo().result_path
    SaveResult(FlipImage((ReadImage(image_path))), result_path)
    Histogram(ReadImage(image_path))
    Size(ReadImage(image_path))

if __name__ == '__main__':
    main()
