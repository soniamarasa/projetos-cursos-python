import matplotlib.pyplot as plt

# x_values = [1, 2, 3, 4, 5]
# y_values = [1, 4, 9, 16, 25]

# plt.scatter(x_values, y_values, s=100)

# # Define o título do gráfico e nomeia os eixos
# plt.title("Square Numbers", fontsize=24)
# plt.xlabel("Value", fontsize=14)
# plt.ylabel("Square of Value", fontsize=14)

# # Define o tamanho dos rótulos das marcações
# plt.tick_params(axis='both', which='major', labelsize=14)

x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]

# plt.scatter(x_values, y_values, c='crimson', edgecolor='none', s=40)

# Ou RGB
# plt.scatter(x_values, y_values, c=(0, 0, 0.8), edgecolor='none', s=40)

# Colormap
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolor='none', s=40)

# Define o título do gráfico e nomeia os eixos
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# Define o intervalo para cada eixo
plt.axis([0, 1100, 0, 1100000])

# Para salvar graficos automaticamente. 
# O primeiro argumento é o nome de um arquivo para a imagem do
# gráfico, que será salvo no mesmo diretório que scatter_squares.py. O
# segundo argumento remove espaços em branco extras do gráfico. Se quiser
# ter espaços em branco extras ao redor do gráfico, você poderá omitir esse
# argumento.

plt.savefig('squares_plot.png', bbox_inches='tight')

plt.show()