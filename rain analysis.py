# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 14:36:31 2020

@author: IHiggins
"""

import webbrowser
import os
from datetime import date
import tkinter
import fuzzy_pandas as fpd
import tkinter as tk
from tkinter import ttk
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from subprocess import call
import numpy as np
import matplotlib.pyplot as plt
import pyodbc
from scipy import stats
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
import pandas as pd
from matplotlib import pyplot as plt
from tkinter import *
from tkinter.ttk import *
import matplotlib
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import numpy as np
import plotly.io as pio #plotly renderer
pio.renderers.default = "browser"
import plotly.graph_objects as go
import tkinter as tk
from tkinter import simpledialog
from tkinter import *   ## notice lowercase 't' in tkinter here
from tkinter import filedialog
import pandas as pd
from datetime import datetime
from datetime import timedelta

import subprocess, sys
#import geopandas as gpd
import seaborn as sbn
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=NRDOSQLPrX01;'
                      'Database=gData;'
                      'Trusted_Connection=yes;')

Rain_Year = pd.read_sql_query('select * from vwRainWaterYearly WHERE Water_Year = 2021;',conn)

print(Rain_Year)

Locs = pd.read_sql_query('select G_ID, NORTHING, EASTING from HIC_GIS_VIEW;',conn)
print(Locs)

Rain_Gages = pd.merge(Rain_Year, Locs, on = 'G_ID')
print(Rain_Gages)

Rain_Gages.to_csv(r"W:\STS\hydro\GAUGE\Temp\Ian's Temp\Rain_DATA.csv")



