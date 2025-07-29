# Find the treasure game
import random

# Generar ubicación del tesoro y bombas sin solaparse
while True:
    treasure_location = random.randint(1, 100)
    bombs = random.sample(range(1, 101), 10)
    if treasure_location not in bombs:
        break

def render_path(treasure_location, bombs, player_location=None):
    path = ["-" for _ in range(100)]

    # Colocar bombas
    for bomb in bombs:
        if 1 <= bomb <= 100:
            path[bomb - 1] = "*"

    # Colocar tesoro
    if 1 <= treasure_location <= 100:
        path[treasure_location - 1] = "0"

    # Colocar jugador (opcional)
    if player_location is not None and 1 <= player_location <= 100:
        path[player_location - 1] = "P"

    # Mostrar el camino
    print("".join(path))

print("*** Welcome to the treasure adventure! ***")
print("Your goal is to reach the treasure without stepping on bombs.")
print("Good luck!\n")

player_location = 0
isWinner = False

render_path(treasure_location, bombs, player_location)

while not isWinner:
    print(f"\nYou're at position {player_location}")
    print("Choose a number between 1 and 5 to jump")

    try:
        salto = int(input("Now jump: "))
        if salto < 1 or salto > 5:
            print("Only jumps between 1 and 5 are allowed.")
            continue
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    player_location += salto

    if player_location > 100:
        print("You went out of the map. You lose!")
        break
    elif player_location == treasure_location:
        print("You found the treasure! You win!")
        render_path(treasure_location, bombs, player_location)
        break
    elif player_location in bombs:
        print("You stepped on a bomb. You lose!")
        render_path(treasure_location, bombs, player_location)
        break
    else:
        print("You're safe... for now.")
        render_path(treasure_location, bombs, player_location)
