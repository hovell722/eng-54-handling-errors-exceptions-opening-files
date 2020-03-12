from order3 import *

# Now that we have functions we just call them :)
open_and_print('order_table_camile.txt')
open_and_print('order.txt')

user_food = input('What do you want to eat?')
user_file = input('where do you want to write?')

write_to_file(user_food, user_file)


user_food = input('What do you want to eat?')#
write_to_order(user_food)