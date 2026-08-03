"""
Program to accept a String as argument for a function and return the number of Vowels & Consonants 
"""

def countVowelsConsonants(word:str)->None:
    vowels = {"a","e","i","o","u"}
    consonant ={'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z'}
    vCount = cCount = 0
    for i in word:
        if i.lower() in vowels:
            vCount += 1
        if i.lower() in consonant:
            cCount += 1
    print(f"{word} contains:\nVovels : {vCount} | Consonants : {cCount}")


countVowelsConsonants("elephants")
