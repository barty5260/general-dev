Sub CheckNewMessages()
    Dim olApp As Outlook.Application
    Dim olNamespace As Outlook.Namespace
    Dim olFolder As Outlook.Folder
    Dim olSubFolder As Outlook.Folder
    Dim olItems As Outlook.Items
    Dim olMail As Outlook.MailItem
    Dim count As Integer
    
    ' Create the Outlook application and get the namespace
    Set olApp = New Outlook.Application
    Set olNamespace = olApp.GetNamespace("MAPI")
    
    ' Get the Test_Figures folder
    Set olFolder = olNamespace.GetDefaultFolder(olFolderInbox).Folders("Test_Figures")
    
    ' Check if the Test_Figures folder exists
    If Not olFolder Is Nothing Then
        ' Get the To_Check subfolder
        Set olSubFolder = olFolder.Folders("To_Check")
        
        ' Check if the To_Check subfolder exists
        If Not olSubFolder Is Nothing Then
            ' Get the collection of items in the To_Check subfolder
            Set olItems = olSubFolder.Items
            
            ' Loop through each item in the collection
            For Each olMail In olItems
                ' Check if the item is a mail item and is unread
                If TypeOf olMail Is Outlook.MailItem And olMail.UnRead Then
                    ' Process the unread mail item
                    ' Replace this line with your own code to handle the unread mail item
                    
                    ' Increase the count of new messages
                    count = count + 1
                End If
            Next olMail
            
            ' Display the count of new messages
            MsgBox count & " new messages found in the To_Check folder."
        Else
            MsgBox "The To_Check folder does not exist."
        End If
    Else
        MsgBox "The Test_Figures folder does not exist."
    End If
    
    ' Release the Outlook objects
    Set olItems = Nothing
    Set olSubFolder = Nothing
    Set olFolder = Nothing
    Set olNamespace = Nothing
    Set olApp = Nothing
End Sub
