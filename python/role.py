class Role(object):
    """docstring for Role."""

    def pouvoir(self):
        raise NotImplementedError("You must implement foo's %s method" % type(self).__name__)
    def devoileRole(self):
        raise NotImplementedError("You must implement foo's %s method" % type(self).__name__)
