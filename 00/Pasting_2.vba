Sub CopySheets()
    
    Dim wbSource1 As Workbook
    Dim wbSource2 As Workbook
    Dim wbDest As Workbook
    Dim wsSource1 As Worksheet
    Dim wsSource2 As Worksheet
    Dim wsDest1 As Worksheet
    Dim wsDest2 As Worksheet
    Dim wsDest3 As Worksheet
    Dim lastColumn As Long
    
    ' Open the source workbooks
    Set wbSource1 = Workbooks.Open("C:\Document1.xlsx")
    Set wbSource2 = Workbooks.Open("C:\Document2.xlsx")
    
    ' Set the source and destination worksheets
    Set wsSource1 = wbSource1.Sheets("Doc 1 sheet 1")
    Set wsSource2 = wbSource2.Sheets("Doc 2 sheet 1")
    Set wbDest = Workbooks.Open(ThisWorkbook.Path & "\test.xlsx")
    Set wsDest1 = wbDest.Sheets("Sheet1")
    Set wsDest2 = wbDest.Sheets("Sheet2")
    Set wsDest3 = wbDest.Sheets("General")
    
    ' Copy and paste the source sheets
    wsSource1.Copy after:=wsDest1
    wsSource2.Copy after:=wsDest2
    
    ' Find the last column in row 1 of the destination sheet
    lastColumn = wsDest3.Cells(1, Columns.Count).End(xlToLeft).Column
    
    ' Copy and paste the data
    wsDest3.Range("C1:F3").Copy wsDest3.Cells(1, lastColumn + 1)
    
    ' Close the workbooks
    wbSource1.Close SaveChanges:=False
    wbSource2.Close SaveChanges:=False
    wbDest.Close SaveChanges:=True
    
End Sub
