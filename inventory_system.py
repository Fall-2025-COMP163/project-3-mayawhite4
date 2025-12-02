"""
COMP 163 - Project 3: Quest Chronicles
Inventory System Module - Starter Code

Name: Maya White

AI Usage: [Document any AI assistance used]

This module handles inventory management, item usage, and equipment.
"""
#from charset_normalizer.cd import characters_popularity_compare
#Do I need to keep this ^
from custom_exceptions import (
    InventoryFullError,
    ItemNotFoundError,
    InsufficientResourcesError,
    InvalidItemTypeError
)

# Maximum inventory size
MAX_INVENTORY_SIZE = 20

# ============================================================================
# INVENTORY MANAGEMENT
# ============================================================================

def add_item_to_inventory(character, item_id):
    """
    Add an item to character's inventory
    
    Args:
        character: Character dictionary
        item_id: Unique item identifier
    
    Returns: True if added successfully
    Raises: InventoryFullError if inventory is at max capacity
    """
    # TODO: Implement adding items
    # Check if inventory is full (>= MAX_INVENTORY_SIZE)
    # Add item_id to character['inventory'] list
    if len(character["inventory"]) >= MAX_INVENTORY_SIZE:
        raise InventoryFullError
    else:
        character["inventory"].append(item_id)
        return True

def remove_item_from_inventory(character, item_id):
    """
    Remove an item from character's inventory
    
    Args:
        character: Character dictionary
        item_id: Item to remove
    
    Returns: True if removed successfully
    Raises: ItemNotFoundError if item not in inventory
    """
    # TODO: Implement item removal
    # Check if item exists in inventory
    # Remove item from list
    if item_id in character["inventory"]:
        character["inventory"].remove(item_id)
        return True
    else:
        raise ItemNotFoundError

def has_item(character, item_id):
    """
    Check if character has a specific item
    
    Returns: True if item in inventory, False otherwise
    """
    # TODO: Implement item check
    if item_id in character["inventory"]:
        return True
    else:
        return False

def count_item(character, item_id):
    """
    Count how many of a specific item the character has
    
    Returns: Integer count of item
    """
    # TODO: Implement item counting
    # Use list.count() method
    amount = character["inventory"].count(item_id)
    return amount

def get_inventory_space_remaining(character):
    """
    Calculate how many more items can fit in inventory
    
    Returns: Integer representing available slots
    """
    # TODO: Implement space calculation
    inventory_amount = len(character["inventory"])
    space_left = MAX_INVENTORY_SIZE - inventory_amount
    return space_left

def clear_inventory(character):
    """
    Remove all items from inventory
    
    Returns: List of removed items
    """
    # TODO: Implement inventory clearing
    # Save current inventory before clearing
    # Clear character's inventory list
    removed_items = []
    for items in range(len(character["inventory"])):
        removed_items.append(character["inventory"][items])
        character["inventory"].pop(items)
    return removed_items


# ============================================================================
# ITEM USAGE
# ============================================================================

def use_item(character, item_id, item_data):
    """
    Use a consumable item from inventory
    
    Args:
        character: Character dictionary
        item_id: Item to use
        item_data: Item information dictionary from game_data
    
    Item types and effects:
    - consumable: Apply effect and remove from inventory
    - weapon/armor: Cannot be "used", only equipped
    
    Returns: String describing what happened
    Raises: 
        ItemNotFoundError if item not in inventory
        InvalidItemTypeError if item type is not 'consumable'
    """
    # TODO: Implement item usage
    # Check if character has the item
    # Check if item type is 'consumable'
    # Parse effect (format: "stat_name:value" e.g., "health:20")
    # Apply effect to character
    # Remove item from inventory
    if item_id in character["inventory"]:
        if "consumable" in character[item_data]:
            cleaned_line = character[item_data].strip()
            split_lines = cleaned_line.split(":")
            if split_lines[0] == "health":
                bonus = int(split_lines[1])
                character["health"] = character["health"] + bonus
                print(f"You have used {character["inventory"][item_id]} a health boost.")
            if split_lines[0] == "strength":
                bonus = int(split_lines[1])
                character["strength"] = character["strength"] + bonus
                print(f"You have used {character["inventory"][item_id]} a strength boost.")
            if split_lines[0] == "magic":
                bonus = int(split_lines[1])
                character["magic"] = character["magic"] + bonus
                print(f"You have used {character["inventory"][item_id]} a magic boost.")
            character["inventory"].pop(item_id)
        else:
            raise InvalidItemTypeError
    else:
        raise ItemNotFoundError

def equip_weapon(character, item_id, item_data):
    """
    Equip a weapon
    
    Args:
        character: Character dictionary
        item_id: Weapon to equip
        item_data: Item information dictionary
    
    Weapon effect format: "strength:5" (adds 5 to strength)
    
    If character already has weapon equipped:
    - Unequip current weapon (remove bonus)
    - Add old weapon back to inventory
    
    Returns: String describing equipment change
    Raises:
        ItemNotFoundError if item not in inventory
        InvalidItemTypeError if item type is not 'weapon'
    """
    # TODO: Implement weapon equipping
    # Check item exists and is type 'weapon'
    # Handle unequipping current weapon if exists
    # Parse effect and apply to character stats
    # Store equipped_weapon in character dictionary
    # Remove item from inventory
    if item_id in character["inventory"]:
        if "weapon" in item_data:
            if character["equipped_weapon"] == " ":
                character["equipped_weapon"] = item_id
            else:
                character["equipped_weapon"] == " "
                character["equipped_weapon"] == item_id
            for bonus in item_data:
                cleaned_line = item_data[bonus].strip()
                split_lines = cleaned_line.split(":")
                if split_lines[0] == "strength":
                    perk = int(split_lines[1])
                    character["strength"] = character["strength"] + perk
                if split_lines[0] == "magic":
                    perk = int(split_lines[1])
                    character["magic"] = character["magic"] + perk
                if split_lines[0] == "health":
                    perk = int(split_lines[1])
                    character["health"] = character["health"] + perk
                if split_lines[0] == "max_health":
                    perk = int(split_lines[1])
                    character["max_health"] = character["max_health"] + perk
            print(f"The weapon you are now equipped with is {item_id}")
            character["inventory"].pop(item_id)
        else:
            raise InvalidItemTypeError
    else:
        raise ItemNotFoundError

def equip_armor(character, item_id, item_data):
    """
    Equip armor
    
    Args:
        character: Character dictionary
        item_id: Armor to equip
        item_data: Item information dictionary
    
    Armor effect format: "max_health:10" (adds 10 to max_health)
    
    If character already has armor equipped:
    - Unequip current armor (remove bonus)
    - Add old armor back to inventory
    
    Returns: String describing equipment change
    Raises:
        ItemNotFoundError if item not in inventory
        InvalidItemTypeError if item type is not 'armor'
    """
    # TODO: Implement armor equipping
    # Similar to equip_weapon but for armor
    if item_id in character["inventory"]:
        if "armor" in item_data:
            if character["equipped_armor"] == " ":
                character["equipped_armor"] = item_id
            else:
                character["equipped_armor"] == " "
                character["equipped_armor"] == item_id
            for bonus in item_data:
                cleaned_line = item_data[bonus].strip()
                split_lines = cleaned_line.split(":")
                if split_lines[0] == "strength":
                    perk = int(split_lines[1])
                    character["strength"] = character["strength"] + perk
                if split_lines[0] == "magic":
                    perk = int(split_lines[1])
                    character["magic"] = character["magic"] + perk
                if split_lines[0] == "health":
                    perk = int(split_lines[1])
                    character["health"] = character["health"] + perk
                if split_lines[0] == "max_health":
                    perk = int(split_lines[1])
                    character["max_health"] = character["max_health"] + perk
            print(f"The armor you are now equipped with is {item_id}")
            character["inventory"].pop(item_id)
        else:
            raise InvalidItemTypeError
    else:
        raise ItemNotFoundError

def unequip_weapon(character):
    """
    Remove equipped weapon and return it to inventory
    
    Returns: Item ID that was unequipped, or None if no weapon equipped
    Raises: InventoryFullError if inventory is full
    """
    # TODO: Implement weapon unequipping
    # Check if weapon is equipped
    # Remove stat bonuses
    # Add weapon back to inventory
    # Clear equipped_weapon from character
    if character["equipped_weapon"] == " ":
        return None
    else:
        if len(character["inventory"]) >= MAX_INVENTORY_SIZE:
            raise InventoryFullError
        else:
            weapon = character["equipped_weapon"]
            character["inventory"].append(character["equipped_weapon"])
            character["equipped_weapon"] = " "

            return weapon

def unequip_armor(character):
    """
    Remove equipped armor and return it to inventory
    
    Returns: Item ID that was unequipped, or None if no armor equipped
    Raises: InventoryFullError if inventory is full
    """
    # TODO: Implement armor unequipping
    if character["equipped_armor"] == " ":
        return None
    else:
        if len(character["inventory"]) >= MAX_INVENTORY_SIZE:
            raise InventoryFullError
        else:
            armor = character["equipped_armor"]
            character["inventory"].append(character["equipped_armor"])
            character["equipped_armor"] = " "

            return armor

# ============================================================================
# SHOP SYSTEM
# ============================================================================

def purchase_item(character, item_id, item_data):
    """
    Purchase an item from a shop
    
    Args:
        character: Character dictionary
        item_id: Item to purchase
        item_data: Item information with 'cost' field
    
    Returns: True if purchased successfully
    Raises:
        InsufficientResourcesError if not enough gold
        InventoryFullError if inventory is full
    """
    # TODO: Implement purchasing
    # Check if character has enough gold
    # Check if inventory has space
    # Subtract gold from character
    # Add item to inventory
    if character["gold"] >= item_data["cost"]:
        if len(character["inventory"]) < MAX_INVENTORY_SIZE:
            character["gold"] -= item_data["cost"]
            character["inventory"].append(item_id)
            return True
        else:
            raise InventoryFullError
    else:
        raise InsufficientResourcesError

def sell_item(character, item_id, item_data):
    """
    Sell an item for half its purchase cost
    
    Args:
        character: Character dictionary
        item_id: Item to sell
        item_data: Item information with 'cost' field
    
    Returns: Amount of gold received
    Raises: ItemNotFoundError if item not in inventory
    """
    # TODO: Implement selling
    # Check if character has item
    # Calculate sell price (cost // 2)
    # Remove item from inventory
    # Add gold to character
    if item_id in character["inventory"]:
        price = item_data["cost"] // 2
        character["inventory"].remove(item_id)
        character["gold"] += price
        return price
    else:
        raise ItemNotFoundError

# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

def parse_item_effect(effect_string):
    """
    Parse item effect string into stat name and value
    
    Args:
        effect_string: String in format "stat_name:value"
    
    Returns: Tuple of (stat_name, value)
    Example: "health:20" → ("health", 20)
    """
    # TODO: Implement effect parsing
    # Split on ":"
    # Convert value to integer
    clean_string = effect_string.strip()
    split_string = clean_string.split(":")
    item1 = split_string[0]
    item2 = split_string[1]
    return (item1, item2)

def apply_stat_effect(character, stat_name, value):
    """
    Apply a stat modification to character
    
    Valid stats: health, max_health, strength, magic
    
    Note: health cannot exceed max_health
    """
    # TODO: Implement stat application
    # Add value to character[stat_name]
    # If stat is health, ensure it doesn't exceed max_health
    if stat_name == "health":
        character["health"] = character["health"] + value
        if character["health"] > character["max_health"]:
            character["health"] = character["max_health"]
    elif stat_name == "magic":
        character["magic"] = character["magic"] + value
    elif stat_name == "strength":
        character["strength"] = character["strength"] + value
    elif stat_name == "max_health":
        character["max_health"] = character["max_health"] + value

def display_inventory(character, item_data_dict):
    """
    Display character's inventory in formatted way
    
    Args:
        character: Character dictionary
        item_data_dict: Dictionary of all item data
    
    Shows item names, types, and quantities
    """
    # TODO: Implement inventory display
    # Count items (some may appear multiple times)
    # Display with item names from item_data_dict
    check_for_doubles = []
    for items in character["inventory"]:
        check_for_doubles.append(items)

    for checks in check_for_doubles:
        count = 0
        for line in check_for_doubles:
            if line == checks:
                count += 1
        cleaned_lines = item_data_dict[checks].strip()
        split_lines = cleaned_lines.split(":")
        print(f"Name: {split_lines[0]} | Type: {split_lines[1]} | Quantity: {count}")

# ============================================================================
# TESTING
# ============================================================================

if __name__ == "__main__":
    print("=== INVENTORY SYSTEM TEST ===")
    
    # Test adding items
    # test_char = {'inventory': [], 'gold': 100, 'health': 80, 'max_health': 80}
    # 
    # try:
    #     add_item_to_inventory(test_char, "health_potion")
    #     print(f"Inventory: {test_char['inventory']}")
    # except InventoryFullError:
    #     print("Inventory is full!")
    
    # Test using items
    # test_item = {
    #     'item_id': 'health_potion',
    #     'type': 'consumable',
    #     'effect': 'health:20'
    # }
    # 
    # try:
    #     result = use_item(test_char, "health_potion", test_item)
    #     print(result)
    # except ItemNotFoundError:
    #     print("Item not found")

