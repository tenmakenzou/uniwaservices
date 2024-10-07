import openpyxl
from datetime import datetime

# will optimise later

def run():


    week_1 = [
        'C3', 'D3', 'E3', 
        'F3', 'G3', 'H3', 
        'I3',
        'C4', 'D4', 'E4', 
        'F4', 'G4', 'H4', 
        'I4',
        'C5', 'D5', 'E5', 
        'F5', 'G5', 'H5', 
        'I5',
        'C6', 'D6', 'E6', 
        'F6', 'G6', 'H6', 
        'I6'
    ]

    week_2 = [
        'C26', 'D26', 'E26', 
        'F26', 'G26', 'H26', 
        'I26',
        'C27', 'D27', 'E27', 
        'F27', 'G27', 'H27', 
        'I27',
        'C28', 'D28', 'E28', 
        'F28', 'G28', 'H28', 
        'I28',
        'C29', 'D29', 'E29', 
        'F29', 'G29', 'H29', 
        'I29'
    ]

    week_3 = [
        'C48', 'D48', 'E48', 
        'F48', 'G48', 'H48', 
        'I48',
        'C49', 'D49', 'E49', 
        'F49', 'G49', 'H49', 
        'I49',
        'C50', 'D50', 'E50', 
        'F50', 'G50', 'H50', 
        'I50',
        'C51', 'D51', 'E51', 
        'F51', 'G51', 'H51', 
        'I51'
    ]

    week_4 = [
        'C71', 'D71', 'E71', 
        'F71', 'G71', 'H71', 
        'I71',
        'C72', 'D72', 'E72', 
        'F72', 'G72', 'H72', 
        'I72',
        'C73', 'D73', 'E73', 
        'F73', 'G73', 'H73', 
        'I73',
        'C74', 'D74', 'E74', 
        'F74', 'G74', 'H74', 
        'I74',
        'C75', 'D75', 'E75', 
        'F75', 'G75', 'H75', 
        'I75'
    ]



    wb = openpyxl.load_workbook('menu.xlsx')
    sheet = wb['Φύλλο1'] 

    target_date = datetime.now()  # datetime of the current day

    def get_row():
        for row in sheet.iter_rows():
            for cell in row:
                if isinstance(cell.value, datetime):  
                    if cell.value.date() == target_date.date():  
                     
                        return cell.coordinate

    x = get_row()

    y = 0 

    if x in week_1:
        y = 2
    if x in week_2:
        y = 26
    if x in week_3:
        y = 46
    if x in week_4:
        y = 71


    def get_date(x, y):
        count = 0
        result = ""  #
        
        for cell in sheet[x[0]][y:]:
            if cell.value is not None:
                if not isinstance(cell.value, datetime):
                    if count == 0:
                        result += "\n    Μεσημεριανό    \n"  
                    if count == 3:
                        result += "\n    Δείπνο    \n"  
                    
                    result += f"- {cell.value}\n"  
                    count += 1
                    if count == 6:
                        break
        
        return result  

    help = get_date(x,y)
    return help

