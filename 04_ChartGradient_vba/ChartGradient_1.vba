Sub CreateChart()
    Dim chart As chart
    Set chart = ActiveSheet.Shapes.AddChart2(227, xlArea).chart
    
    ' Add data to the chart
    chart.SetSourceData Source:=Range("A3:J3")
    
    ' Set the x-axis to display the date values
    chart.Axes(xlCategory).CategoryType = xlTimeScale
    
    ' Set the chart type to area with fill
    chart.ApplyDataLabels
    chart.FullSeriesCollection(1).Format.Line.Visible = False
    chart.FullSeriesCollection(1).Format.Fill.Visible = True
    
    ' Add conditional formatting to the chart series
    With chart.FullSeriesCollection(1).Format.Fill
        .Visible = True
        .TwoColorGradient msoGradientHorizontal, 1
        .GradientStops.Insert RGB(0, 255, 0), 0
        .GradientStops.Insert RGB(255, 0, 0), 1
        .GradientStops.Item(2).Position = 0.5

    End With
    
    ' Set the axis labels and chart title
    chart.Axes(xlCategory).HasTitle = True
    chart.Axes(xlCategory).AxisTitle.Text = "Date"
    chart.Axes(xlValue).HasTitle = True
    chart.Axes(xlValue).AxisTitle.Text = "Value"
    chart.HasTitle = True
    chart.ChartTitle.Text = "My Chart"
End Sub