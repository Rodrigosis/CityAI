class CharacterStatus:

    def __init__(self, health: int = 100, fatigue: int = 0, stress: int = 0, arousal: int = 0, 
                 pain: int = 0, willpower: int = 0, revealing_outfit: int = 0) -> None:
        self.health = health
        self.fatigue = fatigue
        self.stress = stress
        self.arousal = arousal
        self.pain = pain
        self.willpower = willpower
        self.revealing_outfit = revealing_outfit
    
    def __repr__(self):
        return str(self.to_dict())

    def to_dict(self):
        return {
            "health": self.health,
            "fatigue": self.fatigue,
            "stress": self.stress,
            "arousal": self.arousal,
            "pain": self.pain,
            "willpower": self.willpower,
            "revealing_outfit": self.revealing_outfit
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(
            health=data["health"],
            fatigue=data["fatigue"],
            stress=data["stress"],
            arousal=data["arousal"],
            pain=data["pain"],
            willpower=data["willpower"],
            revealing_outfit=data["revealing_outfit"],
        )
