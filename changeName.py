import openpyxl
    
    # Excelファイルを開く
wb = openpyxl.load_workbook( "0805.xlsx" )
    
    # ワークシートの名前を変更する
ws = wb.worksheets[1]
ws.title = "hello"
    
    # Excelファイルを保存する
wb.save( "0805.xlsx" )