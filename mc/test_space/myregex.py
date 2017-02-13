import re

example = ['Buffy', '#1', '"Closet Monster" (2015)  ', '', '', '[Buffy 4]']
p = re.compile('".*"')
p2 = re.compile('\[.*\]')

for item in example:
    if p.search(item):
        print('f')


newlist = list(map(p2.search, example))
#find the element position which is not None

#print([example[index] for index, value in enumerate(newlist) if value is None])


test_string = """Bee Moe $lim    Fatherhood 101 (2013)   (as Brandon Moore)      [Himself - President, Passages]  """

print(re.search(r'\[.*\]', test_string, re.DOTALL))


