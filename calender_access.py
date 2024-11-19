import calender_module

def main():
    # Get user input for year and month
    year = int(input("Enter year (e.g., 2024): "))
    month = int(input("Enter month (1-12): "))
    # Display the calendar for the specific month
    print("\nDisplaying the calendar for the given month:\n")
    calender_module.display_calendar(year, month)
    # Ask if the user wants to see the entire year's calendar
    show_year = input("\nWould you like to see the entire year's calendar? (y/n): ").lower()
    if show_year == 'y':
        print("\nDisplaying the calendar for the entire year:\n")
        calender_module.display_year_calendar(year)
if __name__ == "__main__":
    main()
