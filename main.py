import random
secret_number = random.randint(1, 50)
lives = 5
heading = "Welcome to the number guessing game" #35
print(heading.title().center(55, '~'))
print('Guess a number between 1 to 50')
print("Rules: you will have 5 chances to guess the right number. Only numbers are valid")
user_input = input("Type your number: ")
while True:
	if user_input:
		if (" ") in user_input:
			print("Spaces are invalid!")
			user_input = input("Type your number: ")
		else:
			try:
				# ui = int(user_input)
				user_input = int(user_input)
				if user_input != secret_number:
					lives -= 1
					if user_input < secret_number:
						print(f"Your guessed number {user_input} is less than the secret number!")
						if lives == 0 and user_input != secret_number:
							print("Your lives are over. \nYou loss the game!😭")
							print(f"The secret number was: {secret_number}")
							break
						if lives == 1:
							print(f"Now you have {lives} live only!")
						else:
							print(f"Now you have {lives} lives!")
						user_input = input("Try again: ")
						# if lives == 1 and user_input != secret_number:
						# 	print("Your lives are over. \nYou loss the game!😭")
						# 	print(f"The secret number was: {secret_number}")
						# 	break
						
					elif user_input > secret_number:
						print(f"Your guessed number {user_input} is greater than the secret number!")
						if lives == 0 and user_input != secret_number:
							print("Your lives are over. \nYou loss the game!😭")
							print(f"The secret number was: {secret_number}")
							break
						if lives == 1:
							print(f"Now you have {lives} live only!")	
						else:
							print(f"Now you have {lives} lives!")
						user_input = input("Try again: ")
						# if lives == 1 and user_input != secret_number:
						# 	print("Your lives are over. \nYou loss the game!😭")
						# 	print(f"The secret number was: {secret_number}")
						# 	break
				else:
					print("🎉Congrates you guessed the correct number!🎉")
					break
			except:
				print("Strings are not allowed!")
				user_input = input("Type your number: ")
	else:
			print("You didn't type anything!")
			user_input = input("Type your number: ")
	# if lives == 1 and user_input != secret_number:
	# 	print("Your lives are over. \nYou loss the game!😭")
	# 	print(f"The secret number was: {secret_number}")
	# 	break
