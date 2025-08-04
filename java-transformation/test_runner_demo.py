#!/usr/bin/env python3
"""
Test and Demo Script for Java Runner Fix & Debug System
Demonstrates the system capabilities without requiring Maven installation
"""

import os
import sys
from pathlib import Path
from datetime import datetime

# Add current directory to path
sys.path.insert(0, str(Path(__file__).parent))

try:
    from java_runner_fix_and_debug import SpringBootRunnerAnalyzer
except ImportError as e:
    print(f"❌ Import error: {e}")
    sys.exit(1)

def demo_system_capabilities():
    """Demonstrate the Java Runner system capabilities"""
    print("🎯 Java Runner Fix & Debug System Demo")
    print("="*50)
    
    # Check if Spring Boot app exists
    script_dir = Path(__file__).parent
    app_path = script_dir / "transformation-outputs" / "phase4-code-generation" / "spring-boot-app"
    
    if not app_path.exists():
        print("❌ Generated Spring Boot application not found.")
        print(f"   Expected: {app_path}")
        print("   Please run java_transform.py first.")
        return False
    
    print(f"✅ Found Spring Boot application: {app_path.name}")
    
    try:
        # Initialize the analyzer
        print("\n🚀 Initializing SpringBootRunnerAnalyzer...")
        analyzer = SpringBootRunnerAnalyzer(str(app_path))
        
        # Test individual components
        print("\n📋 Testing Pre-Build Analysis...")
        structure = analyzer._analyze_project_structure()
        print(f"   • Found {len(structure['java_files'])} Java files")
        print(f"   • Found {len(structure['resource_files'])} resource files")
        print(f"   • Total files: {structure['total_files']}")
        
        print("\n🔍 Testing pom.xml Analysis...")
        pom_analysis = analyzer._analyze_pom_xml()
        if pom_analysis['exists']:
            print(f"   • pom.xml found")
            print(f"   • Dependencies: {len(pom_analysis.get('dependencies', []))}")
            print(f"   • Java version: {pom_analysis.get('java_version', 'Not specified')}")
        else:
            print("   • pom.xml not found")
        
        print("\n☕ Testing Source Code Analysis...")
        source_analysis = analyzer._analyze_source_code()
        print(f"   • Classes found: {len(source_analysis['classes_found'])}")
        print(f"   • Controllers: {len(source_analysis['controllers'])}")
        print(f"   • Services: {len(source_analysis['services'])}")
        print(f"   • Repositories: {len(source_analysis['repositories'])}")
        print(f"   • Entities: {len(source_analysis['entities'])}")
        if source_analysis.get('main_class'):
            print(f"   • Main class: {source_analysis['main_class']}")
        
        print("\n🔧 Testing Issue Detection...")
        issues = analyzer._detect_prebuild_issues(structure, pom_analysis, source_analysis)
        if issues:
            for i, issue in enumerate(issues, 1):
                severity = issue.get('severity', 'unknown').upper()
                issue_type = issue.get('type', 'unknown')
                description = issue.get('description', 'No description')
                print(f"   {i}. [{severity}] {issue_type}: {description}")
        else:
            print("   • No issues detected")
        
        print("\n📝 Testing Report Generation...")
        
        # Test English report generation
        en_report = analyzer._generate_english_report()
        print(f"   • English report: {Path(en_report['file_path']).name}")
        
        # Test Thai report generation  
        th_report = analyzer._generate_thai_report()
        print(f"   • Thai report: {Path(th_report['file_path']).name}")
        
        # Test data analysis
        data_report = analyzer._generate_data_analysis_report()
        print(f"   • Data analysis: {Path(data_report['file_path']).name}")
        
        print(f"\n💰 Total AI cost for demo: ${analyzer.total_cost:.6f}")
        
        print("\n🎉 Demo completed successfully!")
        print(f"📁 Check reports in: {analyzer.rd_dir}")
        
        return True
        
    except Exception as e:
        print(f"❌ Demo failed: {e}")
        import traceback
        traceback.print_exc()
        return False

def show_generated_files():
    """Show the generated files and their contents"""
    print("\n📄 Generated Files Overview")
    print("="*40)
    
    rd_dir = Path(__file__).parent / "rd_runner_analytics"
    
    if not rd_dir.exists():
        print("❌ No analytics directory found")
        return
    
    # Show reports
    reports_dir = rd_dir / "reports"
    if reports_dir.exists():
        print(f"\n📊 Reports Directory: {reports_dir}")
        for report_file in reports_dir.glob("*.md"):
            file_size = report_file.stat().st_size if report_file.exists() else 0
            print(f"   • {report_file.name} ({file_size} bytes)")
    
    # Show data files
    data_dir = rd_dir / "data"
    if data_dir.exists():
        print(f"\n📈 Data Directory: {data_dir}")
        for data_file in data_dir.glob("*.json"):
            file_size = data_file.stat().st_size if data_file.exists() else 0
            print(f"   • {data_file.name} ({file_size} bytes)")
    
    # Show logs
    logs_dir = rd_dir / "logs"
    if logs_dir.exists():
        print(f"\n📝 Logs Directory: {logs_dir}")
        for log_file in logs_dir.glob("*.json"):
            file_size = log_file.stat().st_size if log_file.exists() else 0
            print(f"   • {log_file.name} ({file_size} bytes)")

def main():
    """Main demo function"""
    print("🚀 Java Runner Fix & Debug System Test")
    print("=" * 60)
    print(f"📅 Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Check API key
    if not os.getenv("ANTHROPIC_API_KEY"):
        print("❌ ANTHROPIC_API_KEY not set")
        print("   Please set your Claude API key before running")
        return
    
    print("✅ Claude API key found")
    
    # Run demo
    success = demo_system_capabilities()
    
    if success:
        # Show generated files
        show_generated_files()
        
        print("\n🎯 Next Steps:")
        print("   1. Review the generated reports")
        print("   2. Install Maven for full build testing")
        print("   3. Run full analysis: python java_runner_fix_and_debug.py")
        print("   4. Check the RUNNER_README.md for detailed usage")
    else:
        print("\n❌ Demo failed - check error messages above")

if __name__ == "__main__":
    main()
