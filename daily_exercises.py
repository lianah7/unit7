# by Liana Hill
# last updated November 6, 2019
# unit 7 daily exercises
#
# # problem one
# original = "abcdefghij"
# first = original[0:3]
# last = original[3:]
# final = first + last
# print(final)
#
#
# # problem two
# words = "Python"
# for character in words:
#     print(character)
#
#
# # problem three
# def without_end(word):
#     word = word[1: -1]
#     return word
#
#
# print(without_end("Hello"))
# print(without_end("python"))
# print(without_end("coding"))
#
#
# # problem four
# def longest(list_words):
#     longest_word = ""
#     for x in list_words:
#         if len(x) > len(longest_word):
#             longest_word = x
#     return longest_word
#
#
# print(longest(["cat", "dog", "horse"]))
#
#
# # problem five
# def upper_lower():
#     user_word = input("Enter a word")
#     print(user_word.upper())
#     print(user_word.lower())
#
# upper_lower()
#
#
# # problem six
# def title_case():
#     user_sentence = input("Please enter a sentence")
#     title_sentence = user_sentence.split(" ")
#     capital = []
#     for character in title_sentence:
#         capitalized_word = character[0].upper() + character[1:]
#         capital.append(capitalized_word)
#     joined = " ".join(capital)
#     return joined
#
#
# print(title_case())
#
#
# # problem seven
# def replace_four(your_sentence):
#     sentence = your_sentence.split(" ")
#     list_sentence = []
#     for character in sentence:
#         if len(character) == 4:
#             new_word = "#$%@"
#             list_sentence.append(new_word)
#         else:
#             list_sentence.append(character)
#     new_sentence = " ".join(list_sentence)
#     return new_sentence
#
#
# print(replace_four("Suzie is a nice person"))


# problem eight
def bubble_sort(names):
    for x in range(len(names)):

