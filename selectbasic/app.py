
from shiny.express import input, render, ui

ui.input_selectize(
    "var", "Select variable",
    choices=["bill_length_mm", "body_mass_g", "bill_depth_mm"]
)

@render.plot
def hist():
    from matplotlib import pyplot as plt
    from palmerpenguins import load_penguins

    df = load_penguins()
    df[input.var()].hist(grid=False)
    plt.xlabel(input.var())
    plt.ylabel("count")

