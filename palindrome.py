word = input("Enterany word: ")
print(word.lower())
print("hi, you entered "+ word)
word_lenght = len(word)
if word_lenght < 4:
    print("are you kidding me...")
    print("more than four characters are expected!!!")
else:
    print("please wait while we check the word...")
    pal = "".join(reversed(word))
    if word == pal:
        print(f"wow, '{word}' is a palindrome")
    else:
        print(f"ooops {word} is not a palindrome")