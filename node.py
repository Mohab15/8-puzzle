class Node:


    def __init__(self, state, parent=None, action="", col=3):
        self.state = state
        self.index = state.find("0")
        self.parent = parent
        self.action = action
        self.col = col
        if parent is None:
            self.depth = 0
        else:
            self.depth = self.parent.depth + 1

        # Children
        self.children = []



def swap(s, i, j):
    lst = list(s)
    lst[i], lst[j] = lst[j], lst[i]
    return ''.join(lst)
