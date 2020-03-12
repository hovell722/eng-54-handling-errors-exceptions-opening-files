# make some functions

# a function to open and read

def open_and_print(name_file):
    try:
        # with automatically closes files for us :)
        with open(name_file, 'r') as file:
            lines_list = file.readlines()
            for line in lines_list:
                print(line.strip('\n'))

    except FileNotFoundError as err:
        print('Check your file')
        print(err)

    finally:
        print("////// PROGRAM CLOSING! BIP BOP?  ////")

# open and write :) to the file

# I want a function to write Vegan lasanha into order.txt
# I need to define a function

def write_vegan_lasana_to_order():
    try:
        #open the file using with
        # use open function with write capabilities
        with open('order.txt', 'a') as file_to_write:
            # write some code to file
            file_to_write.write('Vegan Lasanha' + '\n')

    except FileNotFoundError as err:
        print('Do not PANIC! but check your file')
        print(err)
    finally:
        print("////// DONE WRITING! --PROGRAM CLOSING! BIP BOP?  ////")


def write_to_order(arg):
    try:
        with open('order.txt', 'a') as file_to_write:
            file_to_write.write(arg + '\n')

    except FileNotFoundError as err:
        print(err)
    finally:
        print("////// DONE WRITING! --PROGRAM CLOSING! BIP BOP?  ////")


def write_to_file(arg, file):
    try:
        with open(file, 'a') as file_to_write:
            file_to_write.write(arg + '\n')

    except FileNotFoundError as err:
        print(err)
    finally:
        print("////// DONE WRITING! --PROGRAM CLOSING! BIP BOP?  ////")


# user_food = input('What do you want to eat?')
# user_file = input('where do you want to write?')
#
# write_to_file(user_food, user_file)

# user_food = input('What do you want to eat?')#
# write_to_order(user_food)
# write_vegan_lasana_to_order()
# open_and_print('order.txt')