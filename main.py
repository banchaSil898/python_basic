import os
from concatenate \
    import single_argument, multiple_argument, calculate_argument, argument_by_number, argument_alias, locals_argument
from sequenceVariable import sequence_tuple, sequence_list, sequence_dictionary
from condition import input_function


def main():
    while True:
        print('1. Show directory in drive C')
        print('2. Multiple calculate')
        print('3. For loop')
        print('4-9. show concatenate argument')
        print('10-12. show concatenate argument')
        print('13. show control flow by condition')
        print('99. exit')
        user_input = int(input('Choice function by number '))
        clear = lambda: os.system('cls')
        clear()
        if user_input == 1:
            set_cover(show_dir, 'asdf;lkajsdf')
        elif user_input == 2:
            set_cover(multiple_calculate)
        elif user_input == 3:
            set_cover(step_for)
        elif user_input == 4:
            set_cover(single_argument)
        elif user_input == 5:
            set_cover(multiple_argument)
        elif user_input == 6:
            set_cover(calculate_argument)
        elif user_input == 7:
            set_cover(argument_by_number)
        elif user_input == 8:
            set_cover(argument_alias)
        elif user_input == 9:
            set_cover(locals_argument)
        elif user_input == 10:
            set_cover(sequence_tuple)
        elif user_input == 11:
            set_cover(sequence_list)
        elif user_input == 12:
            set_cover(sequence_dictionary)
        elif user_input == 13:
            set_cover(input_function)
        elif user_input == 99:
            break


def show_dir(msg):
    print(msg)
    for name_dir in os.listdir('c:\\'):
        print(name_dir)


def multiple_calculate():
    main_number = int(input('choice your main multiple.'))
    multiple = 0
    while multiple < 12:
        multiple += 1
        print("%d * %d = %d" % (main_number, multiple, main_number*multiple))


def step_for():
    print('from 5 to 10')
    for from5_10 in range(5, 10):
        print(from5_10)
    print('from 4 to 21 step 2')
    for from4_21_step2 in range(4, 21, 2):
        print(from4_21_step2)
    print('from 3 to 21 step 3')
    for from3_21_step3 in range(3, 21+1, 3):
        print(from3_21_step3)
    print('from -50 to 10 step 10')
    for from_neg50_21_step10 in range(-50, 10, 10):
        print(from_neg50_21_step10)

def set_cover(func, param=None):
    print("===============================")
    if param:
        func(param)
    else:
        func()
    print("===============================")

main()
