class SexInterest:

    def __init__(self, animals: int = 0, youngers: int = 0, milfs: int = 0, bdsm: int = 0, rape: int = 0) -> None:
        self.animals = animals
        self.youngers = youngers
        self.milfs = milfs
        self.bdsm = bdsm
        self.rape = rape
    
    def __repr__(self):
        return str(self.to_dict())

    def to_dict(self):
        return {
            "animals": self.animals,
            "youngers": self.youngers,
            "milfs": self.milfs,
            "bdsm": self.bdsm,
            "rape": self.rape
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(
            animals=data["animals"],
            youngers=data["youngers"],
            milfs=data["milfs"],
            bdsm=data["bdsm"],
            rape=data["rape"]
        )
