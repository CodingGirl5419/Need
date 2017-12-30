start = '''
You will be asked a series of questions about the book with multiple choice answers.
'''

print(start)

#c = True
#if c == False;
#print("Incorrect")

correct = 0
#incorrect = 0

print("What is the setting of the story?")
print("a. New York/21st century, b. Washington D.C./21st century, c. Nottawa, Wisconsin/21st century")
user_input = input()
if user_input == "c":
    print("Correct! Press 'enter' to move on to the next question.")
    correct = correct + 1
else:
    print("Incorrect. Press 'enter' to move on to the next question.")
user_input = input()
print("Who was the main character?")
print("a. Dr. Jain, b. DJ, c. Kaylee")
user_input = input()
if user_input == "c":
    print("Correct! Press 'enter' to move on to the next question.")
    correct = correct + 1
else:
     print("Incorrect. Press 'enter' to move on to the next question.")
user_input = input()
print("What was Kaylee's brother's name?")
print("a. TJ, b. DJ, c. Danny")
user_input = input()
if user_input == "b":
    print("Correct! Press 'enter' to move on to the next question.")
    correct = correct + 1
else:
    print("Incorrect. Press 'enter' to move on to the next question.")
user_input = input()
print("Who was behind NEED?")
print("a. Nate, b. Kaylee, c. Dr. Jain")
user_input = input()
if user_input == "c":
    print("Correct! Press 'enter' to move on to the next question.")
    correct = correct + 1
else:
    print("Incorrect. Press 'enter' to move on to the next question.")
user_input = input()
print("Why did Nate betray Kaylee to help NEED?")
print("a. Because he did not want Kaylee to find out he was a kidney match for DJ")
print("b. Because he hated Kaylee")
print("c. Because NEED would give him a million dollars")
user_input = input()
if user_input == "a":
    print("Correct! Press 'enter' to move on to the next question.")
    correct = correct + 1
else:
    print("Incorrect. Press 'enter' to move on to the next question.")
user_input = input()
print("What was the intended purpose behind NEED?")
print("a. To secretly film the whole experiment and give it to the government for profit")
print("b. A social experiment that would help keep the country safe in the future")
print("c. To give free gifts to teenagers")
user_input = input()
if user_input == "b":
    print("Correct!")
    correct = correct + 1
else:
    print("Incorrect")
print("--------------------------------------")
print("Yay! Quiz is over!")
print("You got", (correct), "out of 6 correct")
