# Author: Nathan Merrill
import sys

class Argument:
    def __init__(self, name, shortName, takesValue, description):
        self.name = name
        self.shortName = shortName
        self.takesValue = takesValue
        self.description = description

    def check(self, inputArgs, outputArgs):
        found = False
        value = None
        for i, inputArg in enumerate(inputArgs):
            if ('--' + self.name) in inputArg:
                found = True
                inputArgs.pop(i)
                splitArg = inputArg.split('=')
                if self.takesValue:
                    if len(splitArg) == 2:
                        value = splitArg[1]
                        break
                    else:
                        raise ValueError('Value expected. Did you mean ' + inputArg + '=myValue?')
                else:
                    if len(splitArg) != 1:
                        raise ValueError('Value not expected. Did you mean ' + splitArg[0])
            elif (self.shortName is not None) and (inputArg == ('-' + self.shortName)):
                found = True
                if self.takesValue:
                    if (len(inputArgs) >= i + 2) and (inputArgs[i + 1][0] != '-'):
                        value = inputArgs[i + 1]
                        inputArgs.pop(i)
                        inputArgs.pop(i)
                        break
                    else:
                        raise ValueError('Value expected. Did you mean ' + inputArg + ' myValue?')
                else:
                    inputArgs.pop(i)
        if found:
            outputArgs[self.name] = value

class Parser:
    def __init__(self):
        self.inputArgs = sys.argv[1:]
        self.requiredArgs = []
        self.minOperands = 0
        self.maxOperands = None
        self.constraints = {}
        self.customDescription = None
        self.argRules = []
        self.outputArgs = {
            'operands': []
        }
        self.addArg('help', 'h', description='Show this help menu')

    def addArg(self, name, shortName=None, takesValue=False, description=None):
        self.argRules.append(Argument(name, shortName, takesValue, description))

    def setRequiredArgs(self, args):
        self.requiredArgs = args

    def setRequiredOperands(self, min = 0, max = None):
        self.minOperands = min
        self.maxOperands = max

    def setOperandConstraints(self, constraints):
        self.constraints = constraints

    def setCustomDescription(self, description):
        self.customDescription = description

    def parseArgs(self):
        for argRule in self.argRules:
            argRule.check(self.inputArgs, self.outputArgs)
        if 'help' in self.outputArgs:
            if self.customDescription is not None:
                print(self.customDescription.lstrip().rstrip())
            for argRule in self.argRules:
                if argRule.shortName is not None:
                    print('--' + argRule.name + ', -' + argRule.shortName)
                else:
                    print('--' + argRule.name)
                if argRule.description is not None:
                    print('    ' + argRule.description)
            sys.exit()
        self.outputArgs['operands'] = self.inputArgs
        for requiredArg in self.requiredArgs:
            if requiredArg not in self.outputArgs:
                raise ValueError(requiredArg + ' is required')
        if len(self.outputArgs['operands']) < self.minOperands:
            raise ValueError('At least ' + str(self.minOperands) + ' command line operand(s) are required')
        if (self.maxOperands is not None) and (len(self.outputArgs['operands']) > self.maxOperands):
            raise ValueError('This program takes at most ' + str(self.maxOperands) + ' command line operand(s)')
        for i in self.constraints:
            if self.outputArgs['operands'][i] not in self.constraints[i]:
                raise ValueError('Operand #' + str(i) + ' must be one of these: ' + str(self.constraints[i]))
        return self.outputArgs
