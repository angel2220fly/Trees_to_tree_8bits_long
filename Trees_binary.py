# Ask the user to enter a binary string
T8 = input("Enter a binary number (e.g., 11111111): ")

# Convert the binary string T8 to a decimal integer
num = int(T8, 2)  # Convert binary to decimal
print(f"Converted binary {T8} to decimal: {num}")

# Initial calculation
finish = 0
times = 0
binary_representation_before = len(format(num, '01b'))
print("binary_representation_before_long")
print(binary_representation_before)

# Main loop to calculate binary representations
while finish != 1:
    if num > 1000000000:
        print("This number is too big!")  
    elif num < 0:
        print("Please enter a non-negative integer.")
    else:
        max_length = len(format(num, 'b'))
        binary_numbers = []

        # Generate binary numbers of lengths 1 to max_length
        for length in range(1, max_length + 1):
            for i in range(2 ** length):
                binary_numbers.append(format(i, '0' + str(length) + 'b'))

        # Find the largest binary number less than or equal to the given number
        last_binary = None
        for index, binary in enumerate(binary_numbers):
            if index > num:
                break
            last_binary = (binary, index)

        if last_binary:
            binary_representation, index = last_binary
            print(f"{binary_representation}: {index}")
            binary_to_number = int(binary_representation, 2)
            binary_representation = format(binary_to_number, '01b')
            num = binary_to_number
            binary_to_number_number_after = binary_to_number
            print("binary_to_number")
            print(binary_to_number)

            length_tree = len(binary_representation)
            times += 1
            print("times")
            print(times)
            print("length_tree")
            print(str(length_tree))

            if length_tree < 9:
                finish = 1
                length_tree_after = length_tree
                times_after = times
                binary_representation_before_long = binary_representation_before
        else:
            print("No valid binary representation found.")

# Continuation: another loop to perform further calculations
finish = 0
finish1 = 0
times = 0
count_number = 0

while finish1 != 1:
    num = count_number
    binary_representation_before = len(format(num, '01b'))
    finish = 0
    times = 0
    while finish != 2:
        if num < 0:
            print("Please enter a non-negative integer.")
        else:
            max_length = len(format(num, 'b'))
            binary_numbers = []

            for length in range(1, max_length + 1):
                for i in range(2 ** length):
                    binary_numbers.append(format(i, '0' + str(length) + 'b'))

            last_binary = None
            for index, binary in enumerate(binary_numbers):
                if index > num:
                    break
                last_binary = (binary, index)

            if last_binary:
                binary_representation, index = last_binary
                binary_to_number = int(binary_representation, 2)
                binary_representation = format(binary_to_number, '01b')
                num = binary_to_number

                length_tree = len(binary_representation)
                times += 1

                if length_tree < 9:
                    count_number += 1
                    finish = 2

                if (length_tree < 9 and 
                    binary_representation_before == binary_representation_before_long and 
                    times_after == times and 
                    length_tree_after == length_tree and 
                    binary_to_number_number_after == binary_to_number):
                    
                    finish1 = 1
                    
                    print("binary_representation_before_long")
                    print(binary_representation_before_long)
                    print("times_after")
                    print(times_after)
                    print("length_tree_after")
                    print(length_tree_after)
                    print("binary_to_number_number_after")
                    print(binary_to_number_number_after)
                    print("count_number")
                    count_number -= 1
                    print(count_number)
            else:
                print("No valid binary representation found.")