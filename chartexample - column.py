import xlsxwriter

book = xlsxwriter.Workbook("NiitMarksheet.xlsx")
sh = book.add_worksheet("Jadavpur")

        
        
sh.write_row("A1" ,["Name","English","Maths"])
sh.write_row("A2",["AB" , 67,81])
sh.write_row("A3",["CD" , 89,90])
sh.write_row("A4",["EF" , 45,61])
sh.write_row("A5",["GH" , 89,90])
sh.write_row("A6",["IJ" , 87,56])
sh.write_row("A7",["KL" , 12,23])
sh.write_row("A8",["MN" , 78,81])
sh.write_row("A9",["OP" , 66,90])
sh.write_row("A10",["QR" , 56,51])
sh.write_row("A11",["ST" , 78,96])

        
chart = book.add_chart({"type":"column" })
chart.set_title({"name" : "Class 10 Marksheet"})
chart.add_series({"values" : "=Jadavpur!$B$2:$B$11",
                  "categories" : "=Jadavpur!$A$2:$A$11",
                  "name": "=Jadavpur!$B$1",
                  "data_labels":{"value" : True ,
                                 "position":"inside_base"},
                  "fill" : {"color":"green"}
                  })
chart.add_series({"values" : "=Jadavpur!$C$2:$C$11",
                  "name": "=Jadavpur!$C$1",
                 "data_labels":{"value" : True , "position":"outside_end"},
                  "fill" : {"color":"red"}
                 })

chart.set_style(12)
chart.set_x_axis({"name" : "Student Name"})
chart.set_y_axis({"name" : "Marks"})

sh.insert_chart("E2" , chart)

book.close()
