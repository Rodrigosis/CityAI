class CityCharacteristics:

    def __init__(self, economy: int = 1, violence: int = 1, corruption: int = 1) -> None:
        self.economy = economy
        self.violence = violence
        self.corruption = corruption
    
    def __repr__(self):
        return str(self.to_dict())

    def to_dict(self):
        return {
            "economy": self.economy,
            "violence": self.violence,
            "corruption": self.corruption
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            economy=data["economy"],
            violence=data["violence"],
            corruption=data["corruption"]
        )
