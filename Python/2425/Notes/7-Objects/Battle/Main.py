from Character import Droid, RebelSoldier, Wookie
from Enemies import Sith, Empire
import random

print("Welcome to the Star Wars Adventure Game!")
print("Choose your character:")
print("1. Droid")
print("2. Rebel Soldier")
print("3. Wookie")
choice = input("Enter the number of your choice: ")
if choice == "1":
    player = Droid()
elif choice == "2":
    player = RebelSoldier()
elif choice == "3":
    player = Wookie("Player")
else:
    print("Invalid choice. Exiting game.")
    exit()
print(f"\nYou chose {player.name} (Health: {player.health}, Attack: {player.attack}, Defense: {player.defense})")

while player.isAlive():
    print("\nYou explore a distant world controlled by the Empire...")
    input("Press Enter to continue or type 'quit' to exit: ")
    if not player.isAlive():
        print("You have fallen in battle. Game over.")
        break
    enemy = random.choice([Sith(), Empire()])
    print(f"\nA wild {enemy.name} appears!")
    while enemy.isAlive() and player.isAlive():
        print(f"\n{player.name} (Health: {player.health}) vs {enemy.name} (Health: {enemy.health})")
        print("1. Attack")
        if isinstance(player, Droid):
            print("2. Recharge")
        elif isinstance(player, RebelSoldier):
            print("2. Throw Grenade")
        elif isinstance(player, Wookie):
            print("2. Rage Attack")
        print("3. Retreat")
        action = input("Choose your action: ")
        if action == "1":
            damage = player.attack
            enemyDamage = enemy.takeDamage(damage)
            print(f"You dealt {enemyDamage} damage to {enemy.name}.")
        elif action == "2":
            if isinstance(player, Droid):
                recharge = player.recharge()
                print(f"You recharged and regained {recharge} health.")
            elif isinstance(player, RebelSoldier):
                grenadeDamage = player.grenadeThrow()
                enemyDamage = enemy.takeDamage(grenadeDamage)
                print(f"You threw a grenade and dealt {enemyDamage} damage to {enemy.name}.")
            elif isinstance(player, Wookie):
                rageDamage = player.rageAttack()
                enemyDamage = enemy.takeDamage(rageDamage)
                print(f"Your rage attack dealt {enemyDamage} damage to {enemy.name}.")
        elif action == "3":
            print("You retreated from the battle.")
            break
        else:
            print("Invalid action.")
        if enemy.isAlive():
            damage = enemy.attack
            playerDamage = player.takeDamage(damage)
            print(f"{enemy.name} attacked you! You took {playerDamage} damage.")
    if player.isAlive() and not enemy.isAlive():
        print(f"\nCongratulations! You defeated {enemy.name}!")
    if not player.isAlive():
        print("\nYou have fallen in battle. Game over.")
        break
print("\nThanks for playing! May the Force be with you!")









