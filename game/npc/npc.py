class Background:

    def __init__(self, name: str = "", nickname: str = "", traits: str = "", motivation: str = "", 
                 speech_style: str = "", relationships: str = "", quirk: str = "", mood: str = "") -> None:
        self.name = name  # example: Marco
        self.nickname = nickname  # example: the deceiver
        self.traits = traits  # example: sarcastic, greedy, but resourceful and generous
        self.motivation = motivation  # example: Get rich at any cost
        self.speech_style = speech_style  # example: speaks quickly and inserts double-meaning jokes
        self.relationships = relationships  # example: Pretends to be friendly but tries to deceive if profitable
        self.quirk = quirk  # example: Hates jokes about his height (he's short)
        self.mood = mood  # example: Usually relaxed but becomes irritated when contradicted


class PhysicalStatus:

    def __init__(self, strength: int = 10, speed: int = 10, agility: int = 10) -> None:
        self.strength = strength
        self.speed = speed
        self.agility = agility

class MentalStatus:

    def __init__(self, charisma: int = 1, intelligence: int = 1) -> None:
        self.charisma = charisma
        self.intelligence = intelligence


class PhysicalStatus2:

    def __init__(self, health: int = 100, stamina: int = 100) -> None:
        self.health = health
        self.stamina = stamina


class MentalStatus2:

    def __init__(self, Stress: int = 0, concentration: int = 10, sanity: int = 10) -> None:
        self.Stress = Stress
        self.concentration = concentration
        self.sanity = sanity
