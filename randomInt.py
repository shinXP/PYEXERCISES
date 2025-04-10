import random

a = random.randint(1, 9)
attempts = 3

for guess in range(attempts):
	guess == int(input("What is you guess?  "))
	if guess == a:
		print("Exactly Right!")
		break
	elif guess > a:
		print("Too High!")
	elif guess < a:
		print('Too Low!')
	else:
		print("BOBO!")
  
else:
    print("\nYou Lose!")