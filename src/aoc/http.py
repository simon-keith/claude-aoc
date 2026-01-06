"""HTTP client for interacting with Advent of Code."""

import os

import requests


class AoCClient:
    """Client for fetching puzzles, inputs, and submitting answers."""

    def __init__(self) -> None:
        """Initialize the client with session cookie."""
        # User's session cookie (fallback to env var if set)
        self.session = os.environ.get(
            "AOC_SESSION",
            "53616c7465645f5ff08e9d3be1bff143afa69b86a603a80b0f31d11da49204349d802958358b87ea910b02347ceafc4c55cd9f3e39dace82270c1696ce6d52a3",
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
