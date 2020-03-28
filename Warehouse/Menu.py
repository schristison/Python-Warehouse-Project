# define - def
def print_menu():
    print('-' * 80)
    print(' PyHouse - Welcome')
    print('-' * 80)

    print('[1] Register new item')
    print('[2] Display Catalog')
    print('[3] Display Items with no Stock')
    print('[4] Update Stock manually')
    print('[5] Print Stock value')
    print('[6] Remove items from Stock')
    print('[7] List Categories')

    print('[x] Exit')

# define header that would print a title
def print_header(title):
    print('\n\n') # means 2 blank lines
    print('-' * 80)
    print(title)
    print('-' * 80)
    