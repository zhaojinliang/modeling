# coding=utf-8
"""
Author = Eric_Chan
Create_Time = 2016/07/26
"""

import xlrd


def load_data(file_name, sheet_index=None):
    """
    读取xls文件,获得矩阵.
    :param file_name: xls文件路径
    :param sheet_index: xls 打开的sheet序号
    :return: 所有数据二元列表
    """
    if sheet_index is None:
        sheet_index = 0
    data = xlrd.open_workbook(file_name)  # 打开xls
    table = data.sheet_by_index(sheet_index)  # 打开sheet1
    all_data = table._cell_values  # 将所有数据 以二元列表进行构造
    for i in range(all_data.__len__()):  # 将表中数据的整数转化为int类型
        for j in range(all_data[0].__len__()):

            try:
                if all_data[i][j] == int(all_data[i][j]):
                    all_data[i][j] = int(all_data[i][j])
            except ValueError:
                continue
    return all_data


if __name__ == '__main__':
    file_name = 'dataSet/data_1_1.xls'
    print "第一组 对 红"
    all_data = load_data(file_name, 0)
    for i in range(27):  # 0 2
        sample_name = u"酒样品" + str(i+1)
        for j in range(len(all_data)):
            if all_data[j][0] == sample_name:
                temp = all_data[j+11][-10:]
                for t in temp:
                    print t,
                print ';'
                break

    print "\n\n第一组 对 白"
    all_data = load_data(file_name, 1)
    for i in range(28):  # 1
        sample_name = u"酒样品" + str(i + 1)
        for j in range(len(all_data)):
            if all_data[j][2] == sample_name:
                temp = all_data[j+10][-10:]
                for t in temp:
                    print t,
                print ';'
                break

    print "\n\n第二组 对 红"
    all_data = load_data(file_name, 2)
    for i in range(27):  # 0 2
        sample_name = u"酒样品" + str(i+1)
        for j in range(len(all_data)):
            if all_data[j][0] == sample_name:
                temp = all_data[j+11][-10:]
                for t in temp:
                    print t,
                print ';'
                break

    print "\n\n第二组 对 白"
    all_data = load_data(file_name, 3)
    for i in range(28):  # 3
        sample_name = i + 1
        for j in range(len(all_data)):
            if all_data[j][0] == sample_name:
                temp = all_data[j+9][-10:]
                for t in temp:
                    print t,
                print ';'
                break
