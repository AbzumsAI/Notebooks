from __future__ import annotations

import json
from typing import Callable, Any
from urllib import request

JsonData = dict[str, Any]
PostFunc = Callable[[str, JsonData], JsonData]


def default_post(url: str, payload: JsonData) -> JsonData:
    data = json.dumps(payload).encode("utf-8")
    req = request.Request(url, data=data, headers={"Content-Type": "application/json"}, method="POST")
    with request.urlopen(req, timeout=10) as response:
        return json.loads(response.read().decode("utf-8"))


class MastermindClient:
    def __init__(self, base_url: str = "https://mastermind.darkube.app", post: PostFunc = default_post) -> None:
        self.base_url = base_url.rstrip("/")
        self.post = post
        self.game_id: str | None = None

    def start_game(self) -> str:
        data = self.post(f"{self.base_url}/api/game/start", {})
        game_id = str(data.get("game_id") or data.get("id") or "")
        if not game_id:
            raise ValueError("API response did not include a game id")
        self.game_id = game_id
        return game_id

    def send_guess(self, guess: str) -> JsonData:
        if self.game_id is None:
            raise ValueError("Start a game before sending a guess")
        if len(guess) != 4 or not guess.isdigit():
            raise ValueError("Guess must be four digits")
        return self.post(f"{self.base_url}/api/game/guess", {"game_id": self.game_id, "guess": guess})


def prompt_guess(raw_value: str) -> str:
    guess = raw_value.strip()
    if len(guess) != 4 or not guess.isdigit():
        raise ValueError("Enter exactly four digits")
    return guess


def run_sample_game(client: MastermindClient, guesses: list[str]) -> list[JsonData]:
    if client.game_id is None:
        client.start_game()
    results = []
    for raw_guess in guesses:
        results.append(client.send_guess(prompt_guess(raw_guess)))
    return results


def fake_post(url: str, payload: JsonData) -> JsonData:
    if url.endswith("/start"):
        return {"game_id": "demo-game"}
    return {"black": 4, "white": 0, "guess": payload["guess"], "status": "won"}


def demo() -> list[JsonData]:
    client = MastermindClient(post=fake_post)
    return run_sample_game(client, ["1234"])


if __name__ == "__main__":
    print(demo())
