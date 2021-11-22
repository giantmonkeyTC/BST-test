import math


def depthTimesNumber(depth):
    return depth * 2 ** (depth - 1)


def replacedFullListCompCompute(depth, replaceLeafNode, K):
    comp = 0
    for num in range(1, K + 1):
        print(num)
        comp += depth + num
    print(comp)
    fullListNumber = replaceLeafNode * 2
    return (depth + 1 + depth + 2 + depth + 3 + depth + 4) * fullListNumber


def notChangedListCompCompute(depth, nodeNotChanged):
    return (depth + 1 + depth + 2 + depth + 3) * nodeNotChanged


def leafNodesNumber(total, K):
    depth = math.floor(math.log((total + 1) * 2 / K + 1, 2))
    fullTreeNode = 2 ** depth - 1 + (K - 1) * 2 ** (depth - 1)
    leafNode = 2 ** (depth - 1)

    nodeNotAdded = total - fullTreeNode

    replaceLeafNode = math.floor(nodeNotAdded / (K + 1))

    nodeNotAdded = nodeNotAdded - replaceLeafNode * (K + 1)

    # replace one leafNode to linkList to add nodeNotAdded

    replacedFullListComp = replacedFullListCompCompute(depth, replaceLeafNode, K)

    nodeNotChanged = leafNode - replaceLeafNode - 1

    notChangedListComp = notChangedListCompCompute(depth, nodeNotChanged)

    fullNodeComp = 0
    for dep in range(1, depth + 1):
        fullNodeComp += depthTimesNumber(dep)

    totalComp = fullNodeComp + notChangedListComp + replacedFullListComp

    print("depth : %d" % depth)
    print("fullTreeNode : %d" % fullTreeNode)
    print("replaceLeafNode : %d" % replaceLeafNode)
    print("fullNodeComp : %d" % fullNodeComp)
    print("nodeNotAdded : %d" % nodeNotAdded)
    print("replacedFullListComp : %d" % replacedFullListComp)
    print("notChangedListComp : %d" % notChangedListComp)
    print("notChangedListComp : %d" % notChangedListComp)
    print("totalComp = %d" % totalComp)
    print("avgComp = %f" % (totalComp / total))


class Tree():
    def __init__(self, data=None, left=None, right=None, depth=1, parent=None, check=False):
        self.data = data
        self.left = left
        self.right = right
        self.depth = depth


class Term():
    def __init__(self, term=None, freq=None):
        self.term = term
        self.freq = freq / 33400


def constructTree(start, end, mlist, height=1):
    tlist = []
    if (start > end):
        tlist.append(None)
        return tlist
    if (start == end):
        tlist.append(Tree(mlist[start]))
        return tlist
    for num in range(start, end + 1):
        lefts = constructTree(start=start, end=num - 1, mlist=mlist, height=height + 1)
        rights = constructTree(start=num + 1, end=end, mlist=mlist, height=height + 1)
        for left in lefts:
            for right in rights:
                root = Tree(mlist[num])
                root.left = left
                root.right = right
                if (left):
                    left.depth = height + 1
                if (right):
                    right.depth = height + 1
                tlist.append(root)
    return tlist


def pre_order(tree, total=0):
    if tree == None:
        return
    stack = []
    while tree or len(stack) > 0:
        if tree:
            stack.append(tree)
            print(tree.data.term, tree.depth)
            total += tree.data.freq * tree.depth
            tree = tree.left
        else:
            tree = stack[-1]
            stack.pop()
            tree = tree.right
    return total


def printTree(tree, depth=1):
    if (tree == None):
        return
    printTree(tree.right, depth + 1)
    printTree(tree.left, depth + 1)
    print(tree.data.term, depth)


def bestBinaryTree():
    a = Term(1, 4000)
    b = Term(2, 100)
    d = Term(3, 5000)
    e = Term(4, 9000)
    j = Term(5, 100)
    o = Term(6, 10000)
    p = Term(7, 5000)
    w = Term(8, 200)

    mlist = [a, b, d, e, j, o, p, w]

    totalList = []
    trees = constructTree(start=0, end=7, mlist=mlist)
    for tree in trees:
        total = pre_order(tree)
        print(total)
        totalList.append(total)
        print("-----------------")
    print("min:", min(totalList), "total binary trees", len(totalList))


bestBinaryTree()
