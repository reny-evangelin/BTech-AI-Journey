age = int(input("Enter your age: "))
budget = int(input("Enter the Budget: "))
if age >= 18 and budget >= 500:
    print("You can watch an R-Rated Action Movie in IMAX!")
elif age >= 18 and budget < 500:
    print("You can watch an R-Rated Indie Movie on your laptop")
elif age < 18 and budget >= 300:
    print("You can watch an Animated Blockbuster in the theater")
else:
    print("Stay home and watch YouTube for free!")
