import plotly.figure_factory as ff 
import pandas as pd
import csv

df = pd.read_csv("data.csv")

fig1 = ff.create_distplot([df["Height"].tolist()], ['Height'], show_hist=False)
fig1.show()