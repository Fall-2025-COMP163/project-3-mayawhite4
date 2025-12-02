"""
COMP 163 - Project 3: Quest Chronicles
Main Game Module - Starter Code

Name: Maya White

AI Usage: [Document any AI assistance used]

This is the main game file that ties all modules together.
Demonstrates module integration and complete game flow.
"""

# Import all our custom modules
import character_manager
import inventory_system
import quest_handler
import combat_system
import game_data
from custom_exceptions import *

# ============================================================================
# GAME STATE
# ============================================================================

# Global variables for game data
current_character = None
all_quests = {}
all_items = {}
game_running = False

# ============================================================================
# MAIN MENU
# ============================================================================

def main_menu():
    """
    Display main menu and get player choice
    
    Options:
    1. New Game
    2. Load Game
    3. Exit
    
    Returns: Integer choice (1-3)
    """
    # TODO: Implement main menu display
    # Show options
    # Get user input
    # Validate input (1-3)
    # Return choice
    print(f"=== WELCOME! ===")
    print(f"1. New Game")
    print(f"2. Load Game")
    print(f"3. Exit")
    user_input = int(input("Enter your selection: "))
    return user_input

def new_game():
    """
    Start a new game
    
    Prompts for:
    - Character name
    - Character class
    
    Creates character and starts game loop
    """
    global current_character
    
    # TODO: Implement new game creation
    # Get character name from user
    # Get character class from user
    # Try to create character with character_manager.create_character()
    # Handle InvalidCharacterClassError
    # Save character
    # Start game loop
    user_input = input("Enter Characters name:")
    user_class = input("Enter Character class:")
    try:
        character_manager.create_character(user_input, user_class)
        character_manager.save_character(user_input)
        game_loop()
    except InvalidCharacterClassError:
        print("Invalid Character Class")

def load_game():
    """
    Load an existing saved game
    
    Shows list of saved characters
    Prompts user to select one
    """
    global current_character
    
    # TODO: Implement game loading
    # Get list of saved characters
    # Display them to user
    # Get user choice
    # Try to load character with character_manager.load_character()
    # Handle CharacterNotFoundError and SaveFileCorruptedError
    # Start game loop
    saved_characters = character_manager.list_saved_characters()
    print(saved_characters)
    user_input = input("Enter Characters name:")
    try:
        character_manager.load_character(user_input)
        game_loop()
    except CharacterNotFoundError:
        print("Invalid Character")
    except SaveFileCorruptedError:
        print("Invalid Save")

# ============================================================================
# GAME LOOP
# ============================================================================

def game_loop():
    """
    Main game loop - shows game menu and processes actions
    """
    global game_running, current_character
    
    game_running = True
    
    # TODO: Implement game loop
    # While game_running:
    #   Display game menu
    #   Get player choice
    #   Execute chosen action
    #   Save game after each action
    while game_running:
        print(game_menu)
        players_choice = int(input("Enter your choice: "))
        if players_choice == 1:
            view_character_stats()
            save_game()
        if players_choice == 2:
            view_inventory()
            save_game()
        if players_choice == 3:
            quest_menu()
            save_game()
        if players_choice == 4:
            explore()
            save_game()
        if players_choice == 5:
            shop()
            save_game()
        if players_choice == 6:
            save_game()
            game_running = False


def game_menu():
    """
    Display game menu and get player choice
    
    Options:
    1. View Character Stats
    2. View Inventory
    3. Quest Menu
    4. Explore (Find Battles)
    5. Shop
    6. Save and Quit
    
    Returns: Integer choice (1-6)
    """
    # TODO: Implement game menu
    print(f"~~~ GAME MENU ~~~")
    print(f"1. View Character Stats")
    print(f"2. View Inventory")
    print(f"3. Quest Menu")
    print(f"4. Explore (Find Battles)")
    print(f"5. Shop")
    print(f"6. Save and Quit")
    user_input = int(input("What do you want to do: "))
    return user_input

# ============================================================================
# GAME ACTIONS
# ============================================================================

def view_character_stats():
    """Display character information"""
    global current_character
    
    # TODO: Implement stats display
    # Show: name, class, level, health, stats, gold, etc.
    # Use character_manager functions
    # Show quest progress using quest_handler
    print(f"=== CHARACTER STATS ===")
    print(f"Name: {current_character.name}")
    print(f"Class: {current_character.character_class}")
    print(f"Level: {current_character.level}")
    print(f"Health: {current_character.health}")
    print(f"Stats: {current_character.stats}")
    print(f"Gold: {current_character.gold}")
    print(f"Completed Quests: {quest_handler.complete_quest()}")

def view_inventory():
    """Display and manage inventory"""
    global current_character, all_items
    
    # TODO: Implement inventory menu
    # Show current inventory
    # Options: Use item, Equip weapon/armor, Drop item
    # Handle exceptions from inventory_system
    try:
        print(f"=== Inventory ===")
        print(f"Equipped weapon {inventory_system.equip_weapon()}")
        print(f"Equipped armory {inventory_system.equip_armor()}")
        print("")
    except InventoryFullError:
        print("Inventory full")
    except ItemNotFoundError:
        print("Item not found")
    except InsufficientResourcesError:
        print("Insufficient resources")
    except InvalidItemTypeError:
        print("Invalid Item Type")



def quest_menu():
    """Quest management menu"""
    global current_character, all_quests
    
    # TODO: Implement quest menu
    # Show:
    #   1. View Active Quests
    #   2. View Available Quests
    #   3. View Completed Quests
    #   4. Accept Quest
    #   5. Abandon Quest
    #   6. Complete Quest (for testing)
    #   7. Back
    # Handle exceptions from quest_handler
    print(f"=== QUEST MENU ===")
    print(f"1. View Active Quests")
    print(f"2. View Available Quests")
    print(f"3. View Completed Quests")
    print(f"4. Accept Quests")
    print(f"5. Abandon Quests")
    print(f"6. Complete Quests")
    print(f"7. Back")

def explore():
    """Find and fight random enemies"""
    global current_character
    
    # TODO: Implement exploration
    # Generate random enemy based on character level
    # Start combat with combat_system.SimpleBattle
    # Handle combat results (XP, gold, death)
    # Handle exceptions
    try:
        enemy = combat_system.get_random_enemy_for_level()
        combat_system.SimpleBattle
        print(f"{combat_system.get_victory_rewards(enemy)}")
    except InvalidTargetError:
        print("Invalid Target")
    except CombatNotActiveError:
        print("Combat not active")
    except CharacterDeadError:
        print("Character dead")

def shop():
    """Shop menu for buying/selling items"""
    global current_character, all_items
    
    # TODO: Implement shop
    # Show available items for purchase
    # Show current gold
    # Options: Buy item, Sell item, Back
    # Handle exceptions from inventory_system
    try:
        print(f"=== SHOP MENU ===")
        print(f"{all_items}")
        print(f"Gold: {current_character.gold}")
        print(f"1. Buy")
        print(f"2. Sell items")
        print(f"3. Back")
        user_input = int(input("What do you want to do: "))
        if user_input == 1:
            inventory_system.purchase_item(current_character)
        elif user_input == 2:
            inventory_system.sell_item(current_character)
        elif user_input == 3:
            game_menu()
    except InventoryFullError:
        print("Inventory full")
    except ItemNotFoundError:
        print("Item not found")
    except InsufficientResourcesError:
        print("Insufficient resources")
    except InvalidItemTypeError:
        print("Invalid Item Type")

# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

def save_game():
    """Save current game state"""
    global current_character
    
    # TODO: Implement save
    # Use character_manager.save_character()
    # Handle any file I/O exceptions
    try:
        character_manager.save_character()
    except IOError:
        print("Can't save file")

def load_game_data():
    """Load all quest and item data from files"""
    global all_quests, all_items
    
    # TODO: Implement data loading
    # Try to load quests with game_data.load_quests()
    # Try to load items with game_data.load_items()
    # Handle MissingDataFileError, InvalidDataFormatError
    # If files missing, create defaults with game_data.create_default_data_files()
    try:
        game_data.load_quests()
        game_data.load_items()
        game_data.create_default_data_files()
    except MissingDataFileError:
        print("Missing data file")
    except InvalidDataFormatError:
        print("Invalid data format")

def handle_character_death():
    """Handle character death"""
    global current_character, game_running
    
    # TODO: Implement death handling
    # Display death message
    # Offer: Revive (costs gold) or Quit
    # If revive: use character_manager.revive_character()
    # If quit: set game_running = False
    print(f"~~~ CHARACTER DEATH ~~~")
    print("Offer: 1. Revive or 2. Quit")
    user_input = int(input("What do you want to do: "))
    if user_input == 1:
        character_manager.revive_character(current_character)
    elif user_input == 2:
        game_running = False


def display_welcome():
    """Display welcome message"""
    print("=" * 50)
    print("     QUEST CHRONICLES - A MODULAR RPG ADVENTURE")
    print("=" * 50)
    print("\nWelcome to Quest Chronicles!")
    print("Build your character, complete quests, and become a legend!")
    print()

# ============================================================================
# MAIN EXECUTION
# ============================================================================

def main():
    """Main game execution function"""
    
    # Display welcome message
    display_welcome()
    
    # Load game data
    try:
        load_game_data()
        print("Game data loaded successfully!")
    except MissingDataFileError:
        print("Creating default game data...")
        game_data.create_default_data_files()
        load_game_data()
    except InvalidDataFormatError as e:
        print(f"Error loading game data: {e}")
        print("Please check data files for errors.")
        return
    
    # Main menu loop
    while True:
        choice = main_menu()
        
        if choice == 1:
            new_game()
        elif choice == 2:
            load_game()
        elif choice == 3:
            print("\nThanks for playing Quest Chronicles!")
            break
        else:
            print("Invalid choice. Please select 1-3.")

if __name__ == "__main__":
    main()

