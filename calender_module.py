import calendar

def display_calendar(year, month):
    # Validate month range
    if month < 1 or month > 12:
        print("Invalid month! Please enter a month between 1 and 12.")
        return
    # Get the calendar for the month and year
    cal = calendar.month(year, month)
    # Print the calendar
    print(cal)
    
def display_year_calendar(year):
    # Use the calendar module to display the entire year's calendar
    cal = calendar.TextCalendar(calendar.SUNDAY)
    print(cal.formatyear(year))