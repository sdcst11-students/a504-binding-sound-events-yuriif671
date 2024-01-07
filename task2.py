import playsound
import time

questions = ['X^2 + x – 90', 'X^2 + x – 78', 'X^2 – 6x + 8', '5x^2 + 10x + 20', 'X^2 + x – 90', 'X^2 – 6x + 8', 'X^2 + x – 870', '5x2 + 10x + 20', '2x^2 + 2x – 4', '15x^2 – 27x – 6']
options = [
    ['(x – 9)(x – 10)', '(x – 9)(x + 10)', '(x + 9)(x – 10)', 'None of these'],
    ['(x – 9)(x + 10)', '(x + 4)(x + 2)', '5(x - 2)(x + 2)', 'None of these'],
    ['(x – 4)(x + 2)', '(x + 4)(x + 2)', '(x – 4)(x – 2)', 'None of these'],
    ['(x – 4)(x + 2)', '(x + 4)(x + 2)', '(x – 4)(x – 2)', 'None of these'],
    ['5(x - 2)(x + 2)', '5(x + 2)(x + 2)', '5(x^2 + 2x + 4)', 'None of these'],
    ['(x – 9)(x – 10)', '(x – 9)(x + 10)', '(x + 9)(x – 10)', 'None of these'],
    ['(x – 4)(x + 2)', '(x + 4)(x + 2)', '(x – 4)(x – 2)', 'None of these'],
    [ '(x – 4)(x – 2)', '(x + 4)(x + 2)', 'Both 1 & 2', 'None of these'],
    ['5(x - 2)(x + 2)', '5(x + 2)(x + 2)', '5(x^2 + 2x + 4)', 'None of these'],
    ['2(x – 1)(x + 2)', '2(x + 1)(x + 2)', '(2x – 1)(x + 4)', 'None of these'],
    ['3(n + 1)(5n – 2)', '3(5n + 1)(n – 2)', '3(5n + 3)(n – 2)', 'None of these']
]
answers = [2, 4, 3, 3, 2, 3, 4, 3, 1, 2]

def main():
    print('=' * 9 + ' Factor polynomials ' + '=' * 9 + '\n')

    score = 0

    for i in range(len(questions)):
        print(f"{questions[i]}:\n{', '.join(options[i])}")
        answer = int(input("Answer (1-4): "))
        if answer == answers[i]:
            print("Correct!\n")
            playsound.playsound("sounds/correct.mp3", block = False)
            score += 1
        else:
            print("Wrong!\n")
            playsound.playsound("sounds/incorrect.mp3", block = False)

    #i do this because the 'incorrect' sound may still be playing + it is cooler 😎
    print("Loading the score...")
    time.sleep(4)
    print(f"The score is: {score}/{len(questions)}")

main()