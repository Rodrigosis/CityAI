class WorldCharacteristics:

    def __init__(self, human_f: float = 0.4, human_m: float = 0.4, 
                 animals_f: float = 0.09, animals_m: float = 0.09, 
                 monsters_f: float = 0.01, monsters_m: float = 0.01) -> None:
        self.human_f = human_f
        self.human_m = human_m
        self.animals_f = animals_f
        self.animals_m = animals_m
        self.monsters_f = monsters_f
        self.monsters_m = monsters_m
    
    def __repr__(self):
        return str(self.to_dict())

    def to_dict(self):
        return {
            "human_f": self.human_f,
            "human_m": self.human_m,
            "animals_f": self.animals_f,
            "animals_m": self.animals_m,
            "monsters_f": self.monsters_f,
            "monsters_m": self.monsters_m
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            human_f=data["human_f"],
            human_m=data["human_m"],
            animals_f=data["animals_f"],
            animals_m=data["animals_m"],
            monsters_f=data["monsters_f"],
            monsters_m=data["monsters_m"]
        )
