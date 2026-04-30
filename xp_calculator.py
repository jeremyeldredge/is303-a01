"""
Jeremy Eldredge
IS 303 - A01

XP Calculator
This program calculates the number of gaming sessions needed to reach a certain XP goal. The user is prompted to enter their current XP, the XP they earn per session, and their target XP. The program then calculates and displays the number of sessions needed to reach the target XP.

Inputs:
- Player name
- Current XP
- XP earned per session
- Target XP

Processes:
- Calculate the number of sessions needed to reach the target XP

Outputs:
- Player name
- Current XP
- XP earned per session
- Target XP
- Number of sessions needed to reach the target XP
"""
# inputs
player_name = input("Enter your player name: ")
current_xp = int(input("Enter your current XP: "))
xp_per_session = int(input("Enter the XP you earn per session: "))
target_xp = int(input("Enter your target XP: "))

# processes
sessions_needed = (target_xp - current_xp) / xp_per_session

# outputs
print(f"\nPlayer name: {player_name}")
print(f"Current XP: {current_xp}")
print(f"XP earned per session: {xp_per_session}")
print(f"Target XP: {target_xp}")
print(f"Number of sessions needed to reach the target XP: {sessions_needed:.2f}")