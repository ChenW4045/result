task_count = 0

print('今日待辦：')

with open('tasks.txt', 'r', encoding='utf-8') as file:
    for line in file: 
        print(line,end = '')
        task_count += 1
print()
print('待辦行數：', task_count)
print('讀取完成')
