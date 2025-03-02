import sys

if len(sys.argv) != 2:
    print("Usage: python word_count.py <file_path>")
    sys.exit(1)

file_path = sys.argv[1]

try:
    with open(file_path, 'r') as file:
        content = file.read()
        words = content.split()
        word_count = len(words)
        print(f"The file '{file_path}' contains {word_count} words.")
except FileNotFoundError:
    print(f"The file '{file_path}' does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")
