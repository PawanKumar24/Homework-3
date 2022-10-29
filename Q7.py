# Pawan Kumar
# ID: 2046222

tempDict = {}
print("Enter player 1's jersey number:", end ="\n")
jerseyNum = int(input())
print("Enter player 1's rating:",end ="\n")
tempDict[jerseyNum] = int(input())
print()
print("Enter player 2's jersey number:",end ="\n")
jerseyNum = int(input())
print("Enter player 2's rating:",end ="\n")
tempDict[jerseyNum] = int(input())
print()
print("Enter player 3's jersey number:",end ="\n")
jerseyNum = int(input())
print("Enter player 3's rating:",end ="\n")
tempDict[jerseyNum] = int(input())
print()
print("Enter player 4's jersey number:",end ="\n")
jerseyNum = int(input())
print("Enter player 4's rating:",end ="\n")
tempDict[jerseyNum] = int(input())
print()
print("Enter player 5's jersey number:",end ="\n")
jerseyNum = int(input())
print("Enter player 5's rating:",end ="\n")
tempDict[jerseyNum] = int(input())
print()

print("ROSTER")
values = []
for key in tempDict:
    values.append(key)
    pass
values.sort()
for key in values:
    print(f"Jersey number: {key}, Rating: {tempDict[key]}")

choice = ""

while choice != "q":
    print()
    print("MENU")
    print("a - Add player")
    print("d - Remove player")
    print("u - Update player rating")
    print("r - Output players above a rating")
    print("o - Output roster")
    print("q - Quit")
    print()
    print("Choose an option:")
    choice = input()
    if choice == "a":
        print("Enter a new player's jersey number:")
        jerseyNum = int(input())
        print("Enter the player's rating:")
        tempDict[jerseyNum] = int(input())
        values.append(jerseyNum)
        values.sort()
    elif choice == "u":
        print("Enter a jersey number:")
        jerseyNum = int(input())
        print("Enter a new rating for player:")
        if jerseyNum in values:
            tempDict[jerseyNum] = int(input())
            pass
    elif choice == "r":
        print("Enter a rating:")
        rate = int(input())
        print()
        print(f"ABOVE {rate}")
        for key in values:
            if tempDict[key] > rate:
                print(f"Jersey number: {key}, Rating: {tempDict[key]}")
                pass
            pass
    elif choice == "o":
        print("ROSTER")
        for key in values:
            print(f"Jersey number: {key}, Rating: {tempDict[key]}")
            pass
    elif choice == "d":
        print("Enter a jersey number:")
        jerseyNum = int(input())
        values.remove(jerseyNum)
        tempDict.pop(jerseyNum)
