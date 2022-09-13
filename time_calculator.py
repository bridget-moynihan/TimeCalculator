DAYS = ['Sunday', 'Monday', "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday",'Sunday', 'Monday', "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday" ]


#this converts the time to 24 hrs
def convert_24_hr(time):
  time1, type = time.split(" ")
  if type == "AM":
    return time1
  else:
    hour, minute = time1.split(":")
    _24hour = int(hour) + 12
    return str(_24hour) + ":" + minute

#this returns the day of the week, based on how many days have elapsed
def getDayofWeek(dayOfWeek, daysPassed):
  if daysPassed > 7:
    daysPassed = daysPassed - 7
  index = DAYS.index(dayOfWeek.capitalize())
  return DAYS[index+daysPassed%7]

def add_time(start, duration, dayOfWeek = None):
  start =convert_24_hr(start)
  startHour, startMinute = map(int,start.split(":"))
  durationHour, durationMinute = map(int,duration.split(":"))
  addedTime24 = (startHour + (startMinute)/60) + (durationHour + durationMinute/60)
  if addedTime24 >= 24:
    if (startMinute+durationMinute) >= 60:
      durationHour += 1
      minutesPassed = (startMinute+durationMinute)%60
    else:
      minutesPassed = (startMinute+durationMinute)
    daysPassed = (startHour+durationHour)//24
    remHour = (startHour+durationHour)%24
    if remHour >= 24:
      type = "PM"
      hour = remHour - 12
    else:
      if remHour == 0:
        remHour = 12
      type = "AM"
      hour = remHour
    
    if daysPassed == 1:
      daysText = " (next day)"
    else:
      daysText = " (" + str(daysPassed) + " days later)"
    if dayOfWeek == None:
      return (str(hour) + ":" + str(minutesPassed).zfill(2) + " "+ type+ daysText)
    else:
      return (str(hour) + ":" + str(minutesPassed).zfill(2) + " "+ type+ ", " + getDayofWeek(dayOfWeek,daysPassed) +daysText)
    
  else:
    if (startMinute+durationMinute) >= 60:
      durationHour += 1
      minutesPassed = (startMinute+durationMinute)%60
    else:
      minutesPassed = (startMinute+durationMinute)
    hour = startHour + durationHour
    if hour >= 12:
      type = "PM"
      if hour > 12:
        hour = hour - 12
    else:
      type = "AM"
    if dayOfWeek == None:
      return str(hour) + ":" + str(minutesPassed).zfill(2) +" "+ type
    else:
      return str(hour) + ":" + str(minutesPassed).zfill(2) +" "+ type + ", " + dayOfWeek


