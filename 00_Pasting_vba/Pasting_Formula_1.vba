Sub PasteFormula()

    Dim i As Long
    Dim lastRow As Long
    
    ' Find the last row in column A
    lastRow = Range("A" & Rows.Count).End(xlUp).Row
    
    ' Loop through each row from N5 to N300
    For i = 5 To 300
        ' Check if the row number is within the range of column A
        If i - 4 <= lastRow Then
            ' Paste the formula in the current row of column N
            Range("N" & i).Formula = "=A" & i - 4 & "*2"
        End If
    Next i
    
End Sub
