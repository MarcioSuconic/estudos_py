import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot()

lista_meses = ['8/2024', '9/2024', '10/2024', '11/2024', '12/2024', '1/2025', '2/2025', '3/2025']
lista_valores = [6803.8, 5816.1, 4068.2, 4661.8, 3490.4, 8102.1, 5069.7, 5791.1]
ax.plot(lista_meses,lista_valores)

lista_meses = ['8/2024', '9/2024', '10/2024', '11/2024', '12/2024', '1/2025', '2/2025', '3/2025']
lista_valores = [3496.6, 3490.0, 2702.7, 3273.1, 2804.0, 5834.3, 3651.0, 3679.0]
ax.plot(lista_meses, lista_valores)

plt.show()