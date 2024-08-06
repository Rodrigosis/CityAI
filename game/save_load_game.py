import json

from game import Game


def save_game_to_json(game: Game, filename: str):
    with open(filename, 'w') as f:
        json.dump(game.to_dict(), f, indent=4)


def load_game_from_json(filename: str) -> Game:
    with open(filename, 'r') as f:
        data = json.load(f)
        return Game.from_dict(data)
