# Contributing to Claude API Demos

Thank you for your interest in contributing to the Claude API Demos project! This guide will help you get started with contributing to our comprehensive demonstration suite for Anthropic's Claude API.

## 🎯 Project Overview

This project provides professional-grade demonstrations of Claude API capabilities, including:
- Basic API interactions and chat functionality
- Advanced development workflows and code analysis
- Interactive development assistance
- Real-world practical applications
- R&D analytics and decision support tools

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- Anthropic API key from [console.anthropic.com](https://console.anthropic.com/)
- Git for version control
- VS Code (recommended) for development

### Development Setup

1. **Fork and Clone the Repository**
   ```bash
   git clone https://github.com/your-username/ai-instruction.git
   cd ai-instruction
   ```

2. **Set Up Development Environment**
   ```bash
   # Install in development mode
   pip install -e .
   
   # Set your API key
   cp .env.example .env
   # Edit .env and add your ANTHROPIC_API_KEY
   ```

3. **Verify Installation**
   ```bash
   # Run tests
   python -m pytest tests/ -v
   
   # Test demos
   python run_demos.py
   ```

## 📋 Development Guidelines

### Code Style

- **Python**: Follow PEP 8 guidelines
- **Line Length**: Maximum 88 characters (Black formatter)
- **Type Hints**: Use type hints for function parameters and return values
- **Docstrings**: Use Google-style docstrings for all functions and classes

### Code Formatting

We use automated code formatting tools:

```bash
# Format code with Black
python -m black src/ tests/ --line-length 88

# Check code quality with Flake8
python -m flake8 src/ tests/ --max-line-length 88
```

### Testing Requirements

- All new features must include tests
- Tests should use mocking for API calls to avoid costs
- Maintain test coverage above 80%
- Run tests before submitting PR: `python -m pytest tests/ -v`

## 🔧 Types of Contributions

### 1. Demo Enhancements
- Add new demonstration scenarios
- Improve existing demo functionality
- Add new Claude API features

### 2. Documentation
- Improve README and guides
- Add code comments and docstrings
- Create tutorial content

### 3. Testing
- Add test cases for existing functionality
- Improve test coverage
- Add integration tests

### 4. Bug Fixes
- Fix reported issues
- Improve error handling
- Performance optimizations

### 5. New Features
- New demo types (following existing patterns)
- CLI enhancements
- VS Code integration improvements

## 📝 Contribution Process

### 1. Before You Start

- Check existing issues to see if your idea is already being worked on
- For major changes, create an issue first to discuss the approach
- Make sure you understand the project structure and conventions

### 2. Making Changes

1. **Create a Feature Branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make Your Changes**
   - Follow the coding standards
   - Add tests for new functionality
   - Update documentation if needed

3. **Test Your Changes**
   ```bash
   # Run all tests
   python -m pytest tests/ -v
   
   # Test your specific changes
   python run_demos.py
   ```

4. **Commit Your Changes**
   ```bash
   git add .
   git commit -m "feat: add new demo feature for X"
   ```

### 3. Submitting Changes

1. **Push to Your Fork**
   ```bash
   git push origin feature/your-feature-name
   ```

2. **Create a Pull Request**
   - Use a clear, descriptive title
   - Include a detailed description of changes
   - Reference any related issues
   - Include screenshots if UI changes are involved

3. **Address Review Feedback**
   - Respond to reviewer comments
   - Make requested changes
   - Update tests if necessary

## 🏗️ Project Structure

Understanding the project structure will help you contribute effectively:

```
ai-instruction/
├── src/claude_api_demos/         # Main package
│   ├── basic_demo.py            # Basic API demonstrations
│   ├── advanced_demo.py         # Advanced workflows
│   ├── interactive_demo.py      # Interactive assistance
│   ├── real_world_demo.py       # Practical applications
│   ├── rd_analytics_demo.py     # R&D analytics tools
│   └── cli.py                   # Command-line interface
├── tests/                       # Test suite
├── .vscode/                     # VS Code configuration
├── .github/                     # GitHub workflows and templates
├── run_demos.py                 # Demo runner script
└── pyproject.toml               # Package configuration
```

## 🎨 Demo Development Guidelines

When creating new demos, follow these patterns:

### Demo Class Structure
```python
class YourDemo:
    def __init__(self):
        self.client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
        self.model = "claude-3-5-sonnet-20241022"
    
    def your_demo_method(self, input_data: str) -> Dict[str, Any]:
        """
        Demonstrate specific functionality
        
        Args:
            input_data: Description of input
            
        Returns:
            Dict containing results and metadata
        """
        # Implementation here
        pass

def main():
    """Main function to run demonstrations"""
    demo = YourDemo()
    # Run demo methods
    
if __name__ == "__main__":
    main()
```

### Integration Requirements
- Add your demo to `__init__.py` exports
- Update `cli.py` with new menu option
- Update `run_demos.py` with new demo function
- Add VS Code tasks and launch configurations
- Create comprehensive tests

## 🐛 Reporting Issues

When reporting issues, please include:

1. **Environment Information**
   - Python version
   - Operating system
   - Package version

2. **Issue Description**
   - Clear description of the problem
   - Steps to reproduce
   - Expected vs actual behavior

3. **Additional Context**
   - Error messages or logs
   - Screenshots if applicable
   - Related configuration

## 📚 Resources

- [Anthropic Claude API Documentation](https://docs.anthropic.com/)
- [DataCamp Claude Tutorial](https://www.datacamp.com/tutorial/claude-code)
- [Python Packaging Guide](https://packaging.python.org/)
- [pytest Documentation](https://docs.pytest.org/)

## ❓ Getting Help

- **Discussions**: Use GitHub Discussions for questions and ideas
- **Issues**: Create issues for bugs and feature requests
- **Documentation**: Check existing docs and examples

## 🎉 Recognition

Contributors will be recognized in:
- README.md contributors section
- Release notes for significant contributions
- Special mentions for outstanding contributions

## 📄 License

By contributing to this project, you agree that your contributions will be licensed under the same license as the project.

---

Thank you for contributing to Claude API Demos! Your contributions help make this project better for everyone. 🚀
