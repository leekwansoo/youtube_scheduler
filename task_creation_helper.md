# Windows Scheduled Task Creation Guide

## Overview
This document outlines the complete process of creating a Windows scheduled task to automatically run a Streamlit application (`app.py`) daily at 10:40 AM from the `youtube_scheduler` folder.

## Initial Requirements
- **Task Name**: YouTube_Scheduler
- **Schedule**: Daily at 10:40 AM
- **Action**: Run `streamlit run app.py` from `C:\Users\SCLuser\Desktop\youtube_scheduler`
- **Environment**: Python virtual environment (`venv`)

## Challenges Encountered

### 1. Direct schtasks Command Issues
**Problem**: Complex escaping and parsing issues when trying to use `schtasks` directly with embedded commands.

**Failed Attempts**:
```cmd
schtasks /create /tn "YouTube_Scheduler" /tr "cmd /c \"cd /d C:\Users\SCLuser\Desktop\youtube_scheduler && streamlit run app.py\"" /sc daily /st 10:40 /f
```

**Error**: Syntax parsing issues and unexpected token errors in PowerShell.

### 2. Virtual Environment Requirement
**Discovery**: The application requires activation of a Python virtual environment before running Streamlit.

## Solution Process

### Step 1: Create Batch File Helper
Created `start_scheduler.bat` to handle the complex command sequence:

```batch
@echo off
cd /d "C:\Users\SCLuser\Desktop\youtube_scheduler"
call venv\Scripts\activate
streamlit run app.py
```

**Benefits**:
- Simplifies the scheduled task command
- Handles directory navigation
- Activates virtual environment properly
- Avoids command escaping issues

### Step 2: Use PowerShell Instead of schtasks
**Solution**: Used PowerShell `Register-ScheduledTask` cmdlet instead of `schtasks.exe`

**Working Command**:
```powershell
Register-ScheduledTask -TaskName "YouTube_Scheduler" -Trigger (New-ScheduledTaskTrigger -Daily -At "10:40AM") -Action (New-ScheduledTaskAction -Execute "C:\Users\SCLuser\Desktop\youtube_scheduler\start_scheduler.bat") -Force
```

## Final Implementation

### Files Created

#### 1. Batch File: `start_scheduler.bat`
```batch
@echo off
cd /d "C:\Users\SCLuser\Desktop\youtube_scheduler"
call venv\Scripts\activate
streamlit run app.py
```

#### 2. Scheduled Task: `YouTube_Scheduler`
- **Trigger**: Daily at 10:40 AM
- **Action**: Execute the batch file
- **Status**: Ready
- **Next Run**: Daily at 10:40 AM

## Task Management Commands

### PowerShell Task Management
```powershell
# Check task status
Get-ScheduledTask -TaskName "YouTube_Scheduler"

# Get detailed task information
Get-ScheduledTask -TaskName "YouTube_Scheduler" | Get-ScheduledTaskInfo

# Run task manually (for testing)
Start-ScheduledTask -TaskName "YouTube_Scheduler"

# Disable task
Disable-ScheduledTask -TaskName "YouTube_Scheduler"

# Enable task
Enable-ScheduledTask -TaskName "YouTube_Scheduler"

# Delete task
Unregister-ScheduledTask -TaskName "YouTube_Scheduler" -Confirm:$false

# View task configuration details
Get-ScheduledTask -TaskName "YouTube_Scheduler" | Select-Object TaskName, State, @{Name="Triggers";Expression={$_.Triggers}}, @{Name="Actions";Expression={$_.Actions}}
```

### Traditional schtasks Commands (Alternative)
```cmd
# Query task
schtasks /query /tn "YouTube_Scheduler"

# Run task manually
schtasks /run /tn "YouTube_Scheduler"

# Delete task
schtasks /delete /tn "YouTube_Scheduler" /f
```

## Verification Process

After creation, we verified the task using:

1. **Task Information Query**:
```powershell
Get-ScheduledTask -TaskName "YouTube_Scheduler" | Get-ScheduledTaskInfo
```

**Output**:
```
LastRunTime        : 1999/11/30 오전 12:00:00
LastTaskResult     : 267011
NextRunTime        : 2026/02/09 오전 10:40:00
NumberOfMissedRuns : 0
TaskName           : YouTube_Scheduler
TaskPath           : \
```

2. **Task Configuration Check**:
```powershell
Get-ScheduledTask -TaskName "YouTube_Scheduler" | Select-Object TaskName, State, @{Name="Triggers";Expression={$_.Triggers}}, @{Name="Actions";Expression={$_.Actions}}
```

**Output**:
```
TaskName          State Triggers              Actions
--------          ----- --------              -------
YouTube_Scheduler Ready MSFT_TaskDailyTrigger MSFT_TaskExecAction
```

## Key Learnings

### 1. PowerShell vs schtasks
- **PowerShell**: More reliable for complex scenarios, better object handling
- **schtasks**: Good for simple cases, but command escaping can be problematic

### 2. Batch File Approach
- **Advantages**: Simplifies task creation, handles environment setup, easier to debug
- **Best Practice**: Use batch files for multi-step operations in scheduled tasks

### 3. Virtual Environment Handling
- **Critical**: Always activate virtual environment before running Python applications
- **Method**: Use `call venv\Scripts\activate` in batch files

### 4. Testing Strategy
- **Manual Testing**: Use `Start-ScheduledTask` to test without waiting for schedule
- **Verification**: Always check `Get-ScheduledTaskInfo` for next run time
- **Logs**: Monitor Windows Event Viewer for task execution results

## Troubleshooting Tips

### Common Issues
1. **Task doesn't run**: Check user permissions and execution policy
2. **Python not found**: Ensure virtual environment activation is working
3. **Path issues**: Use absolute paths in batch files
4. **Permission denied**: Run PowerShell as Administrator when creating tasks

### Debug Steps
1. Test batch file manually first
2. Check task history in Task Scheduler GUI
3. Verify file paths and permissions
4. Review Windows Event Logs

## Future Modifications

To modify the schedule or action:

### Change Schedule Time
```powershell
# Remove existing task
Unregister-ScheduledTask -TaskName "YouTube_Scheduler" -Confirm:$false

# Create with new time (e.g., 9:30 AM)
Register-ScheduledTask -TaskName "YouTube_Scheduler" -Trigger (New-ScheduledTaskTrigger -Daily -At "9:30AM") -Action (New-ScheduledTaskAction -Execute "C:\Users\SCLuser\Desktop\youtube_scheduler\start_scheduler.bat") -Force
```

### Update Batch File
Simply edit `start_scheduler.bat` to change the application behavior without recreating the scheduled task.

---

## Summary
This process demonstrates the importance of using appropriate tools for the task. While `schtasks` is powerful, PowerShell's `Register-ScheduledTask` provides better reliability for complex scenarios. The batch file approach abstracts the complexity and makes the solution more maintainable.