'''This example shows how to activate a toolbar that disappears if the cursor
leaves a canvas.

.. bokeh-example-metadata::
    :apis: bokeh.plotting.figure.scatter, bokeh.models.tools.Toolbar.autohide
    :refs: :ref:`first_steps_4_toolbar`, :ref:`bokeh.models.tools`
    :keywords: autohide, Toolbar

'''
import numpy as np

from bokeh.layouts import row
from bokeh.plotting import figure, output_file, show

N = 1000
x = np.random.random(size=N) * 100
y = np.random.random(size=N) * 100
radii = np.random.random(size=N) * 1.5
colors = ["#%02x%02x%02x" % (int(r), int(g), 150) for r, g in zip(50+2*x, 30+2*y)]

def make_plot(autohide=None):
    p = figure(width=300, height=300, title='Autohiding toolbar' if autohide else 'Not autohiding toolbar')
    p.scatter(x, y, radius=radii, fill_color=colors, fill_alpha=0.6, line_color=None)
    p.toolbar.autohide = autohide
    return p

output_file("toolbar_autohide.html", title="toolbar_autohide example")

show(row(make_plot(True), make_plot(False)))
