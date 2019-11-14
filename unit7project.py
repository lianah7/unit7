# by Liana Hill
# last updated November 12, 2019
# unit 7 project assignment

alphabet = "abcdefghijklmnopqrstuvwxyz"
encoded_word = []
decoded_word = []


def shift():
    """
    This functions shifts the alphabet the number of times the user chooses
    :return: new alphabet
    """
    user_shift = int(input("How many letters do you want to shift the alphabet? Pick a number between 0 - 26."))
    if user_shift > 26:

    first = alphabet[0:user_shift]
    last = alphabet[user_shift:]
    alphabet_two = last + first
    return alphabet_two


def encode():
    """
    This function uses the new shifted alphabet to encode the user's chosen word or sentence
    :return: nothing
    """
    new_alphabet = shift()
    user_encoded_word = input("Please enter a word to encode")
    user_encoded_word = user_encoded_word.lower()
    final_encoded = ""
    for letter in user_encoded_word:
        if letter not in alphabet:
            encoded_word.append(letter)
        else:
            position = alphabet.index(letter)
            final_position = new_alphabet[position]
            encoded_word.append(final_position)
            final_encoded = "".join(encoded_word)
    print(final_encoded)


def decode():
    """
    This function uses the shifted alphabet to decode the user's word or sentence
    :return: nothing
    """
    new_alphabet = shift()
    user_decoded_word = input("Please enter a word to decode")
    user_decoded_word = user_decoded_word.lower()
    final_decoded = ""
    for letter in user_decoded_word:
        if letter not in alphabet:
            decoded_word.append(letter)
        else:
            position = alphabet.index(letter)
            final_position = new_alphabet[position]
            decoded_word.append(final_position)
            final_decoded = "".join(decoded_word)
    print(final_decoded)


def main():
    while True:
        user_input = input("Press 'e' to encode, 'd' to decode, or 'q' to quit")
        if user_input == 'e':
            encode()
        elif user_input == 'd':
            decode()
        elif user_input == 'q':
            print("See you next time!")
            break


main()
