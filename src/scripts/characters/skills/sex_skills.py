class SexSkills:

    def __init__(self, oral: int = 0, chest: int = 0, hands: int = 0, dick: int = 0, pussy: int = 0, 
                 anal: int = 0, buttock: int = 0, thights: int = 0, feet: int = 0) -> None:
        self.oral = oral
        self.chest = chest
        self.hands = hands
        self.dick = dick
        self.pussy = pussy
        self.anal = anal
        self.buttock = buttock
        self.thights = thights
        self.feet = feet
    
    def __repr__(self):
        return str(self.to_dict())

    def to_dict(self):
        return {
            "oral": self.oral,
            "chest": self.chest,
            "hands": self.hands,
            "dick": self.dick,
            "pussy": self.pussy,
            "anal": self.anal,
            "buttock": self.buttock,
            "thights": self.thights,
            "feet": self.feet
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(
            oral=data["oral"],
            chest=data["chest"],
            hands=data["hands"],
            dick=data["dick"],
            pussy=data["pussy"],
            anal=data["anal"],
            buttock=data["buttock"],
            thights=data["thights"],
            feet=data["feet"]
        )
