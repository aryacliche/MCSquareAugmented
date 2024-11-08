from m5.params import *
from m5.SimObject import SimObject

class MCSquare_CTT(SimObject, should_have_CTT):
    type = 'MCSquare_CTT'
    cxx_header = "mem/mcsquare.h"
    cxx_class = "gem5::memory::MCSquare_CTT"

    ctt_size = Param.Int(4096 if should_have_CTT else 0, "Number of entries that copy tracking table can hold")
    ctt_penalty = Param.Latency("979ps" if should_have_CTT else 0, "Cycle penalty for reading a data copy that was elided")
    ctt_free = Param.Float(0.75 if should_have_CTT else 0, "Fraction of CTT to fill before we start freeing entries")
    ctt_freeing_max = Param.Int(1 if should_have_CTT else 0, "Number of CTT entries to free in parallel")

    wb_dest_reads = Param.Int(3 if should_have_CTT else 0, "Whether to writeback reads to destination; 0 = no, 1 = yes, 2 = adaptive")
