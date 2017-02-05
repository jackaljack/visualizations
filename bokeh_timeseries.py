import pandas as pd
from math import pi
from bokeh.plotting import figure, output_file, show

AAPL = pd.read_csv(
    'http://ichart.yahoo.com/table.csv?s=AAPL&a=0&b=1&c=2000&d=0&e=1&f=2010',
    parse_dates=['Date']
)

output_file('datetime.html')

# create plot with a 'datetime' axis type
p = figure(width=1000, height=600, title='AAPL', x_axis_type='datetime')

# style the axes (not really necessary, the defaults are good enough)
# http://bokeh.pydata.org/en/latest/docs/user_guide/styling.html#axes
p.xaxis.axis_label = 'Date'
p.xaxis.axis_label_text_color = '#ff0000'
p.xaxis.major_label_orientation = pi/6
p.xgrid.grid_line_color = None

p.yaxis.axis_label = 'Price ($)'
p.yaxis.axis_label_text_font_style = 'italic'
p.yaxis.major_label_orientation = 'horizontal'
p.ygrid.grid_line_alpha = 0.7
p.ygrid.grid_line_dash = [6, 4]

# add renderers
p.line(AAPL['Date'], AAPL['Open'], color='orange', alpha=1, legend='Open')
p.line(AAPL['Date'], AAPL['Close'], color='steelblue', alpha=1, legend='Close')

# style the legend
# http://bokeh.pydata.org/en/latest/docs/user_guide/styling.html#legends
p.legend.label_text_font = 'times'
p.legend.location = 'bottom_right'
p.legend.border_line_width = 3
p.legend.border_line_color = 'red'
p.legend.background_fill_color = 'gray'
p.legend.background_fill_alpha = 0.2

show(p)
