with open('tasks.txt', 'r', encoding='utf-8') as file:
    tasks_content = file.read()

print('今日待辦：')
print(tasks_content)
print('讀取完成')
