
def find_parent(parent, v):
    if parent[v] != v:
        parent[v] = find_parent(parent, parent[v])
    return parent[v]

def union_parent(parent, n1, n2):
    n1parent = find_parent(parent, n1)
    n2parent = find_parent(parent, n2)
    
    if n1parent < n2parent:
        parent[n2parent] = n1parent
    else:
        parent[n1parent] = n2parent

def solution(n, costs):
    answer = 0
    parent = [i for i in range(n)]
    costs.sort(key=lambda x: x[2])
    
    for n1, n2, cost in costs:
        if find_parent(parent, n1) == find_parent(parent, n2):
            continue
        
        union_parent(parent, n1, n2)
        answer += cost

    return answer