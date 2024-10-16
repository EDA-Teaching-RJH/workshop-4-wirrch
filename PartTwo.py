def main():
    userInput = input("What drink would you like? : ").lower()
    match userInput:
        case "hot chocolate":
            print(f"Required moneyz = 120")
            transaction(120)
        case "tea":
            print(f"Required moneyz = 100")
            transaction(100)
        case _:
            print("Invalid drink")
            main()



def transaction(reqMoneyz):
    totalMoney = 0

    while totalMoney < reqMoneyz:
        userInput = int(input("Insert a pence coin: "))
        match userInput:
            case 50 | 20 | 10 | 5:
                totalMoney += userInput
        print(f"Total moneyz inserted: {totalMoney}")

    print(f"Change due: {totalMoney - 75}")


main()