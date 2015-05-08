#!/usr/bin/python


"""
Plot Normal distribution
From http://renke.org/2013/02/23/python-plot-number-2/
"""

import math
import matplotlib.pyplot as plt
import numpy


LINE_WIDTH = 3
MEAN = 0
FROM_X = -4
TO_X = 4
NUMBER_OF_SAMPLES = 10000


def pdf(x, mean, var):
  """Probability density function of the Normal distribution"""
  sd = math.sqrt(var)
  return 1 / (sd * (math.sqrt(2 * math.pi))) * (math.e ** -(((x - mean) ** 2) / (2 * var)))


def plot_normal(varlist=[1], colors=['blue', 'red', 'green', 'black']):
	v = 0
	for VAR in varlist:
		v += 1

		SD = math.sqrt(VAR)

		plt.axvline(color=(0.75,0.75,0.75), linewidth=1)
		plt.axhline(color=(0.75,0.75,0.75), linewidth=1)

		xs = numpy.linspace(FROM_X * SD , TO_X * SD, NUMBER_OF_SAMPLES)
		ys = [pdf(x, MEAN, VAR) for x in xs]
		plt.plot(xs, ys, linewidth=LINE_WIDTH, color=colors[v])

		plt.fill_between(xs, 0, ys, where=numpy.logical_and(xs > 3 * -SD, xs < 3 * SD), color=colors[v], alpha=0.2)
		plt.fill_between(xs, 0, ys, where=numpy.logical_and(xs > 2 * -SD, xs < 2 * SD), color=colors[v], alpha=0.2)
		plt.fill_between(xs, 0, ys, where=numpy.logical_and(xs > -SD, xs < SD), color=colors[v], alpha=0.2)

		x_text = SD - SD / 2
		y_text = pdf(x_text, MEAN, VAR) / 2

		plt.text(x_text, y_text, "%.1f%%" % (68 / 2.0,), fontsize=14, ha="center")
		plt.text(-x_text, y_text, "%.1f%%" % (68 / 2.0,), fontsize=14, ha="center")

		x_text = 2 * SD - SD / 2
		y_text = pdf(x_text, MEAN, VAR) / 4

		plt.text(x_text, y_text, "%.1f%%" % ((95 - 68) / 2.0,), fontsize=14, ha="center")
		plt.text(-x_text, y_text, "%.1f%%" % ((95 - 68) / 2.0,), fontsize=14, ha="center")

		x_point = 3 * SD - SD / 2
		y_point = pdf(x_point, MEAN, VAR) * 1.25

		x_text = 3 * SD - SD / 2
		y_text = pdf(x_text, MEAN, VAR) * 3

		text = "%.2f%%" % ((99.7 - 95) / 2.0,)
		plt.annotate(text, (x_point, y_point), (x_text, y_text), 
		             ha="left", fontsize=14, arrowprops=dict(arrowstyle='-'), )

		plt.annotate(text, (-x_point, y_point), (-x_text, y_text), 
		             ha="right", fontsize=14, arrowprops=dict(arrowstyle='-'), )
	
	plt.show()


if __name__ == '__main__':

	plot_normal()