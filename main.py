def hangman(word):
    attempts_left = 5
    state = list("_" * len(word))
    word = list(word)
    print(state)

    while attempts_left > 0:
        guess = input("Enter letter: ")

        if guess in word:
            position = word.index(guess)
            state[position] = guess
            print(state)
        else:
            attempts_left -= 1
            print("Attempts left: ")
            print(attempts_left)


word = input("Word to guess: ")
hangman(word)
