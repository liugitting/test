import cv2

# 尝试打开摄像头
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
if not cap.isOpened():
    print("错误：无法打开摄像头")
    exit()

while True:
    # 获取一帧
    ret, frame = cap.read()
    if not ret:
        print("错误：无法读取帧")
        break

    # 将图像左右调换
    frame = cv2.flip(frame, 1)

    # 保存图像（可在循环中保存多次，或者根据需要）
    if cv2.waitKey(1) & 0xFF == ord('q'): # 如果按下q 就截图保存并退出
        cv2.imwrite("test.png", frame) # 保存路径
        break

    # 如果需要，添加逻辑来查看或处理图像而不显示窗口

# 释放摄像头
cap.release()


