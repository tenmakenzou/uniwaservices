from datetime import datetime

def get_library():
    current_date = datetime.now()
    day_of_week = current_date.weekday()  
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    x = days_of_week[day_of_week]
    current_hour = current_date.hour 
    
    current_time = float(current_date.strftime("%H.%M"))
    if (9.00 <= current_time <= 19.00) and (x != 'Friday') and (x != 'Saturday') and (x != 'Sunday'):
        return "Η Βιβλιοθήκη είναι ανοιχτή\nLibrary is open"
    elif (9.00 <= current_time <= 15.30) and (x == 'Friday') and (x != 'Saturday') and (x != 'Sunday'):
        return "Η Βιβλιοθήκη είναι ανοιχτή\nLibrary is open"
    else:
        return "Η Βιβλιοθήκη είναι κλειστή\nLibrary is closed"


def get_restauraunt():
        current_date = datetime.now()
        current_hour = current_date.hour 
        current_time = float(current_date.strftime("%H.%M"))

        if ((7.30 <= current_time <= 9.0) or (12.30 <= current_time <= 15.40) or (18.00 <= current_time <= 20.30)):
            return("Η σιτίση ειναι ανοιχτή\nRestauraunt is open")
            
        else:
            if current_time < 7.30 or current_time >20.30:
                next_opening_time = "7:30"
                return (f"Η σιτίση είναι κλείστη , ανοίγει στις [{next_opening_time}]\nRestauraunt is closed and opens at [{next_opening_time}]")
            elif current_time < 12.30:
                next_opening_time = "12:30"
                return (f"Η σιτίση είναι κλείστη , ανοίγει στις [{next_opening_time}]\nRestauraunt is closed and opens at [{next_opening_time}]")

            elif current_time < 18.00:
                next_opening_time = "18:00"
                return (f"Η σιτίση είναι κλείστη , ανοίγει στις [{next_opening_time}]\nRestauraunt is closed and opens at [{next_opening_time}]")

