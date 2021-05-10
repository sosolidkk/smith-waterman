class MatrixCell:
    def __init__(self, key, value, parents=None):
        self.key = key
        self.value = value
        self.parents = parents

    def __repr__(self):
        return f"k:{self.key} v:{self.value} p:{self.parent}"

    def __str__(self):
        return f"k:{self.key} v:{self.value} p:{self.parent}"
