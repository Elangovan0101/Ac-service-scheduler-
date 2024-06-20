# Service Scheduler 🌬️📅
![Service Scheduler](https://goblueox.com/wp-content/uploads/2020/06/Why-Should-I-Schedule-a-Yearly-Heating-and-Air-Conditioning-Maintenance-Visit-_-Minneapolis-MN.jpg)
## Equipment Service Scheduler

### Objective 🎯
The primary objective of this project is to create an efficient scheduling system for maintenance services of various equipment. Users can input details such as the total number of equipment units, service frequency requirements, the maximum number of services per day, the number of persons required per unit, the number of hours required per unit, available staff, and a designated weekly off day to generate a comprehensive service schedule.

### Project Details 📋

#### Key Features ✨
- **Year Selection**: Choose the year for scheduling equipment maintenance.
- **Total Units**: Enter the total number of equipment units needing service.
- **Persons per Unit**: Specify the number of persons required to service one unit.
- **Minutes per Unit**: Specify the number of minutes required to service one unit.
- **Available Staff**: Enter the number of available staff.
- **Daily Service Limit**: Automatically calculated based on available staff, persons per unit, and minutes per unit.
- **Week Off Day**: Select a weekly off day to ensure no services are scheduled on that day.
- **Service Frequency**: Select from Monthly, Quarterly, 4 months once, Half-yearly, or Yearly service intervals.
- **Working Hours Per Day**: Specify the total number of working hours per day to customize the schedule.

### Project Summary 📝

#### Project Description ℹ️
The Equipment Service Scheduler is a Streamlit application designed to streamline the scheduling of maintenance for various types of equipment. It takes user inputs for various parameters and generates a detailed schedule for servicing equipment units throughout the year, divided into appropriate intervals based on the selected service frequency.

#### Objective 🌟
The main goal is to automate the scheduling process for equipment maintenance by considering user-defined constraints and requirements, ensuring efficient and balanced workload distribution.

#### Key Project Details 🛠️
- Users can input the total number of equipment units and the number of persons required to service each unit.
- The app allows setting the number of minutes required per unit to calculate the maximum number of services per day.
- The available staff parameter ensures the scheduling is realistic and manageable.
- A specific day of the week can be set as an off day to ensure technicians have regular rest days.
- The user can define the total number of working hours per day to tailor the schedule to their needs.

### Results 📊

#### Schedule Generation 🗓️
The application generates a schedule that evenly distributes maintenance tasks throughout the year, respecting the maximum daily service limit and the specified weekly off day.

#### Example Output 📅
A typical output will show a detailed day-by-day schedule for the selected interval, indicating the number of units to be serviced each day. The app ensures no services are scheduled on the selected off day.

### Conclusion 🚀
The Equipment Service Scheduler effectively automates the planning of maintenance services, taking into account user inputs and constraints to generate an optimized schedule. This helps in better resource management and ensures timely maintenance of equipment units.

### Project Execution 📑

1. **User Input**: Collect user inputs for total units, persons per unit, minutes per unit, available staff, weekly off day, and working hours per day.
2. **Schedule Calculation**: Calculate the service schedule based on the provided inputs.
3. **Display Schedule**: Display the generated schedule in an easy-to-understand format.

### Challenges and Future Work 🛠️

- **Scalability**: Enhancing the app to handle larger datasets and more complex scheduling scenarios.
- **User Interface**: Improving the UI for better user experience and adding more customization options.

### Practical Application 🌐
This scheduler can be used by various service companies to plan their maintenance schedules efficiently, ensuring no overlap and balanced workload for their technicians.

### View Demo 📽️
You can view a live demo of the deployed app (https://service-scheduler-wisdomsoft.streamlit.app/)

### How to Run the Project 🚀

1. Clone the repository: `(https://github.com/Elangovan0101/Service-scheduler.git)`
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Run the Streamlit application with `streamlit run app.py`.
4. Open the generated URL in your web browser to use the Equipment Service Scheduler.

### License 📜
This project is licensed under the MIT License.



