day = input("Enter a day of the week: ").lower()

match day:
    case "monday" | "tuesday" | "wednesday" | "thursday" | "friday":
        print("It's a workday.")
    case "saturday" | "sunday":
        print("It's the holiday.")
    case _:
        print("Invalid day of the week.")
