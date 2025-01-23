import random

def generate_word(vowel):
    match vowel:
        case 'a':
            return random.choice(["apple", "ant", "anchor", "astronaut"])
        case 'e':
            return random.choice(["elephant", "eagle", "engine", "envelope"])
        case 'i':
            return random.choice(["igloo", "island", "ice", "iron"])
        case 'o':
            return random.choice(["orange", "octopus", "owl", "oxygen"])
        case 'u':
            return random.choice(["umbrella", "unicorn", "uranium", "uniform"])
        case _:
            return "Please enter a valid vowel (a, e, i, o, u)"

# Example usage
print("Type quit to Terminate the program")
while True:
    user_input = input("\nEnter a vowel: ").lower()
    if user_input == "quit":
        break
    else:
        word = generate_word(user_input)
        print(f"Generated word: {word}")
