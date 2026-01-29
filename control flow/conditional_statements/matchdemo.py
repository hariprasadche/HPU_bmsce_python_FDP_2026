fruit = input("enter fruit name: ")
match fruit:
    case "apple":
        print("you have given apple")
    case "banana":
        print("you have given banana")
    case _:
        print("invalid input")
