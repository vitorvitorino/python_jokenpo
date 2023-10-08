import random

def game():
    possibleChoices = ['pedra','papel', 'tesoura']
    victory = False
    while victory == False:
        userChoice = input('Pedra, papel ou tesoura?').lower().strip() 
        answer = random.choice(possibleChoices).lower().strip()
        if userChoice not in possibleChoices: 
            print('Você precisa inserir uma resposta válida!')
        elif userChoice == 'pedra' and answer == 'tesoura' or userChoice == 'papel' and answer == 'pedra' or userChoice == 'tesoura' and answer == 'papel':
            print(f'O computador escolheu {answer}, você ganhou!')
            victory = True
            break
        elif userChoice == answer:
            print(f'O computador escolheu {answer}, vocês empataram!')
            victory = False
            continue
        else:
            print(f'O computador escolheu {answer}, você perdeu!')
            victory = False
            continue

game()