# from utill import Stack, Queue 
# def earliest_ancestor(ancestors, starting_node):
#     s= Stack()
#     s.push([starting_node])
#     visited = set()
#     while s.size() > 0 :
#         v = s.pop()
#         l = v[-1]
#         if l not in visited:
#             if l is ancestors:
#                 return v
#             visited.add(l)
#         for next_v in get_neighbors(l):
#                 new_path = v + [next_v]
#                 s.push(new_path)
        
# def get_neighbors(vertex_id):
#     return vertices[vertex_id]