import cv2 as cv
import numpy as np
import customtkinter as ctk
from PIL import Image, ImageTk

# Initialization
root = ctk.CTk()
root.title("Noise Map Generator in OpenCV and Tkinter || by ~shivam.salkar")
root.geometry("700x500")
root.resizable(False, False)

# Labels
imageLabel = ctk.CTkLabel(root, fg_color='transparent', bg_color='transparent', text='')
imageLabel.pack()


def generateFrame():
  frame = np.ones((500, 500), dtype=np.uint8)
  for i in range(1000):
    # color = np.random.choice([0, 255])
    cv.circle(img=frame, center=(np.random.randint(0, 499), np.random.randint(0, 499)), radius=np.random.randint(0, 16), thickness=-1, color=255)
    cv.circle(img=frame, center=(np.random.randint(0, 499), np.random.randint(0, 499)), radius=np.random.randint(0, 16), thickness=-1, color=0)
    cv.circle(img=frame, center=(np.random.randint(0, 499), np.random.randint(0, 499)), radius=np.random.randint(0, 16), thickness=-1, color=255)
  frame = cv.cvtColor(frame, cv.COLOR_GRAY2RGB)
  frame = cv.GaussianBlur(frame, (51, 51), 0)
  pilImage = Image.fromarray(frame)
  
  ctkImage = ctk.CTkImage(light_image=pilImage, dark_image=pilImage, size=(400,300))
  imageLabel.configure(image=ctkImage)

  
  

# Main App Loop
generateFrame()
root.mainloop()


# Exiting
cv.destroyAllWindows()
exit()
