import pyfingerprint.find_port
import sys
import glob
import time
from pyfingerprint.pyfingerprint import PyFingerprint as p
from interruptingcow import timeout

class fingerprint():

    
########################################################################################################################

    def __init__(self):
        
        try:
            self.f = p('/dev/tty.SLAB_USBtoUART', 57600, 0xFFFFFFFF, 0x00000000)

            if ( self.f.verifyPassword() == False ):
                raise ValueError('The given fingerprint sensor password is wrong!')

        except Exception as e:
            print('The fingerprint sensor could not be initialized!')
            print('Exception message: ' + str(e))
            exit(1)

        print('Currently used templates: ' + str(self.f.getTemplateCount()) +'/'+ str(self.f.getStorageCapacity()))

        return

########################################################################################################################

    def get_finger_template_first(self):
        
        try:
            print('Waiting for finger...')

            ## Wait that finger is read
            while ( self.f.readImage() == False ):
                pass

            ## Converts read image to characteristics and stores it in charbuffer 1
            self.f.convertImage(0x01)

        except Exception as e:
            print('Operation failed!')
            print('Exception message: ' + str(e))
            return -1

########################################################################################################################

    def get_finger_template_final(self):

        try:
            print('Waiting for finger...')

            ## Wait that finger is read
            while ( self.f.readImage() == False ):
                pass

            ## Converts read image to characteristics and stores it in charbuffer 1
            self.f.convertImage(0x02)

            ## Compares the charbuffers
            if ( self.f.compareCharacteristics() == 0 ):
                return 0

            self.f.createTemplate()

            t=self.f.downloadCharacteristics(0x01)
            self.f.clearDatabase()
            print('Finger returned successfully!')
            return t

        except Exception as e:
                    print('Operation failed!')
                    print('Exception message: ' + str(e))
                    return -1

########################################################################################################################

    def student_finger_test(self, fingerprint_template = []):

        try:

            self.f.uploadCharacteristics(0x01, fingerprint_template)
            print('Waiting for finger...')

            ## Wait that finger is read
            while ( self.f.readImage() == False ):
                pass

            ## Converts read image to characteristics and stores it in charbuffer 2
            self.f.convertImage(0x02)

            ## Compares the charbuffers
            if ( self.f.compareCharacteristics() == 0 ):
                return 0
            else:
                return 1

        except Exception as e:
                    print('Operation failed!')
                    print('Exception message: ' + str(e))
                    return -1

    def template_add(self, fingerprint_template = []):

        try:
            ## Gets some sensor information
            print('Currently used templates: ' + str(self.f.getTemplateCount()) +'/'+ str(self.f.getStorageCapacity()))

            # self.f.clearDatabase()
            for finger in fingerprint_template:
                self.f.uploadCharacteristics(0x01,finger)
                self.f.uploadCharacteristics(0x02,finger)
                self.f.createTemplate()
                positionNumber = self.f.storeTemplate()
                print positionNumber
            ## Gets some sensor information
            print('Currently used templates: ' + str(self.f.getTemplateCount()) +'/'+ str(self.f.getStorageCapacity()))
            return "okay"
        except Exception as e:
                    print('Operation failed!')
                    print('Exception message: ' + str(e))
                    return -1
    
    def admin_scan(self):

        try:
            print('Waiting for finger...')

            while True:
                try:
                    with timeout(5, exception=RuntimeError):
                        # perform a potentially very slow operation
                        while ( self.f.readImage() == False):
                            # break
                            pass
                        break   
                except RuntimeError:
                    pass
                    return "no one"
                    break

            ## Converts read image to characteristics and stores it in charbuffer 1
            self.f.convertImage(0x01)

            ## Searchs template
            result = self.f.searchTemplate()

            positionNumber = result[0]
            accuracyScore = result[1]

            if ( positionNumber == -1 ):
                print('No match found!')
                return -1
            else:
                print('Found template at position #' + str(positionNumber))
                print('The accuracy score is: ' + str(accuracyScore))
                return positionNumber
        except Exception as e:
                    print('Operation failed!')
                    print('Exception message: ' + str(e))
                    return -1