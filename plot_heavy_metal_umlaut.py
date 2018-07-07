<<<<<<< HEAD
# import matplotlib.pyplot as plt
=======
# import json
# trunk_hash = []
# branch_hash = []
# with open("transaction_test_sqlexport.json") as f:
#     data = json.load(f)
#     for i in range(len(data)):
#         for j in range(len(data)):
#             if data[i]['hash'] == data[j]['branch_transaction_hash']:
#                 branch_hash.append((i,j))
#             if data[i]['hash'] == data[j]['trunk_transaction_hash']:
#                 trunk_hash.append((i,j))
#     print(branch_hash)
#     print(trunk_hash)

import matplotlib.pyplot as plt
>>>>>>> 822425ba534ddba21aff0613d7cb89cdb916f252
import networkx as nx
import json

trunk_hash = []
branch_hash = []
trunk_hash_1 = []
branch_hash_1 = []
bundle_hash = dict()
data_map = dict()
tip0 = []
tip1 = []
index = []
<<<<<<< HEAD
#with open("transaction_test_sqlexport.json") as f:
with open("transactions_2016.json") as f:
=======
with open("transaction_test_sqlexport.json") as f:
# with open("transactions_2016.json") as f:
>>>>>>> 822425ba534ddba21aff0613d7cb89cdb916f252
      data = json.load(f)
      for element in data:
          del element['value']
          del element['address']
          del element['nonce']
          del element['signature_message_fragment']
          del element['tag']
          del element['tagIndex']
          del element['timestamp']
          del element['timestampDate']

<<<<<<< HEAD

=======
# new_data = []
# for i in range(len(data)):
#     if data[i]['current_index'] == data[i]['last_index']:
#         new_data.append(data[i])
# print(len(new_data))
    # bundle_hash
    # print(data[0])
# hash = []
# for x in range(len(data)):
#     for y in range(len(data)):
#      if data[x]['last_index'] != 0 and data[x]['bundle_hash'] == data[y]['bundle_hash']:
#          hash.append((x,y))
#          z = len(hash)
#          print(hash)


# for i in range(len(new_data)):
#     for j in range(len(new_data)):
#         if new_data[i]['hash'] == new_data[j]['branch_transaction_hash']:
#                 branch_hash.append((i,j))
#         if new_data[i]['hash'] == new_data[j]['trunk_transaction_hash']:
#                 trunk_hash.append((i,j))
# for m in range(len(new_data)):
#     if new_data[m]['hash'] == 'IMGKVJILAJVYRHHKLQXAHPFFPEPKFSOZZHESRVMKLKBYJ9DWW99LBPIPDHWQPFWRIZNF9ATZNEAXC9999':
#      print(m)
# print(new_data[23])
#    print(branch_hash)
#    print(trunk_hash)

# for i in range(len(data)):
#         if data[i]['current_index'] == data[i]['last_index']:
#             bundle_hash[data[i]['bundle_hash']] = i
# for i in range(len(data)):
#         data_map[i] = bundle_hash[data[i]['bundle_hash']]
# print(data_map)
# for (i,j) in trunk_hash:
#         trunk_hash_1.append((data_map[i], j))
# for (i,j) in branch_hash:
#         branch_hash_1.append((data_map[i], j))

# for x in range(len(data)):
#     # trunk_found = False
#     # branch_found = False
# #     for y in range(len(data)):
>>>>>>> 822425ba534ddba21aff0613d7cb89cdb916f252
for x_idx, x in enumerate(data):
    for y_idy, y in enumerate(data):
        if data[x_idx]['last_index'] == 0:
            if data[x_idx]['hash'] == data[y_idy]['trunk_transaction_hash']:
                tip0.append((y_idy,x_idx))     #tip0
<<<<<<< HEAD
            if data[x_idx]['hash'] == data[y_idy]['branch_transaction_hash']:
                tip1.append((y_idy,x_idx))    #tip1

=======
                # trunk_found = True
            if data[x_idx]['hash'] == data[y_idy]['branch_transaction_hash']:
                tip1.append((y_idy,x_idx))    #tip1
                # branch_found = True
>>>>>>> 822425ba534ddba21aff0613d7cb89cdb916f252

        elif data[x_idx]['last_index'] != 0:
            if data[x_idx]['current_index'] < data[x_idx]['last_index']:
                 if data[x_idx]['hash'] == data[y_idy]['trunk_transaction_hash']:
                     index.append((y_idy,x_idx))
<<<<<<< HEAD

                 if data[x_idx]['hash'] == data[y_idy]['branch_transaction_hash']:
                     tip0.append((y_idy,x_idx))

=======
                 #     # trunk_found = True
                 if data[x_idx]['hash'] == data[y_idy]['branch_transaction_hash']:
                     tip0.append((y_idy,x_idx))
                     # branch_found = True
>>>>>>> 822425ba534ddba21aff0613d7cb89cdb916f252

            else:
                if data[x_idx]['hash'] == data[y_idy]['trunk_transaction_hash']:
                    tip0.append((y_idy,x_idx))
<<<<<<< HEAD


                if data[x_idx]['hash'] == data[y_idy]['branch_transaction_hash']:
                    tip1.append((y_idy,x_idx))


=======
                    # trunk_found = True

                if data[x_idx]['hash'] == data[y_idy]['branch_transaction_hash']:
                    tip1.append((y_idy,x_idx))
                    # branch_found = True
        # if branch_found == True and trunk_found == True:
        #     break
>>>>>>> 822425ba534ddba21aff0613d7cb89cdb916f252
print(tip0)
print(tip1)
print(index)



#convert the list to json then store in .json  6.7 8.31pm
<<<<<<< HEAD
def store(tip0):
    with open('tip0.json', 'w') as f0:
        f0.write(json.dumps(tip0))
    with open('tip1.json', 'w') as f1:
        f1.write(json.dumps(tip1))
    with open('index.json', 'w') as f2:
        f2.write(json.dumps(index))

store(tip0)

with open('tip0.json') as f1:
    data1=json.load(f1)
# print(type(data1))

with open('tip0.json') as f2:
    data2=json.load(f2)
# print(type(data2))

with open('tip0.json') as f3:
    data3=json.load(f3)
=======
# def store(tip0):
#     with open('tip0.json', 'w') as f0:
#         f0.write(json.dumps(tip0))
#     with open('tip1.json', 'w') as f1:
#         f1.write(json.dumps(tip1))
#     with open('index.json', 'w') as f2:
#         f2.write(json.dumps(index))
#
# store(tip0)
#
# with open('tip0.json') as f1:
#     data1=json.load(f1)
# # print(type(data1))
#
# with open('tip0.json') as f2:
#     data2=json.load(f2)
# # print(type(data2))
#
# with open('tip0.json') as f3:
#     data3=json.load(f3)
>>>>>>> 822425ba534ddba21aff0613d7cb89cdb916f252




#
#
#
G = nx.DiGraph()
# for e in range(len(branch_hash)):
#
#     a = branch_hash[e][1]
#     b = branch_hash[e][0]
#     G.add_edge(a, b)
#
# for e in range(len(trunk_hash)):
#     a = trunk_hash[e][1]
#     b = trunk_hash[e][0]
#
#     G.add_edge(a, b)
<<<<<<< HEAD
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


=======
# for e in range(len(tip0)):
#
#     a = tip0[e][0]
#     b = tip0[e][1]
#     G.add_edge(a, b)
# for e in range(len(tip1)):
#
#     a = tip1[e][0]
#     b = tip1[e][1]
#     G.add_edge(a, b)
# for e in range(len(index)):
#
#     a = index[e][0]
#     b = index[e][1]
#     G.add_edge(a, b)



#   b = data[i]['branch_transaction_hash']
#   c = data[i]['trunk_transaction_hash']
# print(len(branch_hash))


# G.add_edge(c, a)
#G.add_edge(c, d)
#G.add_edge(d, e)
#G.add_edge(e, f)
#G.add_edge(e, d)
#G.add_edge(g, b)
#G.add_edge(d, b)

>>>>>>> 822425ba534ddba21aff0613d7cb89cdb916f252
# write in UTF-8 encoding
fh = open('edgelist.utf-8', 'wb')
fh.write('# -*- coding: utf-8 -*-\n'.encode('utf-8'))  # encoding hint for emacs
nx.write_multiline_adjlist(G, fh, delimiter='\t', encoding='utf-8')

# read and store in UTF-8
fh = open('edgelist.utf-8', 'rb')
H = nx.read_multiline_adjlist(fh, delimiter='\t', encoding='utf-8')

# for n in G.nodes():
#     if n not in H:
#         print(False)

#print(list(G.nodes()))

<<<<<<< HEAD
=======
#distance=nx.dijkstra_path_length(G,a,b) #shortest distance
#print(distance)
#path=nx.dijkstra_path(G,a,e) #shortest path
#print(path)
#num_node=nx.number_of_nodes(G) #number of nodes
#print(num_node)

>>>>>>> 822425ba534ddba21aff0613d7cb89cdb916f252
# pos = nx.spring_layout(G)
# nx.draw(G, pos, font_size=16, with_labels=False)
# for p in pos:  # raise text positions
#     pos[p][1] += 0.07
# nx.draw_networkx_labels(G, pos)
# plt.show()

# print(G.degree(2))
# print(G.in_degree())
# print(G.out_degree())

#degree calculation
<<<<<<< HEAD
degree_list=[]
for k0 in range(len(G.degree())):
  degree = G.degree(k0)
  degree_list +=[degree]
  if G.in_degree(k0) == max(degree_list):
    print("This point dergree has the max degree :", k0)
print(degree_list)
print("max degree is :",max(degree_list))


# #in-degree calculation
in_degree_list = []
for k1 in range(len(G.in_degree())):
  in_degree = G.in_degree(k1)
  in_degree_list +=[in_degree]
  if G.in_degree(k1) == max(in_degree_list):
      print("This point dergree has the max in_degree :", k1)
print(in_degree_list)
print("max in-degree is :",max(in_degree_list))
#
# #out-degree calculation
out_degree_list = []
for k2 in range(len(G.out_degree())):
  out_degree = G.out_degree(k2)
  out_degree_list +=[out_degree]
  if G.out_degree(k2) == max(out_degree_list):
    print("This point dergree has the max out_degree :", k2)

print(out_degree_list)
print("max out-degree is :",max(out_degree_list))



=======
# degree_list=[]
# for k in range(len(G.degree())):
#   degree = G.degree(k)
#   degree_list +=[degree]
# print(degree_list)
# print("max degree is :",max(degree_list))
#
# #in-degree calculation
# in_degree_list = []
# in0 = []
# in1 = []
# in2 = []
# in3 = []
# in4 = []
# in5 = []

# for k in range(len(G.in_degree())):
#   in_degree = G.in_degree(k)
#   in_degree_list +=[in_degree]
#   if G.in_degree(k) == 5:
#       print("This point dergree has the max in_degree :", k)
#   if G.in_degree(k) == 0:
#       in0 += [k]
#   if G.in_degree(k) == 1:
#       in1 += [k]
#   if G.in_degree(k) == 2:
#       in2 += [k]
#   if G.in_degree(k) == 3:
#       in3 += [k]
#   if G.in_degree(k) == 4:
#       in4 += [k]
#   if G.in_degree(k) == 5:
#       in5 += [k]
# print(len(in0))
# print(len(in1))
# print(len(in2))
# print(len(in3))
# print(len(in4))
# print(len(in5))
# print(in_degree_list)
# print("max in-degree is :",max(in_degree_list))
#
# #out-degree calculation
# out0 = []
# out1 = []
# out2 = []
# out3 = []
# out_degree_list = []
# for k in range(len(G.out_degree())):
#   out_degree = G.out_degree(k)
#   out_degree_list +=[out_degree]
#   if G.out_degree(k) == 0:
#       out0 += [k]
#   if G.out_degree(k) == 1:
#       out1 += [k]
#   if G.out_degree(k) == 2:
#       out2 += [k]
#   if G.out_degree(k) == 3:
#       out3 += [k]
# print(len(out0))
# print(len(out1))
# print(len(out2))
# print(len(out3))
#
#
# print(out_degree_list)
# print("max out-degree is :",max(out_degree_list))
#
# print(data[28])
#
>>>>>>> 822425ba534ddba21aff0613d7cb89cdb916f252
# pos = nx.spring_layout(G)
# nx.draw(G, pos, font_size=16, with_labels=False)
# for p in pos:  # raise text positions
#     pos[p][1] += 0.07
# nx.draw_networkx_labels(G, pos)
# plt.show()


<<<<<<< HEAD
=======
##所有节点度的分布表
# degree_his = nx.degree_histogram(G)
# x = range(len(degree_his))
# y = [z / float(sum(degree_his)) for z in degree_his]
# plt.loglog(x,y,color="blue",linewidth=2)
# print(degree_his)
# plt.show()

# print(nx.diameter(G))
>>>>>>> 822425ba534ddba21aff0613d7cb89cdb916f252
