class Vendor:
    def __init__(self, inventory=None):
        if inventory is None:
            self.inventory = []
        else:
            self.inventory = inventory

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        try:
            self.inventory.remove(item)
            return item
        except ValueError:
            return None

    def get_by_id(self, id):
        for item in self.inventory:
            if item.id == id:
                return item
        return None

    def swap_items(self, other_vendor, my_item, their_item):
        if (
            my_item not in self.inventory
            or their_item not in other_vendor.inventory
        ):
            return False
        else:
            self.remove(my_item)
            self.add(their_item)
            other_vendor.remove(their_item)
            other_vendor.add(my_item)
            return True

    def swap_first_item(self, other_vendor):
        if len(self.inventory) == 0 or len(other_vendor.inventory) == 0:
            return False
        my_item = self.inventory[0]
        their_item = other_vendor.inventory[0]

        return self.swap_items(other_vendor, my_item, their_item)

    def get_by_category(self, category):
        category_objects = []

        for item in self.inventory:
            if item.get_category() == category:
                category_objects.append(item)

        return category_objects

    def get_best_by_category(self, category):
        category_objects = self.get_by_category(category)

        if not category_objects:
            return None

        highest_condition = 0
        best_item = category_objects[0]

        for item in category_objects:
            if item.condition > highest_condition:
                highest_condition = item.condition
                best_item = item

        return best_item

    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        my_best_item = self.get_best_by_category(their_priority)
        their_best_item = other_vendor.get_best_by_category(my_priority)

        if my_best_item is None or their_best_item is None:
            return False
        else:
            self.swap_items(other_vendor, my_best_item, their_best_item)
            return True
        
    

        
        
