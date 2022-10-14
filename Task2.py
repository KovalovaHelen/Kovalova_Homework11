"""
Задание #2:
Права доступа
Вирус повредил систему прав доступа к файлам. Известно, что над каждым файлом можно производить определенные действия:
запись – W;
чтение – R;
запуск – X.
На вход программе подается:
число n – количество файлов;
n строк с именами файлов и допустимыми операциями;
число m – количество запросов к файлам;
m запросов вида «операция файл».
Для каждого допустимого запроса программа должна возвращать OK, для недопустимого – Access denied.

Пример ввода:
3
python.exe X
book.txt R W
notebook.exe R W X
5
read python.exe
read book.txt
write notebook.exe
execute notebook.exe
write book.txt

Пример вывода:
Access denied
OK
OK
OK
OK
"""

files = {}
for n in range(int(input())):
    name, *operations = input().split()
    files[name] = operations
access = {"read": "R", "write": "W", "execute": "X"}
for m in range(int(input())):
    acc, nam = input().split()
    print("OK" if access[acc] in files[nam] else "Access denied")
