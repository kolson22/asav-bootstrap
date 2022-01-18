#!/usr/bin/env python3

try:
    import argparse
    import pycdlib
    import os
    from jinja2 import Template
except ImportError:
    print("you need to make sure pycdlib and argparse are installed")

# get the arguments from the cli
parser = argparse.ArgumentParser()
parser.add_argument("-a", "--address",
                    help="The IP address of the outside of the firewall",
                    required=True)
parser.add_argument("-m", "--mask",
                    help="The subnet mask, ex: 255.255.255.0",
                    required=True)
parser.add_argument("-g", "--gateway",
                    help="The default gateway of the outside",
                    required=True)
parser.add_argument("-n", "--name",
                    help="The hostname of the firewall",
                    required=True)
parser.add_argument("-v", "--version",
                    help="The version of the ASA",
                    required=True)
parser.add_argument("-s", "--ssh",
                    help="The IP you will need whitelisted for SSH",
                    required=True)
parser.add_argument("-t", "--throughput",
                    help="The throughput of ASAv, ex: 1G or 100M",
                    required=True)
parser.add_argument("-i", "--idtoken",
                    help="The id token for smart licensing: OPTIONAL")
parser.add_argument("-f", "--filename",
                    help="The filename to output the iso to, ex: firewall.iso",
                    required=True)
args = parser.parse_args()

# open the template file to build the configuration
with open('./templates/asa.jinja2') as template_file:
    template = Template(template_file.read())

# make a rendered configuration with the args as variables
config_output = template.render(
    address=args.address,
    mask=args.mask,
    gateway=args.gateway,
    hostname=args.name,
    version=args.version,
    ssh_allow=args.ssh,
    model=args.throughput
)

# write the rendered configuration to the day0 config file
config_file = open("day0-config", "w")
config_file.write(config_output)
config_file.close()

# if idtoken is present write it to a file
if args.idtoken:
    token_file = open("idtoken", "w")
    token_file.write(args.idtoken)
    token_file.close()

# create the iso object and place the files in there
iso = pycdlib.PyCdlib()
iso.new(joliet=3, vol_ident=args.name.upper())
iso.add_file("day0-config", joliet_path="/day0-config")
if args.idtoken:
    iso.add_file("idtoken", joliet_path="/idtoken")
iso.write(args.filename)
iso.close()

# clean up the config and token file
os.remove("day0-config")
if args.idtoken:
    os.remove("idtoken")
print("Successfully created the boostrap iso: ./" + args.filename)
