Sub DeleteFiles()
    Dim folderPath As String
    Dim fileName As String
    Dim i As Integer
    
    ' Set the folder path
    folderPath = "C:\YourFolderPath\" ' Replace with the desired folder path
    
    ' Delete the files Test1, Quote1, and Fig1
    Dim fileNames As Variant
    fileNames = Array("Test1", "Quote1", "Fig1")
    
    For i = 0 To 2
        fileName = folderPath & fileNames(i)
        If Dir(fileName) <> "" Then
            Kill fileName
        End If
    Next i
    
    ' Display a message indicating completion
    MsgBox "Files deleted successfully!"
End Sub
