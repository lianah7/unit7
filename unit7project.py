# by Liana Hill
# last updated November 12, 2019
# unit 7 project assignment

alphabet = "abcdefghijklmnopqrstuvwxyz"
encoded_word = []


def shift():
    user_shift = int(input("How many letters do you want to shift the alphabet?"))
    first = alphabet[0:user_shift]
    last = alphabet[user_shift:]
    alphabet_two = last + first
    return alphabet_two


def encode(new_alphabet):
    user_word = input("Please enter a word to encode")
    user_word = user_word.lower()
    for letter in user_word:
        position = alphabet.index(letter)
        final_position = new_alphabet[position]
        encoded_word.append(final_position)
        final_encoded = "".join(encoded_word)
    print(final_encoded)


def main():
    new_alphabet = shift()
    user_input = input("Press 'e' to encode, 'd' to decode, or 'q' o quit")
    if user_input == 'e':
    encode(new_alphabet)


main()