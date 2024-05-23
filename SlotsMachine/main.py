import random
import emoji

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_values = {
    "cherry": 10,
    "lemon": 20,
    "orange": 30,
    "plum": 40,
    "bell": 50,
    "bar": 100,
    "7": 200
}

symbol_count = {
    "cherry": 2,
    "lemon": 3,
    "orange": 4,
    "plum": 7,
    "bell": 4,
    "bar": 3,
    "7": 2

}

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, count in symbols.items():
        for _ in range(count):
            all_symbols.append(symbol)
    
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()

def deposit():
    while True:
        amount = input("Enter the amount you want to deposit: $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                print(f"Deposited ${amount}")
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a valid amount.")

    return amount

def get_number_of_lines():
    while True:
        lines = input(f"Enter the number of lines you want to bet on: (1- {MAX_LINES} )? ")
        if lines.isdigit():
            lines = int(lines)
            if lines > 0 and lines <= MAX_LINES:
                print(f"Playing {lines} lines.")
                break
            else:
                print(f"Number of lines must be between 1 and {MAX_LINES}.")
        else:
            print("Please enter a valid number of lines.")

    return lines

def get_bet():
    while True:
        bet = input(f"Enter the amount you want to bet (${MIN_BET}-{MAX_BET}): ")
        if bet.isdigit():
            bet = int(bet)
            if bet >= MIN_BET and bet <= MAX_BET:
                print(f"Betting ${bet}.")
                break
            else:
                print(f"Bet must be between ${MIN_BET} and ${MAX_BET}.")
        else:
            print("Please enter a valid bet.")

    return bet

def get_payout(columns, lines, bet, values):
    payout = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            payout += values[symbol] * bet
            winning_lines.append(line + 1)
    
    return payout, winning_lines

def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = lines * bet

        if total_bet > balance:
            print(f"Insufficient funds. Your balance is ${balance}. Please enter a lower bet.")
            continue
        else:
            balance -= total_bet
            break
    
    print(f"Balance: ${balance}, Lines: {lines}, Bet: ${bet} Total Bet: ${total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    payout, winning_lines = get_payout(slots, lines, bet, symbol_values)
    print(f"winning lines: ", *winning_lines)
    print(f"You won: ${payout}")
    return payout - total_bet

def main():
    balance = deposit()
    while True:
        print(f"Current balance: ${balance}")
        if balance == 0:
            print("You are out of money.")
            break
        play_again = input("Do you want to play? (yes/no) (q to quit): ").lower()
        if play_again == "q":
            break
        if play_again != "yes":
            break
        balance += spin(balance)
    
    
main()