# Marco Wilson - Call Notes (Sept 11-18, 2025)

## 2025-09-11 AM Call Notes - Helm / Hines - Payroll Question on Custom Withdrawal
**Date:** September 11, 2025  
**Attendees:** Lindsay Hernandez, Marco Wilson  
**Recording:** [Helm Hines Meeting Recording](https://ourvolaris-my.sharepoint.com/:v:/g/personal/marco_wilson_helmoperations_com/EZAzWTDTktZEsXSUnpJdh78BcOC8jE0aOEEX_FXZ48qEqQ?e=1NiDdA&nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJTdHJlYW1XZWJBcHAiLCJyZWZlcnJhbFZpZXciOiJTaGFyZURpYWxvZy1MaW5rIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXcifX0%3D)

### Issue Overview
Lindsay was trying to do some custom bank withdrawals (flat amounts) for several employees. The calculated amount she's trying to withdraw ends up with a totally different number/amount. Marco wasn't able to figure out the issue but Lindsay thinks it will be okay as she has a workaround.

### Detailed Discussion Topics:

#### Standard Withdrawal Method
- Successfully tested with Hodge's case ($3.80 daily rate × 2 days = $760)
- Process involves selecting withdrawal by days rather than custom amount
- Requires doubling the values in some instances
- Works correctly for straightforward cases
- **Note:** Lindsay reported Sept 12, 2025 that she tried this with others and the same issue was occurring again

#### Custom Withdrawal Issues
- Custom rate option produces errors and unexpected calculations
- **Example:** Cody Beam's $1,877 withdrawal request generates incorrect calculations
- System displays strange values (e.g., "6.86 times 800.5") with no clear source
- The issue appears consistent across multiple attempts

#### Workaround Solution
For the seven employees with custom withdrawal requests, Lindsay will:
- Zero out their current bank amounts
- Add accruals to their following payroll cycle
- This temporary solution will work while they investigate the underlying issue
- Team is working to transition away from custom amount requests overall

### Action Items:
- ✅ Lindsay to implement the workaround for the seven employees requiring custom withdrawals
- ⏳ Marco to potentially send the recording to the support team for investigation
- ✅ Continue encouraging standardized withdrawal requests rather than custom amounts

---

## 2025-09-11 AM Call Notes - Crowley - Bi-Weekly + Analytics Updates
**Date:** September 11, 2025  
**Attendees:** James Benjamin, Troy Jannelle, Marco Wilson, Liam Cameron  
**Recording:** [Helm Crowley Bi-weekly Meeting Recording](https://ourvolaris-my.sharepoint.com/:v:/g/personal/marco_wilson_helmoperations_com/Ee04HAXn-mFAiqDaQE0NCFsBVH-xt3SHBgy87iSztNwcMg?e=eaXP83&nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJTdHJlYW1XZWJBcHAiLCJyZWZlcnJhbFZpZXciOiJTaGFyZURpYWxvZy1MaW5rIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXcifX0%3D)

### Summary
Good meeting with James and Troy. Things seem to be working smooth overall. 1.33 updates for Crew Scheduling are great but still some room for improvement. James wants bulk uploaders for the new Crew Certs when it comes in 1.33+. Troy wants a mini-dashboard on the boats for engineers. James says the Mainlines integration is good to go now after working with Liam. Troy ran into an error with responsible parties and will create a support ticket.

### Detailed Discussion Topics:

#### Software Updates
- **Release 1.33:** Currently deployed with some room for improvement on crew change displays
- **Release 1.33+:** Coming soon, which will include personnel certifications functionality
- **Release 1.34:** Planned for the coming months with further updates

#### Personnel Certifications Management
- Discussion about the loader functionality for personnel certifications
- James emphasized the need for attachments to be stored at the personnel profile level rather than with individual certifications
- This would prevent duplicate uploads of documents like MMCs that cover multiple certifications
- Would simplify automation with Oracle HR system integration
- Concerns raised about visibility of sensitive attachments and proper naming conventions

#### Analytics Dashboards
- Liam presented updated analytics dashboard for tracking near misses and incidents
- Dashboard aggregates data from multiple form types (injury reports, near misses, incident reports)
- **Features include:**
  - Trending data by vessel, month, quarter, or year
  - Categorization by incident type
  - Filtering capabilities by various parameters

#### Vessel Maintenance Tracking
- Discussion about engineers needing better visibility into maintenance schedules
- Request for a "baby dashboard" for onboard engineers to quickly see:
  - Hours since last oil change
  - Total engine hours
  - Maintenance due dates
- **Challenge:** Crowley's corporate IT security restrictions limit shoreside access on vessels
- Potential solution would require internet connection and additional development

### Action Items:
- ⏳ Marco to talk to Sean about providing loaders for personnel certifications
- ⏳ Liam to implement the updated analytics dashboard in their environment for testing
- ⏳ Troy to submit a support ticket regarding the error code when updating responsible parties
- ⏳ Further discussion needed about analytics dashboards for onboard use

### Other Issues:
- Troy encountering error code when trying to update responsible parties on certain attached assets
- Discussion of using email distribution lists as users to enable fleet-wide notifications