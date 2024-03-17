from datetime import datetime
import pytz

def Date():
    ist_timezone = pytz.timezone('Asia/Kolkata')
    ist_now = datetime.datetime.now(ist_timezone)
    
    ist_date_formatted = ist_now.strftime('%d/%m/%Y')
        
    return ist_date_formatted
