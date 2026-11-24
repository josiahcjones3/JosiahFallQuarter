prompt = input("Do you want to print the list Y/N? ")
geniuses = ["jahlil", "noah", "elijah", "tc", "kevin"]

while prompt == "Y":
    for genius in geniuses:
        print(genius)
    prompt = input("Do you want me to print the list again Y/N? ")