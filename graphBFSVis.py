import networkx as nx #knihovna pro vytváření grafů
import matplotlib.pyplot as plt #knihovna pro vizualizaci
import collections 

 
def BFS(G, root, pos): 
	#datová struktura pro revizi již navštívených uzlů
	visited = [False]*(len(G.nodes()))
	#fronta pro ještě nenavštívené uzly 
	queue = []		
	queue.append(root)
	visited[root] = True
	while queue:
		curr_node = queue.pop(0)
		for i in G[curr_node]:  
			if visited[i] == False:
				queue.append(i)
				visited[i] = True
				#zakreslení a vyznačení nejkratších cest v grafu 
				nx.draw_networkx_edges(G, pos, edgelist = [(curr_node,i)], width = 2.5, alpha = 0.6, edge_color = 'r')
	return



#funkce pro vytvoření grafu ze vstupu textového editoru
def CreateGraph():
	G = nx.DiGraph()
	f = open('input.txt')
	#celkový počet uzlů
	n = int(f.readline())
	#vložím si vstupní parametry do matice
	wtMatrix = []
	for i in range(n):
		list1 = list(map(int, (f.readline()).split()))
		wtMatrix.append(list1)
	root = int(f.readline()) #kořenový uzel
	#přidání hran s jejich délkou 
	for i in range(n):
		for j in range(len(wtMatrix[i])):
			if wtMatrix[i][j] > 0:
    				#přidávám hrany k uzlům
					G.add_edge(i, j, length = wtMatrix[i][j]) 
	return G, root



#vykreslí graf a délky stran
def DrawGraph(G):
	pos = nx.spring_layout(G)
	nx.draw(G, pos, with_labels = True)  #štítky s číslem uzlu
	edge_labels = dict([((u,v,), d['length']) for u, v, d in G.edges(data = True)])
	nx.draw_networkx_edge_labels(G, pos, edge_labels = edge_labels, label_pos = 0.3, font_size = 11) #štítky pro hrany
	return pos




if __name__== "__main__":
	G,root = CreateGraph()
	pos = DrawGraph(G)
	BFS(G, root, pos)
	plt.show()