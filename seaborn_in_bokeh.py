import seaborn as sns
from bokeh import mpl
from bokeh.plotting import output_file, show


sns.set_style('whitegrid')

planets = sns.load_dataset('planets')
ax = sns.violinplot(x='orbital_period', y='method',
                    data=planets[planets.orbital_period < 1000],\
                    scale='width', palette='Set3')

output_file('seaborn_violin.html', title='seaborn_in_bokeh.py example')

show(mpl.to_bokeh())
