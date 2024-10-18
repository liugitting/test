import cv2
import numpy as np
import tkinter as tk
from tkinter import scrolledtext
import time

def get_char(lumiance):
    char="@%#*+=-:."
    index = min(int((lumiance/255.0)*len(char)),len(char)-1)
    return char[index]

def video_to_ascii(video_path,output_width=120,output_height=60):
    cap=cv2.VideoCapture(video_path)

    if not cap.isOpened():
        raise IOError("Error opening video file")
    
    fps =cap.get(cv2.CAP_PROP_FPS)
    frame_count=int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    print(f"FPS:{fps},Frame count:{frame_count}")

    print(f"Output height:{output_height}")

    root=tk.Tk()
    root.title("Video to ASCII Art")

    root.geometry(f"{output_width*8}x{output_height*16}")

    text_wedget = scrolledtext.ScrolledText(root,width=output_width,height=output_height)
    text_wedget.pack()

    frame_index=0
    while True:
        ret,frame=cap.read()
        if not ret:
            break

        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

        resized=cv2.resize(gray,(output_width,output_height),interpolation=cv2.INTER_LINEAR)

        ascii_frame=""
        for row in resized:
            for luminance in row:
                ascii_frame+=get_char(luminance)
            ascii_frame+="\n"

        text_wedget.delete(1.0,tk.END)
        text_wedget.insert(tk.END,ascii_frame)

        root.update()

        time.sleep(1/fps)

        frame_index+=1

    cap.release()
    root.mainloop()

if __name__ == "__main__":
    video_path="C:\\Users\\32922\\Desktop\\python_code\\video\\1.mp4"
    output_width=120
    output_height=60
    video_to_ascii(video_path,output_width,output_height)