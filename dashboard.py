import os
from bokeh.charts import BoxPlot, Bar, Histogram, Scatter, HeatMap, bins,\
    output_file, show, defaults
from bokeh.layouts import layout
from bokeh.palettes import RdYlGn9
from bokeh.sampledata.autompg import autompg as df

# define default width and height of all charts
# it seems that if we define a default height here, we cannot override it later
# with plot_height.
# defaults.width = 600
# defaults.height = 500

# tell Bokeh where to generate the output
output_file('dashboard.html', title='{}'.format(os.path.basename(__file__)))

# BoxPlot: label on the x-axis (can have more than one label), values on the
# y-axis
box = BoxPlot(data=df, label=['cyl', 'origin'], values='mpg', color='cyl',
              marker='square', title='Mpg by Cyl, Origin')

# Histogram: values on both axes (bins on x-axis, count on y-axis)
hist = Histogram(data=df, values='mpg', color='cyl',
                 legend_sort_field='color',
                 legend_sort_direction='ascending',
                 title='Mpg Distribution (color grouped by Cyl)')

# Bar: label on the x-axis (grouped), values on the y-axis (aggregated)
# Note: if we don't specify a sorting order for the legend, it might not be
# sorted automatically
bar = Bar(data=df, label='yr', values='mpg', group='cyl', agg='mean',
          color='cyl', title='MPG by Year (grouped by Cyl)', plot_height=200)

# define some tooltips to display when hovering on the scatter plot data
tooltips = [
    ('Cylinders', '@cyl'),
    ('Weight', '@weight'),
    ('Acceleration', '@accel')
]

scatter = Scatter(df, x='mpg', y='hp', color='cyl',
                  title='HP vs MPG (colored by Cyl)',
                  xlabel='Miles per Gallon', ylabel='Horsepower',
                  legend_sort_field='color',
                  legend_sort_direction='ascending',
                  tooltips=tooltips)

# HeatMap: values defines the color
heatmap = HeatMap(df, x='cyl', y=bins('hp'), values='mpg',
                  title='HP by Cyl (colored by Mpg)', palette=RdYlGn9)

# organize the layout
l = layout([
    [box, hist],
    [bar],
    [scatter, heatmap],
], sizing_mode='scale_width')

# save/show the output
show(l)
