# Open Deploy
The open source datacenter in a box you can use to deploy your own applications and build your own homelab.

## Architecture
### Server
Hosts a Web UI for accessing and administrating your local fog.

### Deploy:
Deploys virtual machines using configured host hypervisor (QEMU)

### Proxy:
Sets up forward or reverse proxying for client access

## Pre-requisites:
- qemu
- python3

## Usage:
### Start Server:
None yet


## To Do:
### Active:
- Create base dashboard page
- Create form for running api calls

### Init:
- Create installation script that sets up config and vm root
- create application home directory structure
- Create uninstall script

### CLI:
- make -h the default for the cli tool
- server should run on host or node when setup

### Server Engine:
- Delete a guest
- Thread the subprocess for booting and return if it simply runs or not. we dont need output yet
- implement a database 
- Log the requests and output into a file

### Server App:
- create login for server
- make pages look pretty
- sanitize api input

### Proxy:
- set up proxy

### Scalability:
Ensure we can IAC deployments in a devopsy method