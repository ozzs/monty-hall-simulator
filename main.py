from tkinter import *
from tkinter import ttk
import pygame

# Import utils
from utils.style_config import create_style
from utils.functions import create_new_window, load_image

# Import all game options for selection
from game_options.manual_run import manual
from game_options.statistics_run import statistics
from game_options.pc_single_run import pc_single_run_delay


def root_window() -> None:
    """Creates root window, then calls main_screen frame

    :return: None
    """
    # Initiate root
    root = Tk()
    root.title("Monty Hall Problem")
    root.geometry("700x550")  # Window size
    root.resizable(False, False)  # Setting the window to be un-resizable

    # Combobox style configuration
    root.option_add("*TCombobox*Listbox.font", ("Arial", "12"))
    root.option_add("*TCombobox*Listbox.Justify", "center")

    # Widgets style configuration
    create_style()

    # Pygame sound mixer initiator
    pygame.mixer.init()

    main_screen()
    root.mainloop()


# Function to load main (initial) screen
def main_screen(frame: Frame = None) -> None:
    """Creates main window with game options

    :param frame: None, no need to destroy previous frame
    :type frame: Frame, default value: None
    :return: None, renders main screen
    """

    # Create new frame of main screen
    main_frame = create_new_window(frame)

    logo_img = load_image("assets/images/monty_hall_logo_title.png", 175, 100)
    Label(main_frame, image=logo_img, borderwidth=0).grid(column=0, row=0, columnspan=3, pady=20)

    # Load curtains image to variable
    curtains_img = load_image("assets/images/curtains_image.webp", 200, 150)

    # Render 3 curtain images to screen
    for i in range(3):
        Label(main_frame, image=curtains_img).grid(column=i, row=1)

    # Instruction label for main screen
    ttk.Label(main_frame, text="Choose Game Type:", style="ST.Label").grid(
        column=0, row=3, columnspan=3, pady=50
    )

    # 'PC One Game' button
    ttk.Button(
        main_frame,
        text="PC One Game",
        style="TButton",
        command=lambda: pc_single_run_delay(main_frame),
    ).grid(column=0, row=4)

    # 'Statistics' button
    ttk.Button(
        main_frame,
        text="Statistics",
        style="TButton",
        command=lambda: statistics(main_frame),
    ).grid(column=1, row=4)

    # 'Human Run' button
    ttk.Button(
        main_frame,
        text="Human Run",
        style="TButton",
        command=lambda: manual(main_frame),
    ).grid(column=2, row=4)
    mainloop()


if __name__ == "__main__":
    root_window()
