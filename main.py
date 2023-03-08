import random

rock = "Rock"
paper = "Paper"
scissors = "Scissors"

player = input("Chose [r]ock, [p]aper or [s]cissors: ")

if player == "r":
  player = rock
elif player == "p":
  player = paper
elif player == "s":
  player = scissors
else:
  print("Invalid Input. Try again...")
  quit()

cpu_move = random.randint(1,3)
cpu = ""
if cpu_move == 1:
  cpu = rock
elif cpu_move == 2:
  cpu = paper
elif cpu_move == 3:
  cpu = scissors


if player == rock and cpu == scissors:
  print("You win!")
elif player == paper and cpu == rock:
  print("You win!")
elif player == scissors and cpu == paper:
  print("You win!")
elif player == cpu:
  print("Draw!")
else:
  print("You lose!")