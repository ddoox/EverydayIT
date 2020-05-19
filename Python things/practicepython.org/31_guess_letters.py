def check(guess, word, transformed_word):
    if guess not in set(word):
        return 0
    else:
        for i in range(0, len(word)):
            if word[i] == guess:
                transformed_word[i] = word[i]
                if "_" not in set(transformed_word):
                    return 10
        return transformed_word


def word_begin(word):
    transform = []
    for letter in word:
        transform.append("_")
    return transform


def win(transformed_word):
    if "_" not in set(transformed_word):
        return True


input_word = "testing"
transformed = word_begin(input_word)
print(" ".join(transformed))

while True:

    x = input("letter: ")

    result = check(x, input_word, transformed)

    if result == 0:
        print("Not found")
        print(" ".join(transformed))
    elif result == 10:
        print("Congratulations, the word: " + input_word)
        break
    else:
        print(" ".join(result))
