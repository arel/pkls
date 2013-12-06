# pkls
*"ls" for pickle files.*

A super simple python module for listing contents of a `pickle` file from the command line.
Unlike your normal `pickle.load()` function, `pkls` gracefully displays classes
even if they are not in your current environment.

## Example
Assuming you have a file named `example.pickle`, you can list its contents like this:
``` bash
$ pkls example.pickle
```
which pretty-prints the contents of `example.pickle`. For example,
``` bash
$ pkls example.pickle
example.pickle
[   1,
    2,
    'Salem',
    {   3: 'Sprague'},
    OrderedDict([(541, 'Oregon')]),
    missing_module.ArelClass : {   'a': 'Camerata', 'b': 123}]
```

## Usage

``` bash
usage: pkls [-h] FILE [FILE ...]

List contents of a pickle file

positional arguments:
  FILE        Pickle files to list.

optional arguments:
  -h, --help  show this help message and exit
```


## Installation

``` bash
$ pip install git+https://github.com/arel/pkls.git
```
