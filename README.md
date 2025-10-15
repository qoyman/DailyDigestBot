# Telegram Bot Starter (Python)

A production-ready starter for a Telegram bot built with **python-telegram-bot v21**.
Includes commands for:
- `/weather <city>` — Weather via OpenWeatherMap
- `/quote` — Motivational quote
- `/meme` — Random meme (demo via placeholder list; swap in your API)
- `/events` — Google Calendar events (stub + setup guide)

## Milestones

### Milestone 1 — Research
- Library: [python-telegram-bot v21](https://docs.python-telegram-bot.org/en/v21.6/)
- HTTP client: [httpx](https://www.python-httpx.org/)
- Weather API: [OpenWeatherMap Current Weather](https://openweathermap.org/current)
- Env: [python-dotenv](https://pypi.org/project/python-dotenv/)
- Testing: [pytest](https://docs.pytest.org/)
- Lint/Format: [ruff](https://docs.astral.sh/ruff/), [black](https://black.readthedocs.io/)
- Optional Calendar: [Google Calendar API](https://developers.google.com/calendar/api/quickstart/python)

### Milestone 2 — Project setup & first checks
- Created project scaffold with `/start`, `/help`, and `/ping` (returns `pong`) to verify bot responsiveness.
- Added unit tests for pure functions (e.g., quote selection).

## Features

- **Weather:** `/weather Lagos` → current conditions & temperature.
- **Quote:** `/quote` → random motivational quote (local list).
- **Meme:** `/meme` → demo meme link (local list). Replace with an API if desired.
- **Calendar (stub):** `/events` shows setup steps; function stub provided.

## Quick Start

1) **Clone** and create a virtualenv:
```bash
git clone https://example.com/telebot-starter.git
cd telebot-starter
python -m venv .venv
. .venv/Scripts/activate  # on Windows PowerShell: .venv\Scripts\Activate.ps1
# or on macOS/Linux:
# source .venv/bin/activate
```

2) **Install deps**:
```bash
pip install -e .[dev]
```

3) **Environment vars**: copy and edit:
```bash
copy .env.example .env   # Windows
# cp .env.example .env   # macOS/Linux
```
Fill `BOT_TOKEN` from **BotFather**, and `OPENWEATHER_API_KEY` from OpenWeather.

4) **Run**:
```bash
python -m src.bot
```

5) **Open telegram**:
- `Search for Digestisp_bot`
**Try commands**:
- `/start`
- `/help`
- `/ping`
- `/weather Lagos`
- `/quote`
- `/meme`
- `/events`

## Best Practices Included

- **Linting/Formatting:** Ruff + Black via pre-commit.
```bash
pre-commit install
pre-commit run -a
```

- **Testing:** Pytest for pure business logic.
```bash
pytest
```

- **GitFlow (lightweight):**
  - `main`: stable
  - `develop`: integration
  - Feature branches: `feature/<short-desc>`
  - Pull Requests with descriptive commit messages:
    - Imperative mood, present tense: "Add weather service"
    - Reference issues/tickets when relevant

## Google Calendar Setup (Optional - Stub)

1. Create a project at Google Cloud Console, enable Calendar API.
2. Create OAuth 2.0 credentials (Desktop App). Download `credentials.json` into the project root.
3. Implement OAuth flow (see `src/services/calendar_stub.py` for guidance) and replace the stubbed `/events` handler.

## Configuration

- **.env**
  - `BOT_TOKEN`: Token from BotFather
  - `OPENWEATHER_API_KEY`: From OpenWeatherMap
  - Optional keys for meme APIs

## Project Structure

```text
telebot-starter/
├── src/
│   ├── bot.py
│   ├── handlers/
│   │   ├── common.py
│   │   └── commands.py
│   └── services/
│       ├── weather.py
│       ├── quotes.py
│       ├── memes.py
│       └── calendar_stub.py
├── tests/
│   └── test_quotes.py
├── .env.example
├── .gitignore
├── README.md
├── pyproject.toml
└── .pre-commit-config.yaml
```

## Windows Notes (Activation)

If you see `ModuleNotFoundError: No module named 'telegram'`, ensure you've **activated** your virtualenv **and** installed dependencies:
```powershell
.venv\Scripts\Activate.ps1
pip install -e .[dev]
```

## License

MIT