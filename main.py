import os
from graphics.connect4InterfaceNoRobot import graphicsApp

if __name__ == "__main__":
    os.environ['KIVY_GL_BACKEND'] = 'sdl2'  # Use pure SDL2 backend for better compatibility
    try:
        graphicsApp().run()
    except Exception as e:
        import traceback
        print("Kivy app crashed with error:")
        traceback.print_exc()