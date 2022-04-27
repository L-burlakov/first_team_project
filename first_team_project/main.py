from first_team_project.address_book_runner import main_book
from first_team_project.Notes import main_notes
from first_team_project.clean import clean_folder


def main():
    answ = ''
    while True:
        answ = input('If U want to work with:\n***' + "\033[0m\033[44m {}" .format('Phone') +
                     '\033[0m' + 'Book ***** ' + "\033[0m\033[44m {}" .format('Note') +
                     '\033[0m' + 's ***** ' + "\033[0m\033[44m {}" .format('Clear') +
                     '\033[0m' + ' Directory ***\n')
        if answ == 'Phone':
            main_book()
        elif answ == 'Notes':
            main_notes()
        elif answ == 'Clear':
            clean_folder()
        elif answ == '.':
            print('Good bye!')
            break
        else:
            print('Please, make your choice. And try again.')
            continue


if __name__ == '__main__':
    main()
