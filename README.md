[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/wnCpjX4n)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=21815755&assignment_repo_type=AssignmentRepo)
# COMP 163: Project 3 - Quest Chronicles

**AI Usage: Free Use (with explanation requirement)**

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


