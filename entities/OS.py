class OS(object):

    distributor_id = ""
    release = ""
    codename = ""
    description = ""

    def __init__(self, distributor_id, release, codename, description):
        self.distributor_id = distributor_id
        self.release = release
        self.codename = codename
        self.description = description


