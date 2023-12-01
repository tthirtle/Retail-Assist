import _global

def show_splash():
    from time import sleep
    from splash.ui import window as splash_screen
    splash_screen.read()


if __name__ == "__main__":
    show_splash()