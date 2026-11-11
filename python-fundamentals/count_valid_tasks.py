valid_task_count = 0

print('有效待辦：')

with open('tasks_with_blanks.txt', 'r', encoding='utf-8') as file:
    for line in file:
        task = line.strip()

        if task != '':
            print(task)
            valid_task_count += 1

print('有效待辦數：', valid_task_count)
print('讀取完成')
