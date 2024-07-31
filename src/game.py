import json
from typing import List, Dict
from scripts.characters import NewCharacter
from scripts.world import NewWorld


class Game:

    def __init__(self, main_character: NewCharacter = NewCharacter(), 
                 secondary_characters: List[NewCharacter] = [], 
                 random_characters: List[NewCharacter] = [], 
                 main_world: NewWorld = NewWorld(),
                 other_worlds: List[NewWorld] = []):
        self.main_character = main_character
        self.secondary_characters = secondary_characters
        self.random_characters = random_characters
        self.main_world = main_world
        self.other_worlds = other_worlds
    
    def __repr__(self) -> str:
        return str(self.to_dict())

    def to_dict(self) -> Dict:
        list_secondary_characters = [i.to_dict() for i in self.secondary_characters]
        list_random_characters = [i.to_dict() for i in self.random_characters]
        list_other_worlds = [i.to_dict() for i in self.other_worlds]
        return {
            "main_character": self.main_character.to_dict(),
            "secondary_characters": list_secondary_characters,
            "random_characters": list_random_characters,
            "main_world": self.main_world.to_dict(),
            "other_worlds": list_other_worlds
        }
    
    @classmethod
    def from_dict(cls, data):
        list_secondary_characters = [NewCharacter.from_dict(i) for i in data['secondary_characters']]
        list_random_characters = [NewCharacter.from_dict(i) for i in data['random_characters']]
        list_other_worlds = [NewWorld.from_dict(i) for i in data['other_worlds']]
        return cls(
            main_character=NewCharacter.from_dict(data["main_character"]),
            secondary_characters=list_secondary_characters,
            random_characters=list_random_characters,
            main_world=NewWorld.from_dict(data["main_world"]),
            other_worlds=list_other_worlds
        )


def save_game_to_json(game: Game, filename: str):
    with open(filename, 'w') as f:
        json.dump(game.to_dict(), f, indent=4)


def load_game_from_json(filename: str) -> Game:
    with open(filename, 'r') as f:
        data = json.load(f)
        return Game.from_dict(data)
