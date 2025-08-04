#!/usr/bin/env python3
"""
AI-Guided Java Migration System - Step by Step Interface
Interactive command-line interface for comprehensive Java application migration
with AI assistance at every step.

Features:
- Step-by-step migration workflow
- Interactive user guidance
- AI-powered recommendations
- Progress tracking and recovery
- Comprehensive reporting
- Multi-language support
"""

import os
import sys
import json
import time
from pathlib import Path
from typing import Dict, List, Any, Optional
from datetime import datetime
import subprocess
import traceback

# Add current directory to path
sys.path.insert(0, str(Path(__file__).parent))

def print_banner():
    """Print the application banner"""
    print("="*80)
    print("🤖 AI-GUIDED JAVA MIGRATION SYSTEM")
    print("   Step-by-Step Transformation with AI Intelligence")
    print("="*80)
    print(f"📅 Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"📁 Working Directory: {Path.cwd()}")
    print("="*80)

def check_prerequisites() -> Dict[str, bool]:
    """Check system prerequisites"""
    print("\n🔍 CHECKING SYSTEM PREREQUISITES")
    print("-" * 40)
    
    checks = {
        "python": False,
        "api_key": False,
        "java_project": False,
        "modules": False
    }
    
    # Check Python version
    python_version = sys.version_info
    if python_version.major >= 3 and python_version.minor >= 8:
        checks["python"] = True
        print(f"✅ Python {python_version.major}.{python_version.minor}.{python_version.micro}")
    else:
        print(f"❌ Python {python_version.major}.{python_version.minor} (requires 3.8+)")
    
    # Check API key
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if api_key:
        checks["api_key"] = True
        masked_key = api_key[:8] + "..." + api_key[-4:] if len(api_key) > 12 else "***"
        print(f"✅ Claude API Key: {masked_key}")
    else:
        print("❌ ANTHROPIC_API_KEY not found")
    
    # Check for Java project
    sample_project = Path("code-samples/imedX")
    if sample_project.exists():
        checks["java_project"] = True
        print(f"✅ Sample Java Project: {sample_project}")
    else:
        print(f"❌ Sample Java Project not found: {sample_project}")
    
    # Check required modules
    try:
        import anthropic
        from dotenv import load_dotenv
        checks["modules"] = True
        print("✅ Required Python modules available")
    except ImportError as e:
        print(f"❌ Missing modules: {e}")
    
    return checks

def get_user_choice(prompt: str, options: List[str], default: Optional[str] = None) -> str:
    """Get user choice with validation"""
    while True:
        print(f"\n{prompt}")
        for i, option in enumerate(options, 1):
            marker = " (default)" if default and option.lower().startswith(default.lower()) else ""
            print(f"  {i}. {option}{marker}")
        
        try:
            choice = input("\nEnter your choice (number or text): ").strip()
            
            # Handle default
            if not choice and default:
                for i, option in enumerate(options):
                    if option.lower().startswith(default.lower()):
                        return option
            
            # Handle numeric input
            if choice.isdigit():
                idx = int(choice) - 1
                if 0 <= idx < len(options):
                    return options[idx]
            
            # Handle text input
            for option in options:
                if choice.lower() in option.lower():
                    return option
            
            print("❌ Invalid choice. Please try again.")
            
        except KeyboardInterrupt:
            print("\n\n👋 Migration cancelled by user.")
            sys.exit(0)

def confirm_action(message: str, default: bool = True) -> bool:
    """Get user confirmation"""
    default_text = "Y/n" if default else "y/N"
    while True:
        try:
            response = input(f"{message} ({default_text}): ").strip().lower()
            if not response:
                return default
            if response in ['y', 'yes', 'true', '1']:
                return True
            if response in ['n', 'no', 'false', '0']:
                return False
            print("Please enter 'y' for yes or 'n' for no.")
        except KeyboardInterrupt:
            print("\n\n👋 Migration cancelled by user.")
            sys.exit(0)

def run_step_with_progress(step_name: str, step_function, *args, **kwargs) -> Any:
    """Run a step with progress indication"""
    print(f"\n🔄 {step_name}")
    print("-" * (len(step_name) + 4))
    
    start_time = time.time()
    try:
        result = step_function(*args, **kwargs)
        duration = time.time() - start_time
        print(f"✅ {step_name} completed in {duration:.1f}s")
        return result
    except Exception as e:
        duration = time.time() - start_time
        print(f"❌ {step_name} failed after {duration:.1f}s: {e}")
        raise

class AIGuidedMigration:
    """Main AI-guided migration orchestrator"""
    
    def __init__(self):
        self.session_id = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.migration_state = {
            "session_id": self.session_id,
            "start_time": datetime.now().isoformat(),
            "steps_completed": [],
            "current_step": None,
            "total_cost": 0.0,
            "errors": [],
            "results": {}
        }
        self.migration_log = Path("migration-session.log")
        
    def log_message(self, message: str, level: str = "INFO"):
        """Log message to file and console"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] {level}: {message}"
        
        with open(self.migration_log, "a", encoding="utf-8") as f:
            f.write(log_entry + "\n")
        
        if level == "ERROR":
            print(f"❌ {message}")
        elif level == "WARNING":
            print(f"⚠️ {message}")
        else:
            print(f"ℹ️ {message}")

    def save_state(self):
        """Save migration state"""
        state_file = Path(f"migration_state_{self.session_id}.json")
        with open(state_file, "w", encoding="utf-8") as f:
            json.dump(self.migration_state, f, indent=2, ensure_ascii=False)

    def run_interactive_migration(self) -> Dict[str, Any]:
        """Run the complete interactive migration process"""
        
        print("\n🚀 STARTING AI-GUIDED MIGRATION")
        print("="*40)
        
        try:
            # Step 1: Project Selection
            self._step1_project_selection()
            
            # Step 2: Migration Strategy
            self._step2_migration_strategy()
            
            # Step 3: Legacy Analysis
            self._step3_legacy_analysis()
            
            # Step 4: Transformation Planning
            self._step4_transformation_planning()
            
            # Step 5: Code Generation
            self._step5_code_generation()
            
            # Step 6: Testing & Validation
            self._step6_testing_validation()
            
            # Step 7: Final Report
            self._step7_final_report()
            
            return self.migration_state
            
        except KeyboardInterrupt:
            print("\n\n👋 Migration interrupted by user.")
            self.save_state()
            return self.migration_state
        except Exception as e:
            self.log_message(f"Migration failed: {e}", "ERROR")
            self.migration_state["errors"].append(str(e))
            self.save_state()
            raise

    def _step1_project_selection(self):
        """Step 1: Select and validate source project"""
        self.migration_state["current_step"] = "project_selection"
        
        print("\n📁 STEP 1: PROJECT SELECTION")
        print("=" * 30)
        
        # Show available projects
        code_samples_dir = Path("code-samples")
        if code_samples_dir.exists():
            projects = [p for p in code_samples_dir.iterdir() if p.is_dir()]
            if projects:
                print(f"\nFound {len(projects)} sample project(s):")
                for project in projects:
                    file_count = len(list(project.rglob("*.java")))
                    print(f"  📂 {project.name} ({file_count} Java files)")
                
                # Auto-select if only one project
                if len(projects) == 1:
                    selected_project = projects[0]
                    if confirm_action(f"Use project '{selected_project.name}'?"):
                        self.migration_state["source_project"] = str(selected_project)
                        self.log_message(f"Selected project: {selected_project}")
                    else:
                        raise ValueError("No project selected")
                else:
                    # Multiple projects - let user choose
                    project_names = [p.name for p in projects]
                    choice = get_user_choice("Select a project to migrate:", project_names)
                    selected_project = code_samples_dir / choice
                    self.migration_state["source_project"] = str(selected_project)
                    self.log_message(f"Selected project: {selected_project}")
            else:
                raise ValueError("No Java projects found in code-samples directory")
        else:
            # Manual project selection
            print("No code-samples directory found.")
            project_path = input("Enter the path to your Java project: ").strip()
            if not Path(project_path).exists():
                raise ValueError(f"Project path does not exist: {project_path}")
            
            self.migration_state["source_project"] = project_path
            self.log_message(f"Selected custom project: {project_path}")
        
        # Validate project
        project_path = Path(self.migration_state["source_project"])
        java_files = list(project_path.rglob("*.java"))
        if not java_files:
            raise ValueError("No Java files found in selected project")
        
        print(f"✅ Project validated: {len(java_files)} Java files found")
        self.migration_state["steps_completed"].append("project_selection")

    def _step2_migration_strategy(self):
        """Step 2: Define migration strategy and options"""
        self.migration_state["current_step"] = "migration_strategy"
        
        print("\n🎯 STEP 2: MIGRATION STRATEGY")
        print("=" * 30)
        
        # Migration type selection
        migration_types = [
            "Full Migration - Complete transformation to Spring Boot",
            "Partial Migration - Modernize specific components only",
            "Analysis Only - Generate reports and recommendations"
        ]
        
        migration_choice = get_user_choice(
            "What type of migration do you want to perform?",
            migration_types,
            default="Full"
        )
        
        self.migration_state["migration_type"] = migration_choice
        
        # Target framework selection
        if "Full" in migration_choice or "Partial" in migration_choice:
            frameworks = [
                "Spring Boot 3.x with Java 21",
                "Spring Boot 2.x with Java 11",
                "Custom configuration"
            ]
            
            framework_choice = get_user_choice(
                "Select target framework:",
                frameworks,
                default="Spring Boot 3.x"
            )
            
            self.migration_state["target_framework"] = framework_choice
        
        # Additional options
        print("\n🔧 Additional Options:")
        
        options = {}
        options["generate_tests"] = confirm_action("Generate unit tests?", default=True)
        options["include_security"] = confirm_action("Include Spring Security configuration?", default=True)
        options["database_migration"] = confirm_action("Include database migration scripts?", default=True)
        options["docker_support"] = confirm_action("Generate Docker configuration?", default=False)
        
        self.migration_state["options"] = options
        
        print(f"\n✅ Migration strategy configured:")
        print(f"   Type: {migration_choice}")
        if "target_framework" in self.migration_state:
            print(f"   Framework: {self.migration_state['target_framework']}")
        print(f"   Options: {sum(options.values())}/{len(options)} enabled")
        
        self.migration_state["steps_completed"].append("migration_strategy")

    def _step3_legacy_analysis(self):
        """Step 3: Analyze legacy codebase"""
        self.migration_state["current_step"] = "legacy_analysis"
        
        print("\n🔍 STEP 3: LEGACY CODE ANALYSIS")
        print("=" * 32)
        
        if not confirm_action("Start legacy code analysis with AI?"):
            print("⏭️ Skipping legacy analysis")
            return
        
        # Import and run legacy analysis
        try:
            from java_migration_rd_analytics import JavaMigrationRDAnalytics
            
            analyzer = JavaMigrationRDAnalytics()
            project_path = Path(self.migration_state["source_project"])
            
            print("🤖 AI is analyzing your legacy codebase...")
            
            # Run analysis
            analysis_result = run_step_with_progress(
                "Scanning project structure",
                analyzer.scan_legacy_project_structure,
                str(project_path)
            )
            
            quality_result = run_step_with_progress(
                "Analyzing code quality",
                analyzer.analyze_legacy_code_quality,
                str(project_path)
            )
            
            # Store results
            self.migration_state["results"]["legacy_analysis"] = {
                "structure": analysis_result,
                "quality": quality_result,
                "cost": getattr(analyzer, "total_cost", 0.0)
            }
            
            self.migration_state["total_cost"] += getattr(analyzer, "total_cost", 0.0)
            
            print(f"\n📊 Analysis Summary:")
            if analysis_result:
                print(f"   • Project structure analyzed")
                print(f"   • Code quality assessed")
                print(f"   • AI cost: ${getattr(analyzer, 'total_cost', 0.0):.6f}")
            
        except ImportError:
            self.log_message("Legacy analysis module not available", "WARNING")
            print("⚠️ Legacy analysis module not available, continuing...")
        except Exception as e:
            self.log_message(f"Legacy analysis failed: {e}", "ERROR")
            if not confirm_action("Continue migration without legacy analysis?"):
                raise
        
        self.migration_state["steps_completed"].append("legacy_analysis")

    def _step4_transformation_planning(self):
        """Step 4: Create transformation plan"""
        self.migration_state["current_step"] = "transformation_planning"
        
        print("\n📋 STEP 4: TRANSFORMATION PLANNING")
        print("=" * 35)
        
        if self.migration_state["migration_type"].startswith("Analysis Only"):
            print("⏭️ Skipping transformation planning for analysis-only mode")
            return
        
        if not confirm_action("Generate AI-powered transformation plan?"):
            print("⏭️ Using default transformation plan")
            return
        
        try:
            from java_transform import JavaTransformationEngine
            
            project_path = self.migration_state["source_project"]
            transformer = JavaTransformationEngine(project_path)
            
            print("🤖 AI is creating your transformation plan...")
            
            # Run planning phases
            planning_results = {}
            
            # Phase 1: Legacy Analysis
            if confirm_action("Run Phase 1 (Legacy Analysis)?", default=True):
                phase1_result = run_step_with_progress(
                    "Executing Phase 1 - Legacy Analysis",
                    self._run_transformation_phase,
                    transformer, 1
                )
                planning_results["phase1"] = phase1_result
            
            # Phase 2: Transformation Planning  
            if confirm_action("Run Phase 2 (Transformation Planning)?", default=True):
                phase2_result = run_step_with_progress(
                    "Executing Phase 2 - Transformation Planning",
                    self._run_transformation_phase,
                    transformer, 2
                )
                planning_results["phase2"] = phase2_result
            
            # Phase 3: Modern Implementation Design
            if confirm_action("Run Phase 3 (Modern Implementation Design)?", default=True):
                phase3_result = run_step_with_progress(
                    "Executing Phase 3 - Modern Implementation Design",
                    self._run_transformation_phase,
                    transformer, 3
                )
                planning_results["phase3"] = phase3_result
            
            self.migration_state["results"]["transformation_planning"] = planning_results
            self.migration_state["total_cost"] += getattr(transformer, "total_cost", 0.0)
            
            print(f"\n📋 Planning Summary:")
            print(f"   • {len(planning_results)} phases completed")
            print(f"   • Documentation generated")
            print(f"   • AI cost: ${getattr(transformer, 'total_cost', 0.0):.6f}")
            
        except ImportError:
            self.log_message("Transformation engine not available", "WARNING")
            print("⚠️ Transformation engine not available")
        except Exception as e:
            self.log_message(f"Transformation planning failed: {e}", "ERROR")
            if not confirm_action("Continue without transformation planning?"):
                raise
        
        self.migration_state["steps_completed"].append("transformation_planning")

    def _step5_code_generation(self):
        """Step 5: Generate modern code"""
        self.migration_state["current_step"] = "code_generation"
        
        print("\n💻 STEP 5: CODE GENERATION")
        print("=" * 26)
        
        if self.migration_state["migration_type"].startswith("Analysis Only"):
            print("⏭️ Skipping code generation for analysis-only mode")
            return
        
        if not confirm_action("Generate Spring Boot application code?"):
            print("⏭️ Skipping code generation")
            return
        
        try:
            from java_transform import JavaTransformationEngine
            
            project_path = self.migration_state["source_project"]
            transformer = JavaTransformationEngine(project_path)
            
            print("🤖 AI is generating your Spring Boot application...")
            
            # Phase 4: Code Generation
            phase4_result = run_step_with_progress(
                "Executing Phase 4 - Code Generation", 
                self._run_transformation_phase,
                transformer, 4
            )
            
            # Check for failures and attempt fixes
            if phase4_result and phase4_result.get("components_failed"):
                print(f"\n🔧 Found {len(phase4_result['components_failed'])} failed components")
                
                if confirm_action("Attempt AI-powered fixes?", default=True):
                    fix_result = run_step_with_progress(
                        "Applying AI-powered fixes",
                        transformer.fix_failed_components,
                        phase4_result
                    )
                    phase4_result = fix_result
            
            self.migration_state["results"]["code_generation"] = phase4_result
            self.migration_state["total_cost"] += getattr(transformer, "total_cost", 0.0)
            
            # Show generation summary
            if phase4_result:
                components_generated = len(phase4_result.get("components_generated", []))
                components_failed = len(phase4_result.get("components_failed", []))
                success_rate = phase4_result.get("success_rate", 0)
                
                print(f"\n💻 Code Generation Summary:")
                print(f"   • Components generated: {components_generated}")
                print(f"   • Components failed: {components_failed}")
                print(f"   • Success rate: {success_rate}%")
                
                if phase4_result.get("application_directory"):
                    print(f"   • Application saved to: {Path(phase4_result['application_directory']).name}")
            
        except ImportError:
            self.log_message("Code generation engine not available", "WARNING")
            print("⚠️ Code generation engine not available")
        except Exception as e:
            self.log_message(f"Code generation failed: {e}", "ERROR")
            if not confirm_action("Continue without code generation?"):
                raise
        
        self.migration_state["steps_completed"].append("code_generation")

    def _step6_testing_validation(self):
        """Step 6: Test and validate generated code"""
        self.migration_state["current_step"] = "testing_validation"
        
        print("\n🧪 STEP 6: TESTING & VALIDATION")
        print("=" * 30)
        
        # Check if we have generated code to test
        if "code_generation" not in self.migration_state["steps_completed"]:
            print("⏭️ No code generated, skipping testing")
            return
        
        code_gen_result = self.migration_state["results"].get("code_generation")
        if not code_gen_result or not code_gen_result.get("application_directory"):
            print("⏭️ No application directory found, skipping testing")
            return
        
        if not confirm_action("Test the generated Spring Boot application?"):
            print("⏭️ Skipping testing and validation")
            return
        
        try:
            from java_runner_fix_and_debug import SpringBootRunnerAnalyzer
            
            app_path = code_gen_result["application_directory"] 
            print(f"🧪 Testing application at: {Path(app_path).name}")
            
            runner = SpringBootRunnerAnalyzer(app_path)
            
            # Run comprehensive testing
            test_results = run_step_with_progress(
                "Running comprehensive testing and analysis",
                runner.analyze_and_run_application
            )
            
            self.migration_state["results"]["testing_validation"] = test_results
            self.migration_state["total_cost"] += getattr(runner, "total_cost", 0.0)
            
            # Show test summary
            if test_results:
                phases_completed = len(test_results.get("phases", {}))
                issues_found = test_results.get("issues_found", 0)
                fixes_applied = test_results.get("fixes_applied", 0)
                success = test_results.get("success", False)
                
                print(f"\n🧪 Testing Summary:")
                print(f"   • Test phases completed: {phases_completed}")
                print(f"   • Issues found: {issues_found}")
                print(f"   • Fixes applied: {fixes_applied}")
                print(f"   • Overall success: {'✅' if success else '❌'}")
                print(f"   • Reports generated: English & Thai")
            
        except ImportError:
            self.log_message("Testing engine not available", "WARNING")
            print("⚠️ Testing engine not available")
        except Exception as e:
            self.log_message(f"Testing failed: {e}", "ERROR")
            if not confirm_action("Continue without testing?"):
                raise
        
        self.migration_state["steps_completed"].append("testing_validation")

    def _step7_final_report(self):
        """Step 7: Generate final migration report"""
        self.migration_state["current_step"] = "final_report"
        
        print("\n📄 STEP 7: FINAL REPORT GENERATION")
        print("=" * 35)
        
        # Update final state
        self.migration_state["end_time"] = datetime.now().isoformat()
        self.migration_state["duration"] = (
            datetime.now() - datetime.fromisoformat(self.migration_state["start_time"])
        ).total_seconds()
        
        # Generate summary report
        report_content = self._generate_migration_report()
        
        # Save report
        report_file = Path(f"migration_report_{self.session_id}.md")
        with open(report_file, "w", encoding="utf-8") as f:
            f.write(report_content)
        
        print(f"📄 Migration report saved: {report_file}")
        
        # Save final state
        self.save_state()
        
        # Show final summary
        self._show_final_summary()
        
        self.migration_state["steps_completed"].append("final_report")

    def _run_transformation_phase(self, transformer, phase_number: int) -> Dict[str, Any]:
        """Run a specific transformation phase"""
        if phase_number == 1:
            # Phase 1: Legacy Analysis
            phase1_result = transformer._phase1_legacy_analysis()
            return phase1_result
        elif phase_number == 2:
            # Phase 2: Transformation Planning
            phase1_result = transformer.migration_state.get("phase1", {})
            phase2_result = transformer._phase2_transformation_planning(phase1_result)
            return phase2_result
        elif phase_number == 3:
            # Phase 3: Modern Implementation
            phase1_result = transformer.migration_state.get("phase1", {})
            phase2_result = transformer.migration_state.get("phase2", {})
            phase3_result = transformer._phase3_modern_implementation(phase1_result, phase2_result)
            return phase3_result
        elif phase_number == 4:
            # Phase 4: Code Generation
            phase1_result = transformer.migration_state.get("phase1", {})
            phase2_result = transformer.migration_state.get("phase2", {})
            phase3_result = transformer.migration_state.get("phase3", {})
            phase4_result = transformer._phase4_code_generation(phase1_result, phase2_result, phase3_result)
            return phase4_result
        else:
            raise ValueError(f"Invalid phase number: {phase_number}")

    def _generate_migration_report(self) -> str:
        """Generate comprehensive migration report"""
        report = f"""# AI-Guided Java Migration Report

**Session ID:** {self.session_id}
**Date:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
**Duration:** {self.migration_state.get('duration', 0):.1f} seconds

## Migration Overview

**Source Project:** {self.migration_state.get('source_project', 'Unknown')}
**Migration Type:** {self.migration_state.get('migration_type', 'Unknown')}
**Target Framework:** {self.migration_state.get('target_framework', 'Not specified')}

## Steps Completed

"""
        
        # Add completed steps
        for i, step in enumerate(self.migration_state["steps_completed"], 1):
            report += f"{i}. ✅ {step.replace('_', ' ').title()}\n"
        
        # Add results summary
        report += f"\n## Results Summary\n\n"
        report += f"**Total AI Cost:** ${self.migration_state['total_cost']:.6f}\n"
        report += f"**Steps Completed:** {len(self.migration_state['steps_completed'])}/7\n"
        report += f"**Errors Encountered:** {len(self.migration_state['errors'])}\n"
        
        # Add detailed results
        if self.migration_state["results"]:
            report += f"\n## Detailed Results\n\n"
            for phase, result in self.migration_state["results"].items():
                report += f"### {phase.replace('_', ' ').title()}\n"
                if isinstance(result, dict):
                    if "success" in result:
                        status = "✅ Success" if result["success"] else "❌ Failed"
                        report += f"**Status:** {status}\n"
                    if "cost" in result:
                        report += f"**Cost:** ${result['cost']:.6f}\n"
                report += "\n"
        
        # Add recommendations
        report += f"\n## Recommendations\n\n"
        
        if "code_generation" in self.migration_state["steps_completed"]:
            report += "- Review generated Spring Boot application\n"
            report += "- Test all endpoints and functionality\n"
            report += "- Configure database connections\n"
            report += "- Set up CI/CD pipeline\n"
        
        if "testing_validation" in self.migration_state["steps_completed"]:
            report += "- Address any remaining test failures\n"
            report += "- Add additional unit tests\n"
            report += "- Performance tune the application\n"
        
        report += f"\n## Next Steps\n\n"
        report += "1. Deploy the application to a test environment\n"
        report += "2. Conduct user acceptance testing\n"
        report += "3. Plan production deployment\n"
        report += "4. Set up monitoring and logging\n"
        
        return report

    def _show_final_summary(self):
        """Show final migration summary"""
        print(f"\n🎉 MIGRATION COMPLETED!")
        print("=" * 25)
        
        print(f"📊 **Summary Statistics:**")
        print(f"   • Session ID: {self.session_id}")
        print(f"   • Duration: {self.migration_state.get('duration', 0):.1f} seconds")
        print(f"   • Steps completed: {len(self.migration_state['steps_completed'])}/7")
        print(f"   • Total AI cost: ${self.migration_state['total_cost']:.6f}")
        print(f"   • Errors: {len(self.migration_state['errors'])}")
        
        if self.migration_state["steps_completed"]:
            print(f"\n✅ **Completed Steps:**")
            for step in self.migration_state["steps_completed"]:
                print(f"   • {step.replace('_', ' ').title()}")
        
        if self.migration_state["errors"]:
            print(f"\n❌ **Errors Encountered:**")
            for error in self.migration_state["errors"]:
                print(f"   • {error}")
        
        # Show output files
        output_files = []
        
        # Check for transformation outputs
        transform_outputs = Path("transformation-outputs")
        if transform_outputs.exists():
            output_files.append(f"📁 {transform_outputs}")
        
        # Check for testing reports
        rd_analytics = Path("rd_runner_analytics")
        if rd_analytics.exists():
            output_files.append(f"📁 {rd_analytics}")
        
        # Check for migration report
        report_files = list(Path(".").glob(f"migration_report_{self.session_id}.*"))
        for report in report_files:
            output_files.append(f"📄 {report}")
        
        if output_files:
            print(f"\n📁 **Generated Files:**")
            for file_item in output_files:
                print(f"   • {file_item}")


def main():
    """Main function for AI-guided migration"""
    print_banner()
    
    # Check prerequisites
    checks = check_prerequisites()
    
    # Check critical requirements
    if not checks["python"]:
        print("\n❌ Python 3.8+ required. Please upgrade Python.")
        return
    
    if not checks["api_key"]:
        print("\n❌ Claude API key required.")
        print("Set ANTHROPIC_API_KEY environment variable:")
        print("   export ANTHROPIC_API_KEY='your-api-key-here'")
        return
    
    if not checks["modules"]:
        print("\n❌ Required Python modules missing.")
        print("Install with: pip install anthropic python-dotenv")
        return
    
    # Show system status
    ready_count = sum(checks.values())
    print(f"\n📊 System Status: {ready_count}/4 checks passed")
    
    if ready_count < 3:
        if not confirm_action("Continue with incomplete setup?", default=False):
            print("👋 Setup incomplete. Please resolve issues and try again.")
            return
    
    # Start migration
    print(f"\n🚀 All systems ready! Starting AI-guided migration...")
    
    try:
        migration = AIGuidedMigration()
        results = migration.run_interactive_migration()
        
        print(f"\n🎊 Migration completed successfully!")
        print(f"📄 Check migration_report_{migration.session_id}.md for details")
        
    except KeyboardInterrupt:
        print(f"\n\n👋 Migration cancelled by user.")
    except Exception as e:
        print(f"\n❌ Migration failed: {e}")
        print(f"📝 Check migration-session.log for details")
        if confirm_action("Show detailed error?", default=False):
            traceback.print_exc()


if __name__ == "__main__":
    main()
