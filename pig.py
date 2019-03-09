# get sentence from user

original = input("What sentence to you want to translate?: ").strip().lower()

# split sentence into words

words = original.split()

# loop through words and convert to pig latin

new_words = []

# if starts with vowel, just add "yay"
# otherwise, move the first consonant cluster to end, and add "ay"

for word in words:
    if word[0] in "aeiou":
        new_word = word + "yay"
        new_words.append(new_word)
    else:
        vowel_pos = 0
        for letter in word:
            if letter not in "aeiou":
                vowel_pos = vowel_pos + 1
            else:
                break
        cons = word[:vowel_pos]
        the_rest = word[vowel_pos:]
        new_word = the_rest + cons + "ay"
        new_words.append(new_word)
        

# stick words back toguether
output = " ".join(new_words)

# output the final string
print(output)
