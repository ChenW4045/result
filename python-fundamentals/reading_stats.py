pages_list = [0,19,20,21]
total_pages = 0
read_days = 0
achieve_days = 0
for e in pages_list:
    total_pages += e
    if e > 0:
        read_days += 1
    if e >= 20:
        achieve_days += 1
print(total_pages)
print(len(pages_list))
print(read_days)
print(achieve_days)
