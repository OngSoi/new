import openpyxl
   
   # 1. Excelファイルを開く
wb = openpyxl.load_workbook( "0805.xlsx" )
   
   # 2. ワークシートを開く
ws_hello = wb["hello"]
ws_hello2 = wb["hello2"]
   
   # 3. データをコピーする
   
   
   # 4. Excelファイルを保存する
wb.save( "0805.xlsx" )