import pandas as pd
from bokeh.plotting import figure, show, output_file
from bokeh.sampledata.stocks import GOOG
from bokeh.models import HoverTool, PanTool, WheelZoomTool


# prepare data
df = pd.DataFrame(GOOG)[:50]
df['date'] = pd.to_datetime(df['date'])
inc = df.close > df.open
dec = df.open > df.close
color = {'inc': '#00ff00', 'dec': '#ff0000'}
w = 12 * 60 * 60 * 1000  # half day in ms

# configure a hover tool
# Don't know why hovering is not working with the red candlesticks
hover = HoverTool(
    tooltips=[
        ('index', '$index'),
        ('(x, y)', '($x, $y)'),
        ('Open', '@open'),  # it seems it works only in bokeh.charts
        ('Close', '@close'),  # it seems it works only in bokeh.charts
    ]
)

TOOLS = [PanTool(), WheelZoomTool(), hover]

# tell Bokeh where to generate the output
output_file('candlestick.html', title='candlestick.py example')

# create plot
p = figure(x_axis_type='datetime', plot_width=1000, tools=TOOLS,
           title='GOOG Candlestick')

# style axes, grid, legend
p.xaxis.axis_label = 'Date'
p.yaxis.axis_label = 'Price ($)'
p.grid.grid_line_alpha = 0.5
p.legend.location = 'bottom_right'

# add renderers
p.segment(x0=df.date, y0=df.high, x1=df.date, y1=df.low, color='black')
p.vbar(x=df.date[inc], width=w, bottom=df.open[inc], top=df.close[inc],
       fill_color=color['inc'], line_color='black', legend='Increment')
p.vbar(x=df.date[dec], width=w, bottom=df.open[dec], top=df.close[dec],
       fill_color=color['dec'], line_color='black', legend='Decrement')

# save/show output
show(p)
