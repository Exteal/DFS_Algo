from _collections import deque


def has_unmarked_child(adjacenct_list, vertex, marked):
    for v in adjacenct_list[vertex]:
        if v not in marked:
            return True
        for w in adjacenct_list[v]:
            if w not in marked:
                return True
    return False

def dfs(starting_vertex):
    adjacency_list = {
        0 : [4, 5],
        1 : [1, 4, 6, 7],
        2 : [3],
        3 : [2],
        4 : [8, 9],
        5 : [10,12],
        6 : [],
        7 : [3],
        8 : [9],
        9 : [10],
        10 : [6 ,8],
        11 : [6, 7, 10],
        12 : []
    }
    pre = {}
    post = {}

    count = 1
    marked = []
    pre[starting_vertex] = count
    count = count + 1
    stack = deque()
    stack2 = deque()
    stack.append(starting_vertex)
    marked.append(starting_vertex)
    while stack or stack2:
        v = stack.pop()
        stack2.append(v)
        if v not in pre.keys():
            pre[v] = count
            count = count+1
        stack_unmarked_children(adjacency_list, marked, stack, v)
        if len(adjacency_list[v]) == 0 or not has_unexplored_child(adjacency_list[v], pre):
            count = backtrack(count, adjacency_list, post, pre, stack2, stack)
        stack_unexplored_components(adjacency_list, marked, stack, stack2)
    return pre, post


def stack_unmarked_children(adjacency_list, marked, stack, v):
    for s in reversed(adjacency_list[v]):
        if s not in marked:
            stack.append(s)
            marked.append(s)


def has_unexplored_child(adjacents , pre):
    for v in adjacents:
        if v not in pre.keys():
            return True
    return False



def backtrack(count, adjacent_list, post, pre, stack2, stack):
    while stack2:
        v = stack2.pop()
        if v in pre.keys() and not has_unexplored_child(adjacent_list[v], pre):
            post[v] = count
            count = count + 1
        else:
            stack.appendleft(v)

    return count


def stack_unexplored_components(adjacency_list, marked, stack, stack2):
    if not stack and not stack2:
        for v in adjacency_list.keys():
            if v not in marked:
                stack.append(v)
                marked.append(v)
                break

list1, list2 = dfs(0)
print(list1)
print(list2)