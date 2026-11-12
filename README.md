# Python Learning Portfolio

記錄 Python 基礎練習與專案實作，逐步建立從資料讀取、
條件檢查到統計摘要的程式開發能力。

## 專案目標

- 熟悉 Python 基礎語法與程式邏輯
- 透過不同輸入與邊界案例驗證程式行為
- 將基礎觀念整合成可執行的小型工具
- 保留程式、測試案例與學習紀錄，呈現實作過程

## 目錄結構

| 目錄 | 說明 |
| --- | --- |
| `python-fundamentals` | 基礎語法與獨立練習 |
| `  mini-projects` | 整合多個觀念的小型專案 |
| `capstone-projects` | 較完整的整合專案與展示作品 |

## 目前練習內容

- 條件判斷與分支邏輯
- 迴圈與計數
- 累計與統計摘要
- 函式與字典
- 文字檔讀取與逐行處理

## 練習範例

### 運動時間統計

檔案：`python-fundamentals/accumulation.py`

根據每日運動分鐘，計算總運動時間、有運動的天數與達標天數。

### 待辦清單讀取與行數統計

檔案：
- `python-fundamentals/read_tasks.py`
- `python-fundamentals/count_tasks.py`
- `python-fundamentals/tasks.txt`
- `python-fundamentals/count_valid_tasks.py`

從文字檔讀取待辦內容，練習整份讀取、逐行處理與行數統計。

測試案例包含：
- 三行待辦
- 單行待辦
- 空檔案

逐行讀取文字檔，使用 `strip()` 清理頭尾空白，
排除空白行及只有空格的行，再統計有效待辦數量。

已通過測試：
- 三項待辦混有空白行及頭尾空格：3 項
- 只有空白行和空格：0 項
- 完全空檔案：0 項

### 閱讀頁數統計

檔案：
- `python-fundamentals/sum_reading_pages.py`
- `python-fundamentals/reading_pages.txt`

逐行讀取文字檔，清理頭尾空白並排除空白行，
將數字文字轉成整數，統計總閱讀頁數與紀錄筆數。

已通過測試：
- 四筆頁數混有空白行與頭尾空格：總頁數 45、紀錄 4 筆
- 只有數值 0：總頁數 0、紀錄 1 筆
- 完全空檔案：總頁數 0、紀錄 0 筆

## 執行方式

在儲存庫根目錄開啟終端機，切換至練習資料夾：

```bash
cd python-fundamentals
```

執行指定程式，例如：

```bash
python count_tasks.py
```

讀檔練習請在對應的資料夾內執行，並保留所需的資料檔。

## 後續規劃

- 排除空白行並清理文字資料
- 練習 CSV 資料讀取
- 整合條件檢查與統計摘要
- 製作 CSV 資料品質檢查工具
