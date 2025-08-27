number = 7

match number:
    case x if x > 0:
        print("Positive")
    case x if x < 0:
        print("Negative")
    case _:
        print("Zero")
