Sub RenameLastThreeModifiedFiles()
    Dim folderPath As String
    Dim fileCount As Integer
    Dim fileName As String
    Dim lastModified As Date
    Dim lastModifiedFiles(2) As Variant
    Dim i As Integer
    
    ' Set the folder path
    folderPath = "C:\YourFolderPath\" ' Replace with the desired folder path
    
    ' Get the file count in the folder
    fileCount = Dir(folderPath & "*.*", vbNormal).Count
    
    ' Loop through each file in the folder
    fileName = Dir(folderPath & "*.*", vbNormal)
    Do While fileName <> ""
        ' Check if the current file is more recent than the stored ones
        If FileDateTime(folderPath & fileName) > lastModified Then
            ' Update the stored last modified files
            lastModifiedFiles(2) = lastModifiedFiles(1)
            lastModifiedFiles(1) = lastModifiedFiles(0)
            lastModifiedFiles(0) = fileName
            lastModified = FileDateTime(folderPath & fileName)
        End If
        
        fileName = Dir()
    Loop
    
    ' Rename the files to Test1, Quote1, and Fig1
    Dim newNames As Variant
    newNames = Array("Test1", "Quote1", "Fig1")
    
    For i = 0 To 2
        fileName = lastModifiedFiles(i)
        If fileName <> "" Then
            Dim newName As String
            newName = newNames(i)
            Name folderPath & fileName As folderPath & newName
        End If
    Next i
    
    ' Display a message indicating completion
    MsgBox "Files renamed successfully!"
End Sub
