download_seconds = [8, 15, 0, 23, -2, 10]

def classify_downloads(download_times):
    results = []
    for seconds in download_times:
        if seconds < 0:
            results.append(f"{seconds} 資料無效")
        elif seconds >= 15:
            results.append(f"{seconds} 下載較慢")
        else:
            results.append(f"{seconds} 正常")
    return results

print(classify_downloads(download_seconds))
print('檢查完成')
