import uuid
CONDITION_DESCRIPTION = ["Poor/Non-Functional", "Fair", "Good", "Very Good", "Excellent", "Brand New"]

class Item:
    def __init__(self, id=None, condition=0):
        if id is None:
            new_id = uuid.uuid4()
            self.id = new_id.int
        else:
            self.id = id

        self.condition = condition

    def get_category(self):
        category = self.__class__.__name__
        return category

    def condition_description(self):
        return CONDITION_DESCRIPTION[self.condition]

    def __str__(self):
        result = (
            f"An object of type {self.get_category()} with id {self.id}."
        )
        return result
    