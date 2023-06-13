Sub CopySheets()
    
    Dim wbSource1 As Workbook
    Dim wbSource2 As Workbook
    Dim wbDest As Workbook
    Dim wsSource1 As Worksheet
    Dim wsSource2 As Worksheet
    Dim wsDest1 As Worksheet
    Dim wsDest2 As Worksheet
    
    ' Open the source workbooks
    Set wbSource1 = Workbooks.Open("C:\Document1.xlsx")
    Set wbSource2 = Workbooks.Open("C:\Document2.xlsx")
    
    ' Set the source and destination worksheets
    Set wsSource1 = wbSource1.Sheets("Sheet1")
    Set wsSource2 = wbSource2.Sheets("Sheet1")
    Set wbDest = Workbooks.Open(ThisWorkbook.Path & "\test.xlsx")
    Set wsDest1 = wbDest.Sheets("Sheet1")
    Set wsDest2 = wbDest.Sheets("Sheet2")
    
    ' Copy and paste the data
    wsSource1.Copy wsDest1.Range("A1")
    wsSource2.Copy wsDest2.Range("A1")
    
    ' Close the workbooks
    wbSource1.Close SaveChanges:=False
    wbSource2.Close SaveChanges:=False
    wbDest.Close SaveChanges:=True
    
End Sub
