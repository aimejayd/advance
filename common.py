from collections import defaultdict


class UnionFind:
    def __init__(self, elements=None):
        """Create a new empty union-find structure.
        If *elements* is an iterable, this structure will be initialized
        with the discrete partition on the given set of elements.
        """
        if elements is None:
            elements = ()
        self.parents = {}
        self.weights = {}
        for x in elements:
            self.weights[x] = 1
            self.parents[x] = x

    def __getitem__(self, object):
        """Find and return the name of the set containing the object."""

        # check for previously unknown object
        if object not in self.parents:
            self.parents[object] = object
            self.weights[object] = 1
            return object

        # find path of objects leading to the root
        path = [object]
        root = self.parents[object]
        while root != path[-1]:
            path.append(root)
            root = self.parents[root]

        # compress the path and return
        for ancestor in path:
            self.parents[ancestor] = root
        return root

    def __iter__(self):
        """Iterate through all items ever found or unioned by this structure.
        """
        return iter(self.parents)

    def to_sets(self):
        """Iterates over the sets stored in this structure.
        For example::
            >>> partition = UnionFind('xyz')
            >>> sorted(map(sorted, partition.to_sets()))
            [['x'], ['y'], ['z']]
            >>> partition.union('x', 'y')
            >>> sorted(map(sorted, partition.to_sets()))
            [['x', 'y'], ['z']]
        """
        # TODO In Python 3.3+, this should be `yield from ...`.
        for block in groups(self.parents).values():
            yield block

    def union(self, *objects):
        """Find the sets containing the objects and merge them all."""
        roots = [self[x] for x in objects]
        # Find the heaviest root according to its weight.
        heaviest = max(roots, key=lambda r: self.weights[r])
        for r in roots:
            if r != heaviest:
                self.weights[heaviest] += self.weights[r]
                self.parents[r] = heaviest


def groups(many_to_one):
    one_to_many = defaultdict(set)
    for v, k in many_to_one.items():
        one_to_many[k].add(v)
    return dict(one_to_many)
