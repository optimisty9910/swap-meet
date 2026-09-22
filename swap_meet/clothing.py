from .item import Item

class Clothing(Item):
    def __init__(self, id=None, fabric="Unknown", condition=0):
        super().__init__(id, condition)
        self.fabric = fabric

    def __str__(self):
        result = (
            f"An object of type Clothing with id {self.id}. "
            f"It is made from {self.fabric} fabric."
        )
        return result
    