import matplotlib.dates as mdates
from pylab import *
# from numpy import array,sin,pi
from numpy import *
from datetime import date

DateOfBirth = input('Enter BirthDate in Format dd-mm-yyyy : ')
DateOfTarget = input('Enter TargetDate In  Format dd-mm-yyyy : ')


DateOfBirth = DateOfBirth.strip()
DateOfTarget = DateOfTarget.strip()


def GetDayMonthYear(DateOfBirth,DateOfTarget):
    try:

        day1,month1,year1 = DateOfBirth.split('-')
        day2,month2,year2 = DateOfTarget.split('-')
        birthday = date(int(year1),int(month1),int(day1)).toordinal()
        targetdate = date(int(year2),int(month2),int(day2)).toordinal()
        return birthday,targetdate
    except Exception as er1:
        print('Error in date Format', str(er1))


def DaysRange(targetdate):

    try:

        RangeOfDay = array(range((targetdate-3),(targetdate+40)))
        return RangeOfDay
    except Exception as er2:
        print('Error in Range days', str(er2))


def GetBiorhythms(RangeOfDay, birthday):
    # list_of_cycles = []
    try:

        physical = sin(2*pi*(RangeOfDay-birthday)/23)
        emotional = sin(2*pi*(RangeOfDay-birthday)/28)
        intellectual = sin(2*pi*(RangeOfDay-birthday)/33)

        list_of_cycles = [physical,emotional,intellectual]

        return list_of_cycles
    except Exception as er3:
        print('Error in Biorhythms Formulas', str(er3))



def ShowGraph(RangeOfDay,list_of_cycles):

    try:

        label = []
        for px in RangeOfDay:
         label.append(date.fromordinal(px))

        fig = figure()
        f_ax = fig.gca()
        plot(label,list_of_cycles[0], linewidth=3, color="r", alpha=.5)
        plot(label,list_of_cycles[1], linewidth=3, color="b", alpha=.5)
        plot(label,list_of_cycles[2], linewidth=3, color="g", alpha=.5)

        # adding a legend
        legend(['Physical', 'Emotional', 'Intellectual'],loc='upper right')
        title("Biorhythms Graph")
        # formatting the dates on the x axis
        f_ax.xaxis.set_major_formatter(mdates.DateFormatter('%d\n%b\n%y\n%a'))
        show()
    except Exception as er4:
        print('Error in Graph plot', str(er4))

birthday,targetdate = GetDayMonthYear(DateOfBirth,DateOfTarget)
RangeOfDay = DaysRange(targetdate)
list_of_cycles = GetBiorhythms(RangeOfDay, birthday)

ShowGraph(RangeOfDay,list_of_cycles)






