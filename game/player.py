class NewPlayer:
    def __init__(self, first_name: str = "Rodrigo", last_name: str = "Souza", title: str = "o louco", health: int = 100,
                 stamina: int = 100, sanity: int = 100, strength: int = 1, dexterity: int = 1, charisma: int = 1,
                 intelligence: int = 1, local_id: int = 0, money: int = 3541):
        self.first_name = first_name
        self.last_name = last_name
        self.title = title
        self.health = health
        self.stamina = stamina
        self.sanity = sanity
        self.strength = strength
        self.dexterity = dexterity
        self.charisma = charisma
        self.intelligence = intelligence
        self.local_id = local_id
        self.money = money
