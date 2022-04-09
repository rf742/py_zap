# py_zap

Python implementation of zap program. (See other repositories of mine for different implementations.)

**zap** is a program to calculate the electrostatic force exerted on each particle within
a system of point charges, in accordance with Coulomb's Law.

## Usage

After cloning this repo, either add the file to $PATH, or navigate to the folder and run:

```
./main.py -i datafile
```

Where the input file contains the data for the system of charges

## I/O

### Input Data File format

* Any line beginning with # is ignored
* Each line contains the data for one point charge
* Each field should be separated by a comma
* The format for a line is: x,y,q
* Where the units should be: m,m,C

```
# This line will be ignored
0,2,5
0,0,2E-6
```

* The file above contains two point charges
* The 1st is located at (0m,2m) and has a charge of 5C
* The 2nd is located at (0m,0m) and has a charge of 2 x 10^-6 C (2 micro Coulombs) 


### Output

This program can output to the terminal or to a csv file.

The default is to output to just the terminal. If you add the -c/--csv flag,
the data will be output in csv format to a file in the current directory named with
zap\_data\_TIMESTAMP.csv, where TIMESTAMP is in the format %Y%m%d%H%M%S.

### Gravity Mode

Due to the similarity in the equations for gravitational and electrostatic attraction
this program has the ability to do gravitational force calculations.

Activate this via commandline switch '-g' like this:

```
./main.py -i datafile -g
```

The input file takes the same format, however the third argument in each line
is now treated as the mass rather than the charge. Note that in gravity mode
the program will verify that the masses are positive and refuse to run if
there are any negative masses.

## Todo

### Immediate Goals

- [x] Implement logic for 1D problems
- [x] Fix logic for 2D problems
- [ ] Add logic for 3D problems
- [x] Error handling for reading data files


### Next Steps

- [x] Use argparse to implement command line args.
  - [x] -v flag
  - [x] -i flag {name of file to get input data from}
  - [x] -c flag {name of file to output csv data to}
  - [x] -d flag {switch angles to degrees}
- [ ] Add Test suite

### Long term

- [x] gravity mode
  - [x] Allow command line flag -g to switch to gravity problems
  - [x] Program in graviational constant
  - [x] Check inputs for negative "charges"
- [ ] Use plotting software to allow generation of diagram of
      system.
