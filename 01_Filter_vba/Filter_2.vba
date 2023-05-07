Sub FilterSortZoomCopy()

    ' Apply filter on row 4
    Rows("4:4").Select
    Selection.AutoFilter

    ' Sort column J from largest to smallest
    Range("J5").Select
    Range(Selection, Selection.End(xlDown)).Select
    ActiveWorkbook.Worksheets("Sheet1").Sort.SortFields.Clear
    ActiveWorkbook.Worksheets("Sheet1").Sort.SortFields.Add2 Key:=Range("J5:J" & Range("J" & Rows.Count).End(xlUp).Row), _
        SortOn:=xlSortOnValues, Order:=xlDescending, DataOption:=xlSortNormal
    With ActiveWorkbook.Worksheets("Sheet1").Sort
        .SetRange Range("A4:J" & Range("J" & Rows.Count).End(xlUp).Row)
        .Header = xlYes
        .MatchCase = False
        .Orientation = xlTopToBottom
        .SortMethod = xlPinYin
        .Apply
    End With

    ' Remove data smaller than 1 in column J
    Dim i As Long
    For i = Range("J" & Rows.Count).End(xlUp).Row To 5 Step -1
        If Range("J" & i).Value < 1 Then
            Range("J" & i).EntireRow.Delete
        End If
    Next i

    ' Change view to 75% zoom
    ActiveWindow.Zoom = 75
    
    ' Copy string
    Dim lastRow As Long
    lastRow = Range("N" & Rows.Count).End(xlUp).Row
    Range("N5:N" & lastRow).Value = "specific string or formula"
    
End Sub
