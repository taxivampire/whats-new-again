# What's New, Again?

How do you say **“bug fixes and improvements”** for the tenth time?

A Codex skill for indie iOS developers writing the **What’s New** field in App Store Connect. Tell it what changed, in English or Chinese, and get a short English note you can paste into the store. For routine maintenance, “the usual fixes” is enough.

[简体中文](README.zh-CN.md) · [Six real App Store examples](references/app-store-examples.en.md)

### Three maintenance releases

These three drafts came from the same project with the same brief: bug fixes and usability improvements.

| Release | What’s New |
| --- | --- |
| First | We fixed a few bugs and made the app a little easier to use. |
| Next | A few bug fixes and a little polish. |
| Next | This update smooths out some rough edges and fixes a handful of bugs. |

### Try it on your next release

You’ll need Node.js for the installer and Python 3 for local draft history. From the project where you write release notes, install the skill for Codex:

```sh
npx skills add Rip-Busy/whats-new-again --skill whats-new-again --agent codex
```

Open a new Codex chat in that project and enter:

```text
$whats-new-again The usual fixes.
```

Only fixed bugs this time? Say “bug fixes only.” Have a specific change to share? Try “Fixed the blank screen when opening the app from a notification.” You can also ask for a preview to try it without saving a draft.

### What it remembers

The skill reads the eight most recent drafts for the same app and locale, then varies the opening or rhythm. A small Python 3 helper also checks the full local history for repeated wording, ignoring case, spaces and punctuation. It stores drafts in `.whats-new/history.sqlite3` in the project. A draft is saved when it is generated. If you write notes for several apps in the same project, include the app name each time.

### Read the examples

Todoist changed the joke between two maintenance releases. Strava kept a familiar sign-off. AllTrails made do with three words. The collection links each excerpt to the app’s US version history so you can compare the voices yourself. [Read the six examples](references/app-store-examples.en.md).
