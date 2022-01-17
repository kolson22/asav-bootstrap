try:
    import argparse
    import pycdlib
except ImportError:
    print("you need to make sure pycdlib and argparse are installed")

parser = argparse.ArgumentParser()
parser.add_argument("echo", help="The thing you want to echo, dummy")
parser.add_argument("-v", "--verbose",
                    help="The thing you want to echo, dummy",
                    action="store_true")
parser.add_argument("-a", "--address",
                    help="The IP address of the firewall")
args = parser.parse_args()
if args.verbose:
    print("super verbose mode activated")

f = open('test.txt', 'w')
f.write(args.echo)
f.close()

iso = pycdlib.PyCdlib()
iso.new(joliet=3)
foostr = b'foo\n'
iso.add_file('test.txt', joliet_path="/test.txt")
iso.write("test.iso")
iso.close()
