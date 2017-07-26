word = input("Input a word: ")

if word.isalpha() and len(word) >0:
    print(word[1:] + word[0] + "ay")
else:
    print("No input or non alphanumeric value!")


