# smith-waterman
### Usage
Run the command with an file named `input.fast` into the root folder and the output will e written to a txt file named as `output.txt`

```sh
$ python main.py
```

### Help
```sh
$ python main.py --help
usage: Params for processing .FASTA files [-h] [-m MATCH] [-M MISSMATCH] [-g GAP]

optional arguments:
  -h, --help            show this help message and exit
  -m MATCH, --match MATCH
                        Input the match value. Defaults to 2
  -M MISSMATCH, --missmatch MISSMATCH
                        Input the missmatch value. Defaults to -3
  -g GAP, --gap GAP     Input the gap value. Defaults to -4
```

### References
- [Wikipedia](https://en.wikipedia.org/wiki/Smith%E2%80%93Waterman_algorithm)
