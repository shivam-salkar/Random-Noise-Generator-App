import cv2 as cv
import numpy as np
import customtkinter as ctk
from PIL import Image, ImageTk
import time
import datetime
import os


# Initialization
os.makedirs("Maps", exist_ok=True)
root = ctk.CTk()
root.title("Noise Map Generator in OpenCV and Tkinter || by ~shivam.salkar")
root.geometry("700x500")
root.resizable(False, False)
save_frame = None

def generateFrame():
  global save_frame
  frame = np.ones((300, 300), dtype=np.uint8)
  for i in range(1000):
    # color = np.random.choice([0, 255])
    cv.circle(img=frame, center=(np.random.randint(0, 499), np.random.randint(0, 499)), radius=np.random.randint(0, 16), thickness=-1, color=255)
    cv.circle(img=frame, center=(np.random.randint(0, 499), np.random.randint(0, 499)), radius=np.random.randint(0, 16), thickness=-1, color=0)
    cv.circle(img=frame, center=(np.random.randint(0, 499), np.random.randint(0, 499)), radius=np.random.randint(0, 16), thickness=-1, color=255)
  frame = cv.cvtColor(frame, cv.COLOR_GRAY2RGB)
  blur_size = int(blurSlider.get())
  # Ensure blur size is odd
  if blur_size % 2 == 0:
    blur_size += 1
  frame = cv.GaussianBlur(frame, (blur_size, blur_size), 0)
  save_frame = frame
  blurValueLabel.configure(text=f"Blur: {blur_size}")
  pilImage = Image.fromarray(frame)
  
  ctkImage = ctk.CTkImage(light_image=pilImage, dark_image=pilImage, size=(400,300))
  imageLabel.configure(image=ctkImage)
  
def save():
  if save_frame is not None:
    x = datetime.datetime.now()
    cv.imwrite(f"Maps/{x.strftime('%Y-%m-%d_%H-%M-%S')}.jpg", save_frame)

# Labels
imageLabel = ctk.CTkLabel(root, fg_color='transparent', bg_color='transparent', text='')
imageLabel.pack(pady=30)

sliderFrame = ctk.CTkFrame(root, fg_color='transparent', bg_color='transparent')
sliderFrame.pack()
blurValueLabel = ctk.CTkLabel(sliderFrame, text="Blur: 71")
blurValueLabel.pack()
blurSlider = ctk.CTkSlider(sliderFrame, width=300, height=30, from_=3, to=101, number_of_steps=49)
blurSlider.set(71)
blurSlider.pack()

cframe = ctk.CTkFrame(root , fg_color='transparent', bg_color='transparent')
cframe.pack(pady=10)

generateButton = ctk.CTkButton(cframe, text='Generate', border_width=2, corner_radius=0, border_spacing=10, border_color='white', fg_color='transparent', font=("HP Simplified Hans", 15, 'bold'), command=generateFrame)
generateButton.pack(side='left', padx=10, pady=10)
saveButton = ctk.CTkButton(cframe, text='Save', border_width=2, corner_radius=0, border_spacing=10, border_color='white', fg_color='transparent', font=("HP Simplified Hans", 15, 'bold'), command=save)
saveButton.pack(side='left', padx=10, pady=10)

  
  

# Main App Loop
generateFrame()
root.mainloop()


# Exiting
cv.destroyAllWindows()
exit()
