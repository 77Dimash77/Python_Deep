# Напишите функцию, которая принимает на вход строку - абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

import ntpath

def split_file_path(file_path):
    path, file_name = ntpath.split(file_path)
    name, extension = ntpath.splitext(file_name)
    return path, name, extension

file_path = r"C:\path\to\example.txt"
path, name, extension = split_file_path(file_path)
print("Путь:", path)
print("Имя файла:", name)
print("Расширение файла:", extension)
