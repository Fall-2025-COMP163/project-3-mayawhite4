"""
COMP 163 - Project 3: Quest Chronicles
Quest Handler Module - Starter Code

Name: Maya White

AI Usage: [Document any AI assistance used]

This module handles quest management, dependencies, and completion.
"""
import character_manager
from custom_exceptions import (
    QuestNotFoundError,
    QuestRequirementsNotMetError,
    QuestAlreadyCompletedError,
    QuestNotActiveError,
    InsufficientLevelError
)

# ============================================================================
# QUEST MANAGEMENT
# ============================================================================

def accept_quest(character, quest_id, quest_data_dict):
    """
    Accept a new quest
    
    Args:
        character: Character dictionary
        quest_id: Quest to accept
        quest_data_dict: Dictionary of all quest data
    
    Requirements to accept quest:
    - Character level >= quest required_level
    - Prerequisite quest completed (if any)
    - Quest not already completed
    - Quest not already active
    
    Returns: True if quest accepted
    Raises:
        QuestNotFoundError if quest_id not in quest_data_dict
        InsufficientLevelError if character level too low
        QuestRequirementsNotMetError if prerequisite not completed
        QuestAlreadyCompletedError if quest already done
    """
    # TODO: Implement quest acceptance
    # Check quest exists
    # Check level requirement
    # Check prerequisite (if not "NONE")
    # Check not already completed
    # Check not already active
    # Add to character['active_quests']
    if quest_id in quest_data_dict:
        if character["level"] >= quest_data_dict[quest_id]["required_level"]:
            if quest_data_dict[quest_id]["prerequisite"] == "NONE":
                if quest_id not in character["completed_quests"]:
                    if quest_id not in character["active_quests"]:
                        character["active_quests"].append(quest_id)
                else:
                    raise QuestAlreadyCompletedError
            elif quest_data_dict[quest_id]["prerequisite"] in character["completed_quests"]:
                if quest_id not in character["completed_quests"]:
                    if quest_id not in character["active_quests"]:
                        character["active_quests"].append(quest_id)
                else:
                    raise QuestAlreadyCompletedError
            else:
                raise QuestRequirementsNotMetError
        else:
            raise InsufficientLevelError
    else:
        raise QuestNotFoundError
    return True

def complete_quest(character, quest_id, quest_data_dict):
    """
    Complete an active quest and grant rewards
    
    Args:
        character: Character dictionary
        quest_id: Quest to complete
        quest_data_dict: Dictionary of all quest data
    
    Rewards:
    - Experience points (reward_xp)
    - Gold (reward_gold)
    
    Returns: Dictionary with reward information
    Raises:
        QuestNotFoundError if quest_id not in quest_data_dict
        QuestNotActiveError if quest not in active_quests
    """
    # TODO: Implement quest completion
    # Check quest exists
    # Check quest is active
    # Remove from active_quests
    # Add to completed_quests
    # Grant rewards (use character_manager.gain_experience and add_gold)
    # Return reward summary
    if quest_id in quest_data_dict:
        if quest_id in character["active_quests"]:
            character["active_quests"].remove(quest_id)
            character["completed_quests"].append(quest_id)
            character_manager.gain_experience(character, quest_data_dict[quest_id]["xp_amount"])
            character_manager.add_gold(character, quest_data_dict[quest_id]["gold"])
            reward_summary = {"xp_amount": quest_data_dict[quest_id]["xp_amount"], "gold": quest_data_dict[quest_id]["gold"]}
            return reward_summary
        else:
            raise QuestNotActiveError
    else:
        raise QuestNotFoundError

def abandon_quest(character, quest_id):
    """
    Remove a quest from active quests without completing it
    
    Returns: True if abandoned
    Raises: QuestNotActiveError if quest not active
    """
    # TODO: Implement quest abandonment
    if quest_id in character["active_quests"]:
        removal = character["active_quests"].pop(quest_id)
        return removal
    else:
        raise QuestNotActiveError

def get_active_quests(character, quest_data_dict):
    """
    Get full data for all active quests
    
    Returns: List of quest dictionaries for active quests
    """
    # TODO: Implement active quest retrieval
    # Look up each quest_id in character['active_quests']
    # Return list of full quest data dictionaries
    current_quests = []
    for quest in quest_data_dict:
        if quest == character["active_quests"]:
            current_quests.append(quest)
    return current_quests


def get_completed_quests(character, quest_data_dict):
    """
    Get full data for all completed quests
    
    Returns: List of quest dictionaries for completed quests
    """
    # TODO: Implement completed quest retrieval
    finished_quests = []
    for quest in quest_data_dict:
        if quest == character["completed_quests"]:
            finished_quests.append(quest)
    return finished_quests

def get_available_quests(character, quest_data_dict):
    """
    Get quests that character can currently accept
    
    Available = meets level req + prerequisite done + not completed + not active
    
    Returns: List of quest dictionaries
    """
    # TODO: Implement available quest search
    # Filter all quests by requirements
    can_do_quest = []
    for quests in quest_data_dict:
        if character["level"] >= quests["level"]:
            if quests["prerequisite"] in character["completed_quests"]:
                if (quests not in character["completed_quests"]) and (quests not in character["active_quests"]):
                    can_do_quest.append(quests)
    return can_do_quest


# ============================================================================
# QUEST TRACKING
# ============================================================================

def is_quest_completed(character, quest_id):
    """
    Check if a specific quest has been completed

    Returns: True if completed, False otherwise
    """
    # TODO: Implement completion check
    if quest_id in character["completed_quests"]:
        return True
    else:
        return False

def is_quest_active(character, quest_id):
    """
    Check if a specific quest is currently active

    Returns: True if active, False otherwise
    """
    # TODO: Implement active check
    if quest_id in character["active_quests"]:
        return True
    else:
        return False

def can_accept_quest(character, quest_id, quest_data_dict):
    """
    Check if character meets all requirements to accept quest
    
    Returns: True if can accept, False otherwise
    Does NOT raise exceptions - just returns boolean
    """
    # TODO: Implement requirement checking
    # Check all requirements without raising exceptions
    quest_dict = quest_data_dict[quest_id]
    if character["level"] >= quest_dict["level"]:
        if quest_dict["prerequisite"] in character["completed_quests"]:
            if (quest_dict not in character["completed_quests"]) and (quest_dict not in character["active_quests"]):
                return True
    else:
        return False

def get_quest_prerequisite_chain(quest_id, quest_data_dict):
    """
    Get the full chain of prerequisites for a quest
    
    Returns: List of quest IDs in order [earliest_prereq, ..., quest_id]
    Example: If Quest C requires Quest B, which requires Quest A:
             Returns ["quest_a", "quest_b", "quest_c"]
    
    Raises: QuestNotFoundError if quest doesn't exist
    """
    # TODO: Implement prerequisite chain tracing
    # Follow prerequisite links backwards
    # Build list in reverse order
    quest_prerequisites = []
    for quest in range(len(quest_data_dict[quest_id]["prerequisite"])):
        quest_prerequisites.append(quest_data_dict[quest_id]["prerequisite"][-1])
    return quest_prerequisites

# ============================================================================
# QUEST STATISTICS
# ============================================================================

def get_quest_completion_percentage(character, quest_data_dict):
    """
    Calculate what percentage of all quests have been completed
    
    Returns: Float between 0 and 100
    """
    # TODO: Implement percentage calculation
    # total_quests = len(quest_data_dict)
    # completed_quests = len(character['completed_quests'])
    # percentage = (completed / total) * 100
    total_quests = len(quest_data_dict)
    completed_quests = len(character["completed_quests"])
    percentage = (completed_quests / total_quests) * 100
    return percentage

def get_total_quest_rewards_earned(character, quest_data_dict):
    """
    Calculate total XP and gold earned from completed quests
    
    Returns: Dictionary with 'total_xp' and 'total_gold'
    """
    # TODO: Implement reward calculation
    # Sum up reward_xp and reward_gold for all completed quests
    total_xp = 0
    total_gold = 0
    for quest in character["completed_quests"]:
        total_xp += quest_data_dict[quest]["xp_amount"]
        total_gold += quest_data_dict[quest]["gold"]
    return {"total_xp": total_xp, "total_gold": total_gold}

def get_quests_by_level(quest_data_dict, min_level, max_level):
    """
    Get all quests within a level range
    
    Returns: List of quest dictionaries
    """
    # TODO: Implement level filtering
    quest_list = []
    for quest in quest_data_dict:
        if min_level <= quest["level"] <= max_level:
            quest_list.append(quest)
    return quest_list

# ============================================================================
# DISPLAY FUNCTIONS
# ============================================================================

def display_quest_info(quest_data):
    """
    Display formatted quest information
    
    Shows: Title, Description, Rewards, Requirements
    """
    # TODO: Implement quest display
    print(f"\n=== {quest_data['title']} ===")
    print(f"Description: {quest_data['description']}")
    # ... etc
    print(f"Rewards: {quest_data["rewards"]}")
    print(f"Requirements: {quest_data["requirements"]}")

def display_quest_list(quest_list):
    """
    Display a list of quests in summary format
    
    Shows: Title, Required Level, Rewards
    """
    # TODO: Implement quest list display
    print(f"Title: {quest_list[0]} | Required Level: {quest_list[1]} | Rewards: {quest_list[2]}")

def display_character_quest_progress(character, quest_data_dict):
    """
    Display character's quest statistics and progress
    
    Shows:
    - Active quests count
    - Completed quests count
    - Completion percentage
    - Total rewards earned
    """
    # TODO: Implement progress display
    print(f"{character["name"]}")
    print(f"Active quests: {character["active_quests"]}")
    print(f"Completed quests: {character["completed_quests"]}")
    print(f"Completion percentage: {character["completion_total"]}")
    print(f"Total rewards earned: {character["total_rewards_earned"]}")

# ============================================================================
# VALIDATION
# ============================================================================

def validate_quest_prerequisites(quest_data_dict):
    """
    Validate that all quest prerequisites exist
    
    Checks that every prerequisite (that's not "NONE") refers to a real quest
    
    Returns: True if all valid
    Raises: QuestNotFoundError if invalid prerequisite found
    """
    # TODO: Implement prerequisite validation
    # Check each quest's prerequisite
    # Ensure prerequisite exists in quest_data_dict
    for quest in quest_data_dict:
        for prerequisites in quest_data_dict[quest]["prerequisite"]:
            if prerequisites == "NONE":
                continue
            elif prerequisites in quest_data_dict:
                continue
            else:
                raise QuestNotFoundError
    return True


# ============================================================================
# TESTING
# ============================================================================

if __name__ == "__main__":
    print("=== QUEST HANDLER TEST ===")
    
    # Test data
    # test_char = {
    #     'level': 1,
    #     'active_quests': [],
    #     'completed_quests': [],
    #     'experience': 0,
    #     'gold': 100
    # }
    #
    # test_quests = {
    #     'first_quest': {
    #         'quest_id': 'first_quest',
    #         'title': 'First Steps',
    #         'description': 'Complete your first quest',
    #         'reward_xp': 50,
    #         'reward_gold': 25,
    #         'required_level': 1,
    #         'prerequisite': 'NONE'
    #     }
    # }
    #
    # try:
    #     accept_quest(test_char, 'first_quest', test_quests)
    #     print("Quest accepted!")
    # except QuestRequirementsNotMetError as e:
    #     print(f"Cannot accept: {e}")

