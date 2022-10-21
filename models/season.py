import csv
import logging
import os
from models.club import Club
from utils.contants import HEADER_TITLE_CLUB, HEADER_TITLE_GAMES_DRAWN, HEADER_TITLE_GAMES_LOST, HEADER_TITLE_GAMES_WON, HEADER_TITLE_GOALS_CONCEDED, HEADER_TITLE_GOALS_SCORED


class Season:
    """
    A class used to extract and hold stats for a single season.

    ...

    Attributes
    ----------
    year : int
        the season year
    club_list : list<Club>
        a list of clubs that played in this season
    csv_header_list : list<str>
        a tuple holding the CSV column names

    Methods
    -------
    __extract_stats(match_list)
        extract clubs performances for the current season
    __add_match_stats_to_club(clubId, clubName, scored, conceded)
        add single match perfomance to the general club stats
    export_to_csv()
        create a CSV file with stats for this season
    """

    def __init__(self, year, match_list) -> None:
        """
        Parameters
        ----------
        year : int
            the season year
        match_list : list
            data of matches played in this season
        """

        self.year = year
        self.club_list = []

        self.csv_header_list = (
            HEADER_TITLE_CLUB,
            HEADER_TITLE_GAMES_WON,
            HEADER_TITLE_GAMES_DRAWN,
            HEADER_TITLE_GAMES_LOST,
            HEADER_TITLE_GOALS_SCORED,
            HEADER_TITLE_GOALS_CONCEDED
        )

        self.__extract_stats(match_list)

    def __extract_stats(self, match_list) -> None:
        """
        Parameters
        ----------
        match_list : list
            data of matches played in this season
        """

        # loop through matches and extract data for home team away team and score
        for match in match_list:
            home_team = match['homeTeam']
            away_team = match['awayTeam']
            score = match['score']

            # goals scored by home team
            home_team_score = score['fullTime']['home']

            # goals scored by away team
            away_team_score = score['fullTime']['away']

            # Add match data for the home team to the club stats
            self.__add_match_stats_to_club(
                home_team['id'], home_team['name'], home_team_score, away_team_score)

            # Add match data for the away team to the club stats
            self.__add_match_stats_to_club(
                away_team['id'], away_team['name'], away_team_score, home_team_score)

    def __add_match_stats_to_club(self, club_id, club_name, goal_scored_count, goal_conceded_count) -> None:
        """
        Parameters
        ----------
        club_id : int
            the ID of the club
        club_name : string
            the name of the blub
        goal_scored_count : int
            the total number of goals scored by the club in this match
        goal_conceded_count : int
            the total nubmer of goals conceded by the club in this match
        """

        # filter clubs list to find out if this club has already been added to list
        matching_club_list = [
            club for club in self.club_list if club.club_id == club_id]

        # check if club already exists in list
        if len(matching_club_list) > 0:
            # if the club already exists, save it in variable club
            club = matching_club_list[0]
        else:
            # if the club doens't exists yet, create an instance of Club and append it clubs
            club = Club(club_id, club_name)
            self.club_list.append(club)

        if goal_scored_count is not None and goal_conceded_count is not None:
            # If the match has been played, record the club perfomance for this match
            club.record_match(goal_scored_count, goal_conceded_count)

    def export_to_csv(self, output_dir) -> None:
        """
        create a CSV file with stats for this season
        """

        default_output_dir = os.getenv('DEFAULT_OUTPUT_DIR')
        if not os.path.exists(default_output_dir):
            os.makedirs(default_output_dir)


        file_name = os.path.join(default_output_dir, f"season-{self.year}.csv")

        if output_dir is not None:
            if not os.path.exists(output_dir):
                os.makedirs(output_dir)
            file_name = os.path.join(output_dir, f'season-{self.year}.csv')

        with open(file_name, 'w', encoding='UTF8') as file:
            writer = csv.DictWriter(
                file, delimiter=',', fieldnames=self.csv_header_list)

            # write the csv header row
            writer.writeheader()

            # sort clubs by number of matches won
            self.club_list.sort(key=lambda club: club.match_won_count, reverse=True)

            for club in self.club_list:
                # write a row to the csv file
                writer.writerow({
                    HEADER_TITLE_CLUB: club.name,
                    HEADER_TITLE_GAMES_WON: club.match_won_count,
                    HEADER_TITLE_GAMES_DRAWN: club.match_drawn_count,
                    HEADER_TITLE_GAMES_LOST: club.match_lost_count,
                    HEADER_TITLE_GOALS_SCORED: club.goal_scored_count,
                    HEADER_TITLE_GOALS_CONCEDED: club.goal_conceded_count
                })

            logging.debug(f"Successfully created the file: {file_name}.")
