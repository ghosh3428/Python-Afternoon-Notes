from pyexcel_xlsx import save_data

sheetdata = [
                ["Roll" ,"Name","Marks"],
                [13,"Suraj",434],
                [14,"Vijay",384],
                [16,"Ajay",489],
                [18,"Rohan",281],
                [20,"Rajiv",337],
                [None,"Total Marks","=sum(C2:C6)"],
                [None,"Max Marks","=max(C2:C6)"],
                [None,"Min Marks","=min(C2:C6)"],
                [None,"Average Marks","=average(C2:C6)"]
    ]
worksheet = {"Marksheet" : sheetdata}

save_data("Class10Marksheet.xlsx" , worksheet)

print("Data Saved Successfully")
