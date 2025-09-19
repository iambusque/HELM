# Weekly AM Notes Collection Service

This service automatically collects Account Manager call notes and daily digests from Confluence and organizes them in the HELM vault.

## Service Overview

The Weekly AM Notes Collection Service performs the following tasks:
1. **Search** for recent call notes and daily digests from the last 7 days
2. **Collect** content from Confluence (SAL and CS spaces)
3. **Organize** notes by Account Manager in individual folders
4. **Generate** summary reports with cross-AM insights
5. **Archive** previous week's notes for historical reference

## Service Configuration

### Schedule
- **Frequency:** Weekly
- **Day:** Every Monday
- **Time:** 9:00 AM EST
- **Collection Period:** Previous 7 days (Monday to Sunday)

### Data Sources
- **Confluence Sales Space (SAL):** Call notes with pattern "AM Call Notes"
- **Confluence Client Services Space (CS):** Daily digests
- **Search Criteria:** Created or modified within the last 7 days

### Output Structure
```
HELM/AM Call Notes/
├── [AM Name]/
│   ├── Call_Notes_YYYY-MM-DD_to_YYYY-MM-DD.md
│   └── [Previous weeks archived]
├── AM_Notes_Summary_YYYY-MM-DD_to_YYYY-MM-DD.md
└── service/
    ├── weekly_collection_config.yaml
    ├── am_collection_script.py
    └── logs/
```

## Implementation Options

### Option 1: GitHub Actions (Recommended)
Create a GitHub Actions workflow that runs weekly and uses the Atlassian MCP tools.

### Option 2: Local Scheduled Task
Set up a Windows scheduled task or PowerShell script.

### Option 3: Cloud Function
Deploy as an Azure Function or AWS Lambda with scheduled trigger.

## Service Scripts

### Configuration File
```yaml
# weekly_collection_config.yaml
service:
  name: "Weekly AM Notes Collection"
  schedule: "0 9 * * 1"  # Every Monday at 9 AM
  
data_sources:
  confluence:
    base_url: "https://edocgroup.atlassian.net"
    spaces:
      - "SAL"  # Sales space for call notes
      - "CS"   # Client Services space for daily digests
    search_patterns:
      call_notes: "title ~ \"call notes\" OR title ~ \"Call Notes\""
      daily_digests: "title ~ \"Daily Digest\""
  
output:
  base_path: "c:\\Users\\andre.busque\\OneDrive - Volaris Group\\Desktop\\Palantir\\HELM\\AM Call Notes"
  archive_previous: true
  generate_summary: true
  
account_managers:
  primary_sales:
    - "Jonah Vos"
    - "Marco Wilson" 
    - "Andrew Watson"
    - "Ted Hobby"
    - "Jonathan Mann"
  regional:
    - "Nimish Bajaj"
    - "Diego Vasquez"
    - "Alex Beiza"
    - "Vinicius Beato"
    - "Nathan"
  client_services:
    - "Carmen Mazzarelli"
    - "Chris Grayson"
    - "Justin Bonnieux"
    - "Janie Snyders"
    - "James Duerksen"
    - "Owen Duckett"
    - "Sebastian Beiza"
    - "Wyatt Robinson"
    - "RPJ"
    - "Nigel Dufty"

notifications:
  enabled: true
  email: "andre.busque@helmoperations.com"
  summary_only: true
```

### Python Collection Script
```python
#!/usr/bin/env python3
"""
Weekly AM Notes Collection Service
Automatically collects and organizes Account Manager call notes from Confluence
"""

import os
import json
import yaml
from datetime import datetime, timedelta
from pathlib import Path
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('logs/am_collection.log'),
        logging.StreamHandler()
    ]
)

class AMNotesCollector:
    def __init__(self, config_path="weekly_collection_config.yaml"):
        self.config = self.load_config(config_path)
        self.base_path = Path(self.config['output']['base_path'])
        self.setup_directories()
        
    def load_config(self, config_path):
        """Load configuration from YAML file"""
        with open(config_path, 'r') as file:
            return yaml.safe_load(file)
    
    def setup_directories(self):
        """Create necessary directories"""
        self.base_path.mkdir(exist_ok=True)
        (self.base_path / "service" / "logs").mkdir(parents=True, exist_ok=True)
        
        # Create AM folders
        all_ams = (
            self.config['account_managers']['primary_sales'] +
            self.config['account_managers']['regional'] +
            self.config['account_managers']['client_services']
        )
        
        for am in all_ams:
            (self.base_path / am).mkdir(exist_ok=True)
    
    def get_date_range(self):
        """Get the date range for the previous week"""
        today = datetime.now()
        # Get last Monday
        days_since_monday = today.weekday()
        last_monday = today - timedelta(days=days_since_monday + 7)
        last_sunday = last_monday + timedelta(days=6)
        
        return last_monday.strftime("%Y-%m-%d"), last_sunday.strftime("%Y-%m-%d")
    
    def search_confluence_notes(self, start_date, end_date):
        """Search for call notes and daily digests in date range"""
        # This would use the MCP Atlassian tools
        # Implementation would call the same search functions used manually
        pass
    
    def organize_notes_by_am(self, notes_data):
        """Organize collected notes by Account Manager"""
        organized_notes = {}
        
        for note in notes_data:
            # Extract AM name from attendees or title
            am_name = self.extract_am_name(note)
            if am_name:
                if am_name not in organized_notes:
                    organized_notes[am_name] = []
                organized_notes[am_name].append(note)
        
        return organized_notes
    
    def extract_am_name(self, note):
        """Extract Account Manager name from note data"""
        # Logic to identify AM from attendees, title, or content
        # Would use the same patterns identified in manual collection
        pass
    
    def generate_am_files(self, organized_notes, start_date, end_date):
        """Generate markdown files for each AM"""
        for am_name, notes in organized_notes.items():
            if notes:
                filename = f"Call_Notes_{start_date}_to_{end_date}.md"
                filepath = self.base_path / am_name / filename
                
                content = self.format_am_notes(am_name, notes, start_date, end_date)
                
                with open(filepath, 'w', encoding='utf-8') as file:
                    file.write(content)
                
                logging.info(f"Created {filepath}")
    
    def format_am_notes(self, am_name, notes, start_date, end_date):
        """Format notes into markdown"""
        content = f"# {am_name} - Call Notes ({start_date} to {end_date})\\n\\n"
        
        for note in notes:
            content += f"## {note['title']}\\n"
            content += f"**Date:** {note['date']}\\n"
            content += f"**Attendees:** {note.get('attendees', 'N/A')}\\n\\n"
            content += note.get('content', '') + "\\n\\n---\\n\\n"
        
        return content
    
    def generate_summary_report(self, organized_notes, start_date, end_date):
        """Generate cross-AM summary report"""
        filename = f"AM_Notes_Summary_{start_date}_to_{end_date}.md"
        filepath = self.base_path / filename
        
        # Generate summary using same logic as manual process
        # Include key themes, action items, and cross-AM insights
        pass
    
    def archive_previous_week(self):
        """Archive previous week's files if enabled"""
        if self.config['output']['archive_previous']:
            # Move or rename previous week's files
            pass
    
    def send_notification(self, summary_data):
        """Send completion notification"""
        if self.config['notifications']['enabled']:
            # Send email summary
            pass
    
    def run_collection(self):
        """Main collection process"""
        try:
            logging.info("Starting weekly AM notes collection")
            
            start_date, end_date = self.get_date_range()
            logging.info(f"Collecting notes for period: {start_date} to {end_date}")
            
            # Archive previous week if enabled
            self.archive_previous_week()
            
            # Search for notes
            notes_data = self.search_confluence_notes(start_date, end_date)
            logging.info(f"Found {len(notes_data)} notes")
            
            # Organize by AM
            organized_notes = self.organize_notes_by_am(notes_data)
            
            # Generate AM files
            self.generate_am_files(organized_notes, start_date, end_date)
            
            # Generate summary
            self.generate_summary_report(organized_notes, start_date, end_date)
            
            # Send notification
            self.send_notification(organized_notes)
            
            logging.info("Weekly collection completed successfully")
            
        except Exception as e:
            logging.error(f"Collection failed: {str(e)}")
            raise

if __name__ == "__main__":
    collector = AMNotesCollector()
    collector.run_collection()
```

### GitHub Actions Workflow
```yaml
# .github/workflows/weekly-am-notes.yml
name: Weekly AM Notes Collection

on:
  schedule:
    - cron: '0 9 * * 1'  # Every Monday at 9 AM UTC
  workflow_dispatch:  # Allow manual trigger

jobs:
  collect-notes:
    runs-on: ubuntu-latest
    
    steps:
    - name: Checkout repository
      uses: actions/checkout@v3
    
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.9'
    
    - name: Install dependencies
      run: |
        pip install pyyaml requests python-dateutil
    
    - name: Run AM Notes Collection
      env:
        CONFLUENCE_TOKEN: ${{ secrets.CONFLUENCE_TOKEN }}
        CONFLUENCE_EMAIL: ${{ secrets.CONFLUENCE_EMAIL }}
      run: |
        python service/am_collection_script.py
    
    - name: Commit and push changes
      run: |
        git config --local user.email "action@github.com"
        git config --local user.name "GitHub Action"
        git add "AM Call Notes/"
        git commit -m "Weekly AM notes collection $(date +'%Y-%m-%d')" || exit 0
        git push
```

### PowerShell Scheduled Task Script
```powershell
# weekly_am_collection.ps1
param(
    [string]$ConfigPath = "weekly_collection_config.yaml"
)

# Set execution policy for script
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser -Force

# Load configuration
$config = Get-Content $ConfigPath | ConvertFrom-Yaml

# Log function
function Write-Log {
    param([string]$Message)
    $timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    Write-Host "[$timestamp] $Message"
    Add-Content -Path "service/logs/am_collection.log" -Value "[$timestamp] $Message"
}

# Main collection function
function Invoke-AMNotesCollection {
    try {
        Write-Log "Starting weekly AM notes collection"
        
        # Calculate date range
        $today = Get-Date
        $lastMonday = $today.AddDays(-(7 + $today.DayOfWeek.value__))
        $lastSunday = $lastMonday.AddDays(6)
        
        $startDate = $lastMonday.ToString("yyyy-MM-dd")
        $endDate = $lastSunday.ToString("yyyy-MM-dd")
        
        Write-Log "Collecting notes for period: $startDate to $endDate"
        
        # Call the Python script or implement PowerShell MCP calls
        python service/am_collection_script.py
        
        Write-Log "Collection completed successfully"
        
    } catch {
        Write-Log "Collection failed: $($_.Exception.Message)"
        throw
    }
}

# Run the collection
Invoke-AMNotesCollection
```

## Setup Instructions

### 1. Choose Implementation Method
- **GitHub Actions:** Best for automated, cloud-based execution
- **Local Scheduled Task:** Best for local control and immediate setup
- **Cloud Function:** Best for enterprise integration

### 2. Configure Authentication
- Set up Confluence API tokens
- Configure access permissions for MCP tools
- Set up notification email credentials

### 3. Install and Test
- Deploy the chosen solution
- Run initial test collection
- Verify output format and organization

### 4. Monitor and Maintain
- Check logs for successful runs
- Update AM lists as team changes
- Adjust search patterns as needed

## Benefits

### Automation
- ✅ **Consistent Collection:** Never miss weekly summaries
- ✅ **Time Savings:** Eliminates manual collection process
- ✅ **Standardized Format:** Consistent organization and formatting

### Organization
- ✅ **Historical Archive:** Maintains weekly records automatically
- ✅ **Cross-AM Insights:** Identifies patterns and themes
- ✅ **Action Item Tracking:** Surfaces follow-ups and blockers

### Integration
- ✅ **HELM Vault Sync:** Direct integration with Obsidian workflow
- ✅ **Notification System:** Email summaries of weekly activity
- ✅ **Scalable Design:** Easy to add new AMs or data sources

## Maintenance

### Weekly Tasks
- Review generated summaries for accuracy
- Follow up on action items identified
- Update customer mappings as needed

### Monthly Tasks
- Review service logs for issues
- Update AM lists for team changes
- Optimize search patterns based on usage

### Quarterly Tasks
- Archive older notes to reduce file size
- Review service performance and optimization
- Update notification preferences

---

**Service Status:** Ready for Implementation  
**Recommended Start:** Next Monday (September 23, 2025)  
**Estimated Setup Time:** 2-4 hours depending on chosen method