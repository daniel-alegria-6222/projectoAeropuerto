from datetime import date
from re import compile

class Fecha:
    date_pattern = compile(r"^\d\d-\d\d-\d\d\d\d$")

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


    def __init__ (self, day, month, year ):
        self.day     = day
        self.month   = month # 1..12
        self.year    = year
        if Fecha.isLeapYear( year ):
            self.DAYS_IN_MONTH[1] = 29

    def getNamedMonth ( self ):
        return Fecha.MONTHS[self.month-1]

    @staticmethod
    def isFechaStr ( fecha_string ):
        return Fecha.date_pattern.match( fecha_string )

    @staticmethod
    def newFromStr ( fecha_string ):
        if Fecha.isFechaStr(fecha_string):
            # fecha_string tienen la forma 'dd-mm-yyyy'
            return Fecha( *[int(e) for e in fecha_string.split("-")] )

    @staticmethod
    def today (  ):
        t = date.today()
        return Fecha( t.day, t.month, t.year )


    def __str__ ( self ):
        return f"{self.day:02}-{self.month:02}-{self.year:04}"

    def __eq__ ( self, other ):
        return ( self.day   == other.day   and 
                 self.month == other.month and 
                 self.year  == other.year  )

class Hora:
    time_pattern = compile(r"^\d\d:\d\d$")

    def __init__ (self, hour, minute):
        self.hour    = hour
        self.minute  = minute

    def __str__ ( self ):
        return f"{self.hour}:{self.minute}"

    def __eq__ ( self, other ):
        return self.hour == other.hour and self.minute == other.minute

    @staticmethod
    def isHoraStr ( hora_string ):
        return Hora.time_pattern.match( hora_string )

    @staticmethod
    def newFromStr ( hora_string ):
        if Hora.isHoraStr(hora_string):
            # fecha_string tienen la forma 'hh:mm'
            return Hora( *[int(e) for e in hora_string.split(":")] )

