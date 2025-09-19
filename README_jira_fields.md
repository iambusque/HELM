# Instructions: Grabbing Jira Fields via MCP

## Rule: Always Filter by Component = PMC
- When searching for Jira tickets, always include `component = PMC` in your JQL.
- Example JQL: `component = PMC AND "Target Version/s" = "7.1.34" ORDER BY created DESC`

## 1. Authenticate to Jira via MCP
- Ensure your MCP config is set up with Atlassian credentials and cloudId.

## 2. Search for Issues
- Use the `mcp_atlassian_searchJiraIssuesUsingJql` operation.
- Example JQL: `component = PMC AND "Target Version/s" = "7.1.34" ORDER BY created DESC`
- Specify `fields` in the request to control which fields are returned (e.g., summary, description, key, status, etc).

## 3. Retrieve Issue Details
- Each issue in the response will have a `fields` object with all requested fields.
- Example fields:
  - `summary`
  - `description`
  - `key`
  - `status`
  - `issuetype`
  - `assignee`
  - `reporter`
  - `created`
  - `updated`

## 4. Example Request (pseudo-code)
```
mcp_atlassian_searchJiraIssuesUsingJql({
  cloudId: "<your-cloud-id>",
  jql: 'component = PMC AND "Target Version/s" = "7.1.34"',
  fields: ["summary","description","key","status","issuetype","assignee","reporter","created","updated"],
  maxResults: 5
})
```

## 5. Example Response (truncated)
```
{
  "issues": [
    {
      "key": "CD-30197",
      "fields": {
        "summary": "Fix build issues due to formatting",
        ...
      }
    },
    ...
  ]
}
```

## 6. Tips
- Use JQL to filter by any field (component, label, status, etc).
- You can fetch additional fields by adding them to the `fields` array.
- For full field names, see your Jira instance's field configuration.
