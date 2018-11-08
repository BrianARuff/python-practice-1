class Items:
    def __init__(self, items_list=None):
        if items_list is None:
            items_list = []
            self.items_list = items_list

    def __str__(self):
        return f"{self.items_list}"

    def get_items(self):
        # Test for items in room
        if len(self.items_list) > 0:
            print("There are no items in this room.")
        else:
            return self.items_list

    def add_item(self, item: dict):
        # Ensure item doesn't exist
        if item in self.get_items():
            print(f"\nVALUE ERROR: {item} already exist\n")

        # Ensure type is a dict and then add item if it is
        elif type(item) == dict:
            self.items_list.append(item)
        # Print type error if it is not.
        else:
            print(f"\nTYPE ERROR: {item} is not of type dict\n")

    def remove_item(self, item: dict):
        if type(item) == dict:
            # Remove first of item
            self.items_list.remove(item)
        else:
            print(f"\nTYPE ERROR \n{item} is not of type dict\n")

    def update_item(self, item, name: str=None, description: str=None):
        if type(item) == dict:
            # Get item by index
            item_index = self.get_items().index(item)

            # If item was found update it with given values from function signature
            if item_index >= 0:
                self.get_items()[item_index] = self.get_items()[item_index] = {name: description}
        else:
            print(f"\nTYPE ERROR \n{item} is not of type dict\n")

