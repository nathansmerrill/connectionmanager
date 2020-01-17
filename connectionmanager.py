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

if args['operands'][0] == 'edit':
    os.system('nvim ' + CONFIG_FILE)

elif args['operands'][0] == 'connect':
    serverConfig = config[args['operands'][1]]
    for option in defaultConfig:
        if option not in serverConfig:
            serverConfig[option] = defaultConfig[option]
    os.system(serverConfig['command'] + ' ' + serverConfig['user'] + '@' + serverConfig['ip'] + ' -p ' + serverConfig['port'])