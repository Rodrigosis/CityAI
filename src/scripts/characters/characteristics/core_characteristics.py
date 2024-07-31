from typing import List


class CoreCharacteristics:
    
    def __init__(self, intelligence: int = 100, charisma: int = 20, 
                 strength: int = 50, speed: int = 50) -> None:
        self.intelligence = intelligence
        self.charisma = charisma
        self.strength = strength
        self.speed = speed
    
    def __repr__(self):
        return str(self.to_dict())

    def to_dict(self):
        return {
            "intelligence": self.intelligence,
            "charisma": self.charisma,
            "strength": self.strength,
            "speed": self.speed
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(
            intelligence=data["intelligence"],
            charisma=data["charisma"],
            strength=data["strength"],
            speed=data["speed"]
        )
