import random
import json
import uuid
from typing import List, Dict


class NewJobsPosition:

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
