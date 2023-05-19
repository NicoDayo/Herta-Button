import tkinter as tk
from PIL import ImageTk, Image, ImageSequence
import pygame

class KuruKuruKururin:
    def __init__(self, window):
        self.sound_files = ["sounds/Herta Kurukuru.wav", "sounds/Herta Kururin.wav"]
        self.current_sound_index = 0
        self.animation_speed = 200
        self.current_frame_index = 0
        self.button_gif = self.load_button_gif()
        pygame.mixer.init()
        self.sounds = [pygame.mixer.Sound(sf) for sf in self.sound_files]
        try:
            herta_image = Image.open("herta.png").convert("RGBA")
            herta_image = herta_image.resize((200, 200))
            self.herta_photoimage = ImageTk.PhotoImage(herta_image)
        except (FileNotFoundError, OSError) as err:
            print("Error loading image", err)
            self.herta_photoimage = None

        image_label = tk.Label(window, image=self.herta_photoimage, bg="white")
        image_label.pack(pady=0)

        self.button = tk.Button(window, bd=0, bg="white", 
        image=self.button_gif[0] if self.button_gif else None, relief=tk.RAISED)
        self.button.pack(pady=10)

        self.button.bind("<Button-1>", self.on_button_click)
        self.button.bind("<ButtonRelease-1>", self.on_button_release)

    def load_button_gif(self):
        try:
            button_image = Image.open("button.gif")
            frames = []
            for frame in ImageSequence.Iterator(button_image):
                resized_frame = frame.resize((170, 170))
                photo = ImageTk.PhotoImage(resized_frame)
                frames.append(photo)
            return frames
        except (FileNotFoundError, OSError) as err:
            print("Error loading button:", err)
        return None

    def herta(self):
        self.sounds[self.current_sound_index].play()
        self.current_sound_index = (self.current_sound_index + 1) % len(self.sound_files)

        self.current_frame_index = 0
        self.update_animation()

    def update_animation(self):
        self.button.config(image=self.button_gif[self.current_frame_index])
        self.current_frame_index = (self.current_frame_index + 1) % len(self.button_gif)
        if self.current_frame_index != 0:
            window.after(self.animation_speed, self.update_animation)
        else:
            self.button.config(image=self.button_gif[0], relief=tk.RAISED)
    
    def on_button_click(self, event):
        click_frame_index = 1 
        self.button.config(image=self.button_gif[click_frame_index])

    def on_button_release(self, event):
        release_frame_index = 0 
        self.button.config(image=self.button_gif[release_frame_index])
        self.herta()

window = tk.Tk()
window.title("KuruKuruKururin")
window.geometry("200x400")
window.configure(bg="white")
window.resizable(False, False)

app = KuruKuruKururin(window)

window.mainloop()