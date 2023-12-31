import networkx as nx           #para generar grafos
import matplotlib.pyplot as plt #para graficar
import random                   #para aleatorizar el colroeado de los nodos

#---------------------------------- algoritmos --------------------------------------------------------------------
def traffic_colors(G):
    colors_dict = {}
    nodes_ordered = list(G.nodes())
    random.shuffle(nodes_ordered)
    
    for vertex in nodes_ordered:
        intersection_key = int(str(vertex).split('_')[0])  # Extract the intersection number from the node name

        # Check if a color has already been assigned within this intersection
        if intersection_key not in [int(i.split('_')[0]) for i in list(colors_dict.keys())]:
            colors_dict[vertex] = 1
        else:
            colors_dict[vertex] = 0

        print("Nodo:", vertex)
        print(intersection_key)
        print("Color:", colors_dict[vertex])
        print("Diccionario:", colors_dict)
        print("----------------------------------------------------------")

    ordered_nodes = list(G.nodes())
    node_colors = [colors[(colors_dict[i])] for i in ordered_nodes]

    return node_colors

#------------------------- Main --------------------------------------------------------
#Grafo dirigido
G = nx.DiGraph()

#Cada row representa una interseccion, y los semaforos que tiene
nodes = ['{}_{}'.format(i,j) for j in range(1,5) for i in range(1,5)] 

edges = [ ('5_4', '1_3'), ('5_4', '1_4'), ('5_4', '1_2'),
          ('5_3', '1_1'), ('5_3', '1_3'), ('5_3', '1_4'),
          ('1_4', '2_3'), ('1_4', '2_4'), ('1_4', '2_2'),
          ('1_3', '3_1'), ('1_3', '3_3'), ('1_3', '3_4'),
          
          ('6_1', '2_2'), ('6_1', '2_1'), ('6_1', '2_3'),
          ('6_3', '2_1'), ('6_3', '2_3'), ('6_3', '2_4'),
          ('2_1', '1_2'), ('2_1', '1_1'), ('2_1', '1_3'),   
          ('2_3', '4_1'), ('2_3', '4_3'), ('2_3', '4_4'),
          
          ('7_4', '3_2'), ('7_4', '3_3'), ('7_4', '3_4'), 
          ('7_2', '3_1'), ('7_2', '3_2'), ('7_2', '3_4'), 
          ('3_2', '1_1'), ('3_2', '1_2'), ('3_2', '1_4'),
          ('3_4', '4_2'), ('3_4', '4_3'), ('3_4', '4_4'),
          
          ('8_1', '4_2'), ('8_1', '4_1'), ('8_1', '4_3'),
          ('8_2', '4_1'), ('8_2', '4_2'), ('8_2', '4_4'),
          ('4_1', '3_2'), ('4_1', '3_1'), ('4_1', '3_3'),
          ('4_2', '2_1'), ('4_2', '2_2'), ('4_2', '2_4') ]

colors = ['red', 'green']

pos = {'1_1': (0, 8), '1_2': (2, 9), '1_3': (1, 6),
       '1_4': (3, 7), '5_4': (-2, 7), '5_3': (1, 11),

       '2_1': (6, 8), '2_2': (8, 9), '2_3': (7, 6),
       '2_4': (9, 7), '6_1': (11, 8), '6_3': (7, 11),

       '3_1': (0, 2), '3_2': (2, 3), '3_3': (1, 0),
       '3_4': (3, 1), '7_4': (-2, 1), '7_2': (2, -2),

       '4_1': (6, 2), '4_2': (8, 3), '4_3': (7, 0),
       '4_4': (9, 1), '8_1': (11, 2), '8_2': (8, -2)
}

#agregar al grafo nodos y aristas
G.add_nodes_from(nodes)
G.add_edges_from(edges)

print("----------------------------------------------------------")
print("NODOS:", nodes)
print("----------------------------------------------------------")
print("ARISTAS:", edges)
print("----------------------------------------------------------")
print("NUMERO DE COLORES", len(colors))
print("----------------------------------------------------------")

# Gráfica
fig = plt.figure(figsize=(6,6))
ax = fig.add_axes([0,0,1,1])
ax.axhline(1.5, lw=75, zorder=1, color='lightgrey')
ax.axhline(7.5, lw=75, zorder=1, color='lightgrey')
ax.axvline(1.5, lw=75, zorder=1, color='lightgrey')
ax.axvline(7.5, lw=75, zorder=1, color='lightgrey')

nx.draw(G, pos, with_labels=True, node_size=700, node_color=traffic_colors(G), font_size=10, font_color="black", font_weight="bold", arrowsize=20, ax=ax)

#Iterate 10 times to simulate time passing by and traffic lights being recoded
for _ in range(10):
    plt.pause(5)
    nx.draw(G, pos, with_labels=True, node_size=700, node_color=traffic_colors(G), font_size=10, font_color="black", font_weight="bold", arrowsize=20, ax=ax)

# Show the final plot
plt.show()
