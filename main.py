from flip_image import FlipImage, ShowFlipImage
from histogram import Histogram, ShowHistogram
from read_image import ReadImage
from input_info import InputInfo
from save_result import SaveResult
from size import Size

def main() -> None:
    input_info = InputInfo()
    image_path = input_info[0]
    result_path = input_info[1]
    parametr = input_info[2]

    ShowFlipImage(FlipImage(ReadImage(image_path), parametr), ReadImage(image_path))
    ShowHistogram(Histogram(ReadImage(image_path)))
    Size(ReadImage(image_path))
    SaveResult([FlipImage(ReadImage(image_path), parametr)], result_path)

if __name__ == '__main__':
    main()
