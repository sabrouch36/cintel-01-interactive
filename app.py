import numpy as np
import matplotlib.pyplot as plt
from shiny import App, ui, render

app_ui = ui.page_fluid(
    ui.h2("Interactive Histogram App"),
    ui.input_slider(
        "selected_number_of_bins", 
        "Number of Bins", 
        min=0, 
        max=100, 
        value=20
    ),
    ui.output_plot("histogram_plot")
)

def server(input, output, session):
    @output
    @render.plot(alt="A histogram showing random data")
    def histogram_plot():
        np.random.seed(42)
        data = 100 + 15 * np.random.randn(437)
        plt.hist(data, bins=input.selected_number_of_bins(), density=True, color='green')  # ✅ couleur
        plt.title("Random Data Histogram")
        plt.xlabel("Value")
        plt.ylabel("Density")

app = App(app_ui, server)
