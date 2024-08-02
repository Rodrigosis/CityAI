

class Newbuilding:
    
    def __init__(self, id: str = '', building_name: str = 'local', building_type: str = 'street') -> None:
        self.id = id
        self.building_name = building_name
        self.building_type = building_type
    
    def __repr__(self):
        return str(self.to_dict())

    def to_dict(self):
        return {
            "id": self.id,
            "building_name": self.building_name,
            "building_type": self.building_type
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            id=data["id"],
            building_name=data["building_name"],
            building_type=data["building_type"]
        )
