# progressbar
Python CLI Progress bar. This module is an iterator that can not only, iterate, but display its self as a progressbar along with some other usefull iformation such as iterations a second, estimated time, elapsed time, etc.

```00:25 100% [====================] [100/100] 3.99/s 00:00```

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

Maybe you dont want to use it as an iterable and you just want a progressbar. You can manually control its progress. Example, you want to view download progress:

```
progress = Progressbar(download_size, unit=" MB/s") # create the object

...

progress.__iter__() # This will start the clock and initiate the iterable

...

progress.current = 220 # set the curent progress ex. 200/1000 Mb downloaded
download_speed = progress.rate() # get any sort of stistics you may want, the download rate for exmple
print(progress) # display progress bar. Manually iterating the object it will not display automaticly
```

This would print (No underscores in bar. They are just there to keep spacing):

```00:53  20% [====________________] [ 200/1000] 3.75 Mb/s 03:32```

### API
**Class: Progressbar**

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
