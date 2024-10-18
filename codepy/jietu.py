import numpy as np
from PIL import ImageGrab, Image, ImageTk
import cv2
import time
import os
import tkinter as tk
from tkinter import *


# 获取当前时间并格式化
def get_current_time():
    current_time = time.localtime()
    return time.strftime('%Y-%m-%d %H-%M-%S', current_time)

# 使用os.path处理文件路径
output_directory = 'C:/Users/32922/Desktop/image'
os.makedirs(output_directory, exist_ok=True)  # 确保目录存在

def capture_full_screen():
    root.withdraw()
    time.sleep(1)
    # 截取屏幕
    img = ImageGrab.grab(bbox=(0, 0, 1920, 1080))  # bbox 定义左、上、右和下像素的4元组
    img = np.array(img)  # 直接将获取的图像转换为numpy数组
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)  # 转换颜色格式

    # 获取当前时间并生成文件路径
    now_time = get_current_time()
    file_path = os.path.join(output_directory, f'{now_time}.png')
    print(file_path)
    # 保存图像
    cv2.imwrite(file_path, img)

    root.deiconify()  # 显示隐藏的窗口
    label.config(text=f"succeed! {now_time}.png", bg="lightblue", fg="red")

root = tk.Tk()
label = tk.Label(root)
button = tk.Button(root, text="截图", width=15, command=capture_full_screen)

buttonBye = tk.Button(root, text="退出", width=15, command=root.destroy)
label.pack()

button.pack(side=tk.LEFT)
buttonBye.pack(side=tk.LEFT)
root.mainloop()
