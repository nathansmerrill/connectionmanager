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

command = args['operands'][0]

defaultConfig = {
    'command': 'ssh',
    'user': getpass.getuser(),
    'ip': 'localhost',
    'port': '22',
    'key': None,
    'justRunCommand': False
}

if (command == 'edit') or (command == 'e'):
    os.system('nvim ' + CONFIG_FILE)

try:
    serverName = args['operands'][1]
except IndexError:
    raise ValueError('The ' + command + ' command needs takes the server to use')

serverConfig = config[serverName]
for option in defaultConfig:
    if option not in serverConfig:
        serverConfig[option] = defaultConfig[option]


if (command == 'ping') or (command == 'p'):
    os.system('ping -c 1 ' + serverConfig['ip'])

keyPart = ''
if serverConfig['key'] is not None:
    keyPart = ' -i ' + '/home/nathan/.ssh/' + serverConfig['key'] + ' '
userIpPort = serverConfig['user'] + '@' + serverConfig['ip'] + ':' + serverConfig['port']

if (command == 'connect') or (command == 'c'):
    os.system(serverConfig['command'] + keyPart + ' ssh://' + userIpPort)

if (command == 'scp') or (command == 's'):
    if serverConfig['justRunCommand']:
        os.system(serverConfig['command'])
    else:
        os.system('scp' + keyPart + args['operands'][2] + ' scp://' + userIpPort + '/' + args['operands'][3])
