import subprocess
# --connection-per-second=8 This allows for up to 8 connections per second.
# --sockets=8 Opens up to 8 sockets.
# -s0 Tells HTTrack to disobey robots.txt
# -i or --ignore-case 
# -s or --squeeze-blank-lines Squeeze multiple blank lines.
# -m or --long-prompt Set prompt style.
# -F Sets user agent.

#You can play with connection-per-second and sockets 
#Options
args = "--connection-per-second=8 --sockets=8 --keep-alive --display --verbose --advanced-progressinfo --disable-security-limits -n -i -s0 -m -F 'Mozilla/5.0 (X11;U; Linux i686; en-GB; rv:1.9.1) Gecko/20090624 Ubuntu/9.04 (jaunty) Firefox/3.5' -A100000000 -#L500000000"

#Ask target
print('Enter target:')
t = input()

#Run httrack
subprocess.call(["httrack", t, args, "\websites"])




 

