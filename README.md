# Connection Master
A command line remote server connection and management tool

# Installation
`$ git clone https://github.com/nathansmerrill/connectionmaster ~/connectionmaster`  
`$ echo alias cm='python3 ~/connectionmaster/connectionmaster.py' > ~/.bashrc`  
Set `CONFIG_FILE` in `connectionmaster.py` to your config file location. The default is `/home/nathan/.cmrc.yaml`

# Config file
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
# Usage
There are long and one letter forms for every command
```
$ cm connect myServer
$ cm c myServer
$ cm execute mySecondServer "echo hi > test.txt"
$ cm x mySecondServer "echo hi > test.txt"
$ cm ping myThirdServer
$ cm p myThirdServer
$ cm edit
$ cm e
```

# All config values
### `command`
The command to run   
Defaults to `ssh`
### `user`
The user to log in as  
Defaults to the current user  
### `ip`
The IP to connect to          
Defaults to `localhost`  
### `port`
The port to connect to          
Defaults to `22`  
### `key`
The ssh key to use      
Defaults to no key  
### `jump`
A server to jump ssh through
Defaults to nothing  
### `justRunCommand`
Just runs `command` specified without adding the ip, port, etc  
Default to `False`