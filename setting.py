"""Options"""
import argparse
from dataclasses import dataclass


@dataclass
class ProgramArgs:
    """For type hint"""
    asset_path: str
    result_path: str
    screenshot_path: str
    login_url: str
    post_limit: int


class Options:
    """Initialize the arguments"""
    @staticmethod
    def initialize(parser: argparse.ArgumentParser) -> argparse.ArgumentParser:
        parser.add_argument("--asset_path", type=str, default="./asset/",
                            help="path of credential and target urls")
        parser.add_argument("--result_path", type=str, default="./result/",
                            help="path of result")
        parser.add_argument("--screenshot_path", type=str,
                            default="./result/screenshot/",
                            help="path of screenshot")
        parser.add_argument("--login_url", type=str,
                            default="https://mobile.facebook.com/login",
                            help="login url")
        parser.add_argument("--post_limit", type=int, default=10,
                            help="number of posts to be retrieved")

        return parser

    def parse(self) -> ProgramArgs:
        description = "Facebook page crawler"
        parser = argparse.ArgumentParser(description=description)
        parser = self.initialize(parser)
        namespace = parser.parse_args()
        return ProgramArgs(**vars(namespace))
