# Given a sentence
sentence = "python is easy and python is powerful"

# Tasks
# . Count frequency of each word
# . Store results in dictionary

# Expected output
# {
# "python":2,
# "is":2,
# "easy":1,
# "and":1,
# "powerful":1
# }

words = sentence.split(" ")

word_frequency = {}
for i in words:
    if i not in word_frequency.keys():
        word_frequency[i] = 1
    else:
        word_frequency[i] += 1

print(word_frequency)


