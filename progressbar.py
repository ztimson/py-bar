from time import time
from sys import stdout


class Progressbar:
    """
    An iterable object that can display statics about its self such as time elapsed, percentage, progress as a fraction,
    iterations per second, estimated time and can generate an ascii progressbar.
    """

    def __init__(self, start, end=None, step=1, length=20, unit="/s", color="\033[0;31m", display=True,
                 bar_format="{elapsed} {percentage} {bar} {rate} {eta}"):
        """
        Create an iterable object with the following properties. If no end is specified the start is assumed the end.
        :param start: starting position of iterator (inclusive)
        :param end: ending position of iterator (exclusive)
        :param step: how many integers to add each iteration
        :param length: length of the progress bar (default is 20)
        :param unit: unit to display with the rate (default is /s)
        :param color: ANSI escape codes prepended to output to change color (default is \033[0;31m )
        :param display: automatically display statistics on every iteration (default True)
        :param bar_format: format the way statistics are displayed. Components to display are: elapsed, percentage, bar,
               fraction, rate and eta. These keywords are swapped out for the actual information. (default is
               "{elapsed} {percentage} {bar} {rate} {eta}")
        """
        if end is None:
            self.start = 0
            self.end = start
        else:
            self.start = start
            self.end = end
        self.step = step
        self.length = length
        self.unit = unit
        self.color = color
        self.display = display
        self.bar_format = bar_format

    def __iter__(self):
        """
        initiate iterator which sets the starting point and gets the current time which is used for statistics
        :return: returns the new object
        """
        self.start_time = time()
        self.current = self.start
        return self

    def __next__(self):
        """
        next overload. If display is true the latest stetistics are displayed
        :return: The next number in iterator
        """
        if self.display:
            self.__restart_line()
            stdout.write(str(self))
            stdout.flush()
        if self.current >= self.end:
            raise StopIteration
        self.current += self.step
        return self.current - self.step

    def __str__(self):
        """
        displays the iterator as a string of statistics
        :return: formatted string
        """
        return self.color + self.bar_format.format(bar=self.generate_bar(),
                                                   elapsed=self.__time_format(self.elapsed()),
                                                   eta=self.__time_format(self.estimated_time()),
                                                   fraction=self.fraction(),
                                                   percentage=(str(int(self.percentage() * 100)) + "%").rjust(4),
                                                   rate=str(self.per_second()) + self.unit)

    def elapsed(self):
        """
        calculate the time that has elapsed
        :return: long elapsed time
        """
        return time() - self.start_time

    def estimated_time(self):
        """
        Use the current percentage and elapsed time to determine an ETA
        :return: how much time is left
        """
        try:
            return self.elapsed() / self.percentage() - self.elapsed()
        except ZeroDivisionError:
            return 0

    def fraction(self):
        """
        create a fraction representing the progress and the end of the iterator
        :return: string representing current/end of iterator
        """
        return "%s/%d" % (str(self.current).rjust(len(str(self.end))), self.end)

    def generate_bar(self):
        """
        creates an ascii progressbar
        :return: string progressbar
        """
        bar = "[{0}]".format(("=" * int(self.percentage() * self.length)).ljust(self.length))
        return bar

    def per_second(self):
        """
        use the current number of iterations and the amount of elapsed time to determine how many iterations per second
        :return:
        """
        try:
            return round(self.current / self.step / self.elapsed(), 2)
        except ZeroDivisionError:
            return 0

    def percentage(self):
        """
        use current position / (end - start) to calculate percentage of completion
        :return: float of percentage to completion
        """
        return self.current / (self.end - self.start)

    @staticmethod
    def __restart_line():
        """
        Writes return carriage to stdout and flushes. This allows writing to the same line.
        :return: None
        """
        stdout.write('\r')
        stdout.flush()

    @staticmethod
    def __time_format(time_to_format):
        """
        formats time to mm:ss
        :param time_to_format: long to format
        :return: string of time
        """
        m, s = divmod(time_to_format, 60)
        return "%02d:%02d" % (m, s)
