import haloinfo

exit_sentinel = ['x', 'X']

# Prints info about a Halo game given a code (ex. '1')
print('Enter a Halo game code, such as: ')
haloinfo.print_keys()
code = input()

while(not code == 'X' or code == 'x'):
    while(not haloinfo.check_code_valid(code)) and (not (code in exit_sentinel)):
        print('Code invalid')
        code = input()


    haloinfo.printhalo(code)
    print('Enter a new code:', end = "")
    code = input()

