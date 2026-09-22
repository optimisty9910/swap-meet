from .item import Item

class Electronics(Item):
    def __init__(self, id=None, type="Unknown", condition=0):
        super().__init__(id, condition)
        self.type = type

    def __str__(self):
        result = (
            f"An object of type Electronics with id {self.id}. "
            f"This is a {self.type} device."
        )
        return result
    