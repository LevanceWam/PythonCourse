import csv

# this is to write the csv
# with open("data.csv", "w") as file:
#     writer = csv.writer(file)
#     writer.writerow(["transaction_id", "product_id", "price_id"])
#     writer.writerow([1000, 1, 4])
#     writer.writerow([1001, 3, 23])

# writing the csv
with open("data.csv") as file:
    reader = csv.reader(file)
    # print(list(reader))
    for row in reader:
        print(row)
