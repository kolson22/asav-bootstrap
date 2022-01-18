try:
    import argparse
    import pycdlib
except ImportError:
    print("you need to make sure pycdlib and argparse are installed")

import os
parser = argparse.ArgumentParser()
parser.add_argument("-a", "--address",
                    help="The IP address of the firewall",
                    required=True)
parser.add_argument("-m", "--mask",
                    help="The subnet mask, ex: 255.255.255.0",
                    required=True)
parser.add_argument("-f", "--filename",
                    help="The filename to output the iso to, ex: firewall.iso",
                    required=True)
args = parser.parse_args()

f = open("test.txt", "w")
f.write(args.address + "/" + args.mask)
f.write("\n")
f.close()

iso = pycdlib.PyCdlib()
iso.new(joliet=3)
iso.add_file("test.txt", joliet_path="/test.txt")
iso.write(args.filename)
iso.close()

os.remove("./test.txt")
