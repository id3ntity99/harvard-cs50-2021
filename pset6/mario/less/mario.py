from cs50 import get_int


def make_pyramid(h):
    '''
    # Nested for loop
    for i in range(h):
        for j in range(h):
            if (i + j ) < (h - 1) :
                print(" ", end = '')
            else:
                print("#", end = '')
        print()
    '''

    # Without nested for loop.
    for i in range(h):
        print(" " * (h - i - 1), end='')
        print("#" * (i + 1))


def ask_height():
    # Ask height.
    height = get_int("Height: ")

    # Check validation.
    if height > 8 or height < 1:
        ask_height()
    else:
        make_pyramid(height)


ask_height()