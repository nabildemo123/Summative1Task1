import random

def question():
    """
    Generates a random multiplication equation.

    Returns:
        - A tuple containing two random integers and their product.
        - num_1(int): The first random integer.
        - num_2(int): The second random integer.
        - answer(int): The product of num_1 and num_2.
    """

    num_1 = random.randint(1, 10)
    num_2 = random.randint(1, 10)
    answer = num_1 * num_2
    return num_1, num_2, answer
    
def bonus_question():
    """
    Generates a random division equation.

    Returns:
        - A tuple containing two random integers and their quotient.
        - num_1(int): A random number between 10 and 20.
        - num_2(int): A random number between 1 and 2.
        - answer(float): The quotient of num_1 and num_2.
    """

    num_1 = random.randint(10,20)
    num_2 = random.randint(1,2)
    answer = num_1 / num_2 
    return num_1, num_2, answer

def get_valid_input(prompt):
    """
    Prompt the user for input and validate if it is an integer.

    Args:
        prompt(str): The message displayed to the user.
    Returns:
        user_input(int): A valid integer entered by the user.
    Raises:
        ValueError: If the input cannot be converted to an integer (handled internally).
    """

    
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter an integer.")