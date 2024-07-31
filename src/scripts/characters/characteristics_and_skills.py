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


class Body:

    def __init__(self, body_size: str = 'medium', chest_size: str = 'medium', 
                 buttock_size: str = 'medium', dick_size: str = 'medium',
                 body_type: str = 'slim', hair_type: str = 'straight', hair_length: str = 'long',
                 eye_color: str = 'blue', skin_color: str = 'white') -> None:
        self.body_size = body_size
        self.chest_size = chest_size
        self.buttock_size = buttock_size
        self.dick_size = dick_size
        self.body_type = body_type
        self.hair_type = hair_type
        self.hair_length = hair_length
        self.eye_color = eye_color
        self.skin_color = skin_color
    
    def __repr__(self):
        return str(self.to_dict())

    def to_dict(self):
        return {
            "body_size": self.body_size,
            "chest_size": self.chest_size,
            "buttock_size": self.buttock_size,
            "dick_size": self.dick_size,
            "body_type": self.body_type,
            "hair_type": self.hair_type,
            "hair_length": self.hair_length,
            "eye_color": self.eye_color,
            "skin_color": self.skin_color
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(
            body_size=data["body_size"],
            chest_size=data["chest_size"],
            buttock_size=data["buttock_size"],
            dick_size=data["dick_size"],
            body_type=data["body_type"],
            hair_type=data["hair_type"],
            hair_length=data["hair_length"],
            eye_color=data["eye_color"],
            skin_color=data["skin_color"]
        )


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


class CharacterTraits:

    def __init__(self) -> None:
        pass
    
    def __repr__(self):
        return str(self.to_dict())

    def to_dict(self):
        return {

        }

    @classmethod
    def from_dict(cls, data):
        return cls()
