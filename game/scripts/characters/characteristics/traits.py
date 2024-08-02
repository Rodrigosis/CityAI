class CharacterTraits:

    def __init__(self, foo: int = 100) -> None:
        self.foo = foo
    
    def __repr__(self):
        return str(self.to_dict())

    def to_dict(self):
        return {
            "foo": self.foo
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(
            foo=data["foo"]
        )
