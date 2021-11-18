antw1 = input()
antw2 = input()

if antw1 == "ja":
    if antw2 == "ja":
        print("2")
    else:
        print('1')
else:
    if antw2 == "ja":
        print('1')
    else:
        print('5')
