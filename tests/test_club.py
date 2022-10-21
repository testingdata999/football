
import unittest
import os.path
import sys
from dotenv import load_dotenv
load_dotenv()

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))

from models.premier_league import PremierLeague

class TestingClubStat(unittest.TestCase):
    """
    A test class for number of matches won by Manchester City FC in various seasons
    """

    def test_won_2020(self):
        """
        testing for 2020
        """

        premier_league = PremierLeague([2020])

        filter_data = [
            club for club in premier_league.get_season_list()[0].club_list
            if club.name == "Manchester City FC"]

        if filter_data:
            man_city = filter_data[0]

        self.assertEqual(
            man_city.match_won_count,
            27,
            "The number of matches won by Manchester United in 2020 is not correct"
        )

        self.assertEqual(
            man_city.match_lost_count,
            6,
            "The number of matches lost by Manchester United in 2020 is not correct"
        )

        self.assertEqual(
            man_city.match_drawn_count,
            5,
            "The number of matches drawn by Manchester United in 2020 is not correct"
        )

        self.assertEqual(
            man_city.goal_scored_count,
            83,
            "The number of matches scored by Manchester United in 2020 is not correct"
        )

        self.assertEqual(
            man_city.goal_conceded_count,
            32,
            "The number of matches conceded by Manchester United in 2020 is not correct"
        )

    def test_won_2021(self):
        """
        testing for 2021
        """
        premier_league = PremierLeague([2021])

        filter_data = [
            club for club in premier_league.get_season_list()[0].club_list
            if club.name == "Manchester City FC"]

        if filter_data:
            man_city = filter_data[0]

        self.assertEqual(
            man_city.match_won_count,
            29,
            "The number of matches won by Manchester United in 2021 is not correct"
        )

        self.assertEqual(
            man_city.match_lost_count,
            3,
            "The number of matches lost by Manchester United in 2021 is not correct"
        )

        self.assertEqual(
            man_city.match_drawn_count,
            6,
            "The number of matches drawn by Manchester United in 2021 is not correct"
        )

        self.assertEqual(
            man_city.goal_scored_count,
            99,
            "The number of matches scored by Manchester United in 2021 is not correct"
        )

        self.assertEqual(
            man_city.goal_conceded_count,
            26,
            "The number of matches conceded by Manchester United in 2021 is not correct"
        )


    def test_won_2022(self):
        """
        testing for 2022
        """

        premier_league = PremierLeague([2022])

        filter_data = [club for club in premier_league.get_season_list()[0].club_list if club.name == "Manchester City FC"]

        if filter_data:
            man_city = filter_data[0]

        self.assertEqual(
            man_city.match_won_count,
            7,
            "The number of matches won by Manchester United in 2022 is not correct"
        )

        self.assertEqual(
            man_city.match_lost_count,
            1,
            "The number of matches lost by Manchester United in 2022 is not correct"
        )

        self.assertEqual(
            man_city.match_drawn_count,
            2,
            "The number of matches drawn by Manchester United in 2022 is not correct"
        )

        self.assertEqual(
            man_city.goal_scored_count,
            33,
            "The number of matches scored by Manchester United in 2022 is not correct"
        )

        self.assertEqual(
            man_city.goal_conceded_count,
            10,
            "The number of matches conceded by Manchester United in 2022 is not correct"
        )


if __name__ == '__main__':
    unittest.main()
