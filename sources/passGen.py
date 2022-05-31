# Govine-J
# GITS
# 2022-05-31
from string import ascii_letters 
from random import shuffle

letters = [letter for letter in ascii_letters]
numbers = ['0','1','2','3','4','5','6','7','8','9']
special_chars = ['%', '&', '.', '$', '@', '#', '-']

# Randomizing the all three list. START
shuffle(letters)
shuffle(numbers)
shuffle(special_chars)
# Randomizing the all three list. END


def pass_generator(letter_count: int, special_char_count: int,number_count: int ) -> str:
    """ Take the user count for the amount of letter(s),
        number(s) and special char(s).

    Args:
        letter_count (int): The amount of letter needed in the password.
        special_char_count (int): The amount of special chars needed in the password.
        number_count (int): The amount of numbers needed in the password.

    Returns:
        str: generated password / pin / portpass key.
    """
   
    # Getting the password length. - START
    pass_length = sum([letter_count, special_char_count, number_count])
    # Getting the password length. - END

    # Generating the password based on the counts. - START
    gen_letters = []
    gen_numbers = []
    gen_chars = []

    loop_tracker = 0
    while loop_tracker != pass_length:
        
        if number_count != 0:
            for num in numbers:
                if num not in gen_numbers:
                    if len(gen_numbers) != number_count:
                        gen_numbers.append(num)
        
        if letter_count!= 0:
            for letter in letters:
                if letter not in gen_chars:
                    if len(gen_letters) != letter_count:
                        gen_letters.append(letter)
        
        if special_char_count != 0:
            for char in special_chars:
                if char not in gen_chars:
                    if len(gen_chars) != special_char_count:
                        gen_chars.append(char)
        
        loop_tracker += 1
    # Generating the password based on the counts. - END
   
    # Randomizing the generated password. - START
    generated_pass = gen_letters + gen_numbers + gen_chars
    shuffle(generated_pass)
    # Randomizing the generated password. - END

    # Convert the generated password into a string - START
    portpass_key = ''
    for char in generated_pass:
        portpass_key += char
    return portpass_key
    # Convert the generated password into a string - END
