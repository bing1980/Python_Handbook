def main():

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
    books = ['Dracula', 'Frankenstein', 'The Omen', 'The Exorcist', 'The Legend of Sleepy Hollow']

    print(books * 2)

















# program entry point
if __name__ == '__main__':
    main()

