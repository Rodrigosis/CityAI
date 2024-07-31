class NewMap:

    def __init__(self, locations: List[Location] = []) -> None:
        self.locations = locations
    
    def __repr__(self):
        return str(self.to_dict())
 
    def to_dict(self):
        list_locations = [i.to_dict() for i in self.locations]
        return {
            "locations": list_locations
        }

    @classmethod
    def from_dict(cls, data):
        list_locations = [Location.from_dict(i) for i in data['locations']]
        return cls(
            locations=list_locations
        )
