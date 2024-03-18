N=10
print("Задание 2. Вариант ",(N-1)%10+1,"Дан файл, содержащий текст на русском языке, и некоторая буква.\nПодсчитать, сколько слов начинается с указанной буквы.")
def count_words_starting(path,alpha,mode):
    file=open(path,'r',encoding='utf-8')
    lines=file.readlines()
    file.close()
    count=0
    if mode==2:alpha.lower()
    for line in lines:
        words=line.split()
        for word in words:
            match mode:
                case 1:
                    if word.startswith(alpha):
                        count+=1
                case 2:
                    if word.lower().startswith(alpha):
                        count+=1
    return count

print("""Режимы поиска букв:
      1. Искать точное совпадение
      2. Искать заглавные и строчные буквы""")

alpha=input("Введите букву: ")
path='text.txt'
mode=int(input("Выберите режим поиска: "))
print(count_words_starting(path,alpha,mode), "раз в тексте встречается буква",alpha)