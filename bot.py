def get_position(letter, word_feedback):
    for index, (char, status) in enumerate(word_feedback):
        if char == letter and status in [0, 1]:
            return index
    return -1

def correct(position, letter, words):
    return [w for w in words if len(w) > position and w[position] == letter]

def present(position, letter, words):
    return [
        w for w in words
        if letter in w and (len(w) <= position or w[position] != letter)
    ]

def absent(letter, words, position, word_feedback):
    correct_pos = get_position(letter, word_feedback)
    if correct_pos > -1:
        return [
            w for w in words
            if len(w) > correct_pos and w[correct_pos] == letter
        ]
    else:
        return [w for w in words if letter not in w]

def check_word(word, feedback, words):
    updated_words = words[:]
    word_feedback = list(zip(word, feedback))

    for position, (letter, status) in enumerate(word_feedback):
        if status == 0:
            updated_words = correct(position, letter, updated_words)
        elif status == 1:
            updated_words = present(position, letter, updated_words)
        elif status == 2:
            if word in updated_words:
                updated_words.remove(word)
            updated_words = absent(letter, updated_words, position, word_feedback)

    return updated_words
