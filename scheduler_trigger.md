## Create a trigger to start app every day using schtasks 

## Create tasks  

schtasks /create /tn "Task_Name" /tr "task_resource_path" /sc daily /st 10:40 /f

### Example

schtasks /create /tn "YouTube_Scheduler" /tr "C:\Users\SCLuser\Desktop\youtube_scheduler\start_scheduler.bat" /sc daily /st 10:40 /f

### start_scheduler.bat (The tasks is running in the virtual environment)

@echo off
cd /d "C:\Users\SCLuser\Desktop\youtube_scheduler"
call venv\Scripts\activate
streamlit run app.py

This batch file ensures that:

It changes to the correct directory
Activates your virtual environment (venv) first
Then runs the Streamlit application

## Query tasks

schtasks /query /tn "Task_Name"

### Example

schtasks /query /tn "Youtube_Scheduler"

### For Detail Information

schtasks /query /tn "Youtube_Scheduler" /fo list /v

## Delete tasks  

schtasks /delete /tn "Youtube_Scheduler" /f