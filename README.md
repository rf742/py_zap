# py_zap

Python implementation of zap program.

**zap** is a program to calculate the electrostatic force exerted on each particle within
a system of point charges, in accordance with Coulomb's Law.

## Usage

After cloning this repo, either add the file to $PATH, or navigate to the folder and run:

```
./main.py -i datafile
```

Where the input file contains the data for the system of charges

### Data File format

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


## Todo

### Immediate Goals

- [x] Implement logic for 1D problems
- [x] Fix logic for 2D problems
- [ ] Add logic for 3D problems
- [ ] Error handling for reading data files


### Next Steps

- [ ] Use argparse to implement command line args.
  - [x] -v flag
  - [x] -i flag {name of file to get input data from}
  - [ ] -o flag {name of file to output data to}
- [ ] Add Test suite

### Long term

- [ ] gravity mode
  - [ ] Allow command line flag -g to switch to gravity problems
  - [ ] Program in graviational constant
  - [ ] Check inputs for negative "charges"
- [ ] Use plotting software to allow generation of diagram of
      system.
