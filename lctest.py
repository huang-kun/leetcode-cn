# Copy test code from leetcode playground
# https://leetcode-cn.com/playground/new/empty/

# --------------------------------------------
#   TreeNode
# --------------------------------------------

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def stringToTreeNode(input):
    input = input.strip()
    input = input[1:-1]
    if not input:
        return None

    inputValues = [s.strip() for s in input.split(',')]
    root = TreeNode(int(inputValues[0]))
    nodeQueue = [root]
    front = 0
    index = 1
    while index < len(inputValues):
        node = nodeQueue[front]
        front = front + 1

        item = inputValues[index]
        index = index + 1
        if item != "null":
            leftNumber = int(item)
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(inputValues):
            break

        item = inputValues[index]
        index = index + 1
        if item != "null":
            rightNumber = int(item)
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)
    return root

def treeNodeToString(root):
    if not root:
        return "[]"
    output = ""
    queue = [root]
    current = 0
    while current != len(queue):
        node = queue[current]
        current = current + 1

        if not node:
            output += "null, "
            continue

        output += str(node.val) + ", "
        queue.append(node.left)
        queue.append(node.right)
    return "[" + output[:-2] + "]"

def treeNodeToCompactString(root):
    if root is None:
        return "[]"

    array = []
    queue = [root]
    current = 0

    while current != len(queue):
        node = queue[current]
        current += 1

        if node is None:
            array.append("null")
            continue

        array.append(str(node.val))

        queue.append(node.left)
        queue.append(node.right)

    nulls = 0
    for val in reversed(array):
        if val == "null":
            nulls += 1
        else:
            break
    
    if nulls > 0:
        array = array[:-1*nulls]

    return "[" + ",".join(array) + "]"


class TreeNodeHelper:

    # node1和node2互换位置，思路：首先生成一个新节点temp1替换掉node1的位置
    # 再生成一个新节点temp2替换掉node2的位置，此时node1和node2
    def swap(self, node1, node2):
        node1, temp1 = self.replace(node1)
        node2, temp2 = self.replace(node2)
        self.replace(temp1, node2)
        self.replace(temp2, node1)

    # 将root节点替换为node，如果node为空，就创建一个新节点代替。
    # 这里的替换是指把root与父节点和子节点的关系，都转移给node。
    # 所以还需要一个字典来预先保存好root与父节点的关系。
    def replace(self, root, node=None):
        if node is None:
            node = TreeNode(root.val)

        # assert node.left is None
        # assert node.right is None
        # assert node not in self.cache
        
        # 转移子节点
        node.left = root.left
        node.right = root.right
        
        # 转移父节点
        if root in self.cache:
            super_root, relationship = self.cache[root]
            if relationship == 1:
                super_root.left = node
            elif relationship == 2:
                super_root.right == node
            else:
                pass # assert False
            
            # 更新字典中的父子关系
            del self.cache[root]
            self.cache[node] = (super_root, relationship)
        
        # 更新字典中的孩子关系
        if root.left:
            self.cache[root.left] = (node, 1)
        if root.right:
            self.cache[root.right] = (node, 2)
        
        # 把交换后的root与原树脱离关系
        root.left = None
        root.right = None
        
        # 返回交换后的两个节点
        return root, node