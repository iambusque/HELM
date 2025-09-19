# Instructions: Posting to Obsidian Vault via MCP

## Rule: Folder Structure Must Match Target Version
- When posting a Jira ticket to the vault, always check if the `Target Version` matches the release number in the folder path.
- If the `Target Version` (e.g., 7.1.35) does not match the current release folder (e.g., `1.34`), create a new folder using the same style:
  - Example: `HELM/1.35/Release Notes/Jira Tickets/`
- Place the ticket in the correct versioned folder to keep releases organized.

## Rule: Group by Team Label (Mobile, Retention, Creator)
- Under each versioned folder, group tickets by Label, but only if the Label is one of:
  - `Mobile`
  - `Retention`
  - `Creator`
- Example folder structure:
  - `HELM/1.35/Release Notes/Jira Tickets/Mobile/`
  - `HELM/1.35/Release Notes/Jira Tickets/Retention/`
  - `HELM/1.35/Release Notes/Jira Tickets/Creator/`
- If a ticket does not have one of these labels, place it directly in the `Jira Tickets` folder for that version.

## 1. Prepare Your Note Content
- Format the content as Markdown (recommended for Obsidian).
- Include any fields from Jira you want (summary, description, status, etc).
- Example template:
  ```markdown
  # {key}: {summary}
  **Type:** {issuetype}  
  **Status:** {status}  
  **Assignee:** {assignee}  
  **Reporter:** {reporter}  
  **Created:** {created}  
  **Updated:** {updated}
  ---
  {description}
  ```

## 2. Choose the Destination Path
- Decide the folder and filename in your vault (e.g., `1.34/Release Notes/Jira Tickets/CD-30197.md`).
- The path should be relative to your Obsidian vault root.

## 3. Use the MCP `vault` Operation
- Use the `vault` operation with `action: "create"` (or `update` if overwriting).
- Example request:
  ```json
  {
    "operation": "vault",
    "action": "create",
    "params": {
      "path": "1.34/Release Notes/Jira Tickets/CD-30197.md",
      "content": "# CD-30197: Fix build issues due to formatting\n..."
    }
  }
  ```

## 4. Confirm the Note in Obsidian
- Open your vault and verify the new note appears in the correct folder.
- Obsidian will render the Markdown automatically.

## 5. Tips
- You can automate this process for multiple tickets.
- Use the `update` action to overwrite an existing note.
- Use subfolders for organization by version, team, etc.
