class WorldCharacteristics:

    def __init__(self, economy: int = 1, violence: int = 1, corruption: int = 1, street_animals: int = 1, 
                 monsters: int = 1) -> None:
        self.economy = economy
        self.violence = violence
        self.corruption = corruption
        self.street_animals = street_animals
        self.monsters = monsters
    
    def __repr__(self):
        return str(self.to_dict())

    def to_dict(self):
        return {
            "economy": self.economy,
            "violence": self.violence,
            "corruption": self.corruption,
            "street_animals": self.street_animals,
            "monsters": self.monsters
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            economy=data["economy"],
            violence=data["violence"],
            corruption=data["corruption"],
            street_animals=data["street_animals"],
            monsters=data["monsters"],
        )
