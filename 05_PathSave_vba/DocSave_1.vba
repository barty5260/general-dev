Sub SaveWorkbookToMyDocuments()
    Dim myPath As String
    myPath = Environ$("USERPROFILE") & "\Documents\"
    ActiveWorkbook.SaveAs Filename:=myPath & "MyWorkbook.xlsx", FileFormat:=xlOpenXMLWorkbook
End Sub