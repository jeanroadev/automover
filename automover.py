import tkinter as tk
import pyautogui
import threading
import time

class MouseMoverApp:
    def __init__(self, root):
        self.root = root
        self.root.title("AutoMover | JeanroaDev")
        self.root.geometry("320x150")

        self.start_button = tk.Button(root, text="Iniciar", command=self.start_mouse_mover)
        self.start_button.pack(pady=20)

        self.stop_button = tk.Button(root, text="Detener", command=self.stop_mouse_mover)
        self.stop_button.pack(pady=10)

        self.is_running = False

    def start_mouse_mover(self):
        if not self.is_running:
            self.is_running = True
            self.mouse_mover_thread = threading.Thread(target=self.move_mouse_periodically)
            self.mouse_mover_thread.start()

    def stop_mouse_mover(self):
        self.is_running = False

    def move_mouse_periodically(self):
        while self.is_running:
            pyautogui.moveRel(0, 5)  # Mover el mouse un píxel hacia abajo
            time.sleep(8)  # Esperar 10 segundos

if __name__ == "__main__":
    root = tk.Tk()
    app = MouseMoverApp(root)
    root.mainloop()
