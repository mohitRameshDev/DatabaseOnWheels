from tkinter import messagebox
from tkinter import ttk
from tkinter import *
import docx
import mysql.connector

from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, landscape
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
import pandas as pd
try:
    from dowclass import DOW
except ImportError:
    print('Not found')




r=Tk()
ob=DOW(r)
r.mainloop()