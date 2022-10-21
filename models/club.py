class Club:
    """
    A class used to compute and hold stats for a single club.

    ...

    Attributes
    ----------
    id : int
        the id of the club
    name : string
        the name of the club
    match_won_count : int
        the number of matches match_won_count by the club for a particular season
    match_drawn_count : int
        the number of matches match_drawn_count by the club for a particular season
    match_lost_count : int
        the number of matches match_lost_count by the club for a particular season
    goal_scored_count : int
        the number of goals scored by the club in a particular season
    goal_conceded_count : int
        the number of goals conceded by the club in a particular season

    Methods
    -------
    __win()
        record a new win for the club
    __draw()
        record a draw for the club
    __lose()
        record a loss for the club
    __score(goal_scored_count)
        add number of goals scored by the club in a particular match to
        the total number of goals scored by the club in the season
    __concede(goal_conceded_count)
        add number of goals conceded by the club in a particular match to
        the total number of goals conceded by the club in the season
    record_match(goal_scored_count, goal_conceded_count)
        add match stats to total club stats for season
    """

    def __init__(self, club_id, name) -> None:
        self.club_id = club_id
        self.name = name
        self.match_won_count = 0
        self.match_drawn_count = 0
        self.match_lost_count = 0
        self.goal_scored_count = 0
        self.goal_conceded_count = 0

    def __win(self) -> None:
        """
        record a new win for the club
        """
        self.match_won_count += 1

    def __draw(self) -> None:
        """
        record a new draw for the club
        """
        self.match_drawn_count += 1

    def __lose(self) -> None:
        """
        record a new loss for the club
        """
        self.match_lost_count += 1

    def __score(self, goal_scored_count) -> None:
        """
        Parameters
        ----------
        goal_scored_count : int
            total number of goals scored in a particular match
        """

        self.goal_scored_count += goal_scored_count

    def __concede(self, goal_conceded_count) -> None:
        """
        Parameters
        ----------
        goal_conceded_count : int
            total number of goals conceded in a particular match
        """

        self.goal_conceded_count += goal_conceded_count

    def record_match(self, goal_scored_count, goal_conceded_count) -> None:
        """
        Parameters
        ----------
        goal_scored_count : int
            total number of goals scored in this match
        goal_conceded_count : int
            total number of goals conceded in this match
        """

        if goal_scored_count > goal_conceded_count:
            self.__win()
        elif goal_scored_count < goal_conceded_count:
            self.__lose()
        else:
            self.__draw()

        self.__score(goal_scored_count)
        self.__concede(goal_conceded_count)
