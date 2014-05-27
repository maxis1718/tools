import sys
from subprocess import call
rpm = 4000 if len(sys.argv) == 1 and int(sys.argv[1]) < 2000 else int(sys.argv[1])
call(['/Applications/smcFanControl.app/Contents/Resources/smc', '-k', 'F0Mx', '-w', str(hex(rpm << 2)[2:])])
