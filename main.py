from string import capwords

# def main():

# # f string format is recommended
#     book, author, release_year, goodreads_rating = 'Dracula', 'Bram Stoker', 1897, 4.01
#
#     # print(book + ' is a novel by ' + author + ', published in ' + str(release_year) + '. It has a rating of ' + str(goodreads_rating) + ' on goodreads.')
#
#     print(f'{book} is a novel by {author}, published in {release_year}.'
#           f' It has a rating of {goodreads_rating} on goodreads.')

#-------------------------------------------
# work with input()
# -------------------------------------------

#     name = input('What is your name? ')
#     age = int(input(f'How old are you {name}? '))
#     current_year = int(input(f'What year is this again? '))
#
#     print(f'If my calculations are right, you were born in {current_year - age}')

#-------------------------------------------
# work with strings
#-------------------------------------------
# triple quotes - You can put multi-line strings within triple quotes and Python will preserve the white spaces as well.
#     synopsis = """Dracula comprises journal entries, letters, and telegrams written by the main characters.
#         It begins with Jonathan Harker, a young English lawyer, as he travels to Transylvania.
#         Harker plans to meet with Count Dracula, a client of his firm, in order to finalize a property transaction.
#         When he arrives in Transylvania, the locals react with terror after he discloses his destination: Castle Dracula.
#         Though this unsettles him slightly, he continues onward.
#         The ominous howling of wolves rings through the air as he arrives at the castle.
#         When Harker meets Dracula, he acknowledges that the man is pale, gaunt, and strange.
#         Harker becomes further concerned when, after Harker cuts himself while shaving, Dracula lunges at his throat.
#         Soon after, Harker is seduced by three female vampires, from whom he barely escapes.
#         He then learns Dracula’s secret—that he is a vampire and survives by drinking human blood.
#         Harker correctly assumes that he is to be the count’s next victim.
#         He attacks the count, but his efforts are unsuccessful.
#         Dracula leaves Harker trapped in the castle and then, along with 50 boxes of dirt, departs for England."""
#
#     print('Synopsis:', synopsis)


#-------------------------------------------
# Sequence types (List, tuple, range)
#-------------------------------------------
# Lists in Python (you can create lists of integers, floats, or even of mixed types.)

    # a_random_list = ['Dracula', 1, 5.7, 'Carmilla']
    #
    # print(a_random_list)

# pop() method get rid of the last value in a list
#     horror_books = ['Dracula', 'Carmilla', 'The Imago Sequence']
#
#     print(horror_books.pop())
#     print(horror_books)

#-------------------------------------------
# Tuples in Python (allow mixed types)
# -------------------------------------------

#     a_random_list = ('Dracula', 1, 5.7, 'Carmilla')
#
#     print(a_random_list)

#-------------------------------------------
# Ranges in Python
# -------------------------------------------

# a_range = range(5, 15)  # 5 到 14
    #
    # print(a_range)
    #
    # list_a_range = list(a_range)
    #
    # print(list_a_range)
    #
    # tuple_a_range = tuple(a_range)
    #
    # print(tuple_a_range)


#--------------------------------------------
# for loop
#--------------------------------------------

    # random_numbers = [6, 1, 3, 8, 0, 9, 12, 3, 4, 0, 54, 8, 100, 55, 60, 70, 85]
    # multiplied_random_numbers = []
    #
    # for number in random_numbers:
    #     multiplied_random_numbers.append(number * 2)
    #
    # print(multiplied_random_numbers)

#--------------------------------------------
# while loop
#--------------------------------------------

    # number = 1
    # while number < 11:
    #     print(number)
    #     number += 1

# --------------------------------------------
# Use the + and * Operators
# --------------------------------------------
# The + operator lets you merge two sequences together.
#     books = ['Dracula', 'Frankenstein', 'The Omen', 'The Exorcist', 'The Legend of Sleepy Hollow']
#     more_books = ['And Then There Were None', 'The ABC Murders', 'The Valley of Fear', 'The Hound of the Baskervilles',
#                   'The Chestnut Man']
#
#     print(books + more_books)

# The * operator, on the other hand, makes multiple copies of a given sequence.
#     books = ['Dracula', 'Frankenstein', 'The Omen', 'The Exorcist', 'The Legend of Sleepy Hollow']
#
#     print(books * 2)

# --------------------------------------------
# String Operations
# --------------------------------------------
# capitalize() - capital first letter of a string
#     country_name = 'bangladesh'
#
#     print(country_name.capitalize())

# title() - capital first letter of each word (cannot deal with 's)
#     book_name = 'the house of silk'
#
#     print(book_name.title())

# capwords() - capital first letter of each word (can deal with 's)
# need to import capwords from string

    # book_name = "alice's adventures in wonderland"
    #
    # print(capwords(book_name))

# istitle() method that can check whether a given string is in title case or not

    # book_name = 'hearts in atlantis'
    #
    # print(f'Is "{book_name}" in title case? {book_name.istitle()}')
    # print(f'Is "{book_name.title()}" in title case? {book_name.title().istitle()}')

# How to count the number of Occurrences of a substring in a string
#     paragraph = '''At three in the morning the chief Sussex detective, obeying the urgent call from Sergeant Wilson of
#             Birlstone, arrived from headquarters in a light dog-cart behind a breathless trotter. By the five-forty train in
#             the morning he had sent his message to Scotland Yard, and he was at the Birlstone station at twelve o'clock to
#             welcome us. White Mason was a quiet, comfortable-looking person in a loose tweed suit, with a clean-shaved,
#             ruddy face, a stoutish body, and powerful bandy legs adorned with gaiters, looking like a small farmer,
#             a retired gamekeeper, or anything upon earth except a very favourable specimen of the provincial criminal
#             officer.'''
#
#     substring = 'morning'
#
#     print(f'The substring "{substring}" shows up {paragraph.count(substring)} times in the paragraph.')

# Split and Join Strings
# split() split the string into words using the spaces as separators
#     string = 'Holmes was certainly not a difficult man to live with'
#
#     word_list = string.split()
#
#     # print(word_list)
# # join()
#     new_string = ''
#     new_string = new_string.join(word_list)
#     print(new_string)


# --------------------------------------------
# Conditional Statements in Python
# --------------------------------------------
# if ... else
#     number = int(input('what number would you like to check?\n- '))
#
#     if number % 2 == 0:
#         print(f"{number} is even.")
#     else:
#         print(f"{number} is odd.")

# if ... elif ... else

    # year = int(input('which year would you like to check?\n- '))
    #
    # if year % 400 == 0 and year % 100 == 0:
    #     print(f"{year} is leap year.")
    # elif year % 4 == 0 and year % 100 != 0:
    #     print(f"{year} is leap year.")
    # else:
    #     print(f"{year} is not leap year.")


# for ... else

    # number = int(input('what number would you like to check?\n- '))
    #
    # if number == 1:
    #     print(f"{number} is not a prime number.")
    # elif number > 1:
    #     for n in range(2, number):
    #         if (number % n) == 0:
    #             print(f"{number} is not a prime number.")
    #             break
    #     else:
    #         print(f"{number} is a prime number.")


# --------------------------------------------
# Relational and Logical Operators
# --------------------------------------------

#     shield = int(input('what is your shield level? '))
#     sword = int(input('what is your sword level? '))
#     armor = int(input('what is your armor level? '))
#
#     if shield >= 45 and sword >= 48 and armor >= 25:
#         print('you shall pass!')
#     else:
#         print('you shall not pass!')

# --------------------------------------------
# Set
# --------------------------------------------

# set 显示类似 dict, 但是类型不一样

    # numbers = {}
    #
    # print(type(numbers))
    #
    # numbers = set()
    #
    # print(type(numbers))

# no duplicate value in set
#     numbers_list = [1, 2, 3, 4, 5, 3, 2, 4]
#
#     print(numbers_list)
#
#     numbers_set = set(numbers_list)
#
#     print(numbers_set)

# set are mutable, can add new value with add()
#     numbers = {1, 2, 3, 4, 5}
#
#     numbers.add(500)
#
#     print(numbers)

# discard() a value from set, clear() remove all values
#     numbers = {1, 2, 3, 4, 5}
#
#     numbers.discard(3)
#
#     print(numbers)
#
#     numbers.clear() # remove all value
#
#     print(numbers)

# --------------------------------------------
# Mapping Type in Python
# --------------------------------------------
#     programming_books = {
#         'C Programming Language': 35,
#         'Introduction to Algorithms': 100,
#         'Clean Code: A Handbook of Agile Software Craftsmanship': 50
#     }

    # cpl = 'C Programming Language'
    # algo = 'Introduction to Algorithms'
    # # get() method in dictionary
    # print(f"The price of {cpl} is ${programming_books.get(cpl)}")
    # print(f"The price of {algo} is ${programming_books[algo]}")

    # # popitem() :  popitem() method removes the last item in the dictionary and returns that as a tuple
    # print(programming_books.popitem())
    # # pop() method, on the other hand, returns the value for a given key and removes the pair
    # key = 'C Programming Language'
    # print(programming_books.pop(key))
    # print(programming_books)

    # keys(), values(), items()
    # for key in programming_books.keys():
    #     print(key)
    #
    # for value in programming_books.values():
    #     print(value)
    #
    # for item in programming_books.items():
    #     print(item)

# program entry point
# if __name__ == '__main__':
#     main()


####################################################################
# --------------------------------------------
# How to Write Functions in Python
# --------------------------------------------
# def hello(message, is_lower=False):
#     if is_lower:
#         return message.lower()
#     else:
#         return message.upper()
#
#
# def main():
#     uppercase_message = hello('Hello, Universe!')
#     print(uppercase_message)
#
#     lowercase_message = hello('Hello, Universe!', True)
#     print(lowercase_message)
#
#
# if __name__ == '__main__':
#     main()

###################################
# range based for loop
# def natural_sum(last_number):
#     if last_number < 1:
#         return last_number
#
#     total = 0
#     for number in range(1, last_number + 1):
#         total += number
#
#     return total
#
#
# def main():
#     last_number = int(input('up to which number would you like to calculate the sum?\n- '))
#
#     print(natural_sum(last_number))
#
#########################################
# recursive
# def recursive_natural_sum(last_number):
#     if last_number < 1:
#         return last_number
#
#     return last_number + recursive_natural_sum(last_number - 1)
#
#
# def main():
#     last_number = int(input('up to which number would you like to calculate the sum?\n- '))
#
#     print(recursive_natural_sum(last_number))
#
#
# if __name__ == '__main__':
#     main()


# ----------------------------------------------------
# How to Write Anonymous or Lambda Functions in Python
# ----------------------------------------------------

# def main():
#     numbers = [1, 2, 5, 4, 7, 88, 12, 15, 55, 77, 95]
#     # This lambda takes an argument named number then returns True if that's divisible by two and False otherwise
#
#     # The fileter() function takes a function and an iterable type as its two arguments.
#     even_numbers = filter(lambda number: True if number % 2 == 0 else False, numbers)
#
#     print(list(even_numbers))
#
#
# if __name__ == '__main__':
#     main()

# ----------------------------------------------------
# *args and **kwargs in Python
# ----------------------------------------------------
# you can pass the numbers as a tuple, and not mandatory to name it as *args
# def total(*numbers):
#     print(type(numbers))
#
#     t = 0
#     for number in numbers:
#         t += number
#
#     return t
#
#
# def main():
#     print(total(1, 2, 3, 4, 5))
#
#
# if __name__ == '__main__':
#     main()

# Like *args there is also **kwargs or keyword arguments that will allow you to access the function arguments as a dictionary.

def items(**kwargs):
    print(type(kwargs))

    for key, value in kwargs.items():
        print(f"{key} : {value}")


def main():
    items(
        Apple=10,
        Orange=8,
        Grape=35
    )


if __name__ == '__main__':
    main()











