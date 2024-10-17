# -*- coding: utf-8 -*-
import math
import os

def jisuan_P(n, sita_rad):
    """计算Plm数组的值，并返回该数组"""
    Pln = list()
    for row in range(n+1):
        Pln.append([])
        for clumn in range(row+1):
            Pln[row].append(0)
    Pln[0][0] = 1
    Pln[1][0] = math.sqrt(3) * math.cos(sita_rad)
    Pln[1][1] = math.sqrt(3) * math.sin(sita_rad)
    for row in range(2, n+1):
        coefficient_1 = math.sqrt((2 * row + 1)/(2 * row))
        coefficient_2 = math.sqrt(2 * row + 1)
        Pln[row][row] = coefficient_1 * math.sin(sita_rad) * Pln[row-1][row-1]
        Pln[row][row-1] = coefficient_2 * math.cos(sita_rad) * Pln[row-1][row-1]
    for row in range(2, n+1):
        for clumn in range(0, row-1):
            coefficient_3 = math.sqrt((2 * row + 1) / (row - clumn) / (row + clumn))
            coefficient_4 = math.sqrt(2 * row - 1)
            coefficient_5 = math.sqrt((row - clumn - 1) * (row + clumn -1) / (2 * row - 3))
            Pln[row][clumn] = coefficient_3 * (coefficient_4 * math.cos(sita_rad) * Pln[row - 1][clumn] - coefficient_5 * Pln[row - 2][clumn])
    return Pln


def shuchu_P(shuchu_name, P_data, n):
    """将Plm数组的值输出到指定文件"""
    global lines
    lines = list()
    header_line1 = "标准向前行递推法\n学号:2022302141211, 其中l<=180, 角度为30度\n"
    lines.append(header_line1)
    fenggei='--------------------------------------\n'
    lines.append(fenggei)
    header_line2 = "L      M         Pln[l][m]\n"
    lines.append(header_line2)
    fenggei2='\n'


    for n in range(0,n+1):
        for m in range(0, n+1):
            # showstr=f'Pln({n},{m}): '
            # line1 = "{:<7d}{:<6d}".format( n,m)
            # line2= "{:.16f}\n".format(P_data[n][m])
            # line=line1+showstr+line2
            line= "{:<7d}{:<6d}{:.16f}\n".format( n,m,P_data[n][m])
            lines.append(line)
        lines.append(fenggei2)
    with open(shuchu_name, 'w', encoding='utf-8') as f:
        f.writelines(lines)


def main():
    """主函数，进行输入处理和调用计算及输出函数"""
    # id_number = input('请输入l:')
    # l = int(id_number)
    l=180
    global sita
    sita=30
    # sita=eval(input('输入角度：'))
    # shuchu_name = f"sita={sita}__l={l}__2022302141211 .txt"
    shuchu_name = "2022302141211 .txt"
    sita_rad = math.radians(sita)
    P_data = jisuan_P(l, sita_rad)
    shuchu_P(shuchu_name, P_data, l)


def test_print_Plm():
    """测试函数，用于打印Pln数组的输出结果"""
    print(lines)


if __name__ == "__main__":
    # while True:
    #     main()
    #     os.system('pause')
    # test_print_Plm()
    main()
    print('文件输出成功！')
    
    print('t2')