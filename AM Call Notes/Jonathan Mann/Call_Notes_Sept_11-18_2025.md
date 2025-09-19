# Jonathan Mann - Call Notes (Sept 11-18, 2025)

## 2025-09-16 AM Call Notes - Scripps Institution of Oceanography (SIO) - Demo
**Date:** September 16, 2025  
**Attendees:** Jonathan Mann, Paul Cyr, Joost Van Der Zwaag, Faye Shitu, Jessica Nakashima, Anthony Taienao, Camilla King  

### Customer Interest Areas
Scripps Institution of Oceanography (SIO) is interested in:
- **Timesheets**
- **Work Rest**
- **Payroll**

### Current Process & Challenges

#### Manual Overtime Tracking
- Taking overtime documents manually
- Manually entering this into excel to track timesheets & hours logs
- Currently using a different payroll system that combines the excel sheets
- Would like to be tracking rest hours (Work Rest) - currently using watch-keepers to track
- Want to look at combine their systems to ensure the checks & balances have been finished off

#### Current Payroll Management Issues
- Each time payroll runs, they go to Helm Connect to run a report based on the crew schedule for the payroll period
- Trying to figure out if the crew is actively working on-board, mainly to track the overtime of crew
- Captain provides a single spreadsheet for each crew member who worked overtime hours for each week
- Captains do not provide the overtime sheets until over the weekend, and staff must work over the weekend to collect the information to then be migrated into the payroll system
- They're currently running against the clock to get the information before the payroll period ends
- Would like to have an easier system to track their daily hours for the crew & over-time, including the pay adjustments, and annual leave accumulations
- Issue with current online timesheets system creating issues for crew who are out at sea & unable to connect to the system

### Next Steps
- **Set-up a Sandbox copy** of the Scripps prod site data for new module trials - Jira Ticket Created
- **Payroll configuration tutorial** with Anthony & Jessica
- **Trial run** of Timesheets & Work Rest
- **Scripps to send out** their google sheets with more info around their current process & data layout they use for Payroll & Payroll codes

---

## 2025-09-15 AM Call Notes - Hullo Ferries - Implementation Training
**Date:** September 15, 2025  
**Attendees:** Jonathan Mann, Janie Snyders, Steven Carrol, Kelly Kur, Derek Lewis, Barry Andrews, Amarjit Dhariwal  

### Key Issues & Solutions

#### SAML Sign-in Issues
- Creating issues for Helm Team
- Helm Team needs accounts updated for logins without Hullo Outlook logins
- Currently unable to de-select SAML logins for helm team users
- **Solution:** Added Kelly as an Admin to change set-up users

#### Hullo Engine Hours Reporting
- Uses live engine reporting technology
- Would like to have an API that could auto populate the engine readings into Helm CONNECT

#### Hullo Logbook Trial
- During an on-site from Isaac, he mentioned they could trial logbook
- Hullo would like to know if Logbook is compliant with Transport Canada
- Thinks it is something they can look at in the future but is not the current focus of their implementation

#### Hullo SharePoint Issues
- Having issues with documents on SharePoint
- Looking forward to swapping to Helm Documents as currently having issues with people using older forms/documents in SharePoint rather than the most up-to-date version

### Feature Improvement Requests

#### Missing Feature in Document Folder
- **Issue:** Under Set-up < Compliance < Document Folders - No options to delete line item once this has been added in

#### Potential Quick Win - Template Categories
- **Location:** Set-up > Operations > Template Categories
- **Issue:** Limitation for 14 characters in the title box of the template categories
- **Suggestion:** Potential quick win to extend amount of characters allowed in title

---

## 2025-09-11 Uncruise Bi-Weekly Call Notes
**Date:** September 10, 2025  
**Attendees:** Jonah Vos, Jonathan Mann, Flynn  

### Key Discussion Points

#### Attached Assets Components
- Not available right now, but we hope to have this in 2026
- Ideally this would be ready for them by the time their season starts up in Feb/March, but that is unlikely
- **Workaround:** List the lifeboats as components and then the maintenance will be tracked on the boats
- **Main concern:** What happens when the lifeboats move to another vessel?
- If I deactivate a lifeboat on one vessel and move it to another > replace the lifeboat on vessel B with the one from Vessel A, does the maintenance history and template schedule move with it?
- If it doesn't then this would not really work for them as the maintenance needs to go with the lifeboat

### Next Steps:
- Send a video of how components work
- Send a video of certs 2.0 so Flynn can distribute it