from typing import Optional, List


class Newbuilding:
    
    def __init__(self, id: str = '', building_name: str = 'local', building_type: str = 'story', sub_building: Optional[List] = []) -> None:
        self.id = id
        self.building_name = building_name
        self.building_type = building_type
        self.sub_building = sub_building
    
    def __repr__(self):
        return str(self.to_dict())

    def to_dict(self):
        sub_building_list = [i.to_dict() for i in self.sub_building]
        return {
            "id": self.id,
            "building_name": self.building_name,
            "building_type": self.building_type,
            "sub_building": sub_building_list
        }

    @classmethod
    def from_dict(cls, data):
        sub_building_list = [Newbuilding.from_dict(i) for i in data['sub_building']]
        return cls(
            id=data["id"],
            building_name=data["building_name"],
            building_type=data["building_type"],
            sub_building=sub_building_list
        )
