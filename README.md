[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/wnCpjX4n)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=21815755&assignment_repo_type=AssignmentRepo)
# COMP 163: Project 3 - Quest Chronicles

**AI Usage: Free Use (with explanation requirement)**

## Overview

Build a complete modular RPG adventure game demonstrating mastery of **exceptions and modules**.

## Getting Started

### Step 1: Accept Assignment
1. Click the assignment link provided in Blackboard
2. Accept the assignment - this creates your personal repository
3. Clone your repository to your local machine:
```bash
git clone [your-personal-repo-url]
cd [repository-name]
```

### Step 2: Understand the Project Structure

Your repository contains:

```
quest_chronicles/
├── main.py                     # Game launcher (COMPLETE THIS)
├── character_manager.py        # Character creation/management (COMPLETE THIS)
├── inventory_system.py         # Item and equipment management (COMPLETE THIS)
├── quest_handler.py            # Quest system (COMPLETE THIS)
├── combat_system.py            # Battle mechanics (COMPLETE THIS)
├── game_data.py                # Data loading and validation (COMPLETE THIS)
├── custom_exceptions.py        # Exception definitions (PROVIDED)
├── data/
│   ├── quests.txt             # Quest definitions (PROVIDED)
│   ├── items.txt              # Item database (PROVIDED)
│   └── save_games/            # Player save files (created automatically)
├── tests/
│   ├── test_module_structure.py       # Module organization tests
│   ├── test_exception_handling.py     # Exception handling tests
│   └── test_game_integration.py       # Integration tests
└── README.md                   # This file
```

### Step 3: Development Workflow

```bash
# Work on one module at a time
# Test your code frequently

# Commit and push to see test results
git add .
git commit -m "Implement character_manager module"
git push origin main

# Check GitHub for test results (green checkmarks = passed!, red xs = at least 1 failed test case. Click the checkmark or x and then "Details" to see what test cases passed/failed)
```

## Core Requirements (60 Points)

### Critical Constraint
You may **only** use concepts covered through the **Exceptions and Modules** chapters. 

### 🎨 Creativity and Customization

This project encourages creativity! Here's what you can customize:

**✅ FULLY CUSTOMIZABLE:**
- **Character stats** - Adjust health, strength, magic for balance
- **Enemy stats** - Make enemies easier or harder
- **Special abilities** - Design unique abilities for each class
- **Additional enemies** - Add your own enemy types beyond the required three
- **Game mechanics** - Add status effects, combos, critical hits, etc.
- **Quest rewards** - Adjust XP and gold amounts
- **Item effects** - Create unique items with creative effects

**⚠️ REQUIRED (for testing):**
- **4 Character classes:** Warrior, Mage, Rogue, Cleric (names must match exactly)
- **3 Enemy types:** "goblin", "orc", "dragon" (must exist, stats flexible)
- **All module functions** - Must have the specified function signatures
- **Exception handling** - Must raise appropriate exceptions

**💡 CREATIVITY TIPS:**
1. Start with required features working
2. Add creative elements incrementally
3. Test after each addition
4. Be ready to explain your design choices in the interview
5. Bonus interview points for thoughtful, balanced customization!

**Example Creative Additions:**
- Vampire enemy that heals when attacking
- Warrior "Last Stand" ability that activates when health is low
- Poison status effect that deals damage over time
- Critical hit system based on character stats
- Rare "legendary" weapons with special effects

### Module 1: custom_exceptions.py (PROVIDED - 0 points to implement)

**This module is provided complete.** It defines all custom exceptions you'll use throughout the project.

### Module 2: game_data.py (10 points)

### Module 3: character_manager.py (15 points)

### Module 4: inventory_system.py (10 points)

### Module 5: quest_handler.py (10 points)

### Module 6: combat_system.py (10 points)

### Module 7: main.py (5 points)

## Automated Testing & Validation (60 Points)

## Interview Component (40 Points)

**Creativity Bonus** (up to 5 extra points on interview):
- Added 2+ custom enemy types beyond required three
- Designed unique and balanced special abilities
- Implemented creative game mechanics (status effects, advanced combat, etc.)
- Thoughtful stat balancing with clear reasoning

**Note:** Creativity is encouraged, but functionality comes first! A working game with required features scores higher than a broken game with lots of extras.

## Module Architecture
The following modules: character_manager, combat_system game_data, inventory_system, quest_handler and main are located within the same directory called quest chronicles. All the modules have a special exception module imported for specific exceptiosn that each module uses. Main also has all the other modules imported so that it is able to use the other modules functions and classes. 

## Exception Strategy
I chose to raise an InvalidDataFormatError when the file wasn't formated in the correct format. I raised the MissingDataFileError trying to access a file that wasn't saved or created. I raised the CorruptedDataError when the data is unreadable or unable to be opened. I rasied a InvalidCharacterClassError when the user inputs a class that isn't one of the four given. I raised a CharacterNotFoundError when trying to load a character that doesn't exist. I raised a SaveFileCorruptedError when trying to load a character that doesn't exist but the directory exist. I raised an InvalidSaveDataError when the format or layout of the file wasn't correct. I raised a CharacterDeadError when the character's health was 0. I rasied a InventoryFullError when the length of the inventory was equal to the max inventory space. I raised an ItemNotFoundError when an the item didn't exist in the character's inventory. I rasied an InsufficientResourcesError when the character didn't have enough gold. I raised an InvalidItemTypeError when the item wasn't a type the weapons allowed or consumable. I rasied a QestNotFoundError when the quest didn't exist. I raised a QuestRequirementsNotMetError whent he character didn't meet the requirements needed for the quest they wanted to do. I raised a QuestAlreadyCompletedError when a character was attempting to try and do a quest they already finished. I raised a QuestNotActiveError when the quest wasn't in active quest. I raised a InsufficientLevelError if the character level is too low to finish a quest. I raised an InvalidTargetError when the enemy type given is not one of the three options. I raised a CombatNotActiveError when the player or enemy turn is called outside of the player being activily in a battle. I raised a CharacterDeadError if the character is already dead and the user is trying to start a battle. 

## Design Choices
Creativity wise I chose to keep the design simple since I wanted to focus more on the code. I also didn't have a huge vision on where I wanted to go with this project. 

## AI Usage
I used AI to help me understand why some of the errors I got for the test cases appear. I also used it to help me understand why my code doesn't align with the test case as well as what I should check or correct in order to fix my code and pass the test case. 

## How To Play
How you play this game is you first start off with the main menu where you get to choose whether or not you want to start a new game, load a game, or exit. If yo choose to create a new game you will need to create a new character. If you choose to load the previous game then it will load the character and quest and all the information you had when you played the game previously. If you choose to exit the game then the game won't start. After you start the game you then get to choose what you want to do from the game menu whether that is viewing your character stats or exploring and entering a battle. If you don't want to do any of that there is an option to save and quit where the character you have is saved and you exit the game. If you want to exit from an option you already chose you have the option to go back after selecting your option from the game menu. Then from their you can save and quit or even start a new game. 

### Update README.md

Document your project with:

1. **Module Architecture:** Explain your module organization
2. **Exception Strategy:** Describe when/why you raise specific exceptions
3. **Design Choices:** Justify major decisions
4. **AI Usage:** Detail what AI assistance you used
5. **How to Play:** Instructions for running the game

### What to Submit:

1. **GitHub Repository:** Your completed multi-module project
2. **Interview:** Complete 10-minute explanation session
3. **README:** Updated documentation

## Protected Files Warning

⚠️ **IMPORTANT: Test Integrity**

Test files are provided for your learning but are protected. Modifying test files constitutes academic dishonesty and will result in:

- Automatic zero on the project
- Academic integrity investigation

You can view tests to understand requirements, but any modifications will be automatically detected.
