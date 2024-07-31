class SchoolPerformance:

    def __init__(self, math: int = 0, biology: int = 0, chemical: int = 0, geography: int = 0, 
                 physical: int = 0, philosophy: int = 0, history: int = 0, art: int = 0) -> None:
        self.math = math
        self.biology = biology
        self.chemical = chemical
        self.geography = geography
        self.physical = physical
        self.philosophy = philosophy
        self.history = history
        self.art = art
    
    def __repr__(self):
        return str(self.to_dict())

    def to_dict(self):
        return {
            "math": self.math,
            "biology": self.biology,
            "chemical": self.chemical,
            "geography": self.geography,
            "physical": self.physical,
            "philosophy": self.philosophy,
            "history": self.history,
            "art": self.art
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(
            math=data["math"],
            biology=data["biology"],
            chemical=data["chemical"],
            geography=data["geography"],
            physical=data["physical"],
            philosophy=data["philosophy"],
            history=data["history"],
            art=data["art"],
        )
