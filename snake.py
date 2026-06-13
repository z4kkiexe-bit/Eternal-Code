#kode paling frustasi

import tkinter as tk
import random

root = tk.Tk()
root.title("Snake Game")
canvas = tk.Canvas(
    root,
    bg="black",
    width=400,
    height=400,
)

ular = [(200, 200)]
ukuran = 20
canvas.pack()


def gambar_ular():
    canvas.delete("all")
    for x, y in ular:
        canvas.create_rectangle(x, y, x + ukuran, y + ukuran, fill="green")


gambar_ular()

root.mainloop()
