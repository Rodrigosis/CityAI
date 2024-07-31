

class NewStreet:
    
    def __init__(self, id: str = '', name: str = 'local', location_type: str = 'street', 
                 destinations: List[str] = [], jobs_positions: List[JobsPosition] = []) -> None:
        self.id = id
        self.name = name
        self.location_type = location_type
        self.destinations = destinations
        self.jobs_positions = jobs_positions
    
    def __repr__(self):
        return str(self.to_dict())

    def to_dict(self):
        list_jobs_positions = [i.to_dict() for i in self.jobs_positions]
        return {
            "id": self.id,
            "name": self.name,
            "location_type": self.location_type,
            "destinations": self.destinations,
            "jobs_positions": list_jobs_positions
        }

    @classmethod
    def from_dict(cls, data):
        list_jobs_positions = [JobsPosition.from_dict(i) for i in data['jobs_positions']]
        return cls(
            id=data["id"],
            name=data["name"],
            location_type=data["location_type"],
            destinations=data["destinations"],
            jobs_positions=list_jobs_positions
        )
