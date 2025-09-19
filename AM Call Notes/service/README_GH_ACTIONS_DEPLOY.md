# Deploying Weekly AM Notes Collection via GitHub Actions

This document describes how to deploy and run the `Weekly AM Notes Collection` workflow using GitHub Actions.

Prerequisites
- Repository hosted on GitHub with push access.
- Confluence API token and account email with permission to read pages in the SAL and CS spaces.
- The workflow file is at `.github/workflows/weekly-am-notes.yml`.

Required repository secrets
- `CONFLUENCE_TOKEN` - Confluence API token (personal access token)
- `CONFLUENCE_EMAIL` - Email address associated with the token

Optional secrets (if used later)
- `SMTP_API_KEY` - For email notifications
- `NOTIFY_WEBHOOK` - Webhook URL for alerts (Teams/Slack)

Deployment Steps
1. Move the workflow file to the default branch (already added at `.github/workflows/weekly-am-notes.yml`).
2. Add required repository secrets:
   - Go to `Settings` > `Secrets and variables` > `Actions` > `New repository secret`.
   - Add `CONFLUENCE_TOKEN` and `CONFLUENCE_EMAIL`.
3. (Optional) Add additional secrets for notifications if you want automated email or webhook alerts.
4. Trigger a manual run for testing:
   - Go to `Actions` > `Weekly AM Notes Collection` > `Run workflow`.
   - Set `dry_run` to `true` for a safe test that won't commit files.
5. Review artifacts and logs:
   - The workflow uploads logs as an artifact named `collection-logs`.
   - Check the `AM Call Notes/service/logs/am_collection.log` file in the artifact if available.

Testing Tips
- Start with `dry_run=true` to validate the script runs and searches without committing changes.
- Use `DATE_OVERRIDE` input to run the collection for a specific week (format: `YYYY-MM-DD to YYYY-MM-DD`).
- If the workflow fails, the Actions run will create a GitHub Issue labeled `automation, am-notes, bug` with initial diagnostics.

Security Notes
- Keep `CONFLUENCE_TOKEN` restricted to a service account if possible.
- Rotate tokens periodically.

Next Steps
- Configure email notifications in `weekly_collection_config.yaml` or extend `am_collection_script.py` to send summaries via SMTP/SendGrid.
- Optionally set up an on-call or Slack channel to receive failure notices via `NOTIFY_WEBHOOK`.

If you'd like, I can: 
- Add an issue template for triaging failures.
- Create a GitHub Action secret for you (requires repo permissions).
- Run a dry-run manually to validate the workflow end-to-end.
