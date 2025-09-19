# Next Steps to Enable Weekly AM Notes Collection

## ✅ No Additional Secrets Required
The workflow uses your existing MCP configuration:
- **Cloud ID**: `05fe7108-c795-4295-8062-b43ad1f2e363` 
- **Base URL**: `https://edocgroup.atlassian.net`

## Quick Enable Steps
- Validate workflow placement:
  - Confirm `.github/workflows/weekly-am-notes.yml` exists on default branch

- Run a dry run:
  - Actions > Weekly AM Notes Collection > Run workflow
  - Set `dry_run` to `true`

- Inspect logs and artifacts:
  - Download `collection-logs` artifact from the run
  - Check `AM Call Notes/service/logs/am_collection.log` for errors

- If dry run passes, run full workflow with `dry_run=false`.

- Monitor weekly runs and review generated files in `AM Call Notes/`.

## Optional Enhancements
- Configure notification webhook in `weekly_collection_config.yaml` 
- Add `NOTIFY_WEBHOOK` secret for Slack/Teams alerts
- Implement SMTP notifications in `am_collection_script.py`

**Ready to test?** I can trigger a dry-run now since all MCP credentials are already configured.