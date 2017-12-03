# 要读Csv文件，首先要准备一个csv文件
#导入Csv的包 Csv是python语言内置的包，比较常用，开发和测试所以程序都可能用到
import csv
#要想读取文件的信息，首先要知道文件的存放路径。
path=r'C:\Users\51Testing\PycharmProjects\untitled\Day4\data\member_info.csv'
# 要想读文件的内容，首先要通过路径打开文件。
file=open(path,'r')
#通过CSV 代码库，读取csv格式的内容
data_table=csv.reader(file)
#遍历文件，打印出所有内容
for row in data_table:
    print(row)
