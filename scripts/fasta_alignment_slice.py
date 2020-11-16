#!/usr/bin/env python3

'''
USAGE
    fasta_alignment_slice.py N-M [FILE...]

DESCRIPTION
    Get the range N-M of the input alignement, N and M are 1-base
    closed interval coordinates.

OPTIONS
    --help
        Display this message

'''

import getopt, sys, fileinput, textwrap, fasta

class Options(dict):

    def __init__(self, argv):
        
        # set default
        self.set_default()
        
        # handle options with getopt
        try:
            opts, args = getopt.getopt(argv[1:], "", ['help'])
        except getopt.GetoptError as e:
            sys.stderr.write(str(e) + '\n\n' + __doc__)
            sys.exit(1)

        for o, a in opts:
            if o == '--help':
                sys.stdout.write(__doc__)
                sys.exit(0)

        i, j = map(int, args[0].split("-"))
        self["slice"] = slice(i-1, j)
        self.args = args[1:]
    
    def set_default(self):
    
        # default parameter value
        self["slice"] = None

def main(argv=sys.argv):
    
    # read options and remove options strings from argv (avoid option 
    # names and arguments to be handled as file names by
    # fileinput.input().
    options = Options(argv)
    sys.argv[1:] = options.args
    
    # organize the main job...
    for name, sequence in fasta.reader(fileinput.input()):
        fasta.writer(name, sequence[options["slice"]], sys.stdout)
    
    # return 0 if everything succeeded
    return 0

# does not execute main if the script is imported as a module
if __name__ == '__main__': sys.exit(main())

