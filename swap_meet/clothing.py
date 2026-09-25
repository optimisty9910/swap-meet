from .item import Item

class Clothing(Item):
    def __init__(self, id=None, fabric="Unknown", condition=0):
        super().__init__(id, condition)
        self.fabric = fabric

    def __str__(self):
        item_description = super().__str__()
        clothing_description = f"It is made from {self.fabric} fabric."
        return " ".join((item_description, clothing_description))
    