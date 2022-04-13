import random

list1 = ["green", "blue", "red", "yellow", "white", "brown", "orange", "purple"]
word_str = random.choice(list1)
word_lst = list(word_str)
random.shuffle(word_lst)
word_lst2 = "".join(word_lst)
while True:
    guess = input("Guess the word '{}': ".format(word_lst2))
    if guess == word_str:
        print("You guessed correctly. The word was", word_str)
        break
