# README: Generating Release Notes for HELM

## Purpose
This guide explains how to generate clear, customer-friendly release notes for each HELM release. The goal is to highlight key issues closed in the release, focusing on value and improvements for users, not technical details or customer-specific data.

## Release Notes Workflow
1. **Pull Tickets for the Release**
   - Use the MCP workflow to pull all Jira tickets for the target version (e.g., 1.34).
   - Group tickets by team label (Mobile, Retention, Creator).
   - Exclude any tickets that contain sensitive or customer-specific information.

2. **Summarize Key Issues**
   - For each ticket, write a short, non-technical summary of the improvement or fix.
   - Focus on what changed, what was improved, or what was fixed, in plain language.
   - Avoid technical jargon, internal process notes, or customer names.

3. **Live Markdown Generation**
   - As tickets are pulled, update a Markdown file (e.g., `Release Notes.md`) with the latest summaries.
   - Organize by team label, with a section for each group.
   - Only include tickets that are relevant and user-facing.

## Example Release Notes Structure
```markdown
# HELM 1.34 Release Notes

## Mobile
- Improved how templates are displayed and managed.
- Fixed an issue where some forms could not be completed on the first try.

## Retention
- Enhanced the reliability and consistency of template features.

## Creator
- Streamlined permissions and made it easier to manage assets and requests.
- Improved audit and reporting features for better oversight.
```

## Tips
- Keep each summary to 1-2 sentences.
- Focus on the benefit or outcome for users.
- Regenerate the Markdown file each time new tickets are pulled or updated.
- Review for clarity and remove any internal or customer-specific details before publishing.

---

By following this guide, you can ensure every HELM release has clear, helpful notes that communicate real value to users.