#封装读取Yaml/excel方法
import xlrd
import time
from datetime import datetime
from openpyxl import  Workbook
def read_excel():
    worksheet = xlrd.open_workbook("C://Users/Administrator/PycharmProjects/api_test/Params/Excel/自动化测试数据设计.xlsx")
    sheet = worksheet.sheet_by_name("Sheet1")
    list_data = []
    dict_data = {}
    data = {}
    list_d = []
    for row in range(sheet.nrows):
        print(sheet.row_values(row))
        rowdata = sheet.row_values(row)
        sheetname = rowdata[6].split(",")
        if sheetname[0] in worksheet.sheet_names():
            print(rowdata[6],sheetname[1])
            if sheetname[1].lower() =="json":
                data_sheet = worksheet.sheet_by_name(sheetname[0])
                for data_row in range(data_sheet.nrows):
                    print(data_sheet.row_values(data_row))
                    list_d.append(data_sheet.row_values(data_row))
                data = [dict(zip(list_d[0], v)) for v in list_d if v != list_d[0]]
                print("data:", data)
                rowdata[6] = data
        list_data.append(rowdata)
    dict_data = [dict(zip(list_data[0],v)) for v in list_data if v !=list_data[0] ]
    for i in dict_data:
        pass
        print(i)
def write_excel():
    wb = Workbook()
    ws = wb.active
    ws.title="清关vat对账数据20万"
    row = ["服务商代码*","运单号*",	"提单号*",	"申报价值*",	"VAT*",	"币种*",	"备注"]
    #       ["test1015",	"YT1900301106000002",	"123-20181205",	"59",	"237",	"RMB",	"4"],

    ws.append(row)
    for i in range(2000000):

        ws.append(["test1015",	"YT"+str(1900301106000002+i+1),	"123-20181205",	"59",	"237",	"RMB",	"4"])
        if i % 10000 == 0:
            print(datetime.now(),i)
    #wb.create_sheet("清关vat对账数据20万",index=1)

    wb.save("C:\\Users\\Administrator\\PycharmProjects\\api_test\\Params\\Excel\\清关vat对账数据20万.xlsx")
read_excel()