# Slacktivate

Slacktivate is a Python library and Command-Line Interface
to assist in the provisioning of a Slack workspace, using
both the Slack API and the Slack SCIM API.

## Prerequisites: Having Owner Access and Getting an API Token

In order to use the SCIM API, you need to be an owner of the workspace, and obtain an API token with `admin` scope.

As explained in [the official Slack SCIM API documentation](https://api.slack.com/scim#access), the easiest way to obtain a valid token for the purposes of SCIM provisioning is as follows:
1. As *a Workspace/Organization Owner*, create [a new app for your workspace](https://api.slack.com/apps?new_app=1) (see [here](https://api.slack.com/start/overview#creating) for the documentation).
2. Add the `admin` OAuth scope to [the "User Token Scopes" section](https://api.slack.com/authentication/quickstart#configuring).
3. Install the app to your workspace (see [here](https://api.slack.com/start/overview#installing_distributing) for the documentation).
4. Use the generated token (if you are provided with multiple tokens, use the "OAuth Access Token" not the "Bot User OAuth Access Token").

Note that you can easily *reinstall your app* with different permissions if it turns out you did not select all the necessary permissions.
