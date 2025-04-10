def generate_fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    fib_sequence = [1, 1]
    for _ in range(n - 2):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    
    return fib_sequence

def main():
    try:
        num = int(input("Enter the number of Fibonacci numbers to generate: "))
        if num < 0:
            print("Please enter a positive integer.")
        else:
            print("Fibonacci Sequence:", generate_fibonacci(num))
    except ValueError:
        print("Invalid input! Please enter a valid integer.")

if __name__ == "__main__":
    main()
