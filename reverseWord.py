def reverse_sentence(s):
    words = s.split()
    reversed_words = words[::-1]
    return ' '.join(reversed_words)

def main():
    user_input = input("Enter a string containing multiple words: ")
    result = reverse_sentence(user_input)
    print("Reversed order of words:", result)

if __name__ == "__main__":
    main()

    