# Напишите функцию группового переименования файлов. Она должна:
# a. принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
# b. принимать параметр количество цифр в порядковом номере.
# c. принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
# d. принимать параметр расширение конечного файла.
# e. принимать диапазон сохраняемого оригинального имени. Например для диапазона [3, 6] берутся буквы с 3 по 6 из
# исходного имени файла. К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение

import os
def batch_rename(desired_name, digit_count, original_extension, final_extension, name_range=None):

    files = [file for file in os.listdir() if file.endswith(original_extension)]

    counter = 1

    for file in files:

        index = str(counter).zfill(digit_count)

        original_name = file
        if name_range:
            start, end = name_range
            original_name = original_name[start-1:end]

        new_name = f"{original_name}_{desired_name}_{index}.{final_extension}"

        os.rename(file, new_name)

        counter += 1

batch_rename("newfile", 2, ".txt", "txt", name_range=(3, 6))


