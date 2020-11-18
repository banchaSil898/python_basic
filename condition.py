def input_function():
    int_input = int(input('Input number please '))
    print('you entry %d ' % int_input)
    if int_input == 5:
        print('Is equal 5')
    elif int_input < 5:
        print('Is less than 5')
    else:
        if int_input > 5:
            print('Is more than 5')
            if int_input <= 10:
                print('Is less than or equal 10')
            elif int_input <= 20:
                print('Is less than or equal 20')
            elif int_input <= 30:
                print('Is less than or equal 30')
            elif 30 < int_input < 40:  # int_input > 30 and int_input < 40
                print('Is less than or equal 40')
            elif int_input == 41 or int_input == 45:
                print('And Bingo!!!!! you entry 41 or 45 as i choose')
            else:
                print('Go farrrrrrrrrrrr !!!! ')