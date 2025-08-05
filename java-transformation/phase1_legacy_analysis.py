#!/usr/bin/env python3
"""
Java Migration R&D Analytics
Specialized analysis for migrating Java applications from old versions to modern Spring Boot stack

Migration Focus:
- Old Version: Legacy Java with basic interfaces
- New Version: Spring Boot + JPA + Lombok + Modern practices
- AI-Assisted migration strategy and code transformation
"""

import os
import sys
import json
from pathlib import Path
from typing import Dict, List, Any, Optional
from dotenv import load_dotenv
import datetime

# Load environment variables
load_dotenv()

# Add the parent directory to Python path to import our R&D Analytics
parent_dir = Path(__file__).parent.parent
src_path = parent_dir / "src"
sys.path.insert(0, str(src_path))

# Also add the current directory for local rd_analytics module
current_dir = Path(__file__).parent
sys.path.insert(0, str(current_dir))

try:
    from rd_analytics import RDAnalyticsAssistant, extract_text_from_content
except ImportError:
    print("❌ Error: Could not import RDAnalyticsAssistant. Please run from the project root directory.")
    print("   Make sure you have set up the environment correctly.")
    sys.exit(1)

class JavaMigrationRDAnalytics(RDAnalyticsAssistant):
    """
    Specialized R&D Analytics for Java migration projects
    Extends the base RDAnalyticsAssistant with Java-specific analysis
    Follows GUIDELINE.md for systematic transformation workflow
    """
    
    def __init__(self):
        super().__init__()
        # Override output directory for Java migration specific outputs
        # Set path relative to current script location
        script_dir = Path(__file__).parent
        self.output_dir = script_dir / "migration-outputs"
        self.output_dir.mkdir(exist_ok=True)
        
        # Override parent class directories to use new output directory
        self.logs_dir = self.output_dir / "logs"
        self.logs_dir.mkdir(exist_ok=True)
        
        self.data_dir = self.output_dir / "data"
        self.data_dir.mkdir(exist_ok=True)
        
        self.reports_dir = self.output_dir / "reports"
        self.reports_dir.mkdir(exist_ok=True)
        
        # Reinitialize cost tracker with new output directory
        # Import the CostTracker class here to avoid circular imports
        from rd_analytics import CostTracker
        self.cost_tracker = CostTracker()
        
        # Create Java-specific directories
        self.analysis_dir = self.output_dir / "analysis"
        self.analysis_dir.mkdir(exist_ok=True)
        
        self.code_samples_dir = script_dir / "code-samples"
        self.code_samples_dir.mkdir(exist_ok=True)
        
        self.migration_plans_dir = self.output_dir / "migration-plans"
        self.migration_plans_dir.mkdir(exist_ok=True)
        
        # Load guideline for AI workflow
        self.guideline_path = script_dir / "GUIDELINE.md"
        self.guideline_content = self._load_guideline()
        
        # Initialize state management
        self.project_context_file = self.output_dir / "PROJECT_CONTEXT.json"
        self.session_memory_file = self.output_dir / "AI_SESSION_MEMORY.json"
        self.project_context = self._load_project_context()
        self.session_memory = self._load_session_memory()

    def _load_guideline(self) -> str:
        """Load the GUIDELINE.md for AI workflow instructions"""
        try:
            if self.guideline_path.exists():
                with open(self.guideline_path, 'r', encoding='utf-8') as f:
                    return f.read()
            else:
                print("⚠️ Warning: GUIDELINE.md not found. Creating basic workflow.")
                return "Basic workflow without guideline"
        except Exception as e:
            print(f"⚠️ Warning: Could not load GUIDELINE.md: {e}")
            return "Error loading guideline"

    def _load_project_context(self) -> Dict[str, Any]:
        """Load project context for large project state management"""
        if self.project_context_file.exists():
            try:
                with open(self.project_context_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except Exception as e:
                print(f"⚠️ Warning: Could not load project context: {e}")
        
        # Default project context
        return {
            "project_info": {
                "name": "Unknown",
                "java_version": "8",
                "target_java_version": "21",
                "framework": "Spring Boot 3.x",
                "database": "PostgreSQL",
                "estimated_size": "medium"
            },
            "analysis_progress": {
                "old_structure_scanned": False,
                "old_analysis_complete": False,
                "transformation_guidelines_created": False,
                "new_structure_designed": False
            },
            "current_phase": "initialization",
            "next_tasks": ["Scan legacy project structure"],
            "key_findings": {
                "critical_issues": [],
                "complexity_score": 0,
                "estimated_effort": "unknown"
            }
        }

    def _load_session_memory(self) -> Dict[str, Any]:
        """Load session memory for AI state continuity"""
        if self.session_memory_file.exists():
            try:
                with open(self.session_memory_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except Exception as e:
                print(f"⚠️ Warning: Could not load session memory: {e}")
        
        # Default session memory
        return {
            "last_session": datetime.datetime.now().isoformat(),
            "files_analyzed": [],
            "current_focus": "Project initialization",
            "pending_decisions": [],
            "code_patterns_identified": []
        }

    def _save_project_context(self):
        """Save current project context"""
        try:
            with open(self.project_context_file, 'w', encoding='utf-8') as f:
                json.dump(self.project_context, f, indent=2)
        except Exception as e:
            print(f"⚠️ Warning: Could not save project context: {e}")

    def _save_session_memory(self):
        """Save current session memory"""
        try:
            self.session_memory["last_session"] = datetime.datetime.now().isoformat()
            with open(self.session_memory_file, 'w', encoding='utf-8') as f:
                json.dump(self.session_memory, f, indent=2)
        except Exception as e:
            print(f"⚠️ Warning: Could not save session memory: {e}")

    def scan_legacy_project_structure(self, project_path: str) -> Dict[str, Any]:
        """
        Phase 1.1: Scan legacy project to generate OLD_JAVA_STRUCTURE.md
        Following GUIDELINE.md workflow
        """
        print(f"\n📁 Phase 1.1: Scanning Legacy Project Structure")
        print("=" * 60)
        print(f"🎯 Following GUIDELINE.md - Generating OLD_JAVA_STRUCTURE.md")
        
        # Update project context
        self.project_context["current_phase"] = "legacy_structure_scan"
        self.session_memory["current_focus"] = "Legacy project structure analysis"
        
        project_path_obj = Path(project_path)
        if not project_path_obj.exists():
            error_msg = f"Project path does not exist: {project_path}"
            print(f"❌ {error_msg}")
            return {"error": error_msg}
        
        # Analyze project structure
        structure_info = self._analyze_project_structure(project_path_obj)
        
        prompt = f"""
        As an expert Java architect following the GUIDELINE.md workflow, analyze this legacy Java project structure and generate OLD_JAVA_STRUCTURE.md:

        PROJECT PATH: {project_path}
        STRUCTURE ANALYSIS: {json.dumps(structure_info, indent=2)}
        
        Following the GUIDELINE.md template, create a comprehensive OLD_JAVA_STRUCTURE.md that includes:
        
        1. PROJECT OVERVIEW:
           - Project Name and description
           - Java Version identification
           - Build Tool (Maven/Gradle) analysis
           - Framework detection (if any)
           - Estimated Lines of Code
        
        2. DIRECTORY STRUCTURE:
           - Complete directory tree
           - Package organization analysis
           - Resource file locations
           - Configuration file identification
        
        3. PACKAGE ANALYSIS:
           - Core packages and their purposes
           - Class distribution per package
           - Inter-package dependencies
           - Design pattern usage identification
        
        4. DEPENDENCIES ANALYSIS:
           - External dependencies from pom.xml/build.gradle
           - Internal package dependencies
           - Version analysis and outdated dependencies
        
        5. CONFIGURATION FILES:
           - Properties files analysis
           - XML configuration files
           - Database configuration
           - Logging configuration
        
        6. DATABASE SCHEMA (if applicable):
           - Table identification from entity classes
           - Relationship mapping
           - SQL scripts analysis
        
        7. BUILD CONFIGURATION:
           - Build file analysis (pom.xml/build.gradle)
           - Compilation targets
           - Plugin configuration
           - Test configuration
        
        8. ENTRY POINTS:
           - Main class identification
           - Web endpoints (if applicable)
           - Service interfaces
           - Public APIs
        
        Generate detailed, specific analysis with actual findings from the project structure.
        """
        
        try:
            response = self.client.messages.create(
                model=self.model,
                max_tokens=4000,
                messages=[{"role": "user", "content": prompt}]
            )
            
            # Track cost and usage
            input_tokens = response.usage.input_tokens
            output_tokens = response.usage.output_tokens
            cost = self.cost_tracker.track_usage(
                model=self.model, 
                input_tokens=input_tokens, 
                output_tokens=output_tokens,
                operation="legacy_structure_scan"
            )
            
            structure_result = {
                "timestamp": self.session_id,
                "project_path": project_path,
                "structure_info": structure_info,
                "analysis": extract_text_from_content(response.content),
                "cost_info": {
                    "input_tokens": input_tokens,
                    "output_tokens": output_tokens,
                    "cost": round(cost, 6)
                }
            }
            
            print("📁 Legacy Project Structure Analysis:")
            print("-" * 40)
            print(extract_text_from_content(response.content))
            
            # Print cost summary
            self.cost_tracker.print_call_summary("Structure Scan", cost, input_tokens, output_tokens)
            
            # Save OLD_JAVA_STRUCTURE.md
            self._save_old_java_structure(structure_result)
            
            # Update progress
            self.project_context["analysis_progress"]["old_structure_scanned"] = True
            self.project_context["next_tasks"] = ["Analyze legacy code quality"]
            self.session_memory["files_analyzed"].append("OLD_JAVA_STRUCTURE.md")
            self._save_project_context()
            self._save_session_memory()
            
            return structure_result
            
        except Exception as e:
            error_msg = f"Error scanning legacy project structure: {e}"
            print(f"❌ {error_msg}")
            return {"error": error_msg}

    def _analyze_project_structure(self, project_path: Path) -> Dict[str, Any]:
        """Analyze the actual project structure from filesystem"""
        structure = {
            "project_name": project_path.name,
            "total_files": 0,
            "java_files": [],
            "config_files": [],
            "build_files": [],
            "test_files": [],
            "resource_files": [],
            "packages": set(),
            "dependencies": []
        }
        
        try:
            # Walk through the project directory
            for file_path in project_path.rglob("*"):
                if file_path.is_file():
                    structure["total_files"] += 1
                    relative_path = file_path.relative_to(project_path)
                    
                    if file_path.suffix == ".java":
                        structure["java_files"].append(str(relative_path))
                        # Extract package from Java file
                        package = self._extract_package_from_java_file(file_path)
                        if package:
                            structure["packages"].add(package)
                    
                    elif file_path.name in ["pom.xml", "build.gradle", "build.gradle.kts"]:
                        structure["build_files"].append(str(relative_path))
                        # Extract dependencies
                        deps = self._extract_dependencies_from_build_file(file_path)
                        structure["dependencies"].extend(deps)
                    
                    elif file_path.suffix in [".properties", ".yml", ".yaml", ".xml"]:
                        structure["config_files"].append(str(relative_path))
                    
                    elif "test" in str(relative_path).lower():
                        structure["test_files"].append(str(relative_path))
                    
                    elif file_path.suffix in [".sql", ".json", ".txt"]:
                        structure["resource_files"].append(str(relative_path))
        
            structure["packages"] = list(structure["packages"])
            
        except Exception as e:
            print(f"⚠️ Warning: Error analyzing project structure: {e}")
        
        return structure

    def _extract_package_from_java_file(self, file_path: Path) -> Optional[str]:
        """Extract package declaration from Java file"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                for line in f:
                    line = line.strip()
                    if line.startswith("package ") and line.endswith(";"):
                        return line[8:-1].strip()
                    elif line.startswith("public class") or line.startswith("class"):
                        break  # No package declaration found
        except Exception:
            pass
        return None

    def _extract_dependencies_from_build_file(self, file_path: Path) -> List[str]:
        """Extract dependencies from build file"""
        dependencies = []
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                if file_path.name == "pom.xml":
                    # Simple XML parsing for Maven dependencies
                    import re
                    pattern = r'<dependency>.*?<groupId>(.*?)</groupId>.*?<artifactId>(.*?)</artifactId>.*?</dependency>'
                    matches = re.findall(pattern, content, re.DOTALL)
                    for group_id, artifact_id in matches:
                        dependencies.append(f"{group_id.strip()}:{artifact_id.strip()}")
        except Exception:
            pass
        return dependencies

    def _save_old_java_structure(self, structure_result: Dict[str, Any]):
        """Save OLD_JAVA_STRUCTURE.md following GUIDELINE.md template"""
        filename = "OLD_JAVA_STRUCTURE.md"
        filepath = self.analysis_dir / filename
        
        content = f"""# Legacy Java Project Structure Analysis

**Generated:** {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
**Session ID:** {self.session_id}
**Project Path:** {structure_result['project_path']}

## Project Overview
- **Project Name:** {structure_result['structure_info']['project_name']}
- **Total Files:** {structure_result['structure_info']['total_files']}
- **Java Files:** {len(structure_result['structure_info']['java_files'])}
- **Build Tool:** {'Maven' if any('pom.xml' in f for f in structure_result['structure_info']['build_files']) else 'Gradle' if any('build.gradle' in f for f in structure_result['structure_info']['build_files']) else 'Unknown'}

## AI Analysis Results

{structure_result['analysis']}

## Discovered Structure Details

### Java Files ({len(structure_result['structure_info']['java_files'])})
```
{chr(10).join(structure_result['structure_info']['java_files'][:20])}
{'... and more' if len(structure_result['structure_info']['java_files']) > 20 else ''}
```

### Build Files
```
{chr(10).join(structure_result['structure_info']['build_files'])}
```

### Configuration Files
```
{chr(10).join(structure_result['structure_info']['config_files'][:10])}
{'... and more' if len(structure_result['structure_info']['config_files']) > 10 else ''}
```

### Packages Identified
```
{chr(10).join(structure_result['structure_info']['packages'])}
```

### Dependencies Found
```
{chr(10).join(structure_result['structure_info']['dependencies'][:15])}
{'... and more' if len(structure_result['structure_info']['dependencies']) > 15 else ''}
```

## Cost Information
- **Input Tokens:** {structure_result['cost_info']['input_tokens']:,}
- **Output Tokens:** {structure_result['cost_info']['output_tokens']:,}
- **Analysis Cost:** ${structure_result['cost_info']['cost']:.6f}
"""
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✅ Generated: {filepath}")

    def analyze_legacy_code_quality(self, project_path: str) -> Dict[str, Any]:
        """
        Phase 1.2: Analyze legacy code to generate ANALYTIC_OLD_JAVA.md
        Following GUIDELINE.md workflow
        """
        print(f"\n🔍 Phase 1.2: Analyzing Legacy Code Quality")
        print("=" * 60)
        print(f"🎯 Following GUIDELINE.md - Generating ANALYTIC_OLD_JAVA.md")
        
        # Update project context
        self.project_context["current_phase"] = "legacy_code_analysis"
        self.session_memory["current_focus"] = "Legacy code quality analysis"
        
        # Load structure analysis if available
        old_structure_file = self.analysis_dir / "OLD_JAVA_STRUCTURE.md"
        structure_context = ""
        if old_structure_file.exists():
            with open(old_structure_file, 'r', encoding='utf-8') as f:
                structure_context = f.read()[:2000]  # First 2000 chars for context
        
        # Analyze code files
        project_path_obj = Path(project_path)
        code_analysis = self._analyze_code_quality(project_path_obj)
        
        prompt = f"""
        As an expert Java architect following GUIDELINE.md, analyze this legacy Java codebase for code quality and generate ANALYTIC_OLD_JAVA.md:

        PROJECT STRUCTURE CONTEXT:
        {structure_context}
        
        CODE ANALYSIS RESULTS:
        {json.dumps(code_analysis, indent=2)}
        
        Following the GUIDELINE.md template, create comprehensive ANALYTIC_OLD_JAVA.md with:
        
        1. ARCHITECTURE PATTERNS:
           - Design patterns identification (Factory, Singleton, DAO, etc.)
           - Anti-patterns found in the codebase
           - Architecture style assessment (Layered, MVC, etc.)
        
        2. CODE QUALITY METRICS:
           - Maintainability concerns with specific examples
           - Technical debt identification and prioritization  
           - Code complexity analysis
           - Code duplication assessment
        
        3. SECURITY VULNERABILITIES:
           - SQL injection risks
           - Input validation issues
           - Authentication/Authorization gaps
           - Sensitive data handling
        
        4. PERFORMANCE BOTTLENECKS:
           - Database access patterns
           - Memory usage concerns
           - Threading issues
           - Resource management problems
        
        5. TESTING COVERAGE:
           - Current test coverage assessment
           - Missing test areas identification
           - Test quality evaluation
           - Testing framework analysis
        
        6. DEPENDENCIES ANALYSIS:
           - Outdated dependencies with security risks
           - Unused dependencies
           - Dependency conflicts
           - License compliance issues
        
        7. CONFIGURATION MANAGEMENT:
           - Configuration style assessment
           - Hard-coded values identification
           - Environment-specific configuration gaps
           - Configuration security issues
        
        8. LOGGING ANALYSIS:
           - Logging framework evaluation
           - Log level appropriateness
           - Performance impact of logging
           - Security considerations in logs
        
        9. DATABASE ACCESS PATTERNS:
           - Connection management analysis
           - Query optimization opportunities
           - Transaction management assessment
           - Data access layer evaluation
        
        Provide specific examples with code snippets and actionable recommendations.
        """
        
        try:
            response = self.client.messages.create(
                model=self.model,
                max_tokens=4000,
                messages=[{"role": "user", "content": prompt}]
            )
            
            # Track cost and usage
            input_tokens = response.usage.input_tokens
            output_tokens = response.usage.output_tokens
            cost = self.cost_tracker.track_usage(
                model=self.model, 
                input_tokens=input_tokens, 
                output_tokens=output_tokens,
                operation="legacy_code_analysis"
            )
            
            analysis_result = {
                "timestamp": self.session_id,
                "project_path": project_path,
                "code_analysis": code_analysis,
                "analysis": extract_text_from_content(response.content),
                "cost_info": {
                    "input_tokens": input_tokens,
                    "output_tokens": output_tokens,
                    "cost": round(cost, 6)
                }
            }
            
            print("🔍 Legacy Code Quality Analysis:")
            print("-" * 40)
            print(extract_text_from_content(response.content))
            
            # Print cost summary
            self.cost_tracker.print_call_summary("Code Analysis", cost, input_tokens, output_tokens)
            
            # Save ANALYTIC_OLD_JAVA.md
            self._save_analytic_old_java(analysis_result)
            
            # Update progress
            self.project_context["analysis_progress"]["old_analysis_complete"] = True
            self.project_context["next_tasks"] = ["Create transformation guidelines"]
            self.session_memory["files_analyzed"].append("ANALYTIC_OLD_JAVA.md")
            self._save_project_context()
            self._save_session_memory()
            
            return analysis_result
            
        except Exception as e:
            error_msg = f"Error analyzing legacy code quality: {e}"
            print(f"❌ {error_msg}")
            return {"error": error_msg}

    def _analyze_code_quality(self, project_path: Path) -> Dict[str, Any]:
        """Analyze code quality metrics from the actual codebase"""
        analysis = {
            "complexity_indicators": [],
            "security_issues": [],
            "performance_concerns": [],
            "code_smells": [],
            "testing_gaps": [],
            "dependency_issues": [],
            "total_java_files": 0,
            "test_files_count": 0,
            "test_coverage_ratio": 0.0
        }
        
        try:
            # Analyze Java files for common issues
            java_files = list(project_path.rglob("*.java"))
            analysis["total_java_files"] = len(java_files)
            
            for java_file in java_files[:10]:  # Analyze first 10 files as sample
                try:
                    with open(java_file, 'r', encoding='utf-8') as f:
                        content = f.read()
                        
                        # Check for common code smells
                        if "System.out.println" in content:
                            analysis["code_smells"].append(f"System.out.println usage in {java_file.name}")
                        
                        if "catch (Exception e)" in content and "e.printStackTrace()" in content:
                            analysis["security_issues"].append(f"Generic exception handling in {java_file.name}")
                        
                        if content.count("public class") > 1:
                            analysis["complexity_indicators"].append(f"Multiple classes in {java_file.name}")
                        
                        if "synchronized" in content:
                            analysis["performance_concerns"].append(f"Synchronization usage in {java_file.name}")
                        
                        if "PreparedStatement" not in content and "Statement" in content:
                            analysis["security_issues"].append(f"Potential SQL injection risk in {java_file.name}")
                            
                except Exception:
                    continue
            
            # Analyze test coverage
            test_files = list(project_path.rglob("*Test.java"))
            analysis["test_files_count"] = len(test_files)
            analysis["test_coverage_ratio"] = len(test_files) / max(len(java_files), 1)
            
            if analysis["test_coverage_ratio"] < 0.3:
                analysis["testing_gaps"].append("Low test coverage - less than 30% of classes have tests")
            
        except Exception as e:
            analysis["dependency_issues"].append(f"Analysis error: {str(e)}")
        
        return analysis

    def _save_analytic_old_java(self, analysis_result: Dict[str, Any]):
        """Save ANALYTIC_OLD_JAVA.md following GUIDELINE.md template"""
        filename = "ANALYTIC_OLD_JAVA.md"
        filepath = self.analysis_dir / filename
        
        content = f"""# Legacy Java Code Analysis

**Generated:** {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
**Session ID:** {self.session_id}
**Project Path:** {analysis_result['project_path']}

## Code Quality Summary
- **Total Java Files:** {analysis_result['code_analysis'].get('total_java_files', 'Unknown')}
- **Test Files:** {analysis_result['code_analysis'].get('test_files_count', 0)}
- **Test Coverage Ratio:** {analysis_result['code_analysis'].get('test_coverage_ratio', 0):.2%}

## AI Analysis Results

{analysis_result['analysis']}

## Automated Code Analysis Findings

### Complexity Indicators
```
{chr(10).join(analysis_result['code_analysis'].get('complexity_indicators', []))}
```

### Security Issues Found
```
{chr(10).join(analysis_result['code_analysis'].get('security_issues', []))}
```

### Performance Concerns
```
{chr(10).join(analysis_result['code_analysis'].get('performance_concerns', []))}
```

### Code Smells Detected
```
{chr(10).join(analysis_result['code_analysis'].get('code_smells', []))}
```

### Testing Gaps
```
{chr(10).join(analysis_result['code_analysis'].get('testing_gaps', []))}
```

## Cost Information
- **Input Tokens:** {analysis_result['cost_info']['input_tokens']:,}
- **Output Tokens:** {analysis_result['cost_info']['output_tokens']:,}
- **Analysis Cost:** ${analysis_result['cost_info']['cost']:.6f}
"""
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✅ Generated: {filepath}")

    def analyze_legacy_codebase(self, code_info: Dict[str, Any]) -> Dict[str, Any]:
        """
        Analyze legacy Java codebase to understand current architecture
        """
        print(f"\n🔍 Analyzing Legacy Java Codebase")
        print("=" * 60)
        
        code_str = json.dumps(code_info, indent=2)
        
        prompt = f"""
        As an expert Java architect and migration specialist, analyze this legacy Java codebase:

        LEGACY CODEBASE INFO:
        {code_str}
        
        Please provide detailed analysis of:
        1. ARCHITECTURE ASSESSMENT:
           - Current design patterns used
           - Package structure and organization
           - Interface usage and abstraction levels
           - Dependencies and coupling analysis
        
        2. TECHNOLOGY STACK EVALUATION:
           - Java version and features used
           - Framework dependencies (if any)
           - Database access patterns
           - Configuration management approach
        
        3. CODE QUALITY METRICS:
           - Maintainability concerns
           - Technical debt identification
           - Performance bottlenecks
           - Security vulnerabilities
        
        4. MODERNIZATION OPPORTUNITIES:
           - Areas suitable for Spring Boot migration
           - JPA/Hibernate integration points
           - Lombok adoption benefits
           - Microservices decomposition potential
        
        5. MIGRATION COMPLEXITY ASSESSMENT:
           - High-risk areas requiring careful handling
           - Quick wins for immediate improvement  
           - Dependencies that need updating
           - Testing strategy requirements
        
        Provide specific recommendations with code examples where helpful.
        """
        
        try:
            response = self.client.messages.create(
                model=self.model,
                max_tokens=4000,
                messages=[{"role": "user", "content": prompt}]
            )
            
            # Track cost and usage
            input_tokens = response.usage.input_tokens
            output_tokens = response.usage.output_tokens
            cost = self.cost_tracker.track_usage(
                model=self.model, 
                input_tokens=input_tokens, 
                output_tokens=output_tokens,
                operation="legacy_codebase_analysis"
            )
            
            analysis_result = {
                "timestamp": self.session_id,
                "codebase_info": code_info,
                "analysis": extract_text_from_content(response.content),
                "cost_info": {
                    "input_tokens": input_tokens,
                    "output_tokens": output_tokens,
                    "cost": round(cost, 6)
                }
            }
            
            print("📊 Legacy Codebase Analysis:")
            print("-" * 40)
            print(extract_text_from_content(response.content))
            
            # Print cost summary
            self.cost_tracker.print_call_summary("Legacy Analysis", cost, input_tokens, output_tokens)
            
            # Save analysis
            self._save_legacy_analysis(analysis_result)
            
            return analysis_result
            
        except Exception as e:
            error_msg = f"Error analyzing legacy codebase: {e}"
            print(f"❌ {error_msg}")
            return {"error": error_msg}

    def design_modern_architecture(self, legacy_analysis: Dict[str, Any], requirements: Dict[str, Any]) -> Dict[str, Any]:
        """
        Design modern Spring Boot architecture based on legacy analysis
        """
        print(f"\n🏗️ Designing Modern Spring Boot Architecture")
        print("=" * 60)
        
        context = {
            "legacy_analysis": legacy_analysis,
            "requirements": requirements
        }
        context_str = json.dumps(context, indent=2)
        
        prompt = f"""
        As an expert Spring Boot architect, design a modern architecture for this Java migration:

        CONTEXT:
        {context_str}
        
        Please provide a comprehensive modern architecture design:
        
        1. SPRING BOOT APPLICATION STRUCTURE:
           - Main application class setup
           - Package organization (controller, service, repository, entity)
           - Configuration classes (SecurityConfig, DatabaseConfig, etc.)
           - Application properties structure
        
        2. JPA/HIBERNATE DATA LAYER:
           - Entity design with proper annotations
           - Repository interfaces extending JpaRepository
           - Custom query methods
           - Database migration scripts (Flyway/Liquibase)
        
        3. LOMBOK INTEGRATION:
           - Entity classes with @Data, @Entity annotations
           - Builder patterns for complex objects
           - @Slf4j for logging
           - Constructor generation optimization
        
        4. SPRING BOOT FEATURES TO LEVERAGE:
           - Auto-configuration benefits
           - Actuator for monitoring
           - Profiles for environment management
           - Testing framework integration
        
        5. MIGRATION STRATEGY:
           - Phase-by-phase implementation plan
           - Parallel running approach (if needed)
           - Data migration considerations
           - Rollback strategies
        
        6. CODE EXAMPLES:
           - Before/After comparisons
           - Key transformation patterns
           - Configuration examples
           - Test case templates
        
        Focus on practical, implementable solutions with specific code examples.
        """
        
        try:
            response = self.client.messages.create(
                model=self.model,
                max_tokens=4000,
                messages=[{"role": "user", "content": prompt}]
            )
            
            # Track cost and usage
            input_tokens = response.usage.input_tokens
            output_tokens = response.usage.output_tokens
            cost = self.cost_tracker.track_usage(
                model=self.model, 
                input_tokens=input_tokens, 
                output_tokens=output_tokens,
                operation="modern_architecture_design"
            )
            
            design_result = {
                "timestamp": self.session_id,
                "context": context,
                "architecture_design": extract_text_from_content(response.content),
                "cost_info": {
                    "input_tokens": input_tokens,
                    "output_tokens": output_tokens,
                    "cost": round(cost, 6)
                }
            }
            
            print("🏗️ Modern Architecture Design:")
            print("-" * 40)
            print(extract_text_from_content(response.content))
            
            # Print cost summary
            self.cost_tracker.print_call_summary("Architecture Design", cost, input_tokens, output_tokens)
            
            # Save design
            self._save_architecture_design(design_result)
            
            return design_result
            
        except Exception as e:
            error_msg = f"Error designing modern architecture: {e}"
            print(f"❌ {error_msg}")
            return {"error": error_msg}

    def generate_migration_plan(self, legacy_analysis: Dict[str, Any], 
                               architecture_design: Dict[str, Any],
                               constraints: Dict[str, Any]) -> Dict[str, Any]:
        """
        Generate detailed migration plan with phases, timelines, and risks
        """
        print(f"\n📋 Generating Migration Plan")
        print("=" * 60)
        
        context = {
            "legacy_analysis": legacy_analysis,
            "architecture_design": architecture_design,
            "constraints": constraints
        }
        context_str = json.dumps(context, indent=2)
        
        prompt = f"""
        As an expert migration project manager and Java architect, create a detailed migration plan:

        CONTEXT:
        {context_str}
        
        Create a comprehensive migration plan with:
        
        1. MIGRATION PHASES:
           - Phase breakdown with clear deliverables
           - Dependencies between phases
           - Success criteria for each phase
           - Estimated timeline and effort
        
        2. TECHNICAL MIGRATION STEPS:
           - Code transformation priorities
           - Database migration approach
           - Configuration management migration
           - Testing strategy implementation
        
        3. RISK ASSESSMENT & MITIGATION:
           - High-risk areas identification
           - Mitigation strategies for each risk
           - Contingency plans
           - Rollback procedures
        
        4. RESOURCE REQUIREMENTS:
           - Team composition and skills needed
           - Training requirements
           - Infrastructure needs
           - Budget considerations
        
        5. PARALLEL DEVELOPMENT STRATEGY:
           - How to maintain old system while building new
           - Data synchronization approaches
           - Feature flag strategies
           - Gradual cutover plan
        
        6. QUALITY ASSURANCE:
           - Testing phases (unit, integration, performance)
           - Code review processes
           - Migration validation procedures
           - Performance benchmarking
        
        7. GO-LIVE STRATEGY:
           - Production deployment approach
           - Monitoring and alerting setup
           - User training and documentation
           - Support transition plan
        
        Provide specific timelines, milestones, and actionable tasks.
        """
        
        try:
            response = self.client.messages.create(
                model=self.model,
                max_tokens=4000,
                messages=[{"role": "user", "content": prompt}]
            )
            
            # Track cost and usage
            input_tokens = response.usage.input_tokens
            output_tokens = response.usage.output_tokens
            cost = self.cost_tracker.track_usage(
                model=self.model, 
                input_tokens=input_tokens, 
                output_tokens=output_tokens,
                operation="migration_plan_generation"
            )
            
            plan_result = {
                "timestamp": self.session_id,
                "context": context,
                "migration_plan": extract_text_from_content(response.content),
                "cost_info": {
                    "input_tokens": input_tokens,
                    "output_tokens": output_tokens,
                    "cost": round(cost, 6)
                }
            }
            
            print("📋 Migration Plan:")
            print("-" * 40)
            print(extract_text_from_content(response.content))
            
            # Print cost summary
            self.cost_tracker.print_call_summary("Migration Plan", cost, input_tokens, output_tokens)
            
            # Save plan
            self._save_migration_plan(plan_result)
            
            return plan_result
            
        except Exception as e:
            error_msg = f"Error generating migration plan: {e}"
            print(f"❌ {error_msg}")
            return {"error": error_msg}

    def _save_legacy_analysis(self, analysis: Dict[str, Any]):
        """Save legacy codebase analysis"""
        filename = f"legacy_analysis_{self.session_id}.md"
        filepath = self.analysis_dir / filename
        
        content = f"""# Legacy Java Codebase Analysis
        
**Session ID:** {self.session_id}
**Analysis Date:** {analysis['timestamp']}

## Codebase Information
```json
{json.dumps(analysis['codebase_info'], indent=2)}
```

## Analysis Results

{analysis['analysis']}

## Cost Information
- Input Tokens: {analysis['cost_info']['input_tokens']:,}
- Output Tokens: {analysis['cost_info']['output_tokens']:,}
- Analysis Cost: ${analysis['cost_info']['cost']:.6f}
"""
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

    def _save_architecture_design(self, design: Dict[str, Any]):
        """Save modern architecture design"""
        filename = f"modern_architecture_{self.session_id}.md"
        filepath = self.analysis_dir / filename
        
        content = f"""# Modern Spring Boot Architecture Design
        
**Session ID:** {self.session_id}
**Design Date:** {design['timestamp']}

## Design Context  
```json
{json.dumps(design['context'], indent=2)}
```

## Architecture Design

{design['architecture_design']}

## Cost Information
- Input Tokens: {design['cost_info']['input_tokens']:,}
- Output Tokens: {design['cost_info']['output_tokens']:,}
- Design Cost: ${design['cost_info']['cost']:.6f}
"""
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

    def _save_migration_plan(self, plan: Dict[str, Any]):
        """Save migration plan"""
        filename = f"migration_plan_{self.session_id}.md"
        filepath = self.migration_plans_dir / filename
        
        content = f"""# Java Migration Implementation Plan
        
**Session ID:** {self.session_id}
**Plan Date:** {plan['timestamp']}

## Planning Context
```json
{json.dumps(plan['context'], indent=2)}
```

## Migration Plan

{plan['migration_plan']}

## Cost Information
- Input Tokens: {plan['cost_info']['input_tokens']:,}
- Output Tokens: {plan['cost_info']['output_tokens']:,}
- Planning Cost: ${plan['cost_info']['cost']:.6f}
"""
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)


def demonstrate_java_migration_rd():
    """Demonstrate Java Migration R&D Analytics"""
    print("☕ Java Migration R&D Analytics - Legacy to Modern")
    print("=" * 70)
    
    java_rd = JavaMigrationRDAnalytics()
    
    # Sample legacy codebase information
    legacy_info = {
        "java_version": "Java 8",
        "architecture_type": "Monolithic",
        "design_patterns": ["Factory", "Singleton", "DAO"],
        "database_access": "JDBC with custom connection management",
        "configuration": "Properties files",
        "logging": "java.util.logging",
        "testing": "JUnit 4",
        "build_tool": "Maven",
        "estimated_loc": 50000,
        "main_packages": [
            "com.company.core",
            "com.company.dao", 
            "com.company.service",
            "com.company.util"
        ],
        "key_interfaces": [
            "UserService",
            "OrderService", 
            "PaymentProcessor",
            "ReportGenerator"
        ],
        "main_challenges": [
            "Tight coupling between layers",
            "Manual dependency injection",
            "Boilerplate code for entities",
            "Complex configuration management",
            "Limited testing coverage"
        ]
    }
    
    # 1. Analyze legacy codebase
    print("\n1️⃣ LEGACY CODEBASE ANALYSIS")
    legacy_analysis = java_rd.analyze_legacy_codebase(legacy_info)
    
    # Modern requirements
    modern_requirements = {
        "target_java_version": "Java 21",
        "framework": "Spring Boot 3.x",
        "data_layer": "Spring Data JPA with Hibernate",
        "build_tool": "Maven with Spring Boot plugin",
        "testing": "JUnit 5 + Mockito + TestContainers",
        "monitoring": "Spring Actuator + Micrometer",
        "security": "Spring Security",
        "api_style": "RESTful with OpenAPI documentation",
        "deployment": "Docker containers",
        "performance_requirements": {
            "response_time": "< 200ms for 95% of requests",
            "throughput": "1000+ requests/second",
            "availability": "99.9% uptime"
        }
    }
    
    # 2. Design modern architecture
    print("\n2️⃣ MODERN ARCHITECTURE DESIGN")
    architecture_design = java_rd.design_modern_architecture(legacy_analysis, modern_requirements)
    
    # Migration constraints
    migration_constraints = {
        "timeline": "6 months",
        "team_size": 4,
        "budget": "$200,000",
        "downtime_tolerance": "< 4 hours",
        "parallel_operation_required": True,
        "data_migration_window": "Weekend maintenance windows",
        "training_budget": "$20,000",
        "infrastructure_budget": "$30,000"
    }
    
    # 3. Generate migration plan
    print("\n3️⃣ MIGRATION PLAN GENERATION")
    migration_plan = java_rd.generate_migration_plan(
        legacy_analysis, 
        architecture_design, 
        migration_constraints
    )
    
    # 4. Generate session summary
    print("\n4️⃣ SESSION SUMMARY")
    session_summary = java_rd.get_session_summary()
    
    # 5. Generate multilingual summary (if implemented)
    if hasattr(java_rd, 'generate_multilingual_summary'):
        print("\n5️⃣ MULTILINGUAL SUMMARY")
        multilingual_summary = java_rd.generate_multilingual_summary(session_summary)
    
    print(f"\n🎉 Java Migration R&D Analysis Complete!")
    print(f"📁 All outputs saved to: {java_rd.output_dir}")
    print(f"📊 Session ID: {java_rd.session_id}")
    
    # Final cost summary
    final_cost = java_rd.cost_tracker.get_summary()
    print(f"\n💰 Migration Analysis Cost Summary:")
    print(f"   Total API calls: {final_cost['total_api_calls']}")
    print(f"   Total tokens: {final_cost['total_tokens']:,}")
    print(f"   Total cost: ${final_cost['total_cost']:.6f}")
    print(f"   💡 Average cost per analysis: ${final_cost['average_cost_per_call']:.6f}")


def main():
    """Main function for Java Migration R&D Analytics"""
    try:
        demonstrate_java_migration_rd()
        
        print("\n" + "="*70)
        print("☕ Java Migration R&D Features:")
        print("  ✅ Legacy codebase analysis and assessment")
        print("  ✅ Modern Spring Boot architecture design")
        print("  ✅ Detailed migration planning with phases")
        print("  ✅ Risk assessment and mitigation strategies")
        print("  ✅ Cost tracking for migration analysis")
        print("  ✅ Comprehensive documentation generation")
        print("\n💡 Use for:")
        print("  - Java legacy system modernization")
        print("  - Spring Boot migration planning")
        print("  - Technical debt reduction strategies")
        print("  - Architecture transformation projects")
        print("  - Migration cost and timeline estimation")
        
    except Exception as e:
        print(f"❌ Error running Java Migration R&D: {e}")
        print("Make sure your ANTHROPIC_API_KEY is set correctly")


if __name__ == "__main__":
    main()
