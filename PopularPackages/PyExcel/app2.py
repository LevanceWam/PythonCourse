import openpyxl

# this is a violation of command query prinicple


wb = openpyxl.load_workbook("transactions.xlsx")
sheet = wb["Sheet1"]
# when we used the for loop iterate through the first 10 rows everything pass the 4 that
# was already there the cell method magically created the empty rows
# this is a violation that can cause a error in your code
for row in range(1, 10):
    cell = sheet.cell(row, 1)
    print(cell.value)
sheet.append([1, 2, 3])
wb.save("transactions2.xlsx")
