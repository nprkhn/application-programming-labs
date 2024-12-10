from filter import Filter
from make_df import MakeDataFrame
from input_info import InputInfo
from statistical_info import StatisticalInfo, Sizes
from square import CreateSquare, SquareFilter
from square_hist import Histogram

def main() -> None:
    try:
        df = MakeDataFrame(InputInfo().file)
        Sizes(df)
        CreateSquare(df)
        print(Filter(df, 1500, 1500))
        print(SquareFilter(df))
        StatisticalInfo(df)
        Histogram(df)
    except Exception as exc:
        print(f'Error, {exc}')

if __name__ == '__main__':
    main()
