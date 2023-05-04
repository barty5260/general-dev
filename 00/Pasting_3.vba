Sub PasteDataFromExternalWorkbooks()
    Dim sourceWorkbook1 As Workbook
    Dim sourceWorkbook2 As Workbook
    Dim targetWorkbook As Workbook
    
    'Open source workbook 1 and copy data to target sheet 1
    Set sourceWorkbook1 = Workbooks.Open("C:\Users\YourUserName\Documents\Ask1.xlsx")
    Set targetWorkbook = Workbooks("Check.xlsx")
    targetWorkbook.Worksheets("Input1").Activate
    sourceWorkbook1.Worksheets("Sheet1").Cells.Copy
    targetWorkbook.Worksheets("Input1").Range("A1").PasteSpecial xlPasteAll
    
    'Open source workbook 2 and copy data to target sheet 2
    Set sourceWorkbook2 = Workbooks.Open("C:\Users\YourUserName\Documents\Ask2.xlsx")
    targetWorkbook.Worksheets("Input2").Activate
    sourceWorkbook2.Worksheets("Sheet1").Cells.Copy
    targetWorkbook.Worksheets("Input2").Range("A1").PasteSpecial xlPasteAll
    
    'Copy data from General sheet to General sheet
    targetWorkbook.Worksheets("General").Activate
    targetWorkbook.Worksheets("General").Range("F1:G23").Copy
    lastRow = targetWorkbook.Worksheets("General").Cells(Rows.Count, 1).End(xlUp).Row
    targetWorkbook.Worksheets("General").Cells(lastRow + 1, 1).PasteSpecial xlPasteValues

    'Close source workbooks
    sourceWorkbook1.Close
    sourceWorkbook2.Close
End Sub
