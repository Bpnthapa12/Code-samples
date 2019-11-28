user_input = input("Enter a number of your choice:- ")
length = len((user_input))
a = 0
b = 0
d = 0
e = 0
f = 0
g = 0
h = 0
c = 0
j = 0
k =0
for i in range(0,length):
    if user_input[i] == "0":
        a += 1
    if user_input[i] == "1":
        b += 1
    if user_input[i] == "2":
        d += 1
    if user_input[i] == "3":
        e += 1
    if user_input[i] == "4":
        f += 1
    if user_input[i] == "5":
        g += 1
    if user_input[i] == "6":
        h += 1
    if user_input[i] == "7":
        c += 1
    if user_input[i] == "8":
        j += 1
    if user_input[i] =="9":
        k += 1
print(f"The frecqucny of number 0 is {a} ")
print(f"The frecqucny of number 1 is {b}")
print(f"The frecqucny of number 2 is {d}")
print(f"The frecqucny of number 3 is {e}")
print(f"The frecqucny of number 4 is {f}")
print(f"The frecqucny of number 5 is {g}")
print(f"The frecqucny of number 6 is {h}")
print(f"The frecqucny of number 7 is {c}")
print(f"The frecqucny of number 8 is {j}")
print(f"The frecqucny of number 9 is {k}")