# Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории. Результаты обхода сохраните в файлы json, csv и pickle.
# ○ Для дочерних объектов указывайте родительскую директорию.
# ○ Для каждого объекта укажите файл это или директория.
# ○ Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней с учётом всех вложенных файлов и директорий.\

import os
import json
import csv
import pickle

def get_directory_info(directory):
    def get_dir_size(dir_path):
        total_size = 0
        for dirpath, _, filenames in os.walk(dir_path):
            for filename in filenames:
                filepath = os.path.join(dirpath, filename)
                total_size += os.path.getsize(filepath)
        return total_size

    def save_to_json(data, filename):
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)

    def save_to_csv(data, filename):
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)

    def save_to_pickle(data, filename):
        with open(filename, 'wb') as file:
            pickle.dump(data, file)

    directory_info = []

    for dirpath, dirnames, filenames in os.walk(directory):
        dir_size = get_dir_size(dirpath)
        directory_info.append({
            "path": dirpath,
            "type": "directory",
            "size": dir_size,
            "children": len(dirnames) + len(filenames)
        })
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            file_info = {
                "path": file_path,
                "type": "file",
                "size": os.path.getsize(file_path),
                "children": 0
            }
            directory_info.append(file_info)

    # Сохранение в JSON
    save_to_json(directory_info, "directory_info.json")

    # Сохранение в CSV
    csv_data = [[info["path"], info["type"], info["size"], info["children"]] for info in directory_info]
    save_to_csv(csv_data, "directory_info.csv")

    # Сохранение в pickle
    save_to_pickle(directory_info, "directory_info.pickle")

    print("Информация о директории успешно сохранена в файлах: directory_info.json, directory_info.csv, directory_info.pickle")

# Пример использования
get_directory_info("/path/to/directory")
