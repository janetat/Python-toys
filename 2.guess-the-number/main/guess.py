import random
secret = random.randint(0,101)
#print(secret)
print('The game starts! Please guess the integer between 0 to 100. You have 8 chances!')
guess = 0
counter = 7
while counter >= 0:
    guess = int(input('Guess the number: '))
    if guess > secret:
        print('Guess smaller! %s chances left!' % counter)
    elif guess < secret:
        print('Guess larger! %s chances left!' % counter)
    else:
        print('You made it!')
        break
    counter -= 1