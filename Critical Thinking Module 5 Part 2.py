books = int(input("Input the number of books purchased: "))

if books <= 1:
    print("You have been awarded 0 points")
elif books <= 3:
    print("You have been awarded 5 points")
elif books <= 5:
    print("You have been awarded 15 points")
elif books <= 7:
    print("You have been awarded 30 points")
else:
    print("You have been awarded 60 points")