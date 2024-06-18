# AC Service Scheduler 🌬️📅

![AC Service Scheduler](https://media.istockphoto.com/id/1267057581/photo/a-repairman-checking-the-air-conditioner.jpg?s=612x612&w=0&k=20&c=jsx63zh_etUL0QALeDZNLeE6yIA3bA2xqsv-bRtFBXM=)

## Objective 🎯
The primary objective of this project is to create an efficient scheduling system for air conditioner (AC) maintenance services. Users can input details such as the total number of AC units, quarterly service requirements, the maximum number of services per day, and a designated weekly off day to generate a comprehensive service schedule.

## Project Details 📋

### Key Features ✨
- **Year Selection**: Choose the year for scheduling AC maintenance.
- **Total AC Units**: Enter the total number of AC units needing service.
- **Quarterly Service**: Specify the number of AC units that require quarterly maintenance.
- **Daily Service Limit**: Define the maximum number of AC units that can be serviced per day.
- **Week Off Day**: Select a weekly off day to ensure no services are scheduled on that day.

## Project Summary 📝
### Project Description ℹ️
The AC Service Scheduler is a Streamlit application designed to streamline the scheduling of AC maintenance. It takes user inputs for various parameters and generates a detailed schedule for servicing AC units throughout the year, divided into four quarters.

### Objective 🌟
The main goal is to automate the scheduling process for AC maintenance by considering user-defined constraints and requirements, ensuring efficient and balanced workload distribution.

### Key Project Details 🛠️
- Users can input the total number of AC units and the number of units requiring quarterly service.
- The app allows setting a maximum number of services per day to avoid overloading the technicians.
- A specific day of the week can be set as an off day to ensure technicians have regular rest days.

## Results 📊
### Schedule Generation 🗓️
The application generates a schedule that evenly distributes AC maintenance tasks throughout the year, respecting the maximum daily service limit and the specified weekly off day.

### Example Output 📅
A typical output will show a detailed day-by-day schedule for each quarter, indicating the number of AC units to be serviced each day. The app ensures no services are scheduled on the selected off day.

## Conclusion 🚀
The AC Service Scheduler effectively automates the planning of AC maintenance services, taking into account user inputs and constraints to generate an optimized schedule. This helps in better resource management and ensures timely maintenance of AC units.

#### Project Execution 📑
1. **User Input**: Collect user inputs for total AC units, quarterly service requirements, daily service limit, and weekly off day.
2. **Schedule Calculation**: Calculate the service schedule based on the provided inputs.
3. **Display Schedule**: Display the generated schedule in an easy-to-understand format.

#### Challenges and Future Work 🛠️
- **Scalability**: Enhancing the app to handle larger datasets and more complex scheduling scenarios.
- **User Interface**: Improving the UI for better user experience and adding more customization options.

#### Practical Application 🌐
This scheduler can be used by HVAC companies to plan their maintenance schedules efficiently, ensuring no overlap and balanced workload for their technicians.

## How to Run the Project 🚀
1. Clone the repository. https://github.com/Elangovan0101/Ac-service-scheduler-.git
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Run the Streamlit application with `streamlit run app.py`.
4. Open the generated URL in your web browser to use the AC Service Scheduler.

## License 📜
This project is licensed under the MIT License.
