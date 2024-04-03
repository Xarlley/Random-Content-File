import random

def generate_random_numbers(size_in_bytes):
    numbers = [str(random.randint(0, 9)) for _ in range(size_in_bytes)]
    return ''.join(numbers)

def write_to_file(filename, content):
    with open(filename, 'w') as f:
        f.write(content)

def main():
    file_size_mb = 1
    file_size_bytes = file_size_mb * 1024 * 1024 * 2  # 1MB in bytes
    content = generate_random_numbers(file_size_bytes)
    filename = 'random_numbers.txt'
    write_to_file(filename, content)
    print(f"File '{filename}' with size {file_size_mb}MB generated successfully.")

if __name__ == "__main__":
    main()