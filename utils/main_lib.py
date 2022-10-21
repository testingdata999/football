import os
from argparse import ArgumentParser


def env(key) -> str:
    """
    Get value of an evn variable
    :return: env variable
    """
    return os.getenv(key)


def argparser():
    """
    Parse command line arguments.
    :return: command line arguments
    """

    parser = ArgumentParser()

    parser.add_argument(
        "-s",
        "--season_list",
        required=False,
        type=str,
        help="A list of season years e.g:\"[2020,2021,2022]\"",
        default="[2020,2021,2022]"
    )

    parser.add_argument(
        "-o",
        "--output_dir",
        required=False,
        type=str,
        default=None,
        help="Specify the path of the output directory default = ./data/")

    args = parser.parse_args()
    args.season_list = parse_season_list(args)

    return args


def parse_season_list(args):
    """
    Retrieve season years as a list from argpasser
    :return years: list
    """

    season_list = args.season_list

    season_list = list(map(str, season_list.strip('[]').split(",")))

    return season_list
