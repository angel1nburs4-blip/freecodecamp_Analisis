from medical_data_visualizer import draw_cat_plot, draw_heat_map
import matplotlib.pyplot as plt

# Dibujar catplot
fig_cat = draw_cat_plot()
fig_cat.savefig('catplot.png')
plt.close(fig_cat)

# Dibujar heatmap
fig_heat = draw_heat_map()
fig_heat.savefig('heatmap.png')
plt.close(fig_heat)

print("Gráficos generados: catplot.png y heatmap.png")