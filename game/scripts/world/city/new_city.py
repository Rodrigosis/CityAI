from game.scripts.world.city.streets.new_street import NewStreet


class NewCity:

    def __init__(self, id: str = '', city_name: str = 'main_city', 
                 streets: NewStreet[NewStreet] = []) -> None:
        self.id = id
        self.city_name = city_name
        self.streets = streets
    
    def __repr__(self):
        return str(self.to_dict())
 
    def to_dict(self):
        streets_list = [i.to_dict() for i in self.streets]
        return {
            "id": self.id,
            "city_name": self.city_name,
            "streets": streets_list
        }

    @classmethod
    def from_dict(cls, data):
        streets_list = [NewStreet.from_dict(i) for i in data['streets']]
        return cls(
            id=data["id"],
            city_name=data["city_name"],
            streets=streets_list
        )
