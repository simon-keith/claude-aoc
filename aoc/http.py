"""HTTP client for interacting with Advent of Code."""

import os

import requests


class AoCClient:
    """Client for fetching puzzles, inputs, and submitting answers."""

    def __init__(self) -> None:
        """Initialize the client with session cookie from environment.

        Raises:
            ValueError: If AOC_SESSION environment variable is not set

        """
        self.session = os.environ.get("AOC_SESSION")
        if not self.session:
            raise ValueError(
                "AOC_SESSION environment variable not set. "
                "Get your session cookie from adventofcode.com and set it with: "
                "export AOC_SESSION='your_session_cookie'"
            )
        self.headers = {
            "User-Agent": "github.com/simon/claude-aoc by simon@example.com",
        }
        self.cookies = {"session": self.session}
        self.timeout = 30  # 30 second timeout for all requests

    def fetch_puzzle(self, year: int, day: int) -> str:
        """Fetch puzzle HTML.

        Args:
            year: Year of the puzzle
            day: Day of the puzzle (1-25)

        Returns:
            HTML content of the puzzle page

        """
        url = f"https://adventofcode.com/{year}/day/{day}"
        response = requests.get(
            url, headers=self.headers, cookies=self.cookies, timeout=self.timeout
        )
        response.raise_for_status()
        return response.text

    def fetch_input(self, year: int, day: int) -> str:
        """Fetch input data.

        Args:
            year: Year of the puzzle
            day: Day of the puzzle (1-25)

        Returns:
            Input data as text

        """
        url = f"https://adventofcode.com/{year}/day/{day}/input"
        response = requests.get(
            url, headers=self.headers, cookies=self.cookies, timeout=self.timeout
        )
        response.raise_for_status()
        return response.text

    def submit_answer(
        self,
        year: int,
        day: int,
        part: int,
        answer: str | int,
    ) -> str:
        """Submit answer and return response HTML.

        Args:
            year: Year of the puzzle
            day: Day of the puzzle (1-25)
            part: Part number (1 or 2)
            answer: The answer to submit

        Returns:
            HTML response from submission

        """
        url = f"https://adventofcode.com/{year}/day/{day}/answer"
        data = {"level": str(part), "answer": str(answer)}
        response = requests.post(
            url,
            headers=self.headers,
            cookies=self.cookies,
            data=data,
            timeout=self.timeout,
        )
        response.raise_for_status()
        return response.text
