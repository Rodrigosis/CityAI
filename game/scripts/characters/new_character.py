from game.scripts.characters.characteristics.core_characteristics import CoreCharacteristics
from game.scripts.characters.characteristics.lewd_characteristics import LewdCharacteristics
from game.scripts.characters.characteristics.sex_interest import SexInterest
from game.scripts.characters.characteristics.status import CharacterStatus
from game.scripts.characters.characteristics.traits import CharacterTraits
from game.scripts.characters.skills.skills import Skills
from game.scripts.characters.skills.sex_skills import SexSkills
from game.scripts.characters.skills.school_skills import SchoolPerformance
from game.scripts.characters.body import Body


class NewCharacter:

    def __init__(self, id: str = '', name: str = 'Liam', age: int = 20, 
                 what_room_am_i_in: str = 'bedroom',
                 where_i_am: str = 'home',
                 what_world_am_i_in: str = 'main_world',
                 character_status: CharacterStatus = CharacterStatus(),
                 character_traits: CharacterTraits = CharacterTraits(),
                 core_characteristics: CoreCharacteristics = CoreCharacteristics(), 
                 lewd_characteristics: LewdCharacteristics = LewdCharacteristics(), 
                 sex_interest: SexInterest = SexInterest(),
                 sex_skills: SexSkills = SexSkills(), 
                 skills: Skills = Skills(), 
                 body: Body = Body(), 
                 school_performance: SchoolPerformance = SchoolPerformance()) -> None:
        self.id = id
        self.name = name
        self.age = age
        self.what_room_am_i_in = what_room_am_i_in
        self.where_i_am = where_i_am
        self.what_world_am_i_in = what_world_am_i_in
        self.character_status = character_status
        self.character_traits = character_traits
        self.core_characteristics = core_characteristics
        self.lewd_characteristics = lewd_characteristics
        self.sex_interest = sex_interest
        self.sex_skills = sex_skills
        self.skills = skills
        self.body = body
        self.school_performance = school_performance
    
    def __repr__(self):
        return str(self.to_dict())

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "what_room_am_i_in": self.what_room_am_i_in,
            "where_i_am": self.where_i_am,
            "what_world_am_i_in": self.what_world_am_i_in,
            "character_status": self.character_status.to_dict(),
            "character_traits": self.character_traits.to_dict(),
            "core_characteristics": self.core_characteristics.to_dict(),
            "lewd_characteristics": self.lewd_characteristics.to_dict(),
            "sex_interest": self.sex_interest.to_dict(),
            "sex_skills": self.sex_skills.to_dict(),
            "skills": self.skills.to_dict(),
            "body": self.body.to_dict(),
            "school_performance": self.school_performance.to_dict()
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(
            id=data["id"],
            name=data["name"],
            age=data["age"],
            what_room_am_i_in=data["what_room_am_i_in"],
            where_i_am=data["where_i_am"],
            what_world_am_i_in=data["what_world_am_i_in"],
            character_status=CharacterStatus.from_dict(data['character_status']),
            character_traits=CharacterTraits.from_dict(data['character_traits']),
            core_characteristics=CoreCharacteristics.from_dict(data['core_characteristics']),
            lewd_characteristics=LewdCharacteristics.from_dict(data['lewd_characteristics']),
            sex_interest=SexInterest.from_dict(data['sex_interest']),
            sex_skills=SexSkills.from_dict(data['sex_skills']),
            skills=Skills.from_dict(data['skills']),
            body=Body.from_dict(data['body']),
            school_performance=SchoolPerformance.from_dict(data['school_performance'])
        )
