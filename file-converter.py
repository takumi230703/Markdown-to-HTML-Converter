import sys
import markdown

inputfile = sys.argv[2]
outputfile = sys.argv[3]
contents = ''

if sys.argv[1] == 'markdown':
    with open(inputfile) as f:
        contents = f.read()
    html = markdown.markdown(contents)
    with open(outputfile, 'w') as f:
        f.write(html)
else: print('Invalid command.')
