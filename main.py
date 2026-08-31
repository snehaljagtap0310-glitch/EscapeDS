import tkinter as tk
from gui.home import HomeScreen


def main():

    root = tk.Tk()

    HomeScreen(root)

    root.mainloop()


if __name__ == "__main__":
    main()