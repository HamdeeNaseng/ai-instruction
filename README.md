# Claude API Demos - Professional Development Suite

This project provides comprehensive demonstrations of the Anthropic Claude API, packaged as a professional Python library with full VS Code integration. Inspired by the [DataCamp Claude tutorial](https://www.datacamp.com/tutorial/claude-code).


## [Slide AI INSTRUCTION]("https://www.canva.com/design/DAGvEhuRSOw/zY3r_FQYtsCLPLQaUaW0fg/view?utm_content=DAGvEhuRSOw&utm_campaign=designshare&utm_medium=link2&utm_source=uniquelinks&utlId=h517c4cbccb")

## <iframe src="https://www.canva.com/design/DAGvEhuRSOw/zY3r_FQYtsCLPLQaUaW0fg/view?utm_content=DAGvEhuRSOw&utm_campaign=designshare&utm_medium=link2&utm_source=uniquelinks&utlId=h517c4cbccb" width="100%" height="500"></iframe>

## 🚀 Quick Start

### 1. Install Package
```powershell
# Install in development mode
pip install -e .

# Set your API key
$env:ANTHROPIC_API_KEY = "your-api-key-here"
```

### 2. Run Demos
```powershell
# Use the CLI interface
claude-demos

# Or run specific demos
 python src/claude_api_demos/cli.py
```

## � Package Features

- **Professional Python Package** - Installable with pip, includes CLI tool
- **VS Code Integration** - Complete development environment with tasks and debugging
- **Comprehensive Test Suite** - Full test coverage with pytest
- **Multiple Demo Types** - Basic, advanced, interactive, and real-world examples
- **CLI Interface** - Command-line tool with interactive menus

## 🎯 Demo Types

### Basic Demo (`basic_demo.py`)
- Simple chat interactions
- Code analysis and explanation  
- Multi-turn conversations
- JSON response handling

### Advanced Demo (`advanced_demo.py`)
- Code review and refactoring
- Test case generation
- Performance optimization
- File analysis workflows

### Interactive Demo (`interactive_demo.py`)
- Real-time chat interface
- Developer assistance mode
- Project analysis capabilities

### Real World Demo (`real_world_demo.py`)
- Practical development scenarios
- Code documentation generation
## 🛠️ VS Code Development

### Quick Access (Ctrl+Shift+P)

**Tasks: Run Task**
- Install Package (Development Mode)
- Run All Tests  
- Run Basic Demo
- Run Advanced Demo
- Run Interactive Demo
- Run CLI - Interactive Menu
- Clean Build Files
- Format Code with Black

**Debug Configurations (F5)**
- Debug any demo type
- Run tests with debugging
- Debug current file

### Project Structure

```
ai-instruction/
├── src/claude_api_demos/     # Main package
│   ├── basic_demo.py         # Basic demonstrations
│   ├── advanced_demo.py      # Advanced workflows
│   ├── interactive_demo.py   # Interactive chat
│   ├── real_world_demo.py    # Practical examples
│   └── cli.py                # Command-line interface
├── tests/                    # Test suite
├── .vscode/                  # VS Code configuration
├── pyproject.toml            # Package configuration
└── README.md                 # This file
```

## 🎯 API Key Setup

**PowerShell:**
```powershell
$env:ANTHROPIC_API_KEY = "your-api-key-here"
```

**Command Prompt:**
```cmd
set ANTHROPIC_API_KEY=your-api-key-here
```

**Or create `.env` file:**
```
ANTHROPIC_API_KEY=your-api-key-here
```

## 💡 Usage Examples

### CLI Interface
```powershell
# Interactive menu
claude-demos

# Direct command
python src/claude_api_demos/cli.py
```

### Individual Demos
```powershell
python src/claude_api_demos/basic_demo.py
python src/claude_api_demos/advanced_demo.py
python src/claude_api_demos/interactive_demo.py interactive
```

### Python API
```python
from claude_api_demos import ClaudeClient, AdvancedClaudeDemo

# Basic usage
client = ClaudeClient()
response = client.chat("Explain Python decorators")

# Advanced usage  
demo = AdvancedClaudeDemo()
results = demo.code_review_and_refactor('your_file.py')
```

## 🧪 Testing

```powershell
# Run all tests
python -m pytest tests/ -v

# Or use VS Code task "Run All Tests"
```

## 🔧 DataCamp Tutorial Inspiration

This project implements functionality similar to the [DataCamp Claude tutorial](https://www.datacamp.com/tutorial/claude-code):

| Feature | Implementation |
|---------|----------------|
| Code Analysis | ✅ `basic_demo.py`, `advanced_demo.py` |
| Interactive Chat | ✅ `interactive_demo.py` |
| Documentation | ✅ `real_world_demo.py` |
| Professional Package | ✅ Complete pip-installable package |
| VS Code Integration | ✅ Tasks, debugging, settings |

## 🎓 Learning Resources

- [Anthropic Claude API Documentation](https://docs.anthropic.com/)
- [DataCamp Claude Tutorial](https://www.datacamp.com/tutorial/claude-code)
- [Claude API Best Practices](https://docs.anthropic.com/en/docs/build-with-claude/best-practices)

## 🤝 Contributing

Feel free to extend the demos with your own examples! Each demo file is modular and can be easily modified or extended.

## 📝 Development Notes

- Package is installable with `pip install -e .`
- VS Code provides complete development environment
- All tests pass with pytest
- Code formatted with Black, linted with Flake8
- CLI tool available as `claude-demos` after installation

---

**Note:** This project requires an active Anthropic API key. Get yours at [console.anthropic.com](https://console.anthropic.com/).
