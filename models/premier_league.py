from repositories.season_repository import SeasonRepository


class PremierLeague:
    """
    A class used to hold the stats for all desired seasons in Premier League.

    ...

    Attributes
    ----------
    __season_list : list<Season>
        a list of Season objects.

    Methods
    -------
    export_season_list_to_csvs()
        write CSV files for all seasons in the format season-{year}.csv
    """

    def __init__(self, year_list) -> None:
        """
        Parameters
        ----------
        year_list : list<int>
            The seasons to analyse.
        """

        self.__season_list = []

        for year in year_list:
            season = SeasonRepository.fetch_season_by_year(year)
            if season is not None:
                self.__season_list.append(season)

    def get_season_list(self) -> list:
        """
        Getter for __season_list
        """
        return self.__season_list


    def export_season_list_to_csvs(self, output_dir) -> None:
        """
        Parameters
        ----------
        output_dir : str
            The output directory
        """

        # For each season call the member function write_csv() to create a CSV file for that season
        for season in self.__season_list:
            season.export_to_csv(output_dir)
