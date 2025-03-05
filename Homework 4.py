#N1
# N,M=map( int,input().split())
# res = []
# for i in range(M):
#     x, y = (int(x) for x in input().split())
#     res.append((x, y))
# print(res)

#N2
# def adj_matrix(N, edge_list):
#     res = [[0 for j in range(N)] for i in range(N)]
#
#     for x, y in edge_list:
#         res[x][y] = 1
#         res[y][x] = 1
#
#     return res
# N=4
# res=[(0,1),(1,3)]
# A= adj_matrix(N, res)
# for p in A:
#     print(p)

#N3
# def reverse(matrix):
#     n= len(matrix)
#     r_matrix=[[0 for i in range(n)] for j in range(n)]
#     for i in range(n):
#         for j in range(n):
#             if matrix[i][j]==1:
#                 r_matrix[j][i]=1
#     return r_matrix
# matr= [
#     [0, 0, 1, 1],
#     [0, 0, 1, 0],
#     [1, 1, 0, 0],
#     [1, 0, 1, 0]
# ]
# r_matrix=reverse(matr)
# for line in r_matrix:
#     print(line)

#N5
# def DFS(curr_node, adj_list, visited=None):
#     print(f"{curr_node}")
#     visited.add(curr_node)
#     for adj_node in adj_list[curr_node]:
#         if adj_node not in visited:
#             DFS(adj_node, adj_list, visited)
#     print(f"{curr_node}")

# adj_list={0:[1],1:[2,3],2:[1,3],3:[1,2]}
# visited=set()
# DFS(2, adj_list, visited)

#N6
# def FB(curr_node, adj_list):
#     d = [float("inf")] * len(adj_list)
#     d[curr_node] = 0
#     for i in range(len(adj_list) - 1):
#         for x, y in adj_list:
#             if d[x] != float("inf") and d[x] < d[y]:
#                 d[y] = d[x]
#         for x, y in adj_list:
#             if d[x] != float("inf") and d[x] < d[y]:
#                  print("Отрицательный цикл")
#     return d
#
# adj_list = [(0, 1),(0,2), (1, 3), (1, 4),(4,5), (5,3),(4,2)]
# d = FB(0,adj_list)
# print(d)