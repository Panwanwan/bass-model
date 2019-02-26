# 最小二乘法
from math import e  # 引入自然数e
import numpy as np  # 科学计算库
import matplotlib.pyplot as plt  # 绘图库
import csv
from scipy.optimize import leastsq  # 引入最小二乘法算法

# 样本数据(Xi,Yi)，需要转换成数组(列表)形式
ti = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11])

# 读取文件
def read_data(filename):
    data_csv = []
    with open(filename) as f:
        reader = csv.reader(f)
        # print(list(reader))
        for row in reader:
            # 行号从1开始
            # print(reader.line_num, row)
            data_csv.append(row)
    data_number = []
    for i in range(1,len(data_csv)):
        numbers = list(map(int, data_csv[i][1:12]))
        data_number.append(numbers)
    return data_number



# 需要拟合的函数func :指定函数的形状，即n(t)的计算公式
def func(params, t):
    m, p, q = params
    fz = (p * (p + q) ** 2) * e ** (-(p + q) * t)  # 分子的计算
    fm = (p + q * e ** (-(p + q) * t)) ** 2  # 分母的计算
    nt = m * fz / fm  # nt值
    return nt


# 误差函数函数：x,y都是列表:这里的x,y更上面的Xi,Yi中是一一对应的
# 一般第一个参数是需要求的参数组，另外两个是x,y
def error(params, t, y):
    return func(params, t) - y


# k,b的初始值，可以任意设定, 一般需要根据具体场景确定一个初始值
p0 = [100, 0.3, 0.3]


# 读出数据
filename = 'a_sku_timeseries11.csv'
data_number = read_data(filename)


# 把error函数中除了p0以外的参数打包到args中(使用要求)

# params = leastsq(error, p0, args=(ti, np.array(data_number[1])))
# params = params[0]

params_data = []
for row in data_number:
    params = leastsq(error, p0, args=(ti, np.array(row)))
    params = list(params[0])
    params_data.append(params)
    m, p, q = params

with open('C:/Users/zhixingluo/Desktop/数据处理/data_result.csv', 'w', newline='') as csvfile:
    writer  = csv.writer(csvfile)
    for row in params_data:
        writer.writerow(row)