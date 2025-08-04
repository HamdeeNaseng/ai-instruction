# AI-Guided Java Migration System - User Guide

## 🚀 Quick Start

The AI migration system is now located in the **root directory** for easy access to your `.env` configuration.

### Prerequisites

1. **Python 3.8+** installed
2. **API Key** set in `.env` file:
   ```
   ANTHROPIC_API_KEY=your-key-here
   ```
3. **Required modules** installed:
   ```bash
   pip install anthropic python-dotenv
   ```

### Usage

From the root directory, simply run:
```bash
python run_ai_migration.py
```

## 🎯 Features

### 7-Step Migration Process
1. **📁 Project Selection** - Choose your Java project
2. **🎯 Migration Strategy** - Define migration approach
3. **🔍 Legacy Analysis** - AI-powered code analysis
4. **📋 Transformation Planning** - Generate migration plan
5. **💻 Code Generation** - Create Spring Boot application
6. **🧪 Testing & Validation** - Comprehensive testing
7. **📄 Final Report** - Complete migration report

### Migration Options
- **Full Migration** - Complete Spring Boot transformation
- **Partial Migration** - Modernize specific components
- **Analysis Only** - Reports and recommendations

### Framework Targets
- Spring Boot 3.x with Java 21 (recommended)
- Spring Boot 2.x with Java 11
- Custom configuration

## 📊 What Gets Generated

### Analysis Reports
- `OLD_JAVA_STRUCTURE.md` - Legacy project structure
- `ANALYTIC_OLD_JAVA.md` - Code quality analysis
- Cost tracking and AI usage metrics

### Migration Outputs
- Modern Spring Boot application code
- Configuration files (application.yml, pom.xml)
- Unit tests and security configurations
- Docker support (optional)

### Validation Reports
- English and Thai language reports
- Performance analysis
- Error detection and fixes
- R&D analytics data

## 🔧 Configuration

### Environment Variables (.env file)
```env
ANTHROPIC_API_KEY=your-claude-api-key-here
```

### Project Structure
```
ai-instruction/
├── .env                     # Your API key here
├── run_ai_migration.py      # Main migration system
├── java-transformation/     # Transformation modules
│   ├── code-samples/        # Sample projects
│   ├── java_transform.py    # Core transformation engine
│   └── java_runner_fix_and_debug.py  # Testing system
└── migration_report_*.md    # Generated reports
```

## 💡 Tips

- **API Cost**: Typical migration costs $0.02-$0.05 in Claude API usage
- **Time**: Full migration takes 5-10 minutes depending on project size
- **Interruption**: Press Ctrl+C to safely stop - progress is saved
- **Resume**: Check `migration_state_*.json` to review session details

## 🎯 Example Usage

1. **Quick Analysis**: Choose "Analysis Only" for code quality reports
2. **Full Migration**: Choose "Full Migration" for complete Spring Boot transformation
3. **Custom Project**: Provide your own Java project path when prompted

## 📝 Generated Files

After migration, you'll find:
- `migration_report_YYYYMMDD_HHMMSS.md` - Comprehensive report
- `migration-session.log` - Detailed execution log
- `java-transformation/transformation-outputs/` - Generated code
- `java-transformation/rd_runner_analytics/` - Analysis reports

The system is designed to be user-friendly with step-by-step guidance throughout the migration process!
