class Skills:

    def __init__(self, swimming: int = 0, dancing: int = 0, athletics: int = 0, housekeeping: int = 0, 
                 stealing: int = 0, religion: int = 0) -> None:
        self.swimming = swimming
        self.dancing = dancing
        self.athletics = athletics
        self.housekeeping = housekeeping
        self.stealing = stealing
        self.religion = religion
    
    def __repr__(self):
        return str(self.to_dict())

    def to_dict(self):
        return {
            "swimming": self.swimming,
            "dancing": self.dancing,
            "athletics": self.athletics,
            "housekeeping": self.housekeeping,
            "stealing": self.stealing,
            "religion": self.religion
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(
            swimming=data["swimming"],
            dancing=data["dancing"],
            athletics=data["athletics"],
            housekeeping=data["housekeeping"],
            stealing=data["stealing"],
            religion=data["religion"]
        )
