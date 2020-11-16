# python-fasta
Useful python scripts for simple FASTA file manipulations.

## Setup
* Download python-fasta.
* Run the python setup.py script with the python 3 interpreter.
```bash
python3 setup.py build
sudo python3 setup.py install
```
This will install the module fasta containing reader and writer functions, as well as a serie of scripts in /usr/local/bin/.

## Scripts

### fasta_2nuc.py
```
USAGE
    fasta_2nuc.py [OPTION] [FILE...]

DESCRIPTION
    Format a FASTA file into the PAML format (phylip interleaved with names of max length 30).
    
OPTIONS
    --help
        Display this message
```

### fasta_alignment_slice.py
```
USAGE
    fasta_alignment_slice.py N-M [FILE...]

DESCRIPTION
    Get the range N-M of the input alignement, N and M are 1-base
    closed interval coordinates.

OPTIONS
    --help
        Display this message
```

### fasta_dealign.py
```
USAGE
    fasta_dealign.py [OPTION] [FILE...]

DESCRIPTION
    Remove gaps from FASTA sequences.

OPTIONS
    --help
        Display this message
```

### fasta_filter.py        
```
USAGE
    fasta_filter.py [OPTION] LIST [FILE...]

DESCRIPTION
    Filter a FASTA files with a given list of sequence headers.
    
OPTIONS
    --short
        Read only the header's leading string before the first space in
        the input FASTA file
        
    --help
        Display this message
```

### fasta_grepheader.py
```
USAGE
    fasta_grepheader.py [OPTION] PATTERN [FILE...]

DESCRIPTION
    Find sequences using grep pattern to search matching headers.

OPTIONS
    -v, --invert-match
        Select non matching headers

    -x, --line-regexp
        Match full header line
    
    --help
        Display this message
```

### fasta_len.py
```
USAGE
    fasta_len.py [OPTION] [FILE...]

DESCRIPTION
    Display sequence lengths

OPTIONS
    --help
        Display this message
```

### fasta_range.py
```
USAGE
    fasta_range.py [OPTION] A-B [FILE...]

DESCRIPTION
    Extract all sequences of the FASTA input file from positions A to B.
    
OPTIONS
    --help
        Display this message
```

### fasta_rename.py
```
USAGE
    fasta_rename.py [OPTION] TABLE [FILE...]

DESCRIPTION
    Replace header in the input FASTA file using a correspondance table.

    TABLE file must list correspondances separated by a tabulation in 
    the following order:
    
    <old name>TAB<new name>
    ...
    
OPTIONS
    --help
        Display this message
```
