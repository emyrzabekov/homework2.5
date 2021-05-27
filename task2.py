import random

names = ['dhhgfjjhsa.txt', 'hhdsdahffh.txt', 'afdgdhjsds.txt',
         'sggjghddss.txt', 'fjdjgdghdf.txt', 'sjssahjfga.txt',
         'agsgdjhhfj.txt', 'gafadhadda.txt', 'hdagajfhhj.txt',
         'fhjhafhdfa.txt']

choice = random.choice(names)
print(choice)
f = open(choice, 'w')


def work_with_file(names):
    for choice in names:
        try:
            with open (choice, 'r'):
                f = open(choice, 'w')
            f.write('Эржан')
            f.close()
        except FileNotFoundError:
            print("Такого файла не существует!")


work_with_file(names)
