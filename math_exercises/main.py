import random
import atexit
import operator

math_operators = {'+': operator.add, '-': operator.sub, 
                  '*': operator.mul, '/': operator.truediv} # Division is improper?


def score_printer():
    print(f'Session score:')
    print('/n')


def simple_arithmatics():
    math = ['addition', 'subtraction', 'multiply', 'divide']
    equation_selection = random.choice(math)

    question = ''
    answer = 0

    if equation_selection == 'addition':
        value1 = random.randint(10,99)
        value2 = random.randint(10,99)

        question = str(value1) + " + " + str(value2) + ' = ?'
        answer = value1 + value2
    
    elif equation_selection == 'subtraction':
        value1 = random.randint(10,99)
        value2 = random.randint(10,99)

        question = str(value1) + ' - ' + str(value2) + ' = ?'
        answer = value1 - value2

    elif equation_selection == 'multiply':
        value1 = random.randint(1, 13)
        value2 = random.randint(1, 13)

        question = str(value1) + ' x ' + str(value2) + ' = ?'
        answer = value1 * value2
    
    elif equation_selection == 'divide':
        print(f'Note: Format should be:')
        print(f'[whole number]r[remainder]')

        # Temporary division - answer is without remainder
        value1 = random.randint(10,99)

        while True:
            try: 
                value2 = random.randint(1, int(value1/2))
            except:
                continue
            break

        question = str(value1) + ' / ' + str(value2) + ' = ?'
        # TO DO: create a condition if there wasn't a remainder 
        if value1%value2 == 0:
            answer = str(value1//value2)
        else: 
            answer = str(value1 // value2) + 'r' + str(value1%value2)


    return question,str(answer)


def linear_equations():
    operators = ['*', '+', '-']                             # Division has been removed
    constant_count = random.randint(1, 5)
    coefficient_count = random.randint(1, 5)

    question = ''
    answer = ''

    while constant_count != 0 and coefficient_count != 0:
        if constant_count != 0:
            operator_choice = random.choice(operators)
            # Broken link: math_operators[operator_choice](constant_count)
            
            constant_count -= 0


    equation_variable = random.randint(1, 10)

    print(equation_variable)
    answer = 5 + equation_variable - 4

    return question,str(answer)


def quadratic_equations():
    print('Not completed')


def main():
    set_difficulty = {'easy': False, 'normal': False, 'hard': False}    # In Development
    decimal_condition = False                                           # In Development
    math_questions = [simple_arithmatics(), linear_equations(), quadratic_equations()] # Not all are developed

    # Following three values not used as in development
    questions = 0
    correct_attempts = 0
    incorrect_attempts = 0

    math_question, math_answer = linear_equations() #simple_arithmatics()
    print(f'{math_question}') 
    
    # Enter and check user answer
    user_answer = input('Enter your answer: ')

    while True:
        if user_answer == math_answer:
            print(f'Correct')
            break
        elif user_answer == 'give up':
            break
        elif user_answer == 'quit':
            exit(0)
        else:
            print(f'Incorrect')
            user_answer = input('Incorrect. Enter another answer:')


if __name__ == '__main__':
    while True:
        main()

    # Print score on exit
    atextit.register(score_printer())
