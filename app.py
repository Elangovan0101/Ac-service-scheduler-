import streamlit as st
import datetime
from collections import defaultdict

def days_in_month(year, month):
    if month == 12:
        next_year = year + 1
        next_month = 1
    else:
        next_year = year
        next_month = month + 1
    last_day_of_month = datetime.date(next_year, next_month, 1) - datetime.timedelta(days=1)
    return last_day_of_month.day

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

def add_months(source_date, months):
    month = source_date.month - 1 + months
    year = source_date.year + month // 12
    month = month % 12 + 1
    day = min(source_date.day, days_in_month(year, month))
    return datetime.date(year, month, day)

def schedule_service(year, total_units, max_units_per_day, week_off_days, start_months, service_frequency, yearly_off_days):
    schedule = defaultdict(list)
    unit_index = 0

    for start_month in start_months:
        current_date = datetime.date(year, start_month, 1)
        days_in_current_month = days_in_month(year, start_month)
        
        while current_date.weekday() in week_off_days:
            current_date += datetime.timedelta(days=1)
        
        for day in range(1, days_in_current_month + 1):
            if current_date.weekday() not in week_off_days:
                if current_date.day in yearly_off_days:
                    schedule[current_date].append("Yearly off")
                else:
                    units_to_service_today = []
                    for _ in range(max_units_per_day):
                        unit_index += 1
                        if unit_index > total_units:
                            break
                        units_to_service_today.append(unit_index)
                    schedule[current_date].extend(units_to_service_today)
                    if unit_index >= total_units:
                        break
            current_date += datetime.timedelta(days=1)
    
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
                next_service_date = add_months(date, i * months_increment)
                if next_service_date.year == year:
                    additional_schedule[next_service_date].extend(current_units)
    else:
        for date in list(schedule.keys()):
            current_units = schedule[date]
            next_date = date
            while next_date.year == year:
                next_date = add_months(next_date, 1)
                if next_date.year == year:
                    additional_schedule[next_date].extend(current_units)
    
    schedule.update(additional_schedule)

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

    st.image("logo.jpg", width=150)
    
    equipment_types = ['Split AC', 'PACKAGE UNIT AC', 'Pest Control']
    equipment_type = st.selectbox('Select type of equipment/service', equipment_types)
    
    year = st.number_input('Enter the year', min_value=2022, max_value=2100, value=2025)
    total_units = st.number_input(f'Enter total number of {equipment_type}s', min_value=1, value=50)
    persons_per_unit = st.number_input('Enter number of persons required to service one unit', min_value=1, value=2)
    minutes_per_unit = st.number_input('Enter number of minutes required for one unit', min_value=1, value=60)
    available_staff = st.number_input('Enter the number of available staff', min_value=1, value=10)
    working_hours_per_day = st.number_input('Enter the number of working hours per day', min_value=1, max_value=24, value=10)
    
    total_working_minutes = working_hours_per_day * 60
    
    max_units_per_day = (available_staff * total_working_minutes) // (persons_per_unit * minutes_per_unit)
    
    service_frequencies = ['Monthly', 'Quarterly', '4 months once', 'Half-yearly', 'Yearly']
    service_frequency = st.selectbox('Select service frequency', service_frequencies)
    
    week_off_days = st.multiselect(
        'Select week off days',
        ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
        default=['Friday']
    )
    
    week_off_day_indices = [ ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'].index(day) for day in week_off_days ]

    yearly_off_days = []
    st.subheader("Yearly Off Days")
    default_calendar_year = 2025
    if service_frequency == 'Monthly' or service_frequency == 'Yearly':
        for month in range(1, 13):
            if st.checkbox(f"Select yearly off day for Month {month}"):
                off_day = st.date_input(f"Choose a date for Month {month}", datetime.date(default_calendar_year, month, 1))
                yearly_off_days.append(off_day.day)
    else:
        if service_frequency == 'Quarterly':
            for quarter in range(1, 5):
                if st.checkbox(f"Select yearly off day for Quarter {quarter}"):
                    off_day = st.date_input(f"Choose a date for Quarter {quarter}", datetime.date(default_calendar_year, 3 * (quarter - 1) + 1, 1))
                    yearly_off_days.append(off_day.day)

        elif service_frequency == '4 months once':
            for four_months in range(1, 5):
                if st.checkbox(f"Select yearly off day for 4 months {four_months}"):
                    off_day = st.date_input(f"Choose a date for 4 months {four_months}", datetime.date(default_calendar_year, 4 * (four_months - 1) + 1, 1))
                    yearly_off_days.append(off_day.day)

        elif service_frequency == 'Half-yearly':
            for half_year in range(1, 3):
                if st.checkbox(f"Select yearly off day for Half-year {half_year}"):
                    off_day = st.date_input(f"Choose a date for Half-year {half_year}", datetime.date(default_calendar_year, 6 * (half_year - 1) + 1, 1))
                    yearly_off_days.append(off_day.day)

    if st.button('Generate Schedule'):
        start_months = get_starting_months(service_frequency)
        full_schedule = schedule_service(year, total_units, max_units_per_day, week_off_day_indices, start_months, service_frequency, yearly_off_days)
        st.header(f"{equipment_type}s to be Serviced per Day")
        for date, units_list in sorted(full_schedule.items()):
            if date.weekday() in week_off_day_indices:
                st.write(f"{date}: Week off")
            elif "Yearly off" in units_list:
                st.write(f"{date}: Yearly off")
            elif not units_list:
                st.write(f"{date}: 0 {equipment_type}s")
            else:
                st.write(f"{date}: {len(units_list)} {equipment_type}(s) - {units_list}")

        st.subheader("Debug Information")
        st.write(f"Total {equipment_type}s: {total_units}")
        st.write(f"Max {equipment_type}s per day: {max_units_per_day}")
        st.write(f"Service Frequency: {service_frequency}")
        st.write(f"Week off days: {', '.join(week_off_days)}")
        if yearly_off_days:
            st.write(f"Yearly off days: {', '.join(str(day) for day in yearly_off_days)}")

if __name__ == '__main__':
    main()
