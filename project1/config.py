import sys
from django.db import connections
from django.db.utils import OperationalError
from tkinter import *
import ctypes

def Mbox(title, text, style):
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)

class database:
    def connect_db():
        db_conn = connections['default']
        my_conn = db_conn.cursor()
    
    def connect_getaccount(my_conn):
        my_conn.execute("SELECT * FROM accounts")
