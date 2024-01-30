class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner='None'):
        self.name = name
        if pet_type in Pet.PET_TYPES:
            self.pet_type = pet_type
        else:
            raise Exception
        self._owner = owner
        Pet.all.append(self)

    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, value):
        if not isinstance(value, Owner):
            raise Exception
        self._owner = value
    
class Owner:

    def __init__(self, name):
        self.name = name

    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]
    
    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception
        else:
            pet.owner = self
    
    def get_sorted_pets(self):
        return sorted([pet for pet in Pet.all if pet.owner == self], key=lambda x: x.name)
        