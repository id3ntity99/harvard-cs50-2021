from cs50 import get_string


def get_result(index):
    # Print out final result.
    if index < 1:
        print("Before Grade 1")
    elif index > 16:
        print("Grade 16+")
    else:
        print(f"Grade {index}")


def calculate_grade(sentences, words, letters):
    # Calculate index.
    L = (letters / words) * 100
    S = (sentences / words) * 100

    # Round up the result.
    index = round((0.0588 * L) - (0.296 * S) - 15.8)
    get_result(index)


def check_text(text):
    sentences = 0
    words = 1
    letters = 0

    # Count sentences, words and letters.
    for c in text:
        if c == "." or c == "!" or c == "?":
            sentences += 1
        elif c == " ":
            words += 1
        elif c.isalpha():
            letters += 1
    calculate_grade(sentences, words, letters)


def get_text():
    text = get_string("Text: ")
    check_text(text)


get_text()
