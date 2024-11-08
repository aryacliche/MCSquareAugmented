from m5.params import *
from m5.SimObject import SimObject

class MCSquare_CTT(SimObject):
    type = 'MCSquare'
    cxx_header = "mem/mcsquare.h"
    cxx_class = "gem5::memory::MCSquare_CTT"

    ctt_size = Param.Int(4096, "Number of entries that copy tracking table can hold")
    ctt_penalty = Param.Latency("979ps", "Cycle penalty for reading a data copy that was elided")
    ctt_free = Param.Float(0.75, "Fraction of CTT to fill before we start freeing entries")
    ctt_freeing_max = Param.Int(1, "Number of CTT entries to free in parallel")
    
    wb_dest_reads = Param.Int(3, "Whether to writeback reads to destination; 0 = no, 1 = yes, 2 = adaptive")