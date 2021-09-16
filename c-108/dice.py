import random
import plotly.express as px
import plotly.figure_factory as ff

count = []
dice_result = []
for i in range(0,100):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    value = dice1 + dice2
    dice_result.append(value)
    count.append(i)

fig = px.bar(x = dice_result, y = count)
fig.show()
fig1 = ff.create_distplot([dice_result],['result'],show_hist=False)
fig1.show()