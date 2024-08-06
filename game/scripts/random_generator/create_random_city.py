import random
import json
import uuid
from typing import List, Dict

from scripts.world.city.new_city import NewCity
from scripts.world.city.streets.new_street import NewStreet
from scripts.world.city.streets.buildings.new_building import Newbuilding


class CreateRandomCity:

    def __init__(self) -> None:
        pass

    def create_city(self) -> NewCity:
        id = id = str(uuid.uuid4())

        streets = []
        for i in range(random.randint(10, 50)):
            streets.append(self._create_street())

        city = NewCity(id=id, city_name=f"city {id[:2]}", streets=streets)
        city = self._create_house_and_apartiments(city)
        return city

    def _create_street(self) -> NewStreet:
        id = id = str(uuid.uuid4())

        buildings = []
        for i in range(random.randint(1, 4)):
            buildings.append(self._create_buildin())

        return NewStreet(id=id, street_name=f"street {id[:3]}", street_type="street", buildings=buildings)
    
    def _create_buildin(self) -> Newbuilding:
        id = id = str(uuid.uuid4())

        return Newbuilding(id=id, building_name=f"local {id[:4]}", building_type="story")

    def _create_house_and_apartiments(self, city: NewCity) -> NewCity:

        for street in city.streets:
            for i in range(random.randint(1, 4)):
                id = id = str(uuid.uuid4())

                if i >= 3:
                    h = Newbuilding(id=id, building_name=f'house {id[:4]}', building_type='house')
                else:
                    apartiments = []
                    for ap_house in range(random.randint(5, 10)):
                        ap_id = str(uuid.uuid4())
                        apartiments.append(Newbuilding(id=ap_id, building_name=f'apartment {ap_id[:4]}', building_type='ap_house'))
                    h = Newbuilding(id=id, building_name=f'residential building {id[:4]}', building_type='residential building', sub_building=apartiments)

                street.buildings.append(h)

        return city
