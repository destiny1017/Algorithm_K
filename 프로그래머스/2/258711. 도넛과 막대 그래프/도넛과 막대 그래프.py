# 조건
# 1. 연결 : in == 0, out >= 2
# 2. 막대 : in == 0
# 3. 8자 : in == 2, out == 2
# 4. 도넛 : in, out 순환
# 구현 순서
# 1. graph dict 생성하여 모든 노드 및 간선정보 저장
# 2. graph 순회하여 연결그래프 제거
# 2. graph 차례대로 순회하며 막대 및 8자그래프 선별
# 3. 막대 및 8자 그래프 간선대로 순회하며 dict에서 제거
# 4. 남은 dict에서 순환 그래프 제거
import sys
sys.setrecursionlimit(10 ** 6)

def cycle_edge(now, st, node_list, node_map):
    node_list.append(now)
    if node_map[now]['egress'][0] == st:
        return node_list
    return cycle_edge(node_map[now]['egress'][0], st, node_list, node_map)


def string_nodes(now, node_list, node_map):
    node_list.append(now)
    if node_map[now]['egress']:
        string_nodes(node_map[now]['egress'][0], node_list, node_map)
    return node_list


def solution(edges):
    result = [0, 0, 0, 0]
    node_map = {}
    for st, ed in edges:
        if st not in node_map:
            node_map[st] = {'ingress': [], 'egress': []}
        if ed not in node_map:
            node_map[ed] = {'ingress': [], 'egress': []}
        node_map[st]['egress'].append(ed)
        node_map[ed]['ingress'].append(st)

    # 연결 노드 찾고 간선 제거
    for key in node_map:
        n = node_map[key]
        if not n['ingress'] and len(n['egress']) >= 2:
            result[0] = key
            for node in n['egress']:
                node_map[node]['ingress'].remove(key)
            node_map.pop(key)
            break

    string_list = []
    octa_list = []

    # 막대그래프 및 8자그래프 찾기
    for key in node_map:
        if not node_map[key]['ingress']:
            string_list.append(key)
        elif len(node_map[key]['ingress']) == 2 == len(node_map[key]['egress']):
            octa_list.append(key)

    # 막대그래프 연결 노드 모두 제거
    for string in string_list:
        nodes = string_nodes(string, [], node_map)
        while nodes:
            node_map.pop(nodes.pop(), None)

    # 8자그래프 연결 노두 모두 제거
    for octa in octa_list:
        while node_map[octa]['egress']:
            nodes = []
            nodes.extend(cycle_edge(octa, octa, [], node_map))
            nodes.remove(octa)
            while nodes:
                node_map.pop(nodes.pop(), None)
            del node_map[octa]['egress'][0]
        node_map.pop(octa, None)

    # 도넛그래프 개수 카운트
    while node_map:
        result[1] += 1
        key = next(iter(node_map))
        nodes = cycle_edge(key, key, [], node_map)
        while nodes:
            node_map.pop(nodes.pop(), None)

    result[2], result[3] = len(string_list), len(octa_list)

    return result