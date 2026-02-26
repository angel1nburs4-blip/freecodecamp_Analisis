from sea_level_predictor import draw_plot
import matplotlib.pyplot as plt

# Dibujar la predicción y guardar la figura
fig = draw_plot()
plt.close(fig)
print("Gráfico generado: sea_level_plot.png")