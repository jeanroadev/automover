import tkinter as tk
import pyautogui
import threading
import time
import random

class MouseMoverApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("300x150")
        self.root.title("AutoMover | JeanroaDev")

        self.is_running = False

        self.start_button = tk.Button(root, text="Iniciar", command=self.start_mouse_mover)
        self.start_button.pack(pady=20)

        self.stop_button = tk.Button(root, text="Detener", command=self.stop_mouse_mover)
        self.stop_button.pack(pady=10)

    def start_mouse_mover(self):
        if not self.is_running:
            self.is_running = True
            self.mouse_mover_thread = threading.Thread(target=self.move_mouse_periodically)
            self.mouse_mover_thread.start()

    def stop_mouse_mover(self):
        self.is_running = False

    def move_mouse_periodically(self):
        while self.is_running:
            new_x = random.randint(0, pyautogui.size().width)
            new_y = random.randint(0, pyautogui.size().height)
            pyautogui.moveTo(new_x, new_y)
            time.sleep(random.uniform(1, 5))

    def on_exit(self):
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = MouseMoverApp(root)

    # Mostrar la ventana
    root.protocol("WM_DELETE_WINDOW", app.on_exit)
    root.mainloop()
