print("Pomyśl liczbę od 0 do 1000, a ja ją zgadnę w max. 10 próbach")
min = 0
max = 1000

# computer using 10 moves to guess number.
# user answer the questions
for _ in range(10):
    guess = round((max - min)/2 + min)
    print(f"Zgaduję: {guess}")
    print("Zgadłem?")
    answer = input("TAK/NIE? ")
    if answer == 'TAK':
        print('Wygrałem')
        break
    elif answer == 'NIE':
        print("Za dużo?")
        answer = input("TAK/NIE? ")
        if answer == 'TAK':
            max = guess
        elif answer == 'NIE':
            print("Za mało?")
            answer = input("TAK/NIE? ")
            if answer == 'TAK':
                min = guess
            elif answer == 'NIE':
                print('Nie oszukuj!')
            else:
                print('Wprowadź odpowiedź TAK/NIE (dużymi literami) i zacznij grę od początku')
                break
        else:
            print('Wprowadź odpowiedź TAK/NIE (dużymi literami) i zacznij grę od początku')
            break
    else:
        print('Wprowadź odpowiedź TAK/NIE (dużymi literami) i zacznij grę od początku')
        break