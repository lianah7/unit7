# by Liana Hill
# last updated November 6, 2019
# unit 7 daily exercises


# problem one
original = "abcdefghij"
first = original[0:3]
last = original[3:]
final = first + last
print(final)


# problem two
words = "Python"
for character in words:
    print(character)


# problem three
def without_end(word):
    word = word[1: -1]
    return word


print(without_end("Hello"))
print(without_end("python"))
print(without_end("coding"))


# problem four
def longest(list_words):
    longest_word = ""
    for x in list_words:
        if len(x) > len(longest_word):
            longest_word = x
    return longest_word


print(longest(["cat", "dog", "horse"]))

# problem five
def upper_lower():
    user_word = input("Enter a word")

