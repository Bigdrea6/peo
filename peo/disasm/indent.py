def organize(msgs):
    max_size = max([len(msgs[i][1]) for i in range(len(msgs)) if len(msgs[i]) >= 2])
    
    for i in range(len(msgs)):
        if len(msgs[i]) >= 2:
            l = max_size - len(msgs[i][1])
            msgs[i][1] = msgs[i][1] + " " * l
        
        elif len(msgs[i]) == 1:
            if "<" in msgs[i][0]:
                msg = msgs[i][0].split(" ")
                msgs[i][0] = msg[1]

    return msgs

def indent(arrows, msgs):
    max_size = max(len(arrow) for arrow in arrows)

    for i in range(len(msgs)):
        if len(msgs[i]) == 1:
            l = max_size - len(arrows[i]) -2
        else:
            l = max_size - len(arrows[i])
        msgs[i][0] = " " * l + arrows[i] + " " + msgs[i][0]
    
    return msgs