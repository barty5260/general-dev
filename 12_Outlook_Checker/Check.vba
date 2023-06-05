Sub CheckNewMessages()
    Dim OutlookApp As Object
    Dim OutlookNamespace As Object
    Dim OutlookFolder As Object
    Dim OutlookMail As Object
    
    ' Create Outlook application object
    Set OutlookApp = CreateObject("Outlook.Application")
    
    ' Get the MAPI namespace
    Set OutlookNamespace = OutlookApp.GetNamespace("MAPI")
    
    ' Get the inbox folder named "Test"
    On Error Resume Next
    Set OutlookFolder = OutlookNamespace.GetDefaultFolder(6).Folders("Test")
    On Error GoTo 0
    
    ' Check if the folder exists
    If Not OutlookFolder Is Nothing Then
        ' Loop through the items in the folder
        For Each OutlookMail In OutlookFolder.Items
            ' Check if the item is an unread email
            If OutlookMail.UnRead Then
                ' Process the new email as needed
                MsgBox "New email received: " & OutlookMail.Subject
            End If
        Next OutlookMail
    Else
        MsgBox "The 'Test' folder does not exist."
    End If
    
    ' Clean up objects
    Set OutlookMail = Nothing
    Set OutlookFolder = Nothing
    Set OutlookNamespace = Nothing
    Set OutlookApp = Nothing
End Sub
