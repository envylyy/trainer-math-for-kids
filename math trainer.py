import random

correct = 0

while True:
    try:
        level = int(input('Select a level:\n1.Easy (numbers from 1 to 9)\n2.Medium (numbers from 10 to 99)\n3.Hard (numbers from 100 to 999)\nWrite the number: '))
        if (1 > level) or (level > 3):
            print('You need to choose a number from 1 to 3. Try again:)')
            continue
        break
    except ValueError:
        print("Oh! It looks like that's not a number?")

while True:
    try:
        problems = int(input('How many problems do you want to solve? Write the number: '))
        if problems <= 0:
            print('You need to enter a number greater than 0. Try again:)')
            continue
        break
    except ValueError:
        print("Oh! It looks like that's not a number?\n")

min_num = [1, 10, 100]
max_num = [9, 99, 999]

great1 = "Well done! That's the right answer!\n"
great2 = "Wow! It’s like you’ve got a calculator in your head!\n"
great3 = "You're just a young scientist!\n"

for _ in range(problems):
    if level == 1:
        number1 = random.randint(min_num[0], max_num[0])
        number2 = random.randint(min_num[0], max_num[0])
    elif level == 2:
        number1 = random.randint(min_num[1], max_num[1])
        number2 = random.randint(min_num[1], max_num[1])
    else:
        number1 = random.randint(min_num[2], max_num[2])
        number2 = random.randint(min_num[2], max_num[2])
    random_operation = random.choice(['+', '-', '*', ':'])

    if random_operation == '+':
        correct_answer = number1 + number2
    elif random_operation == '-':
        if number1 < number2:
            number1, number2 = number2, number1
        correct_answer = number1 - number2
    elif random_operation == ':':
        number2 = random.randint(1, max_num[level - 1])
        correct_answer = random.randint(1, max_num[level - 1] // number2)
        number1 = number2 * correct_answer
    else:
        correct_answer = number1 * number2

    print(f"What's {number1} {random_operation} {number2}?")

    while True:
        try:
            answer1 = int(input('Enter the answer: '))
            break
        except ValueError:
            print("Oh! It looks like that's not a number?\n")

    if answer1 == correct_answer:
        great_answer = random.choice([great1, great2, great3])
        print(great_answer)
        correct += 1
    else:
        print('You made a mistake:( Try solving the problem again')

        tryy = 0
        max_try = 3

        while tryy < max_try:
            try:
                answer2 = int(input(f'What do you think the answer of the example is {number1} {random_operation} {number2}? Enter the answer: \n'))
                if answer2 == correct_answer:
                    print('Right! I knew you could do it;)\n')
                    correct += 1
                    break
                else:
                    tryy += 1
                    if tryy < max_try:
                        print(f"Well, it's wrong again:( There are still attempts left: {max_try - tryy}. Try again!")
                    else:
                        print(f"Don’t worry! The correct answer is this: {correct_answer}. But you're still doing great!\n")
            except ValueError:
                print("Oh! It looks like that's not a number?")

print()
print(f'All done! You got {correct} out of {problems} correct!')
if correct == problems:
    print('Wow! You are a real math genius!')
elif correct >= problems * 0.5:
    print('Great job! You did a good job today!')
else:
    print('Don’t be upset! Shall we move on to the next section or review the topic?')