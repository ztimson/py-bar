# progressbar
Python CLI Progress bar. This module is an iterator that can not only, iterate, but display its self as a progressbar along with some other usefull iformation such as iterations a second, estimated time, elapsed time, etc.

### Authors
 * [Zak Timson](http://zakscode.com)

### License
GNU GENERAL PUBLIC LICENSE, Version 3, 29 June 2007. read LICENSE for more

### Install
Copy the script to your project and import it with:
```import progressbar```
or
```from progressbar import Progressbar```

### Quick Start
Use in a forloop:
```for i in Progressbar(100)```

Dont like it auto writing to the stdout? Do it your self.
```
progress = Progressbar(100, display=False) # display false stops the auto writing
for i in progress:
	print(str(progress)) # using the to string will maunually write it
```

### API
class: Progressbar

**Attributes**

start - iterator starting position

end - iterator ending position

current - curent iteration

step - number to be added to current each iteraton

length - length of characters in the progress bar

units - unit to append to rate

color - ANSI escape code to change color of text

display - automaticly display the to string with each iteration

bar_format - string which dictates how things are displayed ex "{elapesed} - {eta}" could look like: 00:00 - 00:10. See the statistics portion to see what can be displayed

**Available Statistics**
elapsed - running time of iterator. displayed as: mm:ss

percentage - percentage of completion. displayed as: 100%

bar - the progress bar. displayed as: |==========|

fraction - current / end. displayed as: [100/100]

rate - iterations per second. displayed as: 2.00/s (unit can be changed, see units attribute)

eat - estimated time until completion. displayed as: mm:ss

**Methods**
elapsed(self) - running time of iterator

estimated_time(self) - estimated time until iterator completes

fraction(self) - create string representing the fraction, complete over total

generate_bar - generates the progress bar and returns string

per_second - calculates the rate or speed of iterations per second

percentage - floating point of completion

### Bug Reporting
Please submit bugs to the github [issue tracker](https://github.com/zaktimson/progressbar/issues)
