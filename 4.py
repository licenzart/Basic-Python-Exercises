#Count the specific letter in a data #Practice exercise basic coding

alphabet = input("What letter you want to count for the frequency?\n")
oritext = input("Please enter the text you want to search.\n")
lowalphabet = alphabet.lower()
text = oritext.lower()

print("This is your text",text)
print("This is the letter you want to search is", alphabet)
import time
time.sleep(3)

count = 0
for letter in text:
	if letter == lowalphabet:
		count = count + 1
print("The letter occurs", count, "times")