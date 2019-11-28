user_input = input("Enter a number of your choice:- ")
length = len((user_input))
temp = [None] * 10
for j in range (0,10):
    temp[j] = 0
 
for i in range(0,length):
    if user_input[i] == "0":
        temp[0] += 1
    if user_input[i] == "1":
        temp[1] += 1
    if user_input[i] == "2":
        temp[2] += 1
    if user_input[i] == "3":
        temp[3] += 1
    if user_input[i] == "4":
        temp[4] += 1
    if user_input[i] == "5":
        temp[5] += 1
    if user_input[i] == "6":
        temp[6] += 1
    if user_input[i] == "7":
        temp[7] += 1
    if user_input[i] == "8":
        temp[8] += 1
    if user_input[i] =="9":
        temp[9] += 1
print(f"The frecqucny of number 0 is {temp[0]} ")
print(f"The frecqucny of number 1 is {temp[1]}")
print(f"The frecqucny of number 2 is {temp[2]}")
print(f"The frecqucny of number 3 is {temp[3]}")
print(f"The frecqucny of number 4 is {temp[4]}")
print(f"The frecqucny of number 5 is {temp[5]}")
print(f"The frecqucny of number 6 is {temp[6]}")
print(f"The frecqucny of number 7 is {temp[7]}")
print(f"The frecqucny of number 8 is {temp[8]}")
print(f"The frecqucny of number 9 is {temp[9]}")