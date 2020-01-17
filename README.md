# Connection Manager
A command line remote server connection and management tool

## Installation
`$ git clone https://github.com/nathansmerrill/connectionmanager ~/connectionmanager`  
`$ echo alias cm='python3 ~/connectionmanager/connectionmanager.py' > ~/.bashrc`

## Usage
```
$ cm connect myServer
$ cm ping myServer2
$ cm edit
```

## Config file
```yaml
myServer:
    ip: 'xxx.xxx.xxx.xxx'
    user: 'myUser'

mySecondServer:
    ip: 'yyy.yyy.yyy.yyy'
    port: '2000'
```
## All config values
`command`   - defaults to `ssh`
`user`      - defaults to the current user
`ip`        - defaults to `localhost`
`port`      - defaults to `22`
`key`       - defaults to no key