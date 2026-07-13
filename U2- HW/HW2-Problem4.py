# Problem 4: Season Classifier

while True:
    # INPUT
    entry = input("Enter month number (1-12) or 'exit' to finish: ")
    if entry.lower() == "exit":
        break
    month = int(entry)

    # PROCESS
    if month < 1 or month > 12:
        season = None
    elif month in (12, 1, 2):
        season = "Winter"
    elif month in (3, 4, 5):
        season = "Spring"
    elif month in (6, 7, 8):
        season = "Summer"
    else:
        season = "Fall"

    # OUTPUT
    if season is None:
        print("Invalid month. Please enter a number between 1 and 12.")
    else:
        print(season)