import logging
import requests

from models.season import Season
from utils.main_lib import env

class SeasonRepository:
    """
    A repository used to fetch Premier League's seasons data.

    ...

    Methods
    -------
    fetch_season_by_year(cls, year)
        fetch data of a season by year
    """

    @classmethod
    def fetch_season_by_year(cls, year: int) -> Season:
        """
        Parameters
        ----------
        year : int
        	The year of the season to fetch.
        """

        if int(year) not in (2020, 2021, 2022):
            logging.error(
                f"Invalid season year: {year} not in supported range (2020, 2021, 2022). Skiping this year."
            )
            return None

        token = env('FOOTBALL_API_TOKEN')

        url = f"{env('FOOTBALL_API_BASE_URL')}/v4/competitions/PL/matches?season={year}"

        try:
            # Get football stats for the current season
            match_response = requests.get(url, headers={"X-Auth-Token": token})

            if match_response.ok:
                data = match_response.json()

                # Extract matches from the response
                match_list = data['matches']

                # Create a Season object with the data loaded
                season = Season(year, match_list)

                logging.debug(f"Successfully fetched data for the season: {year}.")

                return season

            logging.error(f"{year} season: Error while trying to fetch {url}... {match_response.status_code}")

        except requests.exceptions.Timeout:
            logging.error(f"{year} season: Timeout while trying to fetch {url}... Retrying")
            return cls.fetch_season_by_year(year)

        except requests.exceptions.TooManyRedirects:
            logging.error(f"{year} season: Error while trying to fetch {url}... Too Many Redirects")

        except requests.exceptions.RequestException as exception:
            logging.error(f"{year} season: Error while trying to fetch {url}... {exception.strerror}")

        return None
