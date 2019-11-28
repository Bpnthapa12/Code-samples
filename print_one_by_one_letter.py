temp = []
ask = int(input("Enter how many name do you want to enter? "))
for i in range(1,ask+1):
    ask_2 = input(f"Enter {i} name:- ")
    temp.append(ask_2)
print(temp)
for j in temp:
    length = len(j)
    print("")
    for k in range(0,length):
        print(j[k])
