import sys
import appengine.appengine as ae
def main(arg, argv):
    return ae.go()

if __name__=="__main__":
    sys.exit(main(len(sys.argv), sys.argv))