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
- create server engine (handle requests)
- Parse user input and call CLI tool directly


- make -h the default for the cli tool
- server should run on host or node when setup

- Create web UI
- implement a database 
- create login for server
- sanitize api input
- set up proxy