import cv2
import tkinter as tk
from tkinter import filedialog

class PhotoApp:
    def __init__(self, root):
        self.root = root
        self.cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # Utilisez cv2.CAP_DSHOW pour Windows pour désactiver le miroir
        self.capture_button = tk.Button(root, text="Capture", command=self.capture_photo)
        self.capture_button.pack()

    def capture_photo(self):
        ret, frame = self.cap.read()
        if ret:
            # Inverser l'effet miroir (mirroring) en utilisant cv2.flip
            frame = cv2.flip(frame, 1)  # 1 pour l'inversion horizontale, 0 pour l'inversion verticale, -1 pour les deux

            # Ouvrir une boîte de dialogue pour enregistrer l'image capturée
            file_path = filedialog.asksaveasfilename(
                defaultextension=".jpg",
                filetypes=[("JPEG files", "*.jpg"), ("All files", "*.*")])
            if file_path:
                # Enregistrer le cadre capturé sous forme de fichier image
                cv2.imwrite(file_path, frame)
                print(f"Photo enregistrée à {file_path}")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = PhotoApp(root)
    app.run()

