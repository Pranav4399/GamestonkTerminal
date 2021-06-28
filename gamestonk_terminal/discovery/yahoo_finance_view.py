""" Yahoo Finance View """
__docformat__ = "numpy"

import argparse
from typing import List
import pandas as pd
from gamestonk_terminal.helper_funcs import parse_known_args_and_warn


def gainers_view(other_args: List[str]):
    """Prints top N gainers

    Parameters
    ----------
    other_args : List[str]
        argparse other args - ["-n", "20"]
    """

    parser = argparse.ArgumentParser(
        add_help=False,
        prog="gainers",
        description="Print up to 25 top ticker gainers. [Source: Yahoo Finance]",
    )

    parser.add_argument(
        "-n",
        "--num",
        action="store",
        dest="n_gainers",
        type=int,
        default=10,
        choices=range(1, 25),
        help="Number of the top gainers stocks to retrieve.",
    )

    ns_parser = parse_known_args_and_warn(parser, other_args)
    if not ns_parser:
        return

    df_gainers = pd.read_html(
        "https://in.finance.yahoo.com/gainers/"
    )[0]
    print(df_gainers.head(ns_parser.n_gainers).to_string(index=False))
    print("")


def losers_view(other_args: List[str]):
    """Prints top N loosers

    Parameters
    ----------
    other_args : List[str]
        argparse other args - ["-n", "20"]
    """

    parser = argparse.ArgumentParser(
        add_help=False,
        prog="losers",
        description="Print up to 25 top ticker losers. [Source: Yahoo Finance]",
    )

    parser.add_argument(
        "-n",
        "--num",
        action="store",
        dest="n_losers",
        type=int,
        default=10,
        choices=range(1, 25),
        help="Number of the top losers stocks to retrieve.",
    )

    ns_parser = parse_known_args_and_warn(parser, other_args)
    if not ns_parser:
        return

    df_losers = pd.read_html(
        "https://in.finance.yahoo.com/losers"
    )[0]
    print(df_losers.head(ns_parser.n_losers).to_string(index=False))
    print("")
