import matplotlib.pyplot as plt
import networkx as nx
import json

#convert .json to list
with open('tip0.json') as f1:
        tip0 = json.load(f1)
with open('tip1.json') as f2:
        tip1 = json.load(f2)
with open('index.json') as f3:
        index = json.load(f3)


G = nx.DiGraph()

for e in range(len(tip0)):
    a = tip0[e][0]
    b = tip0[e][1]
    G.add_edge(a, b)
for e in range(len(tip1)):
    a = tip1[e][0]
    b = tip1[e][1]
    G.add_edge(a, b)
for e in range(len(index)):
    a = index[e][0]
    b = index[e][1]
    G.add_edge(a, b)

degree_list = []
max_degree_node = []
for k0 in range(len(G.degree())):
  degree = G.degree(k0)
  degree_list +=[degree]

max_dgree = max(degree_list)
for k00 in range(len(G.degree)):
    if G.degree(k00) == max_dgree:
      max_degree_node +=[k00]

print("This point dergree has the max degree :", max_degree_node)
print("degree_list is : ", degree_list)
print("max degree is :",max(degree_list))

out_degree_list = []
max_out_degree_node = []
min_out_degree_node = []

for k4 in range(len(G.out_degree())):
  out_degree = G.out_degree(k4)
  out_degree_list +=[out_degree]

max_outdgree = max(out_degree_list)
for k41 in range(len(G.out_degree)):
  if G.out_degree(k41) == max_outdgree:
      max_out_degree_node +=[k41]
  if G.out_degree(k41) == 0:
      min_out_degree_node += [k41]
print("This point dergree has the max out_degree :", max_out_degree_node)
print("This point dergree has the min out_degree :", min_out_degree_node)
print("out_degree_list is : ", out_degree_list)
print("max out-degree is :",max(out_degree_list))
print("min out-degree is :",min(out_degree_list))


in_degree_list = []
max_in_degree_node = []
min_in_degree_node = []

for k4 in range(len(G.in_degree())):
  in_degree = G.in_degree(k4)
  in_degree_list +=[in_degree]

max_indgree = max(in_degree_list)
for k41 in range(len(G.in_degree)):
  if G.in_degree(k41) == max_indgree:
      max_in_degree_node +=[k41]
  if G.in_degree(k41) == 0:
      min_in_degree_node +=[k41]
print("This point dergree has the max in_degree :", max_in_degree_node)
print("This point dergree has the min in_degree :", min_in_degree_node)
print("in_degree_list is : ", in_degree_list)
print("max in-degree is :",max(in_degree_list))
print("min in-degree is :",min(in_degree_list))


with open('transactions_2016.json') as f:
        data = json.load(f)
print("This point dergree has the max in_degree :", data[392]['hash'])
print("This point dergree has the min out_degree :", data[6133])
print("This point dergree has the min in_degree :", data[0])











