from lib.executor import execute
from second.main import fixer, find_noun_and_verb
print('hello')
fixer()

print('find noun and verb')
noun, verb = find_noun_and_verb()
print(f'noun {noun}, verb: {verb}, ret: {100 * noun + verb}')
