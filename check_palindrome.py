# This program is written in Python programming language to check th given word is equal or not if reversed (in short palindrome.)

word = input("Enter a word you want:- ")
length = len(word)
second = ""
for i in range(length-1,-1,-1):
    second += word[i]
if word == second:
    print(f"The word {word.upper()} is palindrome")
else:
    print(f"The word {word.upper()} is not palidrome")