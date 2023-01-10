from pyexcel_xlsx import read_data


data = read_data("class10marksheet.xlsx")

for i in data.values():
    for row in i:
        print(row)
