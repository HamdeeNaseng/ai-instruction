# Claude API Demos - Development Guidelines

## Table of Contents
- [Project Overview](#project-overview)
- [Development Workflow](#development-workflow)
- [Code Standards](#code-standards)
- [Testing Guidelines](#testing-guidelines)
- [Documentation Standards](#documentation-standards)
- [Git Workflow](#git-workflow)
- [VS Code Integration](#vs-code-integration)
- [R&D Analytics Guidelines](#rd-analytics-guidelines)
- [Security Guidelines](#security-guidelines)
- [Release Process](#release-process)

## Project Overview

This project is a professional Claude API demonstration suite packaged as `claude-api-demos`, showcasing comprehensive API usage patterns through multiple demo types with enterprise development infrastructure.

### Architecture Principles
- **Modular Design**: Each demo is a standalone class with standardized patterns
- **Professional Packaging**: pip-installable with proper project structure
- **Enterprise Integration**: Full CI/CD, dual repository management, comprehensive testing
- **R&D Analytics**: Specialized tools for data analysis and decision support

## Development Workflow

### Environment Setup
1. **Clone Repository**:
   ```bash
   git clone https://gitlab.intermedisoft.com/research/ai-instruction.git
   cd ai-instruction
   ```

2. **Install Development Dependencies**:
   ```powershell
   # Use trusted hosts for corporate networks
   pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org -e .
   ```

3. **Configure Environment**:
   ```bash
   # Copy and edit environment file
   cp .env.example .env
   # Edit .env with your ANTHROPIC_API_KEY
   ```

### Daily Development
1. **Pull Latest Changes**:
   ```bash
   git pull origin main
   ```

2. **Create Feature Branch**:
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Run Tests Before Changes**:
   ```bash
   python -m pytest tests/ -v
   ```

4. **Make Changes Following Standards** (see Code Standards section)

5. **Test Your Changes**:
   ```bash
   # Run specific demo
   python src/claude_api_demos/your_demo.py
   
   # Run all tests
   python -m pytest tests/ -v
   ```

6. **Commit and Push**:
   ```bash
   git add .
   git commit -m "feat: descriptive commit message"
   git push origin feature/your-feature-name
   ```

## Code Standards

### Demo Module Pattern
Every demo must follow this structure:

```python
#!/usr/bin/env python3
"""
Demo Description
Brief explanation of what this demo showcases
"""

import os
import anthropic
from typing import Dict, List, Any, Optional
from pathlib import Path

class YourDemo:
    """Demo class with descriptive docstring"""
    
    def __init__(self):
        self.client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
        self.model = "claude-3-5-sonnet-20241022"  # Always use latest model
    
    def your_method(self) -> Dict[str, Any]:
        """Method with proper type hints and docstring"""
        try:
            # Implementation with error handling
            response = self.client.messages.create(
                model=self.model,
                max_tokens=2000,
                messages=[{"role": "user", "content": "your prompt"}]
            )
            return {"result": response.content[0].text}
        except Exception as e:
            return {"error": f"Error: {e}"}

def main():
    """Demo entry point - always include this"""
    print("🚀 Your Demo Title")
    print("=" * 60)
    
    demo = YourDemo()
    # Demo execution logic
    
    print("✅ Demo completed!")

if __name__ == "__main__":
    main()
```

### Code Quality Standards
- **Type Hints**: Use type hints for all function parameters and return values
- **Docstrings**: Google-style docstrings for all classes and methods
- **Error Handling**: Always wrap Claude API calls in try/except blocks
- **Logging**: Use descriptive print statements for demo progress
- **Constants**: Use uppercase for constants, latest Claude model version

### File Organization
- **Demo Files**: `src/claude_api_demos/demo_name.py`
- **Tests**: `tests/test_demo_name.py` (mirror src structure)
- **Outputs**: Create structured directories as needed
- **Documentation**: Update relevant docs when adding features

## Testing Guidelines

### Test Structure
```python
import pytest
from unittest.mock import patch, Mock
from claude_api_demos.your_demo import YourDemo

class TestYourDemo:
    def setup_method(self):
        """Setup before each test"""
        self.demo = YourDemo()
    
    @patch('claude_api_demos.your_demo.anthropic.Anthropic')
    def test_your_method_success(self, mock_anthropic):
        """Test successful API call"""
        # Mock setup
        mock_client = Mock()
        mock_response = Mock()
        mock_response.content = [Mock(text="Expected response")]
        mock_client.messages.create.return_value = mock_response
        mock_anthropic.return_value = mock_client
        
        # Test execution
        result = self.demo.your_method()
        
        # Assertions
        assert "result" in result
        assert result["result"] == "Expected response"
    
    @patch('claude_api_demos.your_demo.anthropic.Anthropic')
    def test_your_method_error(self, mock_anthropic):
        """Test error handling"""
        mock_anthropic.side_effect = Exception("API Error")
        
        result = self.demo.your_method()
        
        assert "error" in result
```

### Test Requirements
- **Mock API Calls**: Always mock `anthropic.Anthropic` in unit tests
- **Error Cases**: Test both success and error scenarios
- **Edge Cases**: Test boundary conditions and invalid inputs
- **Integration Tests**: Include tests that verify demo workflows

### Running Tests
```bash
# Run all tests with verbose output
python -m pytest tests/ -v

# Run specific test file
python -m pytest tests/test_your_demo.py -v

# Run with coverage
python -m pytest tests/ --cov=src/claude_api_demos --cov-report=html
```

## Documentation Standards

### README Updates
When adding new demos:
1. Update demo list in README.md
2. Add usage examples
3. Update feature matrix if applicable

### Docstring Format
Use Google-style docstrings:

```python
def analyze_data(self, data: Dict[str, Any], context: str = "") -> Dict[str, Any]:
    """Analyze experimental data and provide insights.
    
    Args:
        data: Dictionary containing experimental data points
        context: Optional context for analysis interpretation
        
    Returns:
        Dictionary containing analysis results with keys:
            - 'insights': List of key findings
            - 'recommendations': List of recommended actions
            - 'confidence': Confidence score (0-1)
            
    Raises:
        ValueError: If data format is invalid
        APIError: If Claude API call fails
        
    Example:
        >>> demo = RDAnalyticsDemo()
        >>> data = {'temperature': [25, 30, 35], 'yield': [0.78, 0.85, 0.88]}
        >>> result = demo.analyze_data(data, "synthesis optimization")
        >>> print(result['insights'])
    """
```

### Code Comments
- **Complex Logic**: Comment non-obvious algorithms or business logic
- **API Interactions**: Document Claude API parameters and expected responses
- **Configuration**: Comment configuration choices and parameters

## Git Workflow

### Branch Naming
- **Features**: `feature/description-of-feature`
- **Bug Fixes**: `bugfix/description-of-fix`
- **Documentation**: `docs/description-of-changes`
- **Experiments**: `experiment/description-of-experiment`

### Commit Messages
Follow conventional commits format:
```
type(scope): description

[optional body]

[optional footer]
```

Types:
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes
- `refactor`: Code refactoring
- `test`: Test additions/changes
- `chore`: Maintenance tasks

Examples:
```bash
feat(analytics): add experimental design recommendation system
fix(cli): resolve API key validation error message
docs(readme): update installation instructions for corporate networks
```

### Pull Request Process
1. **Create PR** from feature branch to `main`
2. **Fill PR Template** with description, testing notes, breaking changes
3. **Ensure CI Passes** - all tests, linting, security checks
4. **Request Review** from team members
5. **Address Feedback** and update branch
6. **Merge** after approval (use squash merge for clean history)

## VS Code Integration

### Required Extensions
- Python (Microsoft)
- Pylance
- Black Formatter
- GitLens
- GitHub Pull Requests

### Workspace Settings
The project includes VS Code settings for:
- Python interpreter configuration
- Code formatting (Black)
- Linting (Flake8)
- Testing (pytest)
- Debugging configurations

### Tasks Usage
Use `Ctrl+Shift+P` → "Tasks: Run Task":
- **Install Package (Development Mode)**: Sets up development environment
- **Run All Tests**: Executes full test suite
- **Run [Demo Name]**: Executes specific demos
- **Format Code with Black**: Formats all Python files

### Debugging
Use `F5` to debug:
- Any demo file
- Test files
- Current active file

## R&D Analytics Guidelines

### Output Organization
Structure outputs in `rd_analytics_outputs/`:
```
rd_analytics_outputs/
├── logs/                    # Session tracking
│   └── session_YYYYMMDD_HHMMSS.json
├── reports/                 # Generated reports
│   ├── analysis_YYYYMMDD_HHMMSS.md
│   └── technical_report_YYYYMMDD_HHMMSS.md
└── data/                   # Experimental data
    └── metrics_YYYYMMDD_HHMMSS.csv
```

### Session Management
- Use timestamp-based session IDs: `YYYYMMDD_HHMMSS`
- Log all operations with structured data
- Maintain traceability for audit purposes

### Report Standards
- **Executive Reports**: High-level summaries with recommendations
- **Technical Reports**: Detailed analysis with methodology
- **Decision Matrices**: Structured decision support with scoring
- **Experimental Designs**: Statistical rigor with power analysis

## Security Guidelines

### API Key Management
- **Never commit** API keys to version control
- **Use .env files** for local development
- **Environment variables** for production
- **Masked display** in CLI tools for security

### Sensitive Data
- **Exclude** from git: API keys, secrets, personal data
- **Sanitize** outputs before committing
- **Review** .gitignore regularly

### Code Security
- **Validate inputs** from external sources
- **Sanitize** file paths and user inputs
- **Handle errors** gracefully without exposing sensitive information

## Release Process

### Version Management
- Follow Semantic Versioning (SemVer)
- Update version in `pyproject.toml`
- Tag releases in git: `v1.0.0`

### Release Checklist
1. **Update Version** in pyproject.toml
2. **Update CHANGELOG.md** with new features/fixes
3. **Run Full Test Suite** and ensure all pass
4. **Update Documentation** if needed
5. **Create Release PR** for review
6. **Tag Release** after merge
7. **GitHub Actions** will handle publishing

### Hotfix Process
For critical bug fixes:
1. Create `hotfix/` branch from main
2. Apply minimal fix
3. Test thoroughly
4. Fast-track review process
5. Deploy immediately after merge

## Best Practices Summary

### Development
- ✅ Use development installation: `pip install -e .`
- ✅ Follow demo module pattern consistently
- ✅ Always include proper error handling
- ✅ Use latest Claude model version
- ✅ Write comprehensive tests

### Code Quality
- ✅ Type hints for all functions
- ✅ Google-style docstrings
- ✅ Descriptive variable names
- ✅ Consistent code formatting (Black)
- ✅ Regular linting (Flake8)

### Collaboration
- ✅ Descriptive commit messages
- ✅ Small, focused pull requests
- ✅ Thorough code reviews
- ✅ Documentation updates
- ✅ Test coverage maintenance

### Security
- ✅ Never commit secrets
- ✅ Use environment variables
- ✅ Validate all inputs
- ✅ Handle errors gracefully
- ✅ Regular security reviews

---

This document is living and should be updated as the project evolves. For questions or suggestions, please create an issue or submit a pull request.
