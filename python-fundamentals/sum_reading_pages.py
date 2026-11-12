total_pages = 0
record_count = 0

with open('reading_pages.txt', 'r', encoding='utf-8') as file:
    for line in file:
        text = line.strip()

        if text != '':
            pages = int(text)
            total_pages += pages
            record_count += 1

print('總閱讀頁數：', total_pages)
print('紀錄筆數：', record_count)
