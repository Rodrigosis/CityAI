import random
import json
import uuid
from typing import List, Dict, Optional

from scripts.world.new_world import NewWorld
from scripts.random_generator.create_random_city import CreateRandomCity


class CreateRandomWorld:

    def __init__(self) -> None:
        pass
    
    def create_world(self, num_of_cities: Optional[int] = 5) -> NewWorld:
        id = id = str(uuid.uuid4())
        ran = CreateRandomCity()

        cities = []
        for i in range(num_of_cities):
            cities.append(ran.create_city())

        
        return NewWorld(id=id, world_name=f"world {id[:2]}", cities=cities)
