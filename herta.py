import tkinter as tk
from playsound import playsound
from PIL import ImageTk, Image

class KuruKuruKururin:
    def __init__(self, window):
        self.sound_files = ["sounds/Herta Kurukuru.wav", "sounds/Herta Kururin.wav"]
        self.current_sound_index = 0
        self.animation_speed = 50
        self.current_frame_index = 0
        self.button_frames = self.load_button_frames()

        try:
            herta_image = Image.open("herta.png").convert("RGBA")
            herta_image = herta_image.resize((200, 200))
            self.herta_photoimage = ImageTk.PhotoImage(herta_image)
        except (FileNotFoundError, OSError) as e:
            print("Error loading static image:", e)
            self.herta_photoimage = None

        image_label = tk.Label(window, image=self.herta_photoimage, bg="white")
        image_label.pack(pady=0)

        self.button = tk.Button(window, bd=0, bg="white", command=self.herta, image=self.button_frames[0] if self.button_frames else None, relief=tk.RAISED)
        self.button.pack(pady=20)

    def load_button_frames(self):
        button_frames = []
        try:
            button_image = Image.open("button.gif").convert("RGBA")
            frame_count = 0
            while True:
                try:
                    button_image.seek(frame_count)
                    resized_image = button_image.resize((160, 160))
                    button_frames.append(ImageTk.PhotoImage(resized_image))
                    frame_count += 1
                except EOFError:
                    break
        except (FileNotFoundError, OSError) as e:
            print("Error loading button image:", e)
        return button_frames

    def herta(self):
        sound_file = self.sound_files[self.current_sound_index]
        playsound(sound_file)
        self.current_sound_index = (self.current_sound_index + 1) % len(self.sound_files)

        self.current_frame_index = 0
        self.update_animation()

    def update_animation(self):
        self.button.config(image=self.button_frames[self.current_frame_index])
        self.current_frame_index = (self.current_frame_index + 1) % len(self.button_frames)
        if self.current_frame_index != 0:
            window.after(self.animation_speed, self.update_animation)
        else:
            self.button.config(image=self.button_frames[0], relief=tk.RAISED)


window = tk.Tk()
window.title("KuruKuruKururin")
window.geometry("200x400")
window.configure(bg="white")

app = KuruKuruKururin(window)

window.mainloop()
