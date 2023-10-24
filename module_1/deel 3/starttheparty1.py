gastheer = True
gasten = True
drank = True
chips = True

if not chips or (chips and not drank) or (chips and not gasten and not drank) or (not gasten and not gastheer) or (gastheer and not (chips or gasten)):
    print('geen feest')
else:
    print('begin het feestje')
