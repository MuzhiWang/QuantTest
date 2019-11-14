import unittest
import pandas as pd
import numpy as np

class TestUtils(unittest.TestCase):

    # @unittest.skip
    def test_df_add_column(self):
        df = pd.DataFrame(np.random.randn(20, 2), columns=['one', 'two']).query('one>0')
        df2 = pd.DataFrame(np.random.randn(20, 2), columns=['one', 'two'])
        df2["three"] = df["one"]
        df3 = pd.DataFrame()
        df3['one'] = df['one']
        df3['two'] = df2['one']
        print(df2)
        print(df3.to_string())
        df4 = df2.fillna(method='ffill')
        print(df4.to_string())

    def test_df_merge_and_add_columns_with_time_as_index(self):
        df = pd.DataFrame({'A': range(10, 20), 'B': range(30, 40), 222: range(50, 60)})
        df = df.set_index('A')
        print(df.to_string())

        df2 = pd.DataFrame({'A': range(15, 20), 'E': range(30, 35), 'F': range(50, 55)})
        df2 = df2.set_index('A')
        df2['D'] = df['B']
        print(df2.to_string())

        # df3 = df2.copy(deep=True)
        df3 = df.merge(df2, how='left', left_index=True, right_index=True)
        print(df3.to_string())

        df4 = df.merge(pd.DataFrame(), how='left', left_index=True, right_index=True)
        print(df4.to_string())

        df5 = df3.copy(deep=True)
        df5['score'] = df3.apply(lambda row: TestUtils.__get_ed_score(row), axis=1)
        print(df5.to_string())

        df6 = pd.DataFrame()
        df2 = df2.reset_index('A')
        df6['indexxx'] = df2['A']
        print(df6.to_string())

    @staticmethod
    def __get_ed_score(row):
        count = len(row) - row.isnull().sum()
        print(f"row's count: {count}")
        print(f"row's sum: {row.sum()}")
        return row.sum() / count


if __name__ == '__main__':
    unittest.main()
