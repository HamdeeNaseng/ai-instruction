# Java Runner Fix & Debug System

This system provides comprehensive analysis, debugging, and monitoring for Spring Boot applications with AI-powered issue resolution and detailed R&D reporting.

## 🚀 Features

- **Automated Analysis** - Complete Spring Boot application analysis
- **AI-Powered Debugging** - Intelligent issue detection and resolution
- **Multi-Language Reporting** - Reports in English and Thai
- **Build Management** - Maven build testing and error fixing
- **Performance Monitoring** - Runtime performance analysis
- **R&D Analytics** - Detailed data collection and insights
- **Cost Tracking** - Monitor Claude API usage costs

## 📁 Generated Reports

The system creates comprehensive reports in the `rd_runner_analytics/` directory:

### Reports Directory (`reports/`)
- `analysis_report_en_[session_id].md` - English analysis report
- `analysis_report_th_[session_id].md` - Thai analysis report

### Data Directory (`data/`)
- `analysis_data_[session_id].json` - Structured metrics and analytics

### Logs Directory (`logs/`)
- `session_logs_[session_id].json` - Detailed session logs

## 🔄 Analysis Phases

### Phase 1: Pre-Build Analysis
- Project structure analysis
- pom.xml dependency checking
- Java source code analysis
- Issue detection

### Phase 2: Build & Compilation
- Maven build attempts (up to 3 retries)
- Build error analysis
- AI-powered fix suggestions
- Automatic fix application

### Phase 3: Runtime Testing
- Application startup testing
- Endpoint connectivity testing
- Database connectivity testing
- Health endpoint monitoring

### Phase 4: Performance Analysis
- Memory usage analysis
- Response time metrics
- Resource utilization monitoring
- Performance recommendations

### Phase 5: Issue Resolution
- AI-powered issue analysis
- Automated fix suggestions
- Resolution attempt tracking
- Success rate monitoring

### Phase 6: R&D Reporting
- Comprehensive report generation
- Multi-language documentation
- Data analytics compilation
- Session logs aggregation

## 🛠️ Usage

### Basic Usage
```bash
# Run the analysis system
python java_runner_fix_and_debug.py
```

### Programmatic Usage
```python
from java_runner_fix_and_debug import SpringBootRunnerAnalyzer

# Initialize analyzer
analyzer = SpringBootRunnerAnalyzer("path/to/spring-boot-app")

# Run complete analysis
results = analyzer.analyze_and_run_application()

# Check results
if results["success"]:
    print(f"Analysis complete - Cost: ${results['total_cost']:.6f}")
    print(f"Issues found: {results['issues_found']}")
    print(f"Fixes applied: {results['fixes_applied']}")
```

## 📊 Report Contents

### English Report Features
- Executive summary
- Key metrics and KPIs
- Detailed issue listings
- Applied fixes documentation
- Build attempt analysis
- Performance insights
- Security considerations
- Actionable recommendations

### Thai Report Features (รายงานภาษาไทย)
- สรุปผลการดำเนินงาน
- ตัวชี้วัดหลัก
- รายการปัญหาที่พบ
- การแก้ไขที่ดำเนินการ
- การวิเคราะห์การ build
- ข้อมูลเชิงลึกด้านประสิทธิภาพ
- ข้อพิจารณาด้านความปลอดภัย
- ข้อแนะนำที่ปฏิบัติได้

### Data Analytics
- Issues by severity distribution
- Build success rate calculations
- Fix success rate metrics
- Cost breakdown analysis
- Session performance metrics

## 🔧 Dependencies

- Python 3.8+
- anthropic (Claude API)
- python-dotenv
- Maven (for build testing)
- Java Development Kit

## ⚙️ Configuration

Set your Claude API key:
```bash
# Environment variable
export ANTHROPIC_API_KEY="your-api-key-here"

# Or create .env file
echo "ANTHROPIC_API_KEY=your-api-key-here" > .env
```

## 📈 Monitoring & Analytics

The system automatically tracks:
- **Build Performance** - Success rates, error patterns
- **Issue Resolution** - Fix success rates, common problems
- **Cost Analysis** - API usage costs by operation type
- **Session Metrics** - Duration, phases completed
- **Performance Trends** - Response times, resource usage

## 🎯 AI-Powered Features

### Intelligent Issue Detection
- Automatic problem identification
- Severity assessment
- Root cause analysis
- Solution prioritization

### Smart Fix Application
- Context-aware solutions
- Safe automatic fixes
- Manual intervention alerts
- Rollback capabilities

### Performance Optimization
- Resource usage analysis
- Bottleneck identification
- Optimization recommendations
- Best practice suggestions

## 🚨 Error Handling

The system includes robust error handling:
- **Build Failures** - Multiple retry attempts with AI fixes
- **Runtime Errors** - Graceful degradation and reporting
- **API Errors** - Retry logic and fallback strategies
- **File Operations** - Backup and recovery mechanisms

## 🔍 Troubleshooting

### Common Issues

1. **Maven Not Found**
   - Install Maven: https://maven.apache.org/install.html
   - Add Maven to PATH

2. **Build Failures**
   - Check Java version compatibility
   - Verify dependencies in pom.xml
   - Review build error logs

3. **API Key Issues**
   - Verify ANTHROPIC_API_KEY is set
   - Check API key permissions
   - Monitor usage limits

### Debug Tips

- Check session logs in `rd_runner_analytics/logs/`
- Review detailed error messages in reports
- Monitor cost usage in data analytics
- Use verbose logging for troubleshooting

## 📝 Example Output

```
🚀 Spring Boot Runner & Debug System Initialized
📁 Application: /path/to/spring-boot-app
📊 R&D Analytics: /path/to/rd_runner_analytics
🆔 Session ID: 20250804_155018

📋 PHASE 1: PRE-BUILD ANALYSIS
✅ Pre-build analysis complete - Found 2 potential issues

🔨 PHASE 2: BUILD & COMPILATION
✅ Build successful on attempt 1

🏃 PHASE 3: RUNTIME TESTING
✅ Runtime testing complete - 4/4 tests passed

📊 PHASE 4: PERFORMANCE ANALYSIS
✅ Performance analysis complete - 3 recommendations generated

🔧 PHASE 5: AI-POWERED ISSUE RESOLUTION
✅ Issue resolution complete - 2/2 issues resolved

📝 PHASE 6: R&D REPORT GENERATION
✅ Report generation complete - 4 reports created

🎉 ANALYSIS COMPLETE!
💰 Total Cost: $0.045620
🐛 Issues Found: 2
🔧 Fixes Applied: 2
```

## 🌟 Advanced Features

- **Continuous Monitoring** - Scheduled analysis runs
- **Integration APIs** - REST endpoints for external tools
- **Custom Metrics** - User-defined performance indicators
- **Alert Systems** - Notifications for critical issues
- **Historical Analysis** - Trend analysis across sessions
