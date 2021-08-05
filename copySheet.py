import openpyxl
    
    # Excelファイルを開く
wb = openpyxl.load_workbook( "0805.xlsx" )
    
    # ワークシートをコピーする
ws_copy = wb.copy_worksheet( wb["hello"] )
    
    # 新しいワークシートに名前をつける
ws_copy.title = "hello2"
    
    # Excelファイルを保存する
wb.save( "0805.xlsx" )