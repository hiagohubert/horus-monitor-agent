class CPU(object):
    architecture = ""
    vendor_id = ""
    model_name = ""
    cpu_cores = 0
    percent_used = 0.0

    def __init__(self, architecture, vendor_id, model_name, cpu_cores, percent_used):
        self.architecture = architecture
        self.vendor_id = vendor_id
        self.model_name = model_name
        self.cpu_cores = cpu_cores
        self.percent_used = percent_used

