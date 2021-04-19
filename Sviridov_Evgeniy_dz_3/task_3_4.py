import os


def make_file(file_name):
    if os.path.exists(file_name):
        print('Файл существует')
    else:
        tmp_text = [t for t in 'abcdefg']
        tmp_digit = [d for d in (1, 2, 3, 4, 5, 6, 7)]
        with open(file_name, 'w') as f:
            for t, d in zip(tmp_text, tmp_digit):
                f.write(f'\'{t}\', {d}\n')
        open_and_read_file(os.path.abspath(file_name))


def open_and_read_file(full_path):
    with open(full_path) as f:
        line = f.readline().strip()
        while line:
            print(line)
            line = f.readline().strip()


make_file('task_3_4_test.txt')
