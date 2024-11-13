import unittest
import pandas as pd

from solution import cut_chunck

class TestSolution(unittest.TestCase):
    def test_add(self):
        df = pd.DataFrame({"dt": [
            '2023-01-01 00:00:01',
            '2023-01-01 00:00:01',
            '2023-01-01 00:00:02',
            '2023-01-01 00:00:02',
            '2023-01-01 00:00:02',
            '2023-01-01 00:00:03'
        ]})

        list_df = list((
             pd.DataFrame({"dt": [
            '2023-01-01 00:00:01',
            '2023-01-01 00:00:01']}),
            pd.DataFrame({"dt": [
            '2023-01-01 00:00:02',
            '2023-01-01 00:00:02',
            '2023-01-01 00:00:02']}),
            pd.DataFrame({"dt": ['2023-01-01 00:00:03']}))
        )

        new_list_df = cut_chunck(df, 2)
        for i in range(len(new_list_df)):
            pd.testing.assert_frame_equal(new_list_df[i].reset_index(drop=True), list_df[i].reset_index(drop=True))


if __name__ == '__main__':
        unittest.main()