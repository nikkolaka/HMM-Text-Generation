import re
from statistics import mode
import random


def train_trigram(text, model={}):
    # remove punctuations
    text = remove_punctuation(text)

    # split text into words inlcuding periods question marks and exclamation marks
    words = re.split(r'(\s+|[.!?])', text)

    words = [word for word in words if word.strip()]

    for i in range(len(words) - 2):
        word1 = words[i]
        word2 = words[i + 1]
        word3 = words[i + 2]

        if (word1, word2) not in model:
            model[(word1, word2)] = [word3]
        else:
            model[(word1, word2)].append(word3)

    return model


def get_next_word_bigram(word, model):
    # build bigram model
    bigram = {}

    for tuple in model:
        if tuple[0] == word:
            if word not in bigram:
                bigram[word] = [tuple[1]]
            else:
                bigram[word].append(tuple[1])

    return str(mode(bigram[word]))


def get_next_word_trigram(tuple, model):
    (word1, word2) = tuple

    return str(mode(model[(word1, word2)]))


def generate_text(model, num_words):
    stop_words = [".", "?", "!", "dwellings", "london", "moor", "discover", "man", "later", "danger", "hospital",
                  "whale", "more", "time", "box", "existence", "birlstone"]

    string = " "
    first_word = random.choice(list(model.keys()))[0]
    second_word = get_next_word_bigram(first_word, model)
    string += str(first_word) + " " + str(second_word)
    count = 2
    third_word = ""

    while count <= num_words:
        third_word = get_next_word_trigram((first_word, second_word), model)

        first_word = second_word
        second_word = third_word
        if third_word in stop_words:

            if third_word == "." or third_word == "?" or third_word == "!":
                string += str(third_word) + "\n"
            else:
                string += " " + str(third_word)
                count += 1

            first_word = random.choice(list(model.keys()))[0]
            second_word = get_next_word_bigram(first_word, model)
            # string += str(first_word)+ " " + str(second_word)

        else:
            string += " " + str(third_word)
            count += 1

    if third_word != "." and third_word != "?" and third_word != "!":
        string += "."

    return string


def remove_punctuation(string):
    result = ""

    for char in string:
        # check whether character is uppercase then convert to lowercase
        if char.isupper():
            char = char.lower()

        if not re.match(r"[.,\/#$%\^&\*;:\"{}=\-_`~()@1234567890]", char):
            result += char

    string = result
    return string
