def add_to_list(lst):
    item = input("Enter an item to add to the list (or 'done' to finish): ")
    while item.lower() != 'done':
        lst.append(item)
        item = input("Enter another item (or 'done' to finish): ")

    print("Item added to the list.")
    return lst

def remove_from_list(lst):
    print("Current items in the list:", lst)
    item_to_remove = input("Enter an item to remove from the list (or 'done' to finish): ")
    while item_to_remove.lower() != 'done':
        if item_to_remove in lst:
            lst.remove(item_to_remove)
            print(f"'{item_to_remove}' removed from the list.")
        else:
            print(f"'{item_to_remove}' not found in the list.")
        print("Updated list:", lst)
        item_to_remove = input("Enter another item to remove (or 'done' to finish): ")

    print("Items removed from the list.")
    return lst

def print_list(lst):
    print("Current items in the list:")
    for item in lst:
        print("-", item)
    print("")