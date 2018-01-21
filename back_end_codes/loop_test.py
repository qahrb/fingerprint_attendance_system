import time
from pyfingerprint.pyfingerprint import PyFingerprint as p
from interruptingcow import timeout


try:
    f = p('/dev/tty.SLAB_USBtoUART', 57600, 0xFFFFFFFF, 0x00000000)

    if ( f.verifyPassword() == False ):
        raise ValueError('The given fingerprint sensor password is wrong!')
except Exception as e:

    print('The fingerprint sensor could not be initialized!')
    print('Exception message: ' + str(e))
    exit(1)
while True:
    try:
        with timeout(0.5, exception=RuntimeError):
            # perform a potentially very slow operation
            while ( f.readImage() == False):
                # break
                pass
            break   
    except RuntimeError:
        print "didn't finish within 5 seconds"

