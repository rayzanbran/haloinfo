import haloinfohelper
import helper

exit_sentinel = ['x', 'X']

# Prints info about a Halo game given a code (ex. '1')
print('Enter a Halo game code, such as: ')
haloinfohelper.print_keys()
code = helper.get_code()

while(not code == 'X' or code == 'x'):
    while(not haloinfohelper.check_code_valid(code)) and (not (code in exit_sentinel)):
        print('Code invalid')
        code = helper.get_code()


    haloinfohelper.printhalo(code)
    print('Enter a new code:', end = "")
    code = helper.get_code()

