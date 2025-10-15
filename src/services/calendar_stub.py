def calendar_help_text() -> str:
    return (
        "Google Calendar is not configured yet.\n"
        "Steps:\n"
        "1) Enable Calendar API in Google Cloud.\n"
        "2) Create OAuth credentials and download credentials.json to project root.\n"
        "3) Implement token flow and events list; wire here.\n"
        "See README for details."
    )