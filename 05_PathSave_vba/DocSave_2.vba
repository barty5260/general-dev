Sub SaveWorkbookToMyDocuments()
    Dim myPath As String
    myPath = Environ$("USERPROFILE") & "\Documents\"
    Dim fileName As String
    fileName = "MyExcel_" & Format(Date, "yyyy.mm.dd") & ".xlsx"
    ActiveWorkbook.SaveAs Filename:=myPath & fileName, FileFormat:=xlOpenXMLWorkbook
End Sub
