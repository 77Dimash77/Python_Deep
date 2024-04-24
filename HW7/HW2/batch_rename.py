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
