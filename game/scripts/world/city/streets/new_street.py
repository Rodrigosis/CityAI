from typing import List

from scripts.world.city.streets.buildings.new_building import Newbuilding


class NewStreet:
    
    def __init__(self, id: str = '', street_name: str = 'street', street_type: str = 'street', 
                 buildings: List[Newbuilding] = []) -> None:
        self.id = id
        self.street_name = street_name
        self.street_type = street_type
        self.buildings = buildings
    
    def __repr__(self):
        return str(self.to_dict())

    def to_dict(self):
        buildings_list = [i.to_dict() for i in self.buildings]
        return {
            "id": self.id,
            "street_name": self.street_name,
            "street_type": self.street_type,
            "buildings": buildings_list
        }

    @classmethod
    def from_dict(cls, data):
        buildings_list = [Newbuilding.from_dict(i) for i in data['buildings']]
        return cls(
            id=data["id"],
            street_name=data["street_name"],
            street_type=data["street_type"],
            buildings=buildings_list
        )
