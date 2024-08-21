from shiny.express import input, render, ui


ui.input_slider("n", "숫자를 선택해봐", 0, 100, 20)


@render.code
def txt():
    return f"n*2 is {input.n() * 2}"
