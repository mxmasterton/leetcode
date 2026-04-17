class TreeNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

class TreeMap:
    def __init__(self):
        self.root = None

    def insert(self, key: int, value: int) -> None:
        new_node = TreeNode(key, value)

        if not self.root:
            self.root = new_node
        else:
            current = self.root
            while True:
                if key < current.key:
                    if not current.left:
                        current.left = new_node
                        break
                    current = current.left
                elif key > current.key:
                    if not current.right:
                        current.right = new_node
                        break
                    current = current.right
                else:
                    current.value = value
                    break

    def get(self, key: int) -> int:
        current = self.root
        while current:
            if key < current.key:
                current = current.left
            elif key > current.key:
                current = current.right
            else:
                return current.value
        return -1

    def getMin(self) -> int:
        if not self.root:
            return -1

        current = self.root
        while current.left:
            current = current.left
        return current.value
        
    def getMax(self) -> int:
        if not self.root:
            return -1

        current = self.root
        while current.right:
            current = current.right
        return current.value

    def remove(self, key: int) -> None:
        self.root = self.removeHelper(self.root, key)

    def removeHelper(self, current: TreeNode, key: int) -> TreeNode:
        if not current:
            return None

        if key > current.key:
            current.right = self.removeHelper(current.right, key)
        elif key  < current.key:
            current.left = self.removeHelper(current.left, key)
        else:
            if not current.left:
                return current.right
            elif not current.right:
                return current.left
            else:
                successor = current.right
                while successor.left:
                    successor = successor.left

                current.key = successor.key
                current.value = successor.value
                current.right = self.removeHelper(current.right, successor.key)

        return current

    def getInorderKeys(self) -> List[int]:
        out = []

        def dfs(current):
            if current:
                dfs(current.left)
                out.append(current.key)
                dfs(current.right)
        
        dfs(self.root)
        return out

