N = input()
alphabet = 'abcdefghijklmnopqrstuvwxyz'
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for i in N:
    if i in ALPHABET:
        if ALPHABET.index(i) + 13 <= 25:
            a = ALPHABET.index(i) + 13
            print(ALPHABET[a], end="")
        else:
            a = ALPHABET.index(i) + 13 - 26
            print(ALPHABET[a], end="")
    elif i in alphabet:
        if alphabet.index(i) + 13 <= 25:
            b = alphabet.index(i) + 13
            print(alphabet[b], end="")
        else:
            b = alphabet.index(i) + 13 - 26
            print(alphabet[b], end="")
    elif i == " " or i.isdigit():     # https://bladejun.tistory.com/27   참고
        print(i, end="")



# https://claude-u.tistory.com/294     answer에 더해가는 식으로

        
    
