# ASAv Bootstrap

## Getting Started

``` bash
pip install -r requirements.txt
```

Modify the './templates/asa.jinja2' file to match the configuration you like'


## How to use once configured

``` bash
python3 configurator.py -a 10.0.0.1 -m 255.255.255.0 -g 10.0.0.254 -n test-firewall -v 9.7.1 -f test-firewall.iso -s 8.8.8.8 -t 1G
```

- "-a" or "--address" is for the outside IP address of GigabitEthernet0/0
- "-m" or "--mask" is for the subnet mask for GigabitEthernet0/0
- "-g" or "--gateway" is the gateway for the outside interface
- "-n" or "--name" is the hostname of the firewall
- "-v" or "--version" is the version of the ASAv
- "-s" or "--ssh" is the IP you want the whitelist for SSH to the outside
- "-t" or "--throughput" is the throughput level you want to license (100M or 1G)
- "-i" or "--idtoken" is the idtoken you want to register it to, OPTIONAL
- "-f" or "--filename" is the filename you want to output to ex: "test-firewall.iso"

## Next Steps
- [x] jinja templating to generate the configuration
- [x] folder structure created to be placed in the iso
- [ ] testing the iso on a lab ASAv
