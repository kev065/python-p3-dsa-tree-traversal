class Tree:
    def __init__(self, root):
        self.root = root

    def get_element_by_id(self, id):
        return self._get_element_by_id(self.root, id)

    def _get_element_by_id(self, node, id):
        if node['id'] == id:
            return node
        for child in node['children']:
            result = self._get_element_by_id(child, id)
            if result is not None:
                return result
        return None
