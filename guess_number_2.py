print("Pomyśl liczbę od 0 do 1000, a ja ją zgadnę w max. 10 próbach")
min = 0
max = 1000

# computer using 10 moves to guess number.
# user answer the questions
for _ in range(10):
    guess = ((max - min) // 2 + min)
    print(f"Zgaduję: {guess}")
    print("Zgadłem?")
    answer = input("TAK/NIE? ")
    if answer.upper() == 'TAK':
        print('Wygrałem')
        break
    elif answer.upper() == 'NIE':
        print("Za dużo?")
        answer = input("TAK/NIE? ")
        if answer.upper() == 'TAK':
            max = guess
        elif answer.upper() == 'NIE':
            print("Za mało?")
            answer = input("TAK/NIE? ")
            if answer.upper() == 'TAK':
                min = guess
            elif answer.upper() == 'NIE':
                print('Nie oszukuj!')
            else:
                print('Wprowadzono inną odpowiedź niż TAK lub nie. Zacznij od początku')
                break
        else:
            print('Wprowadzono inną odpowiedź niż TAK lub nie. Zacznij od początku')
            break
    else:
        print('Wprowadzono inną odpowiedź niż TAK lub nie. Zacznij od początku')
        break
