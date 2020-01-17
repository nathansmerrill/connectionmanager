# Author: Nathan Merrill
import cliparse, yaml, os, getpass

CONFIG_FILE = '/home/nathan/.cmrc.yaml'

with open(CONFIG_FILE, 'r') as stream:
    config = yaml.safe_load(stream)

parser = cliparse.Parser()
parser.setRequiredOperands(1)
parser.setOperandConstraints({
    0: [
        'connect',
        'scp',
        'ping',
        'edit'
    ]
})
args = parser.parseArgs()

defaultConfig = {
    'command': 'ssh',
    'user': getpass.getuser(),
    'ip': 'localhost',
    'port': '22',
    'key': 'id_rsa'
}

if len(args['operands']) > 1:
    serverConfig = config[args['operands'][1]]

if args['operands'][0] == 'connect':
    for option in defaultConfig:
        if option not in serverConfig:
            serverConfig[option] = defaultConfig[option]
    os.system(serverConfig['command'] + ' ' + serverConfig['user'] + '@' + serverConfig['ip'] + ' -p ' + serverConfig['port'] + ' -i ' + '/home/nathan/.ssh/' + serverConfig['key'])

elif args['operands'][0] == 'ping':
    os.system('ping -c 1 ' + serverConfig['ip'])

elif args['operands'][0] == 'edit':
    os.system('nvim ' + CONFIG_FILE)
