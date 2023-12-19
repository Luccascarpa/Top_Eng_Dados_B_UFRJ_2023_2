import csv
import os
import tempfile
import time

def merge_sorted(array1, array2, key_index):
    sorted_array = []
    i, j = 0, 0
    while i < len(array1) and j < len(array2):
        if array1[i][key_index] < array2[j][key_index]:
            sorted_array.append(array1[i])
            i += 1
        else:
            sorted_array.append(array2[j])
            j += 1
    while i < len(array1):
        sorted_array.append(array1[i])
        i += 1
    while j < len(array2):
        sorted_array.append(array2[j])
        j += 1
    return sorted_array

def divide_array(array, key_index):
    if len(array) < 2:
        return array[:]
    else:
        middle = len(array)//2
        l1 = divide_array(array[:middle], key_index)
        l2 = divide_array(array[middle:], key_index)
        return merge_sorted(l1, l2, key_index)

def merge_sort_external(input_filename, output_filename, buffer_size=1000):
    start_time = time.time()
    step_count = 0
    
    with open(input_filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        data = [row for row in reader]

    runs = [data[i:i+buffer_size] for i in range(0, len(data), buffer_size)]
    
    temp_files = []
    for i, run in enumerate(runs):
        step_count += 1
        run = divide_array(run, key_index=0)
        temp_file = tempfile.NamedTemporaryFile(delete=False, mode='w+', newline='', encoding='utf-8')
        temp_files.append(temp_file.name)
        csv.writer(temp_file).writerows(run)
        temp_file.close()

    while len(temp_files) > 1:
        new_temp_files = []
        for i in range(0, len(temp_files), 2):
            if i + 1 < len(temp_files):
                step_count += 1
                file1 = temp_files[i]
                file2 = temp_files[i + 1]
                merged_run = merge_sorted_runs(file1, file2, key_index=0)
                new_temp_file = tempfile.NamedTemporaryFile(delete=False, mode='w+', newline='', encoding='utf-8')
                new_temp_files.append(new_temp_file.name)
                csv.writer(new_temp_file).writerows(merged_run)
                new_temp_file.close()
                os.remove(file1)
                os.remove(file2)
            else:
                new_temp_files.append(temp_files[i])

        temp_files = new_temp_files

    os.rename(temp_files[0], output_filename)
    
    end_time = time.time()
    elapsed_time = end_time - start_time

    return elapsed_time, step_count

def merge_sorted_runs(file1, file2, key_index):
    with open(file1, 'r') as csvfile1, open(file2, 'r') as csvfile2:
        reader1 = csv.reader(csvfile1)
        reader2 = csv.reader(csvfile2)
        run1 = [row for row in reader1]
        run2 = [row for row in reader2]

    return merge_sorted(run1, run2, key_index)

# Example usage:
input_filename = 'input.csv'
output_filename = 'output.csv'
elapsed_time, step_count = merge_sort_external(input_filename, output_filename)

print(f"Elapsed Time: {elapsed_time} seconds")
print(f"Number of Steps/Runs: {step_count}")
