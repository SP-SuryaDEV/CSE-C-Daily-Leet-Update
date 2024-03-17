from datetime import datetime

def Date():
    current_date = datetime.now()
    formatted_date = current_date.strftime('%d/%m/%Y')
    
    return formatted_date
