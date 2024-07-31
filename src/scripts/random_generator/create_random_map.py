import random
import json
import uuid
from typing import List, Dict

from scripts.world import Location


class CreateRandomMap:

    def __init__(self, locations: List[Location] = []) -> None:
        with open('scripts/locations_v2.1.json', 'r') as f:
            metadata_locations = json.load(f)
        
        locals_list = []
        for i in metadata_locations:
            for ii in range(i["percent"]):
                locals_list.append(i)
        
        self.locals_list = locals_list
        self.metadata_locations = metadata_locations
        self.locations = locations
    
    def __repr__(self):
        return str(self.to_dict())
    
    def create_map(self, streets_number: int = 15):

        self.locations = []

        # cria as ruas
        for s in range(streets_number):
            self.create_street()
        
        return self.locations

    def create_street(self):
        id = str(uuid.uuid4())

        pointers = []
        for i in range(random.randint(3, 8)):
            n = random.randint(0, len(self.locals_list)-1)
            matedata = self.locals_list[n]
            local_id = self.create_local(id, matedata)
            pointers.append(local_id)

        street = Location(id=id, name=f'street {id[:3]}', location_type='street', 
                          destinations=pointers)
        self.locations.append(street)

    def create_local(self, street_id: str, metadata: Dict) -> str:
        id = str(uuid.uuid4())

        pointers = [street_id]
        for sub_l in metadata["sub_location"]:
            sub_local_id = self.create_sub_local(id, sub_l)
            pointers.append(sub_local_id)
        local = Location(id=id, name=f'{metadata["local_name"]} {id[:3]}', location_type='local', 
                          destinations=pointers)
        self.locations.append(local)

        return id

    def create_sub_local(self, local_id: str, metadata: Dict) -> str:
        id = str(uuid.uuid4())

        local = Location(id=id, name=f'{metadata["sub_local_name"]} {id[:3]}', location_type='sub_local', 
                         destinations=[local_id])
        self.locations.append(local)

        return id
