Sub CopyColumnNFromDataWorkbook()

    Dim dataWorkbook As Workbook
    Dim dataWorksheet As Worksheet
    Dim lastRow As Long
    
    ' Open the Data workbook
    Set dataWorkbook = Workbooks.Open("C:\Path\To\Data.xlsx")
    
    ' Set the Data worksheet as the active worksheet
    Set dataWorksheet = dataWorkbook.Worksheets("Sheet1")
    dataWorksheet.Activate
    
    ' Find the last row in column N of the Data worksheet
    lastRow = dataWorksheet.Range("N" & Rows.Count).End(xlUp).Row
    
    ' Copy the column N data to the active worksheet
    dataWorksheet.Range("N1:N" & lastRow).Copy Destination:=ActiveSheet.Range("A1")
    
    ' Close the Data workbook without saving changes
    dataWorkbook.Close False
    
End Sub
