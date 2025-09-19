# Jonah Vos - Call Notes (Sept 11-18, 2025)

## 2025-09-18 TBS Weekly Call Notes
**Date:** September 18, 2025  
**Attendees:** Nate, Nigel, Erica, Ted Hobby, Jonah Vos  

### Key Discussion Points:

#### 1.33+ Release
- 1.33 is now closed
- 1.33+ will be launched this week
- TBS will be informed about when it is being released

#### Cargo and Fluid Tracking
- Going back and forth on getting the internal documentation
- Need to clarify end goal for API documentation and access
- Goal: Crew to record fluid readings in templates, then post to Cargo/fluid events in logbook to avoid double entry
- **Next Steps:** Sort this out with both TBS and development

#### Certifications
- TBS is testing out an LMS for posting videos and customer access to renew certifications within Helm
- Nate wondering about API endpoint for certs 2.0 and LMS integration with "Talent LMS"
- Different from current Moxie integration - they want to update certification + personnel record for video training completion
- **Next Steps:** Figure out when the certs 2.0 endpoint will be available

#### Dashboards
- 41 north demo today
- Another demo with brown water this week (initial conversation)

#### Sales and Churn Channel
- Working on form to deploy to customers for change requests to their subscription
- Process plan for week after helm conference to go live with slack channel integration
- **Next Steps:** Nate will work on this after HC25

---

## 2025-09-11 Hornblower Weekly Call Notes
**Date:** September 10, 2025  
**Attendees:** Jonah Vos, Craig Parkhurst  

### Key Discussion Points:

#### Inventory Import
- Completed
- **Next Steps:** Craig to inform the cities of their responsibilities

#### Scripts in Production
- Review alcatraz, canada, Europe, statue for activities field
- Numbers field is good to go
- **Next Steps:** Numbers field script to go September 11, wait for NYCF approval for activity script

#### Documents Beta
- Issue: When you have a note on a document, it shows the number but is cut off by the grid line above
- Good to go in 1.34
- **Next Steps:** Relay feedback about the notes and attachment icon

#### Invoices
- Have the drafts ready, just need to review before sending over
- **Next Steps:** Review draft invoices Karen has sent

#### Fleet Wide Campaign - Fluid Analysis Integration
- October launch, expanding the API integration
- Currently requires a lot of work on every template
- Fleet-wide with Polaris Labs
- **Next Steps:** Likely some API feedback

#### Incident Tracking
- Still waiting to hear if they want to track incidents in Helm
- This will require addition of private tasks and CAs from private forms
- New HR platform includes an incident module so may use that instead of Helm
- HR module also has certs, but doesn't have transparency that Helm does
- They are determining if it makes sense to track in HR or Helm
- Craig said ideally the HR system is the source of truth and then the certs are published in Helm via the API
- Need to show progress on the certs feedback to keep it in Helm full time

#### HMS Dashboard
- They feel like they need it per person per boat instead of how Hornblower has it in their drills dash
- When HMS migrates this will be easier
- **Next Steps:** Check with Liam if the drills dash can be published to HMS without Hornblower viewing it at the company wide scale. Otherwise we wait for them to migrate.

#### Analytics
- **Readings Dashboard:** Everyone loves the hours over time, but doesn't need everything else
- **Maintenance KPI:** Need activity and space filters in the basic analytics dash to help end users track their maintenance KPIs
- Need to get working on the overall maintenance KPI dashboard
- **Login Dashboard:** Want users to go directly to dashboard when logging in instead of their user profile
- Want capability to dictate by role what screen shows up when logging in:
  - Crew land on onboard logs
  - Engineering roles land on advanced search
  - Other mgr/gms land on dashboard
- **Next Steps:** Check in with Liam

#### Component Groups
- CAT 3208 Group > Apply Maintenance Templates to the Group > then add Components to Group
- Create new group from the templates manager?
- Don't add the estimated usage on templates, have it on the component itself
- Multiple components will be on the template and estimated usage is by boat by component
- The estimated run time should display, but should be pulling from the components field itself
- Option to link manufacturing and model automatically then have filters in onboard for make and model
- This will be even more necessary when we move to component groups as the template titles will likely change

---

## 2025-09-11 Uncruise Bi-Weekly Call Notes
**Date:** September 10, 2025  
**Attendees:** Jonah Vos, Jonathan Mann, Flynn  

### Key Discussion Points:

#### Attached Assets Components
- Not available right now, but we hope to have this in 2026
- Ideally this would be ready for them by the time their season starts up in Feb/March, but that is unlikely
- **Workaround:** List the lifeboats as components and then the maintenance will be tracked on the boats
- **Concern:** What happens when the lifeboats move to another vessel?
- If I deactivate a lifeboat on one vessel and move it to another > replace the lifeboat on vessel B with the one from Vessel A, does the maintenance history and template schedule move with it?
- If it doesn't then this would not really work for them as the maintenance needs to go with the lifeboat

### Next Steps:
- Send a video of how components work
- Send a video of certs 2.0 so Flynn can distribute it