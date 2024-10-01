from pathlib import Path 
import sys
from colorama import Fore

'''Третє завдання'''
def main():
    # Перевірка директорії
    if len(sys.argv) < 2:
        user_path = ''
    else:
        user_path = sys.argv[1]

    path = Path(user_path)
#   Перевірка наявності і коректності вводу  
    if path.exists():

#       Перевірка чи це папка чи файл
        if path.is_dir():
            elements = path.iterdir()
            for i in elements:

                # Додавання кольору в файл
                match i.suffix:
                    case '.txt':
                        print (f'{Fore.RESET}{Fore.YELLOW} {i.absolute()}{Fore.RESET}')
                    case '.py':
                        print (f'{Fore.RESET}{Fore.BLUE} {i.absolute()}{Fore.RESET}')
                    case '.cfg':
                        print (f'{Fore.RESET}{Fore.RED} {i.absolute()}{Fore.RESET}')
                    case _:
                        print (f'{Fore.RESET}{Fore.BLACK} {i.absolute()}{Fore.RESET}')
        else:
            print ("is a file")
    else:
        print ('невірний шлях', path.absolute())

if __name__ == '__main__':
    main()