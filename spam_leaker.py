#!/usr/bin/env python
import os, time

log_fn = "mem."+str(os.getpid())+".log"

log = open( log_fn, "w" )

iter_per_log = 100

while 1:
    log.write( "-----------\n" )
    log.write( time.strftime("%c") + "\n" )
    log.write( "-- /proc/meminfo --\n" )
    mem_data = open( "/proc/meminfo" ).read()
    log.write( mem_data )
    log.write( "-- running cublas_leaker %s times --\n" % (iter_per_log,) )
    log.flush()
    for i in range(iter_per_log):
        os.system( "./cublas_leaker" )
    
