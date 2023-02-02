import xlsxwriter

book = xlsxwriter.Workbook("NiitMarksheet.xlsx")
sh = book.add_worksheet("Jadavpur")

        
        
sh.write_row("A1" ,["Name","Total"])
sh.write_row("A2",["AB" , 456])
sh.write_row("A3",["CD" , 321])
sh.write_row("A4",["EF" , 345])
sh.write_row("A5",["GH" , 489])
sh.write_row("A6",["IJ" , 256])
sh.write_row("A7",["KL" , 196])
sh.write_row("A8",["MN" , 333])
sh.write_row("A9",["OP" , 478])
sh.write_row("A10",["QR" , 431])
sh.write_row("A11",["ST" , 398])

        
chart = book.add_chart({"type":"pie"})
chart.set_title({"name" : "Class 10 Marksheet"})
chart.add_series({"values" : "=Jadavpur!$B$2:$B$11",
                  "categories" : "=Jadavpur!$A$2:$A$11",
                 "points":[
                     {"fill":{"color":"red"}},
                     {"fill":{"color":"green"}},
                     {"fill":{"color":"blue"}},
                     {"fill":{"color":"pink"}},
                     {"fill":{"color":"yellow"}},
                     {"fill":{"color":"brown"}},
                     {"fill":{"color":"magenta"}},
                     {"fill":{"color":"purple"}},
                     {"fill":{"color":"orange"}},
                     {"fill":{"color":"black"}},
                     ],
                  "data_labels" :{"value" : True , "position":"outside_end"}
                  })
chart.set_style(10)

sh.insert_chart("D2" , chart)

book.close()
