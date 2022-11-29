import xlrd
from LIBRARY.config import Config
# path=r"C:\Users\ADMIN\Downloads\signuppage.xlsx"

class ReadExcel:
   def read_test_data(self,sheetname):
       wd=xlrd.open_workbook(Config.DATA_PATH)
       ws=wd.sheet_by_name(sheetname)
       columns=ws.ncols
       rows=ws.get_rows()
       header=next(rows)
       data=[]
       for row in rows:
           values=()
           for j in range(columns):
               values+=(row[j].value,)
           data.append(values)
       return data


   def read_locators(self,sheetname):
      wd=xlrd.open_workbook(Config.DATA_PATH)
      ws=wd.sheet_by_name(sheetname)
      rows=ws.nrows
      # print(rows)
      d={}
      for i in range(1,rows):

          row=ws.row_values(i)
          d[row[0]]=(row[1],row[2])
          # print(row)

      return d
#print(read_locators())