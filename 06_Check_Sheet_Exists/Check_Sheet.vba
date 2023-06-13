Sub CheckSheetExists()
    Dim ws As Worksheet
    Dim sheetName As String
    
    sheetName = "Sheet1"
    
    ' Loop through all worksheets in the workbook
    For Each ws In ThisWorkbook.Worksheets
        If ws.Name = sheetName Then
            MsgBox sheetName & " exists!"
            Exit Sub ' Exit the loop if the sheet is found
        End If
    Next ws
    
    ' If the loop completes without finding the sheet, display a message
    MsgBox sheetName & " does not exist."
End Sub
