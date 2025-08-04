# Claude API Demos - AI Coding Agent Instructions

## Project Overview

This is a professional Claude API demonstration suite packaged as a pip-installable Python library (`claude-api-demos`). The project showcases comprehensive Claude API usage patterns through multiple demo types, with full enterprise development infrastructure including dual GitLab/GitHub repository management.

## Architecture & Key Components

### Package Structure Pattern

- **Main package**: `src/claude_api_demos/` - Follow this importable module pattern
- **Demo modules**: Each demo is a standalone class with `main()` function (e.g., `ClaudeClient`, `AdvancedClaudeDemo`, `RDAnalyticsAssistant`)
- **CLI interface**: `cli.py` provides unified entry point via `claude-demos` command
- **Public API**: All main classes exported through `__init__.py` for programmatic use

### Development Workflow

```powershell
# Install in development mode (always use -e flag)
pip install -e .

# Run demos via VS Code tasks (Ctrl+Shift+P > Tasks: Run Task)
# OR use CLI: claude-demos

# Test with: python -m pytest tests/ -v
```

### Demo Module Pattern

Each demo follows this structure:

```python
class DemoClass:
    def __init__(self):
        self.client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
        self.model = "claude-3-5-sonnet-20241022"  # Always use latest model

    def method_with_claude_call(self):
        # Use try/except for API calls
        # Create output directories as needed
        # Log results for R&D analytics pattern

def main():
    # Demo entry point - always include this
```

### API Key Management

- Uses `python-dotenv` with `.env` file (never commit actual keys)
- `.env.example` shows required format: `ANTHROPIC_API_KEY=your-key-here`
- `cli.py` includes API key validation with masked display
- Always check `os.getenv("ANTHROPIC_API_KEY")` at runtime

### Output Organization

- **General demos**: Store outputs in demo-specific directories
- **R&D Analytics**: Uses structured `rd_analytics_outputs/` with subdirs:
  - `logs/` - Session tracking and analysis logs
  - `reports/` - Generated technical reports
  - `data/` - Experimental data and results
- **File naming**: Use timestamp-based naming (`YYYYMMDD_HHMMSS` pattern)

## Dual Repository Strategy

- **Primary**: GitLab (`https://gitlab.intermedisoft.com/research/ai-instruction.git`)
- **Mirror**: GitHub (`https://github.com/HamdeeNaseng/ai-instruction.git`)
- **Single push**: `git push origin` pushes to both repositories simultaneously
- **Management script**: `git-dual-repo.sh` for advanced operations
- **Documentation**: `GIT_DUAL_SETUP.md` contains complete setup instructions

## VS Code Integration Patterns

### Task Configuration

- **Install Package**: Always use trusted-host flags for corporate networks
- **Demo tasks**: Direct Python execution of demo files
- **Interactive demos**: Use `focus: true` for user interaction
- **Test tasks**: Use pytest with `-v` flag

### Development Commands

```json
// Common task pattern
{
  "label": "Task Name",
  "type": "shell",
  "command": "python",
  "args": ["src/claude_api_demos/demo_file.py"],
  "group": "build",
  "presentation": { "reveal": "always", "panel": "shared" }
}
```

## Testing & Quality Patterns

- **Test structure**: Mirror `src/` structure in `tests/`
- **PyTest configuration**: Use `-v` flag for verbose output
- **Mock API calls**: Always mock `anthropic.Anthropic` in unit tests
- **GitHub Actions**: Full CI/CD with multi-platform testing (Windows/macOS/Linux)

## R&D Analytics Specialization

The `rd_analytics_demo.py` implements enterprise R&D patterns:

- **Structured logging**: JSON-based result tracking with session IDs
- **Data analysis workflows**: Statistical analysis, trend identification
- **Decision matrices**: Automated scoring and recommendation systems
- **Experimental design**: Parameter optimization and hypothesis testing
- **Technical reporting**: Automated report generation with charts/tables

## Common Integration Points

- **Environment setup**: Always validate API key before demos
- **Error handling**: Graceful degradation with helpful error messages
- **User interaction**: Use clear prompts and progress indicators
- **Output management**: Create directories as needed, organize by type/date

## GitHub Infrastructure

- **Workflows**: Complete CI/CD pipeline in `.github/workflows/`
- **Templates**: Issue and PR templates for collaboration
- **Security**: Security policy and automated dependency updates
- **Quality**: Automated code quality checks and formatting

When extending this codebase, maintain the professional packaging structure, follow the demo class patterns, and ensure all new components integrate with the CLI interface and VS Code task system.
