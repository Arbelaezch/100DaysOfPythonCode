from cgitb import text
from tkinter import *
from tkinter import font
from tkinter import messagebox
import math
from turtle import color
import pyperclip
import json
import pandas as pd
import random

data = pd.read_csv("Days16-31:Intermediate/day31/data/test.csv")
data_dict = data.to_dict(orient="records")



word = [item["English"] for item in data_dict if item["French"] == "one"]

print(word)