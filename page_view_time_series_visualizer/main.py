from time_series_visualizer import draw_line_plot, draw_bar_plot, draw_box_plot

# Dibujar gráfico de líneas
fig_line = draw_line_plot()
fig_line.savefig('line_plot.png')

# Dibujar gráfico de barras
fig_bar = draw_bar_plot()
fig_bar.savefig('bar_plot.png')

# Dibujar gráficos de caja
fig_box = draw_box_plot()
fig_box.savefig('box_plot.png')

print("Gráficos generados: line_plot.png, bar_plot.png y box_plot.png")
