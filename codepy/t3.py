# 导入所需的库
import cv2
import numpy as np
import time

# 创建视频捕获对象，打开指定路径的视频文件
cap = cv2.VideoCapture("C:\\Users\\32922\\Desktop\\python_code\\video\\1.mp4")
# 定义视频编码格式
fourcc = cv2.VideoWriter_fourcc(*'XVID')
# 创建视频写入对象，用于保存处理后的视频
out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (640, 480))

# 检查视频是否成功打开
while cap.isOpened():
    ret, frame = cap.read()  # 逐帧读取视频
    if ret == True:
        # 应用Canny边缘检测
        edges = cv2.Canny(frame, 100, 200)
        # 将处理后的帧写入输出视频
        out.write(edges)
        # 显示处理后的帧
        cv2.imshow("frame", edges)
        # 检测按键，如果按下'q'键则退出循环
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break  # 如果未成功读取帧，退出循环


# 释放视频捕获和写入对象
cap.release()
out.release()
# 关闭所有OpenCV窗口
cv2.destroyAllWindows()





   