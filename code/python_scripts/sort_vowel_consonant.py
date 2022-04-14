vowel_list = []
consonant_list = []
vows = "aeiouAEIOU"
with open("wordlist.txt") as file:
    words = list(file)
    for word in words:
        if word[0] in vows:
            # word = word.strip()
            vowel_list.append(word.strip())
        else:
            # word = word.strip()
            consonant_list.append(word.strip())
print("THESE WORDS START WITH CONSONANTS\n", ", ".join(consonant_list))
print("\nTHESE WORDS START WITH VOWELS\n", ", ".join(vowel_list))
