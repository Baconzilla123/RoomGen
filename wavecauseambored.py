wave = True
incr = 1
add = 1
incrs = 0
oldincrs = 0
wavegen = ""
mainincr = 0
while wave:
    oldincr = incr
    while incr > 0:
        wavegen = (wavegen + "#")
        incr = (incr - 1)
    incr = (oldincr + add)
    incrs = (incrs + 1)
    
    if incrs == (oldincrs + 10):
        oldincrs = incrs
        add = add + 1
    mainincr = mainincr + 1
    if mainincr == 100:
        wave = False
    print(wavegen)
    wavegen = ""
