from filter import Filter
from make_df import MakeDataFrame
from input_info import InputInfo
from statistical_info import StatisticalInfo
from square import CreateSquare, SquareFilter
from square_hist import Histogram

def main() -> None:
    df = MakeDataFrame(InputInfo().file)
    StatisticalInfo(df)
    CreateSquare(df)
    print(SquareFilter(df))
    Histogram(df)

if __name__ == '__main__':
    main()
