# Time_class.py
"""Class Time with read-write properites."""

class Time:
    """Class Time with read-write properties"""

    def __init__(self, hour=0, minute=0, second=0):
        """Initialize each atribute."""

        self.hour = hour
        self.minute = minute
        self.second = second

    @property
    def hour(self):
        """Method will return hour"""

        return self._hour

    @hour.setter
    def hour(self, hour):
        """Set the hour - setter"""

        if not (0 <= hour < 24):
            raise ValueError(f'Hour {hour} must be in valid range 0-23')

        self._hour = hour

    @property
    def minute(self):
        """ Method will return minut"""
        return self._minute


    @minute.setter
    def minute(self, minute):
        """ Method will return minut"""

        if  not (0 <= minute < 60):
            raise ValueError('Minute not in range 0-60')

        self._minute = minute

    @property
    def second(self):
        """ Method will return secund"""
        return self._second



    @second.setter
    def second(self, second):
        """ Method will return secund"""

        if  not (0 <= second < 60):
            raise ValueError('Minute not in range 0-60')

        self._second = second

    def set_time(self, hour=0, minute=0, second=0):
        """Set valiue of hour minute and sekunden"""

        self.hour = hour
        self.minute = minute
        self.second = second


    @property
    def time(self):
        """returns time as a tuple"""
        return (self.hour, self.minute, self.second)

    @time.setter
    def time(self, time_tuple):
        """Set a time from a provided tuple"""
        self.set_time(time_tuple[0], time_tuple[1], time_tuple[2])


    def __repr__(self):
        """Return Time string for repr()."""
        return (f'Time(hour={self.hour}, minute={self.minute}, second={self.second}')

    def __str__(self):
        """Return Time string in 12h-hour clock format"""
        return (
            ('12' if self.hour in (0,12) else str(self.hour % 12)) + f':{self.minute:0>2}:{self.second:0>2}' +
            (' AM' if self.hour <12 else 'PM')
        )