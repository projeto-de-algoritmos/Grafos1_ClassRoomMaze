import pymaze, dfs, bfs
from pymaze import maze,agent,textLabel,COLOR
from dfs import *
from bfs import *
from timeit import timeit

#Instancia o labirinto
m=maze()

#Desenha o labirinto
m.CreateMaze(loadMaze= 'maze--2022-06-26--17-20-50.csv',x=4,y=7, theme='light')

searchPath,dfsPath,fwdDFSPath=DFS(m)
bSearch,bfsPath,fwdBFSPath=BFS(m)

textLabel(m,'Número de passos do Caminho do DFS',len(fwdDFSPath)+1)
textLabel(m,'Tamanho do Caminho do BFS',len(fwdBFSPath)+1)
textLabel(m,'Número de passos da Busca do DFS',len(searchPath)+1)
textLabel(m,'Tamanho da Busca do BFS',len(bSearch)+1)


a=agent(m,footprints=True,color=COLOR.yellow,filled=True)

b=agent(m,footprints=True,color=COLOR.blue, shape='arrow')

c=agent(m,footprints=True,color=COLOR.red,shape='arrow',filled=False)

e=agent(m,footprints=True,color=COLOR.green,filled=True)


m.tracePath({e:searchPath},delay=150)
m.tracePath({a:bSearch},delay=200)
m.tracePath({c:fwdBFSPath},delay=200)
m.tracePath({b:fwdDFSPath},delay=150)


m.run()