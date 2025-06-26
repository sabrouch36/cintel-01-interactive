import numpy as np
import matplotlib.pyplot as plt
from shiny import App, ui, render

app_ui = ui.page_fluid(
    ui.h2("Interactive Histogram App"),
    ui.input_slider(
        "selected_number_of_bins", 
        "Number of Bins", 
        min=1, 
        max=100, 
        value=20
    ),
    ui.output_plot("histogram_plot")
)

def server(input, output, session):
    @output
    @render.plot(alt="A histogram with custom color")
    def histogram_plot():
        np.random.seed(42)
        data = 100 + 15 * np.random.randn(437)
        bins = input.selected_number_of_bins()
        
        counts, edges = np.histogram(data, bins=bins, density=True)
        centers = 0.5 * (edges[1:] + edges[:-1])

        plt.bar(centers, counts, width=(edges[1]-edges[0]), color='green', edgecolor='black')
        
        plt.title("Random Data Histogram")
        plt.xlabel("Value")
        plt.ylabel("Density")

app = App(app_ui, server)
