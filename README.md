# Connection Manager
A command line remote server connection and management tool

## Installation
`$ git clone https://github.com/nathansmerrill/connectionmanager ~/connectionmanager`  
`$ echo alias cm='python3 ~/connectionmanager/connectionmanager.py' > ~/.bashrc`  
Set `CONFIG_FILE` in `connectionmanager.py` to your config file location

## Config file
```yaml
myServer:
    ip: 'xxx.xxx.xxx.xxx'
    user: 'myUser'

# The jump option takes the server to jump ssh through
mySecondServer:
    ip: 'yyy.yyy.yyy.yyy'
    port: '2000'
    key: 'mySecondServerKey'
    jump: 'myServer'

# The ip isn't needed when you specify a full command but is needed to ping the server
myThirdServer:
    ip: 'zzz.zzz.zzz.zzz'
    command: 'vncviewer zzz.zzz.zzz.zzz:0'
    justRunCommand: True

```
## Usage
```
$ cm connect myServer
$ cm ping mySecondServer
$ cm edit
```

## All config values
`command`       - defaults to `ssh`  
`user`          - defaults to the current user  
`ip`            - defaults to `localhost`  
`port`          - defaults to `22`  
`key`           - defaults to no key  
`justRunCommand`- default to False