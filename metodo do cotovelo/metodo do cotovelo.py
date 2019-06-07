import matplotlib.pyplot as plt
from math import sqrt
import pandas as pd
import seaborn as sb
from sklearn.cluster import KMeans

df = sb.load_dataset('data-points.csv')

sum_of_squares = []
    for i in range(2, 21):
        kmeans = KMeans(n_clusters=i)
        kmeans.fit(X=df)
        sum_of_squares.append(kmeans.inertia_)
		
		
n = []
a1, b1 = 2, sum_of_squares[0]
a2, b2 = 20, sum_of_squares[len(sum_of_squares)-1]

for j in range(len(sum_of_squares)):
	a0 = j+2
	b0 = sum_of_squares[j]

	numerator = abs((b2-b1)*x0 - (a2-b2)*b0 + a2*b1 - b2*a1)
	denominator = sqrt((b2 - b1)**2 + (a2 - a1)**2)
	n.append(numerator/denominator)


kmeans = KMeans(n_clusters=n)
clusters = kmeans.fit_predict(df)

x1, x2 = 2, 20
intervalo = range(x1,x2+1)

plt.figure(figsize=(15,5))
plt.title('Método do cotovelo')
plt.xlabel('Quantidade de clusters')
plt.ylabel('Soma dos quadrados intra-clusters')
plt.grid()
plt.xticks(intervalo)
plt.plot(intervalo, sum_of_squares) # pontos laranjas
plt.plot(intervalo, sum_of_squares, '.') # linha azul

for x,y in zip(intervalo,sum_of_squares): # colocando nome nos pontos
    label = "a{}".format(x-2)
    plt.annotate(label,
                 (x,y),
                 textcoords="offset points",
                 xytext=(-5,-10),
                 ha='right')
plt.show()

plt.figure(figsize=(15,5))
plt.title('Método do cotovelo')
plt.xlabel('Quantidade de clusters')
plt.ylabel('Soma dos quadrados intra-clusters')
plt.grid()
plt.xticks(intervalo)
plt.plot(intervalo, sum_of_squares) # pontos laranjas
plt.plot(intervalo, sum_of_squares, '.') # linha azul

y2 = sum_of_squares[len(sum_of_squares)-1]
y1 = sum_of_squares[0]

plt.plot([x2, x1], [y2,y1]) # linha verde

for x,y in zip(intervalo,sum_of_squares): # colocando nome nos pontos
    if x < 3 or x > 19:
        label = "a{}".format(x-2)
        plt.annotate(label,
                     (x,y),
                     textcoords="offset points",
                     xytext=(-5,-10),
                     ha='right')
plt.show()




plt.figure(figsize=(15,5))
plt.title('Método do cotovelo')
plt.xlabel('Quantidade de clusters')
plt.ylabel('Soma dos quadrados intra-clusters')
plt.grid()
plt.xticks(intervalo)
plt.plot(intervalo, sum_of_squares)      # pontos laranjas
plt.plot(intervalo, sum_of_squares, '.') # linha azul
plt.plot([x2, x1], [y2,y1])                   # linha verde
for x,y in zip(intervalo,sum_of_squares):   # colocando nome nos pontos
    label = "a{}".format(x-2)
    if label in ['a0', 'a1', 'a18']:
        plt.annotate(label,
                     (x,y),
                     textcoords="offset points",
                     xytext=(-5,-10),
                     ha='right')
plt.show()
