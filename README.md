# Claude API Example Project

This project demonstrates how to use the Anthropic Claude API.

## Setup

1. Install the required packages:
   ```bash
   pip install anthropic python-dotenv
   ```

2. Set up your API key:
   - Get your API key from [Anthropic Console](https://console.anthropic.com/)
   - Create a `.env` file in this directory:
     ```
     ANTHROPIC_API_KEY=your_api_key_here
     ```

## Usage

Run the example script:
```bash
python claude_example.py
```

## Files

- `claude_example.py` - Basic example of using Claude API
- `.env` - Environment variables (create this file with your API key)
- `requirements.txt` - Python dependencies

## API Key

Make sure to set your `ANTHROPIC_API_KEY` environment variable or add it to the `.env` file.
