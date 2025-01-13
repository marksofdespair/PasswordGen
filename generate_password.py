import random
import string
import argparse

def generate_password(length=12, use_uppercase=True, use_numbers=True, use_symbols=True):
    # Defines character pools
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase if use_uppercase else ""
    numbers = string.digits if use_numbers else ""
    symbols = string.punctuation if use_symbols else ""
    
    all_characters = lower + upper + numbers + symbols
    if not all_characters:
        raise ValueError("No character sets selected for password generation.")
    
    # Ensures at least one character from each selected pool
    password = []
    if use_uppercase: password.append(random.choice(upper))
    if use_numbers: password.append(random.choice(numbers))
    if use_symbols: password.append(random.choice(symbols))
    password += random.choices(all_characters, k=length - len(password))
    
    # Shuffles to avoid predictable patterns
    random.shuffle(password)
    return ''.join(password)

def main():
    parser = argparse.ArgumentParser(description="Generate a secure password.")
    parser.add_argument("-l", "--length", type=int, default=12, help="Length of the password (default: 12).")
    parser.add_argument("--no-uppercase", action="store_true", help="Exclude uppercase letters.")
    parser.add_argument("--no-numbers", action="store_true", help="Exclude numbers.")
    parser.add_argument("--no-symbols", action="store_true", help="Exclude symbols.")
    
    args = parser.parse_args()
    
    try:
        password = generate_password(
            length=args.length,
            use_uppercase=not args.no_uppercase,
            use_numbers=not args.no_numbers,
            use_symbols=not args.no_symbols,
        )
        print("Generated Password:", password)
    except ValueError as e:
        print("Error:", e)

if __name__ == "__main__":
    main()

# first run generated passwords like _#L15sXHlwo<, ~mtr4E1YC%z', and Yff|?SR7B%r3
