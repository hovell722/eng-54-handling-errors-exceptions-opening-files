
# this will break because there is no orders
# file = open('order.txt')

# Introducing try: and except: blocks

try:
    # makes file accessible/visible to python
    file = open('order.txt', 'r') # when you use open() you then need to close()

    # Create a **list** with each line
    file_line_list = file.readlines()
    print(file_line_list)

    # iterating of over each item on the list
    for placeholder_variable in file_line_list:
        # placeholder are internal variables
        # it store items from the list and then you can use it in a block
        print(placeholder_variable.rstrip('\n').title())


    # close the file
    file.close() # This is important
    # files that are open by a program
    # cannot be used by other programs (or humans...)

except FileNotFoundError as error_message:
    # print('THERE HAS BEEN AN ERROR! PANIC NOW!')
    print('Sorry, please check the file exists')
    print(error_message)