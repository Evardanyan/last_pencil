import random

def pencil_logic(pencils: int, losing: list) -> int:
    if pencils == 1:
        return 1
    return next((i for i in range(1, 4) if pencils - i in losing), random.choice([1, 2, 3]))

def get_pencils() -> int:
    while True:
        try:
            pencils = int(input("How many pencils would you like to use: "))
            if pencils > 0:
                return pencils
            print("The number of pencils should be positive")
        except ValueError:
            print("The number of pencils should be numeric")

def get_starting_player(players: list) -> str:
    while True:
        starting_player = input(f"Who will be the first ({', '.join(players)}): ")
        if starting_player in players:
            return starting_player
        print(f"Choose between {', '.join(players)}")

def calculate_losing_positions(pencils: int) -> list:
    return [i for i in range(1, pencils + 1) if i % 4 == 1]

def main():
    players = ["John", "Jack"]
    allowed_amounts = ["1", "2", "3"]

    pencils = get_pencils()
    losing_positions = calculate_losing_positions(pencils)
    current_player = get_starting_player(players)

    while pencils > 0:
        print("|" * pencils)
        print(f"{current_player}'s turn!")

        if current_player == "Jack":
            remove_pencils = pencil_logic(pencils, losing_positions)
            print(remove_pencils)
        else:
            while True:
                remove_pencils = input(" ")
                if not remove_pencils.isdigit() or remove_pencils not in allowed_amounts:
                    print("Possible values: '1', '2' or '3'")
                elif int(remove_pencils) > pencils:
                    print("Too many pencils were taken")
                else:
                    remove_pencils = int(remove_pencils)
                    break

        pencils -= remove_pencils
        current_player = players[1] if current_player == players[0] else players[0]

    print(f"{current_player} won!")

if __name__ == "__main__":
    main()
