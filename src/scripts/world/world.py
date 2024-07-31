import random
import json
import uuid
from typing import List, Dict


class JobsPosition:

    def __init__(self, id: str = '', job_type: str = '', character_id: str = '', payment: float = 0,
                 ability_to_climb: List[str] = []) -> None:
        self.id = id
        self.job_type = job_type
        self.character_id = character_id
        self.payment = payment
        self.ability_to_climb = ability_to_climb

    def __repr__(self):
        return str(self.to_dict())

    def to_dict(self):
        return {
            "id": self.id,
            "job_type": self.job_type,
            "character_id": self.character_id,
            "payment": self.payment,
            "ability_to_climb": self.ability_to_climb
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            id=data["id"],
            job_type=data["job_type"],
            character_id=data["character_id"],
            payment=data["payment"],
            ability_to_climb=data["ability_to_climb"]
        )


class Location:
    
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


class Map:

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


class WorldCharacteristics:

    def __init__(self, economy: int = 1, violence: int = 1, corruption: int = 1, street_animals: int = 1, 
                 monsters: int = 1) -> None:
        self.economy = economy
        self.violence = violence
        self.corruption = corruption
        self.street_animals = street_animals
        self.monsters = monsters
    
    def __repr__(self):
        return str(self.to_dict())

    def to_dict(self):
        return {
            "economy": self.economy,
            "violence": self.violence,
            "corruption": self.corruption,
            "street_animals": self.street_animals,
            "monsters": self.monsters
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            economy=data["economy"],
            violence=data["violence"],
            corruption=data["corruption"],
            street_animals=data["street_animals"],
            monsters=data["monsters"],
        )


class NewWorld:

    def __init__(self, id: str = '', 
                 world_name: str = 'main_world', 
                 world_age_days: int = 0, 
                 minutes: int = 0, 
                 hours: int = 0, 
                 day: int = 0, 
                 week: int = 0, 
                 year: int = 0, 
                 season: str = 'winter',
                 map: Map = Map(),
                 world_characteristics: WorldCharacteristics = WorldCharacteristics()) -> None:
        self.id = id
        self.world_name = world_name
        self.world_age_days = world_age_days   
        self.minutes = minutes
        self.hours = hours
        self.day = day
        self.week = week
        self.year = year
        self.season = season
        self.map = map
        self.world_characteristics = world_characteristics

    def update_calendar(self):
        self.day = (self.world_age_days % 365) + 1
        self.week = self.day // 7
        self.year = self.day // 365

        # spring day 80 to 172
        # summer day 173 to 267
        # autumn day 268 to 356
        # winter day 356 to 79

        if 80 <= self.day < 173:
            self.season = 'spring'
        elif 173 <= self.day < 268:
            self.season = 'summer'
        elif 268 <= self.day < 356:
            self.season = 'autumn'
        else:
            self.season = 'winter'
    
    def __repr__(self):
        return str(self.to_dict())

    def to_dict(self):
        return {
            "id": self.id,
            "world_name": self.world_name,
            "world_age_days": self.world_age_days,
            "minutes": self.minutes,
            "hours": self.hours,
            "day": self.day,
            "week": self.week,
            "year": self.year,
            "season": self.season,
            "map": self.map.to_dict(),
            "world_characteristics": self.world_characteristics.to_dict()
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(
            id=data["id"],
            world_name=data["world_name"],
            world_age_days=data["world_age_days"],
            minutes=data["minutes"],
            hours=data["hours"],
            day=data["day"],
            week=data["week"],
            year=data["year"],
            season=data["season"],
            map=data['map'],
            world_characteristics=WorldCharacteristics.from_dict(data['world_characteristics'])
        )
