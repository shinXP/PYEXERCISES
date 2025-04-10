import secrets

def generate_password(length=12):
    lowercase = 'abcdefghijklmnopqrstuvwxyz'
    uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numbers = '0123456789'
    symbols = '!@#$%^&*()_+-=[]{}|;:,.<>?'

    # Ensure at least one character from each category (cryptographically secure)
    password_chars = [
        secrets.choice(lowercase),
        secrets.choice(uppercase),
        secrets.choice(numbers),
        secrets.choice(symbols)
    ]

    # Combine all characters for remaining length
    all_chars = lowercase + uppercase + numbers + symbols
    remaining_length = length - 4

    # Add secure random choices
    password_chars += [secrets.choice(all_chars) for _ in range(remaining_length)]

    # Cryptographically secure shuffle using Fisher-Yates algorithm
    for i in range(len(password_chars) - 1, 0, -1):
        j = secrets.randbelow(i + 1)
        password_chars[i], password_chars[j] = password_chars[j], password_chars[i]

    return ''.join(password_chars)


def main():
    print("Secure Password Generator")
    while True:
        choice = input("\nGenerate new password? (y/n): ").lower()
        if choice == 'n':
            print("Security tip: Always store passwords securely!")
            break
        elif choice == 'y':
            try:
                length = max(int(input("Length (12+ recommended): ").strip() or 12), 4)
            except ValueError:
                length = 12
            print(f"\nGenerated Password: {generate_password(length)}")
            print("Warning: This password appears only once. Save it securely!")
        else:
            print("Invalid choice - please enter 'y' or 'n'")


if __name__ == "__main__":
    main()