from main import main_book
from Notes import main_notes
from clean import clean_folder

answ =''
while True:
    answ = input('If U want to work with:\n***' + "\033[0m\033[44m {}" .format('Phone') + '\033[0m' + 'Book ***** ' + "\033[0m\033[44m {}" .format('Note') + '\033[0m' + 's ***** ' + "\033[0m\033[44m {}" .format('Clear') + '\033[0m' + ' Directory ***\n')
    if answ == 'Phone':
        main_book()
    elif answ == 'Notes':
        main_notes()
    elif answ == 'Clear':
        clean_folder()
    else:
        print('Please, make your choice. And try again.')
        continue