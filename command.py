class CommandSet(object):

    def __init__(self,
                 kreport_file,
                 domain,
                 output_path,
                 excluded_nodes,
                 min_reads_viruses,
                 min_reads_bacteria,
                 min_reads_archaea,
                 min_reads_eukarya,
                 min_level,
                 keep_sublevels):

        self.kreport_file = kreport_file
        self.domain = domain
        self.output_path = output_path
        self.excluded_nodes = excluded_nodes
        self.min_reads_viruses = min_reads_viruses
        self.min_reads_bacteria = min_reads_bacteria
        self.min_reads_archaea = min_reads_archaea
        self.min_reads_eukarya = min_reads_eukarya
        self.min_level = min_level
        self.keep_sublevels = keep_sublevels
