import matplotlib.pyplot as plt

class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Reg_Node:
    def __init__(self, pos, data=0):
        self.pos = pos
        self.data = data

class QuadtreeNode:
    def __init__(self, top_left, bot_right):
        self.top_left = top_left
        self.bot_right = bot_right
        self.data = None
        self.is_leaf = True
        self.top_left_tree = None
        self.top_right_tree = None
        self.bot_left_tree = None
        self.bot_right_tree = None

class Quadtree:
    def __init__(self, top_left, bot_right):
        self.root = QuadtreeNode(top_left, bot_right)

    def insert(self, node, current_node=None):
        if current_node is None:
            current_node = self.root

        if not self.in_boundary(node.pos, current_node.top_left, current_node.bot_right):
            return

        if current_node.is_leaf and current_node.data is None:
            current_node.data = node
            return

        if current_node.is_leaf and current_node.data is not None:
            current_node.is_leaf = False
            self.insert(current_node.data, current_node)

        if node.pos.x <= (current_node.top_left.x + current_node.bot_right.x) / 2:
            # topLeftTree
            if node.pos.y <= (current_node.top_left.y + current_node.bot_right.y) / 2:
                if current_node.top_left_tree is None:
                    current_node.top_left_tree = QuadtreeNode(
                        current_node.top_left,
                        Point2D((current_node.top_left.x + current_node.bot_right.x) / 2,
                                (current_node.top_left.y + current_node.bot_right.y) / 2)
                    )
                self.insert(node, current_node.top_left_tree)

            # bottomLeftTree
            else:
                if current_node.bot_left_tree is None:
                    current_node.bot_left_tree = QuadtreeNode(
                        Point2D(current_node.top_left.x,
                                (current_node.top_left.y + current_node.bot_right.y) / 2),
                        Point2D((current_node.top_left.x + current_node.bot_right.x) / 2,
                                current_node.bot_right.y)
                    )
                self.insert(node, current_node.bot_left_tree)
        else:
            # topRightTree
            if node.pos.y <= (current_node.top_left.y + current_node.bot_right.y) / 2:
                if current_node.top_right_tree is None:
                    current_node.top_right_tree = QuadtreeNode(
                        Point2D((current_node.top_left.x + current_node.bot_right.x) / 2, current_node.top_left.y),
                        Point2D(current_node.bot_right.x,
                                (current_node.top_left.y + current_node.bot_right.y) / 2)
                    )
                self.insert(node, current_node.top_right_tree)

            # bottomRightTree
            else:
                if current_node.bot_right_tree is None:
                    current_node.bot_right_tree = QuadtreeNode(
                        Point2D((current_node.top_left.x + current_node.bot_right.x) / 2,
                                (current_node.top_left.y + current_node.bot_right.y) / 2),
                        current_node.bot_right
                    )
                self.insert(node, current_node.bot_right_tree)

    def search(self, point, current_node=None):
        if current_node is None:
            current_node = self.root

        if not self.in_boundary(point, current_node.top_left, current_node.bot_right):
            return None

        if current_node.is_leaf and current_node.data is not None:
            return current_node.data

        if point.x <= (current_node.top_left.x + current_node.bot_right.x) / 2:
            # topLeftTree
            if point.y <= (current_node.top_left.y + current_node.bot_right.y) / 2:
                if current_node.top_left_tree is None:
                    return None
                return self.search(point, current_node.top_left_tree)

            # bototmLeftTree
            else:
                if current_node.bot_left_tree is None:
                    return None
                return self.search(point, current_node.bot_left_tree)
        else:
            # topRightTree
            if point.y <= (current_node.top_left.y + current_node.bot_right.y) / 2:
                if current_node.top_right_tree is None:
                    return None
                return self.search(point, current_node.top_right_tree)

            # bottomRightTree
            else:
                if current_node.bot_right_tree is None:
                    return None
                return self.search(point, current_node.bot_right_tree)

    def in_boundary(self, point, top_left, bot_right):
        return top_left.x <= point.x <= bot_right.x and top_left.y <= point.y <= bot_right.y

    def visualize(self, current_node=None):
        if current_node is None:
            current_node = self.root

        if current_node.is_leaf and current_node.data is not None:
            plt.plot(current_node.data.pos.x, current_node.data.pos.y, 'bo')
            plt.text(current_node.data.pos.x, current_node.data.pos.y, str(current_node.data.data))
            return

        self.visualize_subtree(current_node.top_left_tree)
        self.visualize_subtree(current_node.top_right_tree)
        self.visualize_subtree(current_node.bot_left_tree)
        self.visualize_subtree(current_node.bot_right_tree)

    def visualize_subtree(self, current_node):
        if current_node is None:
            return

        plt.plot([current_node.top_left.x, current_node.bot_right.x, current_node.bot_right.x,
                  current_node.top_left.x, current_node.top_left.x],
                 [current_node.top_left.y, current_node.top_left.y, current_node.bot_right.y,
                  current_node.bot_right.y, current_node.top_left.y], 'k-')

        if current_node.is_leaf and current_node.data is not None:
            plt.plot(current_node.data.pos.x, current_node.data.pos.y, 'bo')
            plt.text(current_node.data.pos.x, current_node.data.pos.y, str(current_node.data.data))
        else:
            self.visualize_subtree(current_node.top_left_tree)
            self.visualize_subtree(current_node.top_right_tree)
            self.visualize_subtree(current_node.bot_left_tree)
            self.visualize_subtree(current_node.bot_right_tree)

# Exemplo de uso
quadtree = Quadtree(Point2D(0, 0), Point2D(8, 8))
points = [Reg_Node(Point2D(1, 1), 11),
          Reg_Node(Point2D(2, 5), 22),
          Reg_Node(Point2D(7, 6), 33),
          Reg_Node(Point2D(5, 5), 44),
          Reg_Node(Point2D(7, 5), 55)]

for point in points:
    quadtree.insert(point)

# Visualizar a árvore
quadtree.visualize()
plt.show()
