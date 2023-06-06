# File: main.py
# Description: Prototype implementation of Game Developer Contract Matcher (GDCMatcher) case study
# Author: Chris Knowles


# Imports
from ui.menu_ui import MenuUI
from ui.partial_gui import PartialGUI
from engine.main_app import MainApp


# Consts
# Globals
# Classes


# Program entry function
def main():
    """
    Main function, contains creation of UI instance, main application instance and execution of the main application

    :return: None
    """
    # Create Menu UI instance
    menu_ui = MenuUI()

    # Create GUI instance
    gui = PartialGUI()

    # Create main application instance, inject into this the UI instance
    main_app = MainApp("GDCMatcher Prototype", menu_ui)

    # Execute the main application
    main_app.execute()


# Invoke main() program entrance
if __name__ == "__main__":
    # execute only if run as a script
    main()
