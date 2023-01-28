from datetime import date

class Fecha:
    MONTHS = [
        "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", 
        "Agosto", "Setiembre", "Octubre", "Noviembre", "Diciembre",
    ]

    DAYS_IN_MONTH = [
        31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31,
    ]

    @staticmethod
    def isLeapYear ( year ):
        return (year % 4 == 0 and year % 100 != 0 ) or ( year % 400 == 0 )

    @staticmethod
    def today ( ):
        t = date.today() 
        return Fecha( t.day, t.month, t.year )

    def __init__ (self, day, month, year ):
        self.day     = day
        self.month   = month # 1..12
        self.year    = year
        if Fecha.isLeapYear( year ):
            DAYS_IN_MONTH[1] = 29

    def __str__ ( self ):
        return f"{self.day} de {Fecha.MONTHS[self.month-1]}"

    def __eq__ ( self, other ):
        return ( self.day   == other.day   and 
                 self.month == other.month and 
                 self.year  == other.year  )

class Hora:
    def __init__ (self, hour, minute):
        self.hour    = hour
        self.minute  = minute

    def __str__ ( self ):
        return f"{hour.self}:{self.minute}"

    def __eq__ ( self, other ):
        return self.hour == other.hour and self.minute == other.minute

