# example to show git branch
# the example use the try except flow control statement
#
# Master branch use finally block, 
# The Branch "No-finally" will not use finally block
#
# refer: https://docs.python.org/3/whatsnew/2.5.html#pep-341-unified-try-except-finally
#
x = 0
success = False
while True:
    try:
        filename = input("Which file would you like to open? :")
        with open(filename, "r") as fh:
            file_data = fh.read()
    except FileNotFoundError:
        print(f'Sorry, {filename} doesn\'t exist! Please try again.')
    else:
        print(file_data)
        success = True
        break
    finally:
        x += 1
        print('\n === tried:',x," times ===")
        if success == False and x == 3:
            print('Wrong filename 3 times. \n Check name and Rerun.')
            break