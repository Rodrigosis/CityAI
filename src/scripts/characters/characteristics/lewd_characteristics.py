class LewdCharacteristics:

    def __init__(self, seduction: int = 10, purity: int = 1000, promiscuity: int = 0, exhibitionnism: int = 0, 
                 submissiveness: int = 0) -> None:
        self.seduction = seduction
        self.purity = purity
        self.promiscuity = promiscuity
        self.exhibitionnism = exhibitionnism
        self.submissiveness = submissiveness
    
    def __repr__(self):
        return str(self.to_dict())

    def to_dict(self):
        return {
            "seduction": self.seduction,
            "purity": self.purity,
            "promiscuity": self.promiscuity,
            "exhibitionnism": self.exhibitionnism,
            "submissiveness": self.submissiveness
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(
            seduction=data["seduction"],
            purity=data["purity"],
            promiscuity=data["promiscuity"],
            exhibitionnism=data["exhibitionnism"],
            submissiveness=data["submissiveness"]
        )