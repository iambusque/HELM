# Weekly AM Notes Collection - PowerShell Setup

param(
    [string]$ConfigPath = "service\weekly_collection_config.yaml",
    [switch]$TestRun,
    [switch]$SetupSchedule,
    [switch]$InstallDependencies
)

# Set execution policy for script
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser -Force

# Function to write timestamped logs
function Write-Log {
    param(
        [string]$Message,
        [string]$Level = "INFO"
    )
    $timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    $logMessage = "[$timestamp] [$Level] $Message"
    Write-Host $logMessage
    
    # Ensure log directory exists
    $logDir = "service\logs"
    if (-not (Test-Path $logDir)) {
        New-Item -ItemType Directory -Path $logDir -Force | Out-Null
    }
    
    Add-Content -Path "$logDir\am_collection.log" -Value $logMessage
}

# Function to install Python dependencies
function Install-Dependencies {
    Write-Log "Installing Python dependencies..."
    
    # Check if Python is installed
    try {
        $pythonVersion = python --version 2>&1
        Write-Log "Found Python: $pythonVersion"
    } catch {
        Write-Log "Python not found. Please install Python 3.9+ first." "ERROR"
        exit 1
    }
    
    # Install required packages
    $packages = @("pyyaml", "requests", "python-dateutil")
    
    foreach ($package in $packages) {
        Write-Log "Installing $package..."
        pip install $package
        if ($LASTEXITCODE -ne 0) {
            Write-Log "Failed to install $package" "ERROR"
            exit 1
        }
    }
    
    Write-Log "Dependencies installed successfully"
}

# Function to test the collection script
function Test-Collection {
    Write-Log "Running test collection..."
    
    try {
        # Run the Python script in test mode
        python service\am_collection_script.py
        
        if ($LASTEXITCODE -eq 0) {
            Write-Log "Test collection completed successfully"
        } else {
            Write-Log "Test collection failed with exit code $LASTEXITCODE" "ERROR"
        }
    } catch {
        Write-Log "Error running test collection: $($_.Exception.Message)" "ERROR"
    }
}

# Function to set up Windows scheduled task
function Setup-ScheduledTask {
    Write-Log "Setting up Windows scheduled task..."
    
    $taskName = "Weekly-AM-Notes-Collection"
    $scriptPath = (Get-Location).Path + "\weekly_am_collection.ps1"
    
    # Remove existing task if it exists
    try {
        Unregister-ScheduledTask -TaskName $taskName -Confirm:$false -ErrorAction SilentlyContinue
        Write-Log "Removed existing scheduled task"
    } catch {
        # Task doesn't exist, continue
    }
    
    # Create new scheduled task
    $action = New-ScheduledTaskAction -Execute "PowerShell.exe" -Argument "-File `"$scriptPath`""
    
    # Set trigger for every Monday at 9 AM
    $trigger = New-ScheduledTaskTrigger -Weekly -DaysOfWeek Monday -At "09:00"
    
    # Set settings
    $settings = New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries -StartWhenAvailable
    
    # Set principal (run as current user)
    $principal = New-ScheduledTaskPrincipal -UserId $env:USERNAME -LogonType S4U
    
    # Register the task
    try {
        Register-ScheduledTask -TaskName $taskName -Action $action -Trigger $trigger -Settings $settings -Principal $principal -Description "Weekly collection of Account Manager call notes from Confluence"
        Write-Log "Scheduled task '$taskName' created successfully"
        Write-Log "Task will run every Monday at 9:00 AM"
    } catch {
        Write-Log "Failed to create scheduled task: $($_.Exception.Message)" "ERROR"
        exit 1
    }
}

# Main collection function
function Invoke-AMNotesCollection {
    Write-Log "Starting weekly AM notes collection"
    
    try {
        # Check if config file exists
        if (-not (Test-Path $ConfigPath)) {
            Write-Log "Configuration file not found: $ConfigPath" "ERROR"
            exit 1
        }
        
        # Calculate date range for previous week
        $today = Get-Date
        $lastMonday = $today.AddDays(-(7 + [int]$today.DayOfWeek))
        $lastSunday = $lastMonday.AddDays(6)
        
        $startDate = $lastMonday.ToString("yyyy-MM-dd")
        $endDate = $lastSunday.ToString("yyyy-MM-dd")
        
        Write-Log "Collecting notes for period: $startDate to $endDate"
        
        # Set environment variables for the Python script
        $env:COLLECTION_START_DATE = $startDate
        $env:COLLECTION_END_DATE = $endDate
        $env:CONFIG_PATH = $ConfigPath
        
        # Run the Python collection script
        python service\am_collection_script.py
        
        if ($LASTEXITCODE -eq 0) {
            Write-Log "Collection completed successfully"
            
            # Optional: Open the generated summary file
            $summaryFile = "AM Call Notes\AM_Notes_Summary_${startDate}_to_${endDate}.md"
            if (Test-Path $summaryFile) {
                Write-Log "Summary file generated: $summaryFile"
                # Uncomment to automatically open the summary
                # Start-Process $summaryFile
            }
        } else {
            Write-Log "Collection failed with exit code $LASTEXITCODE" "ERROR"
            exit 1
        }
        
    } catch {
        Write-Log "Collection failed: $($_.Exception.Message)" "ERROR"
        throw
    }
}

# Main script logic
try {
    Write-Log "Weekly AM Notes Collection PowerShell Script"
    Write-Log "Working directory: $(Get-Location)"
    
    # Handle command line options
    if ($InstallDependencies) {
        Install-Dependencies
        exit 0
    }
    
    if ($SetupSchedule) {
        Setup-ScheduledTask
        exit 0
    }
    
    if ($TestRun) {
        Test-Collection
        exit 0
    }
    
    # Run normal collection
    Invoke-AMNotesCollection
    
} catch {
    Write-Log "Script failed: $($_.Exception.Message)" "ERROR"
    exit 1
}

Write-Log "Script completed successfully"