from pathlib import Path
import unittest
import os.path
import sys

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))

from main import run

class TestingCSVs(unittest.TestCase):
    """
    a class to test the creation of csv files
    """

    def test_2020(self) -> None:
        """
        Test if a file was created for the 2020 season
        """

        csv2020 = Path("data/season-2020.csv")

        self.assertEqual(
            csv2020.is_file(),
            True,
            "CSV for the 2020 season was not created"
        )

    def test_2021(self) -> None:
        """
        Test if a file was created for the 2021 season
        """

        csv2021 = Path("data/season-2021.csv")

        self.assertEqual(
            csv2021.is_file(),
            True,
            "CSV for the 2021 season was not created"
        )

    def test_2022(self) -> None:
        """
        Test if a file was created for the 2022 season
        """

        csv2022 = Path("data/season-2022.csv")

        self.assertEqual(
            csv2022.is_file(),
            True,
            "CSV for the 2022 season was not created"
        )


if __name__ == '__main__':
    run()
    unittest.main()
