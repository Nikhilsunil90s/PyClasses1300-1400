# ExcelSheet --- SpreadSheets ---- Comma Seperated Values CSV Files
import csv

# LIsts Way
#file = open('sample.csv' , 'w')
#file.close()
# Auto Close File Object
#with open('sample.csv' , 'w') as file:
#    cf = csv.writer(file)
    #data = ['Helo' , 100, 23.56 , False]
    #cf.writerow(data)
    # data = [
    #     ['ColorName' , 'Code' , 'Price'],
    #     ['Red' , '#RRRR' , 66.99],
    #     ['Blue' , '#BBBB' , 88.77]
    # ]
    # cf.writerows(data)

# with open('sample.csv' , 'r') as file:
#     cf = csv.reader(file)
#     for i in cf:
#         print(i)
# Dictionary Way
# import os

# exists = os.path.isfile('mynewcsv.csv')
# with open('mynewcsv.csv' , 'a') as cfile:
#     cf = csv.DictWriter(cfile, fieldnames=['ColorTitle' , 'ColorCode' , 'ColorPrice']) 
#     if not exists:
#         cf.writeheader()
#     data = [
#         {
#         'ColorTitle' : 'Pink',
#         'ColorCode' : '#PPPIL',
#         'ColorPrice' : 34.99
#         },
#         {
#         'ColorTitle' : 'Marron',
#         'ColorCode' : '#PPPML',
#         'ColorPrice' : 54.99
#         },
#         {
#         'ColorTitle' : 'Blue',
#         'ColorCode' : '#PPPBL',
#         'ColorPrice' : 74.99
#         }
#     ]
#     #cf.writerow(data)
#     cf.writerows(data)

with open('mynewcsv.csv' , 'r') as rfile:
    cf = csv.DictReader(rfile)
    for i in cf:
        print(i)
    