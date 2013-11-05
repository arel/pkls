# pkls
*"ls" for pickle files.*

A super simple python module for listing contents of a `pickle` file on the command line.

## Example
Assuming you have a file named `test.pk`, you can list its contents like this:
``` bash
$ pkls test.pk
```
which pretty-prints the contents of `test.pk`. For example,
``` bash
$ pkls test.pk
test.pk
{   'X': array([[58, 99, 45, ..., 82, 90, 17],
       [76, 28, 14, ..., 31, 19, 70],
       [ 7, 37, 21, ..., 78, 88, 87]]),
    'name': 'my data',
    'result': 0.957,
    'y': array([0, 1, 1, ..., 0, 0, 1])}
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

## Caveats

Classes and modules referenced by the pickle file must be present in your current environment.
