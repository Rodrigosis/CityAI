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
