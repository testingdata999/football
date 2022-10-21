import os.path
import sys
import unittest
from dotenv import load_dotenv
load_dotenv()

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))

from models.premier_league import PremierLeague

class TestingSeason(unittest.TestCase):
    """
    a test class for clubs that played in each seasons
    """

    def test_2020_clubs(self):
        """
        testing for the 2020 season
        """

        clubs_2020 = ['Manchester City FC',
                      'Manchester United FC',
                      'Liverpool FC',
                      'Leicester City FC',
                      'West Ham United FC',
                      'Chelsea FC',
                      'Arsenal FC',
                      'Leeds United FC',
                      'Tottenham Hotspur FC',
                      'Everton FC',
                      'Aston Villa FC',
                      'Crystal Palace FC',
                      'Southampton FC',
                      'Newcastle United FC',
                      'Wolverhampton Wanderers FC',
                      'Burnley FC',
                      'Brighton & Hove Albion FC',
                      'Sheffield United FC',
                      'Fulham FC',
                      'West Bromwich Albion FC']

        premier_league = PremierLeague([2020])

        club_list = [club.name for club in premier_league.get_season_list()[0].club_list]

        for club_name in club_list:
            self.assertIn(
                club_name,
                clubs_2020,
                f"{club_name} did not play the premier league in 2020"
            )

    def test_2021(self):
        """
        testing for the 2021 season
        """

        clubs_2021 = ['Manchester City FC', 'Liverpool FC', 'Arsenal FC', 'Tottenham Hotspur FC',
                      'Chelsea FC', 'Manchester United FC', 'West Ham United FC',
                      'Wolverhampton Wanderers FC', 'Leicester City FC', 'Brentford FC',
                      'Aston Villa FC', 'Newcastle United FC', 'Brighton & Hove Albion FC',
                      'Everton FC', 'Crystal Palace FC', 'Leeds United FC', 'Southampton FC',
                      'Burnley FC', 'Watford FC', 'Norwich City FC']

        premier_league = PremierLeague([2021])

        club_list = [club.name for club in premier_league.get_season_list()[0].club_list]

        for club_name in club_list:
            self.assertIn(
                club_name,
                clubs_2021,
                f"{club_name} did not play the premier league in 2021")

    def test_2022(self):
        """
        testing for the 2022 season
        """

        clubs_2022 = ['Arsenal FC', 'Tottenham Hotspur FC', 'Manchester City FC', 'Chelsea FC',
                      'Manchester United FC', 'Liverpool FC', 'Newcastle United FC',
                      'Brighton & Hove Albion FC', 'Crystal Palace FC', 'Fulham FC',
                      'Southampton FC', 'AFC Bournemouth', 'Brentford FC', 'West Ham United FC',
                      'Leeds United FC', 'Wolverhampton Wanderers FC', 'Aston Villa FC',
                      'Everton FC', 'Nottingham Forest FC', 'Leicester City FC']

        premier_league = PremierLeague([2022])

        club_list = [club.name for club in premier_league.get_season_list()[0].club_list]

        for club_name in club_list:
            self.assertIn(
                club_name,
                clubs_2022,
                f"{club_name} did not play the premier league in 2022")


if __name__ == '__main__':
    unittest.main()
