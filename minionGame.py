def minion_game(string):
    vowel = "AEIOU"
    kevin = 0
    stuart = 0
    for i in range(len(string)):
        if string[i] in vowel:
            kevin = kevin + len(string) - i
        else:
            stuart = stuart + len(string) - i
    if stuart > kevin:
        print("Stuart",stuart)
    elif kevin > stuart:
        print("Kevin",kevin)
    else:
        print("Draw")
