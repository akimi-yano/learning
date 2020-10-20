import enum

class Color():
    RED = 'RED'
    BLUE = 'BLUE'
    GREEN = 'GREEN'

print(Color.RED)
print(type(Color.RED))

class Color2(enum.Enum):
    RED = 'RED'
    BLUE = 'BLUE'
    GREEN = 'GREEN'

print(Color2.RED)
print(type(Color2.RED))

print(Color.RED + 'hi')
print(Color2.RED + 'hi')