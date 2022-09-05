#Chinese Zodiac Sign Calculator
print("Welcome to Chinese Zodiac Sign Calculator!")
zodiac_sign = ["Monkey", "Chicken", "Dog", "Pig", "Rat","Cow", "Tiger", "Rabbit", "Dragon", "Snake", "Horse", "Goat"]
def calculator():
	while True:
		year = input("Please enter your year of birth.\n")
		try:
			year = int(year)
		except:
			print("Invalid input. Please enter a proper digit. ex 1962")
			continue
		zodiac_number = year % 12
		print("Your chinese zodiac is " + zodiac_sign[zodiac_number] +  ".")
		break
calculator()
#Continue or Stop
while True:
	ans = input("Do you want to continue? Y or N?")
	ans = ans.lower()
	if ans == "y":
		calculator()
	else:
		print("Thank you. The program will exit now. See you again!")
		break
