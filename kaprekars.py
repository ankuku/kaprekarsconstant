"""
File: kaprekars.py
Author: Ankush
Description:
## Kaprekar's Constant
For any 4 digit number, sorting the digits in descending and ascending order, 
subtracting the smaller number from the larger repeatedly will eventually reach 
the Kaprekar's number, which is 6174, that too in 7 or less steps.
Let's see how this works!
"""

def kaprekar_step(num):
    # Convert the number to a string with 4 digits (at least 1 digit should be distinct from others)
    num_str = f"{num:04d}"
    
    # Sort digits in ascending order
    asc = ''.join(sorted(num_str))
    # print(f"The smallest number with these digits is {asc}.")
    
    # Sort digits in descending order
    desc = ''.join(sorted(num_str, reverse=True))
    # print(f"The largest number with these digits is {desc}.")
    
    # Convert back to integers
    asc_num = int(asc)
    desc_num = int(desc)
    
    # Perform the subtraction
    sub_num = desc_num - asc_num
    print(f"\t{desc_num} - {asc_num} = {sub_num}")
    return sub_num

def kaprekar_process(num):
    # Kaprekar's constant is 6174
    KAPREKAR_CONSTANT = 6174
    iterations = 0
    
    # Run a while loop until the output matches with Kaprekar's number
    while num != KAPREKAR_CONSTANT:
        num = kaprekar_step(num)
        iterations += 1
        print(f"Iteration #{iterations} result: {num}")
        
        # To prevent infinite loops in case of input with identical digits
        if num == 0:
            print("The process cannot proceed further (all digits are identical).")
            break
    
    if num == KAPREKAR_CONSTANT:
        print(f"Kaprekar's constant 6174 reached in {iterations} iterations.")
    else:
        print("Kaprekar's process could not be completed due to invalid input.")


if __name__ == "__main__":
    print("## Kaprekar's Constant ##\nFor any 4 digit number, sorting the digits in descending and ascending order,\nsubtracting the smaller number from the larger repeatedly will eventually reach\nthe Kaprekar's number, which is 6174, in 7 or less steps.\n\n")
    # Take user input
    user_input = input("Enter a 4-digit number: ")

    # Check if the input is a valid 4-digit number
    if len(user_input) == 4 and user_input.isdigit():
        print(f"Your input number is {user_input}.")
        num = int(user_input)
        kaprekar_process(num)
    else:
        print("Please enter a valid 4-digit number.")