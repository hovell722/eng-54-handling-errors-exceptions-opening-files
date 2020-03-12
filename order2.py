# Using `with`

#### open() using `with`:
try:
    # with automatically closes files for us :)
    with open('order3.txt', 'r') as file:
        lines_list = file.readlines()
        for line in lines_list:
            print(line.strip('\n'))

except FileNotFoundError as err:
    print('Check your file')
    print(err)

finally:
    print("////// PROGRAM CLOSING! BIP BOP?  ////")







#### open() without using with:


# try:
#     file = open('order.txt', 'r')
#
#     #do some actions to file
#
#     #close the dike
#     file.close()
#
# except FileNotFoundError as err:
#     print('Check your file')
#     print(err)