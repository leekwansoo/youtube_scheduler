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
"C:\Users\SCLuser\Desktop\Streamlit.lnk"

## Setting Task Scheduler for "Youtube_Scheduler"

step 1. Create icon for "Youtube_Scheduler"
step 2. Create a batchfile "youtube_launcher.bat"
@echo off
"C:\Program Files\Google\Chrome\Application\chrome_proxy.exe" --profile-directory="Default" --ignore-profile-directory-if-not-exists https://youtubepalyer-5ytbbeqqwzsatlgrine6mv.streamlit.app/

step 3. Create schtasks with the "youtube_launcher.bat"
schtasks /create /tn "Youtube_Scheduler" /tr "C:\Users\SCLuser\Desktop\youtube_scheduler\youtube_launcher.bat" /sc once /st 10:45