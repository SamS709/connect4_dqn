from kivy.lang import Builder
from kivy.clock import mainthread
import time
import os
from kivy.properties import StringProperty,ListProperty
from kivy.uix.boxlayout import BoxLayout
import threading


# The bar you see on the top of the UI to go back to the previous screen and test if the connection with the robot can be established

# Load the .kv file only once to prevent duplicates
if not hasattr(Builder, '_box_layout_with_action_bar_loaded'):
    Builder.load_file(os.path.join(os.path.dirname(__file__), 'box_layout_with_action_bar.kv'))
    Builder._box_layout_with_action_bar_loaded = True

class BoxLayoutWithActionBar(BoxLayout):
    title = StringProperty() # c'est une chaîne de caractère qu'on va pouvoir remplir après dans un fichier kv


    
  
        