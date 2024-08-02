from typing import List

from game.scripts.world.city.new_city import NewCity
from game.scripts.world.world_characteristics import WorldCharacteristics


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
                 cities: List[NewCity] = [],
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
        self.cities = cities
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
        cities_list = [i.to_dict() for i in self.cities]
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
            "cities": cities_list,
            "world_characteristics": self.world_characteristics.to_dict()
        }
    
    @classmethod
    def from_dict(cls, data):
        cities_list = [NewCity.from_dict(i) for i in data['cities']]
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
            cities=cities_list,
            world_characteristics=WorldCharacteristics.from_dict(data['world_characteristics'])
        )
