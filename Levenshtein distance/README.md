# Levenshtein distance

## Usage
Run `python3 levenshtein.py X Y `, there `X` and `Y` are
text sequence you want to measure distance between.
For example `python3 levenshtein.py aaabc abc`.
Note that the default alphabet consists of letters
`a`, `b` and `c`. You may add more letters by editing `alphabet`
variable in `levenshtein.py` file.
Also, you may provide your own penalties values for insertion, deletion and 
changing characters, edit `penalties` variable.
## Requirements

For running project such modules for `python 3` are necessary:
- `numpy`
- `pandas`
- `argparse`