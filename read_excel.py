from openpyxl import load_workbook

if __name__ == "__main__":
    wb = load_workbook(filename="sample1.xlsx", read_only=True)
    ws = wb["Sheet1"] # reading from Sheet1
    for i, row in enumerate(ws.rows):
        if i > 0:
            city_id = row[0].value
            city_name = row[1].value
            print("id: {} | city name: {}".format(city_id, city_name))