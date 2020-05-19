import random


def check(guess, _word, transformed_word):
    if guess not in set(_word):
        return 0
    else:
        for i in range(0, len(_word)):
            if _word[i] == guess:
                transformed_word[i] = _word[i]
                if "_" not in set(transformed_word):
                    return 10
        return transformed_word


def word_begin(_word):
    transform = []
    for letter in _word.strip():   # del newline
        transform.append("_")
    return transform


def win(transformed_word):
    if "_" not in set(transformed_word):
        return True


#  Read random word from file, lower letters, drop \n
with open("sowpods.txt", "r") as open_file:
    words = open_file.readlines()

index = random.randint(0, len(words) + 1)
word = words[index].lower()

# input_word = "testing"

transformed = word_begin(word)
print(word)
print(" ".join(transformed))

moves_left = 6
while moves_left:
    print("Moves left: " + str(moves_left))
    user_input = input("letter: ")
    result = check(user_input, word, transformed)

    if result == 0:
        print("Not found")
        print(" ".join(transformed))
        moves_left -= 1
        if moves_left == 0:
            decision = input("1 - try again, 2 - new word, 3 - quit: ")
            if decision == "1":
                print("Good luck")
                print(" ".join(transformed))
                moves_left = 6
                transformed = word_begin(word)
            elif decision == "2":
                moves_left = 6
                index = random.randint(0, len(words) + 1)
                word = words[index].lower()
                transformed = word_begin(word)
                print("New word")
                print(" ".join(transformed))
            else:
                break

    elif result == 10:
        print("Congratulations, word: " + word)
        break
    else:
        print(" ".join(result))


