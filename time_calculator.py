
from datetime import datetime, timedelta

def add_time(str_time: str, duration: str, starting_day: str = "") -> str:
    
    hh_mm = duration.split(":")
    hh = hh_mm[0]
    mm = hh_mm[1]
    
    time_ini = datetime.strptime(str_time, '%I:%M %p')
    time_fin = time_ini + timedelta(hours=int(hh), minutes=int(mm))
    print(time_ini)
    print(time_fin)
    
    diff_days = time_fin.day - time_ini.day
    msg_days = ""
    str_days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    starting_day = starting_day.capitalize()
    
    if diff_days == 1:
        msg_days = "(next day)"
    elif diff_days > 1:
        msg_days = f'({diff_days} days later)'
    
    if diff_days > 0 and starting_day != "":
        inx = str_days.index(starting_day)
        inx_next = inx - 7 if inx > 7 else 7 - inx
        
        if diff_days < 8:
            starting_day = str_days[diff_days - inx_next]
        else:
            diff_count = 7 - (diff_days % 7)
            inx_next = inx - diff_count if inx > diff_count else diff_count - inx
            starting_day = str_days[inx_next]
    
    hh_mm = f"{time_fin.strftime('%I:%M %p')}".split(":")
    hh = int(hh_mm[0])
    mm = hh_mm[1]
    
    result = f"{str(hh)}:{mm}, {starting_day}" if starting_day != "" else f"{str(hh)}:{mm}"
    
    return f"{result} {msg_days}".strip()
