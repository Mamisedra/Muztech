import tkinter as tk
from tkinter import filedialog
import  cv2
from PIL import Image, ImageTk

class PhotoApp:
	def __init__(self, root, width=600, height=780):
		self.root = root
		self.root.title("Photo Capture App")

		self.root.geometry("600x800")

		self.video_label = tk.Label(root)
		self.video_label.pack()

		self.capture_button = tk.Button(root, text="(*)", command=self.capture_photo)
		self.capture_button.pack()

		self.cap = cv2.VideoCapture(0)
		self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
		self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

		self.update_video_stream()

	def update_video_stream(self):
		ret, frame = self.cap.read()
		
		if ret:
			frame = cv2.flip(frame, 1)
			frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
			img = Image.fromarray(frame_rgb)
			imgtk = ImageTk.PhotoImage(image=img)
			self.video_label.imgtk = imgtk
			self.video_label.configure(image=imgtk)
		self.root.after(10, self.update_video_stream)

	def capture_photo(self):
		ret, fram = self.cap.read()
		if ret:
			desired_width = 600
			desired_height = 800

			resized_frame = cv2.resize(fram, (desired_width, desired_height))
	
			file_path = filedialog.asksaveasfilename(
				defaultextension=".jpg",
				filetypes=[("JPEG files", "*.jpg"), ("All files", "*.*")])
			if file_path:
				cv2.imwrite(file_path, fram)
				print(f"Photo bien sauver {file_path}")
	
	def on_closing(self):
		self.cap.release()
		self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = PhotoApp(root, width=600, height=720)
    root.protocol("WM_DELETE_WINDOW", app.on_closing)
    root.mainloop()