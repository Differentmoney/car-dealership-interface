import csv


# 開啟 CSV 檔案
Ms = []
with open('mapping.csv', newline='') as csvfile:

  # 讀取 CSV 檔案內容
    rows = csv.reader(csvfile)

  # 以迴圈輸出每一列
    sk = False
    for row in rows:
        if(not sk):
            sk = True
        elif(row[1] != ''):
            Ms.append(row)
            

VSR = []
VS = []
with open('Sell.csv', newline='') as csvfile:

  # 讀取 CSV 檔案內容
    rows = csv.reader(csvfile)

  # 以迴圈輸出每一列
    sk = False
    for row in rows:
      if(len(row) != 0):
        VS.append(row)
    
print(VS)

VSR = []
with open('SellVehicle.csv', newline='') as csvfile:
  # 讀取 CSV 檔案內容
    rows = csv.reader(csvfile)

  # 以迴圈輸出每一列
    sk = False
    for row in rows:
      tem = []
      tem.append(row[0])
      tem.append('')
      tem.append(row[1])
      tem.append(row[2])
      tem.append(row[3])
      VSR.append(tem)

#print(VSR)
#print(len(VSR))
#print(len(VS))

i = 0
for e in VS:
  for j in Ms:
    if(e[0] == j[0]):
      VSR[i][1] = j[1]
      print("yes#")
      i +=1
      break

print(VSR)




import pandas as pd

df = pd.DataFrame(VSR)
df.to_csv('SellVehicleReal.csv')
