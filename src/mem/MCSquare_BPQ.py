from m5.params import *
from m5.SimObject import SimObject

class MCSquare_BPQ(SimObject):
    type = 'MCSquare_BPQ'
    cxx_header = "mem/mcsquare.h"
    cxx_class = "gem5::memory::MCSquare_BPQ"

    bpq_size = Param.Int(4, "Number of entries that bounce table can hold")
    bpq_penalty = Param.Latency("555ps", "Cycle penalty for bounce table access")