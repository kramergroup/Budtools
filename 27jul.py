from pymatgen import Structure
import os
import json
import datetime
import numpy as np
import shutil


from tkinter import filedialog
from tkinter import *

root = Tk()
root.filename = filedialog.askopenfilename(initialdir="/", title="Select file",)
print(root.filename) # Allows opening a file through gui.


