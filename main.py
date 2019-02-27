import base64
import json
#import xlsxwriter

with open("kick.png","rb") as file:
    str64 = base64.b64encode(file.read())

# Crear JSON y crear archivo

data = {}
data['images'] = []  
data['images'].append({  
    'base': str64
})

with open('data.txt','w') as outfile:
    json.dump(data,outfile)

# Create a workbook and add a worksheet.
# workbook = xlsxwriter.Workbook('Expenses01.xlsx')
# worksheet = workbook.add_worksheet()

# # Some data we want to write to the worksheet.
# expenses = (
#     ['image_1', str64],
#     ['image_1', '123123'],
#     ['image_1', '123123']
# )

# # Start from the first cell. Rows and columns are zero indexed.
# row = 0
# col = 0

# # Iterate over the data and write it out row by row.
# for item, cost in (expenses):
#     worksheet.write(row, col,     item)
#     worksheet.write(row, col + 1, cost)
#     row += 1

# # Write a total using a formula.
# # worksheet.write(row, 0, 'Total')
# # worksheet.write(row, 1, '=SUM(B1:B4)')

# workbook.close()