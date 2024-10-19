from bokeh.layouts import layout  
from bokeh.models import Div, RangeSlider, Spinner
from bokeh.plotting import figure, show  

# Prepara algunos datos para el gráfico
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [4, 5, 5, 7, 2, 6, 4, 9, 1, 3]  

# Crea una figura (gráfico) con un rango de x y dimensiones definidas
p = figure(x_range=(1, 9), width=500, height=250)

# Puntos al gráfico en forma de círculos
points = p.scatter(x=x, y=y, size=30, fill_color="#21a7df")

# Configura un área de texto (Div) con un pequeño mensaje
div = Div(
    text="""
          <p>Selecciona el tamaño del círculo usando este control:</p>
          """,
    width=200,
    height=30,
)

# Configura un spinner (control tipo 'input' numérico) para cambiar el tamaño de los círculos
spinner = Spinner(
    title="Tamaño del círculo",
    low=0,  
    high=60, 
    step=5, 
    value=points.glyph.size,
    width=200,
)
# Vincula el valor del spinner con el tamaño de los círculos (glyph) del gráfico
spinner.js_link("value", points.glyph, "size")

# Configura un deslizador de rango (RangeSlider) para ajustar el rango del eje X
range_slider = RangeSlider(
    title="Ajustar rango del eje X",
    start=0,
    end=10,  
    step=1,  
    value=(p.x_range.start, p.x_range.end),
)
# Valor del deslizador con el rango de inicio y de finalizacion del eje X
range_slider.js_link("value", p.x_range, "start", attr_selector=0)
range_slider.js_link("value", p.x_range, "end", attr_selector=1)

# Crea un layout que organiza los elementos (div, spinner, slider, gráfico)
layout = layout(
    [
        [div, spinner], 
        [range_slider],  
        [p],
    ],
)

# Muestra el resultado final en el navegador
show(layout)
