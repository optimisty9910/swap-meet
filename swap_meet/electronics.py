from .item import Item

class Electronics(Item):
    def __init__(self, id=None, type="Unknown", condition=0):
        super().__init__(id, condition)
        self.type = type

    def __str__(self):
        item_description = super().__str__()
        electronics_description = f"This is a {self.type} device."
        return " ".join((item_description, electronics_description))
    