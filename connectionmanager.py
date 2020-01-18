# Author: Nathan Merrill
import cliparse, yaml, os, getpass, sys

CONFIG_FILE = '/home/nathan/.cmrc.yaml'

with open(CONFIG_FILE, 'r') as stream:
    config = yaml.safe_load(stream)

parser = cliparse.Parser()
parser.setRequiredOperands(1)
parser.setOperandConstraints({
    0: [
        'connect',
        'c',
        'scp',
        's',
        'ping',
        'p',
        'edit',
        'e'
    ]
})
args = parser.parseArgs()

defaultConfig = {
    'command': 'ssh',
    'user': getpass.getuser(),
    'ip': 'localhost',
    'port': '22',
    'key': None,
    'justRunCommand': False
}

if (args['operands'][0] == 'edit') or (args['operands'][0] == 'e'):
    os.system('nvim ' + CONFIG_FILE)
    sys.exit()

serverConfig = config[args['operands'][1]]
for option in defaultConfig:
    if option not in serverConfig:
        serverConfig[option] = defaultConfig[option]

if (args['operands'][0] == 'ping') or (args['operands'][0] == 'p'):
    os.system('ping -c 1 ' + serverConfig['ip'])
    sys.exit()

keyPart = ''
if serverConfig['key'] is not None:
    keyPart = ' -i ' + '/home/nathan/.ssh/' + serverConfig['key'] + ' '
userIpPort = serverConfig['user'] + '@' + serverConfig['ip'] + ':' + serverConfig['port']

if (args['operands'][0] == 'connect') or (args['operands'][0] == 'c'):
    os.system(serverConfig['command'] + keyPart + ' ssh://' + userIpPort)
    sys.exit()

if (args['operands'][0] == 'scp') or (args['operands'][0] == 's'):
    if serverConfig['justRunCommand']:
        os.system(serverConfig['command'])
    else:
        os.system('scp' + keyPart + args['operands'][2] + ' scp://' + userIpPort + '/' + args['operands'][3])
    sys.exit()
