# Java Transformation AI Assistant

This project provides an AI-powered Java transformation system that converts legacy Java applications to modern Spring Boot applications using Claude API.

## 🚀 Quick Start

### 1. Setup Environment
```powershell
# Set your API key
$env:ANTHROPIC_API_KEY = "your-api-key-here"

# Or create .env file in root directory
echo "ANTHROPIC_API_KEY=your-api-key-here" > .env
```

### 2. AI-Guided Interactive Migration (Recommended)
```powershell
# Run the step-by-step AI migration system from root directory
python run_ai_migration.py
```

### 3. Direct Transformation Engine (Advanced)
```powershell
# Navigate to the transformation directory
cd java-transformation

# Transform legacy Java project directly
python java_transform.py
```

## 🤖 AI-Guided Migration System

The `run_ai_migration.py` script provides an **interactive, step-by-step migration experience** that guides you through the entire Java modernization process.

### Features
- **Interactive Setup** - Step-by-step project selection and configuration
- **AI-Powered Analysis** - Comprehensive legacy code assessment
- **Guided Decision Making** - Choose migration strategy and options
- **Progress Tracking** - Visual progress indicators and session management
- **Error Recovery** - Built-in error handling and retry mechanisms
- **Comprehensive Reporting** - Detailed migration reports and documentation

### Migration Workflow

1. **📁 Project Selection** - Choose your legacy Java project
2. **🎯 Migration Strategy** - Define approach (Full/Partial/Analysis Only)
3. **🔍 Legacy Analysis** - AI analyzes your existing codebase
4. **📋 Transformation Planning** - Create detailed migration plan
5. **💻 Code Generation** - Generate modern Spring Boot application
6. **🧪 Testing & Validation** - Test and validate generated code
7. **📄 Final Report** - Comprehensive migration documentation

### Prerequisites
- Python 3.8+
- Claude API key (Anthropic)
- Legacy Java project to migrate

### Usage Example
```powershell
# 1. Set up your API key
$env:ANTHROPIC_API_KEY = "sk-ant-api03-..."

# 2. Run the interactive migration
python run_ai_migration.py

# Follow the interactive prompts:
# ✅ Python 3.13.1
# ✅ Claude API Key: sk-ant-a...GwAA
# ✅ Sample Java Project: imedX (12 Java files)
# ✅ Required Python modules available
# 
# 📊 System Status: 4/4 checks passed
# 🚀 All systems ready! Starting AI-guided migration...
```

## 📁 Project Structure

- `java-transformation/` - Main transformation system
  - `java_transform.py` - Core transformation engine
  - `java_migration_rd_analytics.py` - R&D analytics and monitoring
  - `GUIDELINE.md` - Transformation workflow documentation
  - `code-samples/` - Sample legacy Java projects
  - `transformation-outputs/` - Generated transformation results

## 🔄 Transformation Process

The system follows a comprehensive 4-phase transformation process:

1. **Phase 1: Legacy Analysis** - Analyze existing Java codebase
2. **Phase 2: Transformation Planning** - Create migration strategy
3. **Phase 3: Modern Implementation** - Design new Spring Boot architecture
4. **Phase 4: Code Generation** - Generate actual Spring Boot code

## ✨ Features

- **AI-Powered Analysis** - Deep understanding of legacy Java code
- **Comprehensive Documentation** - Detailed transformation reports
- **Error Handling** - Robust error recovery and iterative fixing
- **Cost Tracking** - Monitor Claude API usage and costs
- **File Management** - Smart file updates and backup system
- **Testing Integration** - Validate generated Spring Boot applications

## 📋 Requirements

- Python 3.8+
- Anthropic Claude API key
- Legacy Java project for transformation

## 🛠️ Usage Examples

### Basic Transformation
```python
from java_transform import JavaTransformationEngine

# Initialize with legacy project path
transformer = JavaTransformationEngine("path/to/legacy/project")

# Execute full transformation
results = transformer.execute_full_transformation()

# Fix any failed components
if results.get("components_failed"):
    results = transformer.fix_failed_components(results)

# Test generated code
test_results = transformer.test_generated_code(results)
```

### Advanced Features
```python
# Check existing files before transformation
file_info = transformer._check_file_exists(Path("output/pom.xml"))

# Safe Claude API calls with retry logic
response = transformer._safe_claude_call("Generate Spring Boot config")

# Update files with merge strategies
result = transformer._update_existing_file(
    file_path, 
    new_content, 
    merge_strategy="merge"
)
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

## 🔧 Error Handling & Recovery

The system includes robust error handling:

- **Content Filtering Recovery** - Automatic retry with modified prompts
- **Rate Limit Handling** - Intelligent backoff and retry
- **File Backup System** - Automatic backups before modifications
- **Iterative Fixing** - Multiple attempts to resolve failed components
- **Comprehensive Testing** - Validation of generated code

## 📊 Cost Monitoring

Track your Claude API usage:

```
Phase 1: Legacy Analysis - $0.041
Phase 2: Transformation Planning - $0.093  
Phase 3: Modern Implementation - $0.056
Phase 4: Code Generation - $0.059
Total Investment: $0.249
```

## 🧪 Testing Generated Code

The system automatically tests generated Spring Boot applications:

- **File Structure Validation** - Ensures all required files exist
- **pom.xml Validation** - Checks Maven configuration
- **Java Syntax Checking** - Basic Java code validation
- **Dependency Analysis** - Verifies Spring Boot dependencies

## 🔄 Iterative Development

For production use, the system supports:

- **Incremental Updates** - Update existing projects
- **Merge Strategies** - Smart content merging
- **Error Recovery** - Fix failed transformations
- **Progress Tracking** - Monitor transformation progress

## 📝 Documentation

Each transformation generates comprehensive documentation:

- `OLD_JAVA_STRUCTURE.md` - Legacy codebase analysis
- `ANALYTIC_OLD_JAVA.md` - Code quality assessment
- `GUILDLINE_TO_TRANSFORM.md` - Transformation strategy
- `RULE_CODE.md` - Coding standards and rules
- `CLEAN_ARCHITECH.md` - Clean architecture design
- `NEW_JAVA_STRUCTURE.md` - Modern application structure
- `ANALYTIC_NEW_JAVA.md` - New architecture analysis

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test with sample Java projects
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙋‍♂️ Support

For support and questions:
- Check the documentation in `java-transformation/GUIDELINE.md`
- Review transformation outputs for debugging
- Check error logs and cost tracking information
