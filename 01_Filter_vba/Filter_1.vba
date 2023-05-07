Sub FilterAndSort()
    ' Apply filter to row 1
    Rows("1:1").AutoFilter
    
    ' Sort column F from largest to smallest
    Range("F:F").Sort key1:=Range("F1"), order1:=xlDescending, Header:=xlYes
    
    ' Filter and remove all rows for which F column is smaller than 1
    ActiveSheet.Range("A1").AutoFilter Field:=6, Criteria1:="<1"
    Range("A2:F" & Cells(Rows.Count, "F").End(xlUp).Row).SpecialCells(xlCellTypeVisible).EntireRow.Delete
    
    ' Turn off the filter
    ActiveSheet.AutoFilterMode = False
End Sub
