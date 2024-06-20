import streamlit as st
import datetime
from collections import defaultdict

# Function to get the number of days in a month
def days_in_month(year, month):
    if month == 12:
        next_year = year + 1
        next_month = 1
    else:
        next_year = year
        next_month = month + 1
    last_day_of_month = datetime.date(next_year, next_month, 1) - datetime.timedelta(days=1)
    return last_day_of_month.day

# Function to get the starting months based on the service frequency
def get_starting_months(frequency):
    if frequency == 'Monthly':
        return list(range(1, 12 + 1))
    elif frequency == 'Quarterly':
        return [1, 4, 7, 10]
    elif frequency == '4 months once':
        return [1, 5, 9]
    elif frequency == 'Half-yearly':
        return [1, 7]
    elif frequency == 'Yearly':
        return [1]
    return []

# Function to schedule services for each interval based on frequency
def schedule_service(year, total_units, max_units_per_day, week_off_days, start_months, service_frequency, available_staff, persons_per_unit):
    schedule = defaultdict(list)
    unit_index = 0

    for start_month in start_months:
        current_date = datetime.date(year, start_month, 1)
        days_in_current_month = days_in_month(year, start_month)
        
        while current_date.weekday() in week_off_days:
            current_date += datetime.timedelta(days=1)
        
        for day in range(1, days_in_current_month + 1):
            if current_date.weekday() not in week_off_days:
                units_to_service_today = []
                available_slots = min(max_units_per_day, available_staff // persons_per_unit)
                for _ in range(available_slots):
                    unit_index += 1
                    if unit_index > total_units:
                        break
                    units_to_service_today.append(unit_index)
                schedule[current_date].extend(units_to_service_today)
                if unit_index >= total_units:
                    break
            current_date += datetime.timedelta(days=1)
    
    # Calculate future service dates based on the frequency
    additional_schedule = defaultdict(list)
    if service_frequency != 'Monthly':
        interval_months = {
            'Quarterly': 3,
            '4 months once': 4,
            'Half-yearly': 6,
            'Yearly': 12
        }
        months_increment = interval_months[service_frequency]
        for date in list(schedule.keys()):
            current_units = schedule[date]
            for i in range(1, 12 // months_increment):
                next_service_date = date + datetime.timedelta(days=i * months_increment * 30)
                if next_service_date.year == year:
                    additional_schedule[next_service_date].extend(current_units)
    else:
        # Monthly scheduling
        for date in list(schedule.keys()):
            current_units = schedule[date]
            next_date = date
            while next_date.year == year:
                next_date = next_date.replace(day=1) + datetime.timedelta(days=32)
                next_date = next_date.replace(day=date.day)
                if next_date.year == year:
                    additional_schedule[next_date].extend(current_units)
    
    schedule.update(additional_schedule)

    # Ensure every day of the year is covered
    all_days_schedule = defaultdict(list)
    for month in range(1, 13):
        days_in_current_month = days_in_month(year, month)
        for day in range(1, days_in_current_month + 1):
            date = datetime.date(year, month, day)
            if date in schedule:
                all_days_schedule[date] = schedule[date]
            else:
                all_days_schedule[date] = []
    
    return all_days_schedule

def main():
    st.title('Service Scheduler')
  
    # Add your logo image
    st.image("logo.jpg", width=150)
    
    # Dropdown for selecting equipment type
    equipment_types = ['Split AC', 'PACKAGE UNIT AC', 'Pest Control']
    equipment_type = st.selectbox('Select type of equipment/service', equipment_types)
    
    # User inputs
    year = st.number_input('Enter the year', min_value=2022, max_value=2100, value=2025)
    total_units = st.number_input(f'Enter total number of {equipment_type}s', min_value=1, value=50)
    persons_per_unit = st.number_input(f'Enter number of persons required to service one {equipment_type}', min_value=1, value=2)
    hours_per_unit = st.number_input(f'Enter number of hours required to service one {equipment_type}', min_value=1.0, value=1.0)
    available_staff = st.number_input('Enter the number of available staff', min_value=1, value=10)
    working_hours_per_day = 10  # Average working hours per day
    
    # Calculate max units per day based on the inputs
    max_units_per_day = int(working_hours_per_day // hours_per_unit)
    
    # Service frequency selection
    service_frequencies = ['Monthly', 'Quarterly', '4 months once', 'Half-yearly', 'Yearly']
    service_frequency = st.selectbox('Select service frequency', service_frequencies)
    
    # Multi-select for week off days without restriction
    week_off_days = st.multiselect(
        'Select week off days',
        ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
        default=['Friday']
    )
    
    week_off_day_indices = [ ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'].index(day) for day in week_off_days ]

    # Button to generate schedule
    if st.button('Generate Schedule'):
        # Generate the schedule
        start_months = get_starting_months(service_frequency)
        full_schedule = schedule_service(year, total_units, max_units_per_day, week_off_day_indices, start_months, service_frequency, available_staff, persons_per_unit)

        # Display the schedule
        st.header(f"{equipment_type}s to be Serviced per Day")
        for date, units_list in sorted(full_schedule.items()):
            if date.weekday() in week_off_day_indices:
                st.write(f"{date}: Week off")
            elif not units_list:
                st.write(f"{date}: 0 {equipment_type}s")
            else:
                st.write(f"{date}: {len(units_list)} {equipment_type}(s) - {units_list}")

        # Display debug information
        st.subheader("Debug Information")
        st.write(f"Total {equipment_type}s: {total_units}")
        st.write(f"Max {equipment_type}s per day: {max_units_per_day}")
        st.write(f"Service Frequency: {service_frequency}")
        st.write(f"Week off days: {', '.join(week_off_days)}")
        st.write(f"No of persons required per {equipment_type}: {persons_per_unit}")
        st.write(f"No of hours required per {equipment_type}: {hours_per_unit}")
        st.write(f"Available staff: {available_staff}")

if __name__ == '__main__':
    main()
