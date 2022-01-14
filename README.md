# easyInfra
 
Easy infrastructure setup for VooDoo Listening Post (LP)...


# Requirements

Tested with:
- DigitalOcean Droplets
- Ubuntu 20.04 LTS
- Datacenter Name: SFO3
- $5/mo


# Usage

Steps:
- mkdir -p /opt/voodoo
- cd /opt/voodoo
- git clone TODO easyInfra TODO
- cd /opt/voodoo/easyInfra
- upload over SSH/SFTP voodoo.zip & voodoo.lic
- cp /root/voodoo.zip /opt/voodoo/easyInfra/
- cp /root/voodoo.lic /opt/voodoo/easyInfra/
- python3 easyInfra.py
- Script does the following:
- Checks to see if docker is install, if not installs docker
- Checks to see if other dependencies are present, if not installs dependencies, e.g. unzip
- 

# References

The following resources were useful references as part of this project
- test
- test

Join Slack for More Info: ... TODO ...


