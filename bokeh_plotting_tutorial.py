from bokeh.plotting import figure, output_file, show
from bokeh.layouts import row

# missing data: Bokeh can deal with NaN values
nan = float('nan')

# tell Bokeh where to generate the output
output_file('bokeh_plotting_tutorial.html')

# create a plot with several renderers
p1 = figure(plot_width=600, plot_height=400, tools='resize, pan, wheel_zoom')
p1.vbar(x=[1, 2, nan, 4], width=0.5, bottom=0, top=[4, 5, nan, 7], color='red')
p1.square([1, 2, 3, 4], [5, 6, 7, 8], size=20, color='green', alpha=0.5)
p1.circle([2.5, 3.5], [5, 6], size=10, color='orange')
p1.x([2.5, 3.5], [4, 4], size=10, color='orange')
p1.cross([1.5, 2.5], [5, 5.5], size=10, color='violet')

# create another plot
p2 = figure(plot_width=600, plot_height=400)
p2.hbar(y=[1, 2, 3], height=0.5, left=0, right=[4, 5, 6], color='navy')

# assemble the layout
my_layout = row(p1, p2)

# save/show the output
show(my_layout)
