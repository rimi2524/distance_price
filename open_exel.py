import openpyxl

filename = "town_data.xlsx"
TownData = openpyxl.load_workbook(filename)

sheet = TownData.worksheets[0]

data = []
for row in sheet.rows:
    data.append([
        row[4].value,
        row[5].value,
        row[6].value,
        row[7].value,
        row[8].value,
        row[9].value,
        row[10].value,
        row[11].value,
    ])

    print(data)