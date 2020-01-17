# Author: Nathan Merrill
import cliparse, yaml

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

