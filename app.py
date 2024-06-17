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

def schedule_quarter(year, total_acs, quarterly_acs, max_ac_per_day, week_off_day, start_month):
    schedule = defaultdict(list)
    ac_index = 0
    current_date = datetime.date(year, start_month, 1)
    days_in_current_month = days_in_month(year, start_month)
    
    while current_date.weekday() == week_off_day:
        current_date += datetime.timedelta(days=1)
    
    for day in range(1, days_in_current_month + 1):
        if current_date.weekday() != week_off_day: 
            acs_to_service_today = []
            for _ in range(max_ac_per_day):
                ac_index += 1
                if ac_index > total_acs:
                    break
                acs_to_service_today.append(ac_index)
                if len(acs_to_service_today) == quarterly_acs:
                    break
            schedule[current_date] = acs_to_service_today
        current_date += datetime.timedelta(days=1)
    
    return schedule

def main():
    st.title('AC Service Scheduler')
  
    st.image("logo.jpg", width=150)

 
    year = st.number_input('Enter the year', min_value=2022, max_value=2100, value=2025)
    total_acs = st.number_input('Enter total number of ACs', min_value=1, value=50)
    quarterly_acs = st.number_input('Enter number of ACs requiring quarterly service', min_value=1, value=50)
    max_ac_per_day = st.number_input('Enter max ACs serviced per day', min_value=1, value=20)
    week_off_day = st.selectbox('Select the week off day', ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'], index=4)

    week_off_day_index = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'].index(week_off_day)
    
    if st.button('Generate Schedule'):
    
        quarters = [1, 4, 7, 10]
        full_schedule = defaultdict(list)

        for month in quarters:
            quarter_schedule = schedule_quarter(year, total_acs, quarterly_acs, max_ac_per_day, week_off_day_index, month)
            for key, value in quarter_schedule.items():
                full_schedule[key].extend(value)

        
        st.header("ACs to be Serviced per Day")
        for date, acs_list in sorted(full_schedule.items()):
            if not acs_list:
                st.write(f"{date}: 0 ACs")
            else:
                st.write(f"{date}: {len(acs_list)} ACs - {acs_list}")

        
        st.subheader("Debug Information")
        st.write(f"Total ACs: {total_acs}")
        st.write(f"Quarterly ACs: {quarterly_acs}")
        st.write(f"Max ACs per day: {max_ac_per_day}")
        st.write(f"Week off day: {week_off_day}")

if __name__ == '__main__':
    main()
