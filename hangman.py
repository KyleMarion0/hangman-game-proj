import random

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
chosen_word_len = len(chosen_word)

placeholder = ""

for char in range(0, chosen_word_len):
  placeholder += "_"
print(placeholder)

game_over = False
correct_letters = []

while not game_over:
  guess = input("Please guess a letter: ").lower()

  display = ""

  for letter in chosen_word:
    if letter == guess:
      display += letter
      correct_letters.append(letter)
    elif letter in correct_letters:
      display += letter
    else:
      display += "_"

  print(display)

  if "_" not in display:
    game_over = True
    print("You win!")
