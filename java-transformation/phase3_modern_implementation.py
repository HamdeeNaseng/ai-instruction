#!/usr/bin/env python3
"""
Phase 3: Modern Implementation
Design and implement the new Spring Boot project structure based on transformation planning.

This phase focuses on:
- Designing new Java structure (NEW_JAVA_STRUCTURE.md)
- Analyzing new architecture (ANALYTIC_NEW_JAVA.md)
- Creating Spring Boot project templates
- Implementing clean architecture patterns
- Setting up modern dependencies and configurations
"""

import os
import json
import sys
import shutil
import traceback
from pathlib import Path
from typing import Dict, List, Any, Optional
import anthropic
from dotenv import load_dotenv
import datetime

# Load environment variables
load_dotenv()

# Add parent directory to path for imports
parent_dir = Path(__file__).parent.parent
src_path = parent_dir / "src"
sys.path.insert(0, str(src_path))
sys.path.insert(0, str(parent_dir))

try:
    from rd_analytics import RDAnalyticsAssistant, extract_text_from_content
    from rd_analytics import CostTracker as ExternalCostTracker
    CostTracker = ExternalCostTracker  # type: ignore
except ImportError:
    print("⚠️ Warning: Could not import RDAnalyticsAssistant. Some features may be limited.")
    # Provide fallback implementations
    class CostTracker:
        def track_usage(self, *args, **kwargs):
            return 0.0
    
    def extract_text_from_content(content_blocks):
        if hasattr(content_blocks, '__iter__'):
            for block in content_blocks:
                if hasattr(block, 'text'):
                    return block.text
        return str(content_blocks)


class ModernImplementationDesigner:
    """
    Phase 3: Modern Implementation Designer
    Creates modern Spring Boot architecture and implementation plans
    """
    
    def __init__(self):
        self.client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
        self.model = "claude-3-5-sonnet-20241022"
        self.cost_tracker = CostTracker()
        self.session_id = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        
        # Create output directories
        self.output_dir = Path("transformation-outputs") / "phase3-modern-implementation"
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
        print(f"🏗️ Modern Implementation Designer Initialized")
        print(f"📁 Output Directory: {self.output_dir}")

    def design_new_java_structure(self, legacy_analysis: Dict[str, Any], 
                                 transformation_plan: Dict[str, Any]) -> Dict[str, Any]:
        """
        Design NEW_JAVA_STRUCTURE.md based on legacy analysis and transformation plan
        """
        print(f"\n🏗️ Designing New Java Structure")
        print("=" * 60)
        
        context = {
            "legacy_info": legacy_analysis,
            "transformation_guidelines": transformation_plan
        }
        
        prompt = f"""
        As an expert Spring Boot architect, design a comprehensive NEW_JAVA_STRUCTURE.md:

        CONTEXT:
        {json.dumps(context, indent=2)[:4000]}
        
        Create a modern Spring Boot 3.x project structure including:
        
        1. PROJECT OVERVIEW:
           - Project name, Java 21+, Spring Boot 3.x
           - Database (PostgreSQL/MySQL), testing frameworks
           - Build tool configuration
        
        2. COMPLETE DIRECTORY STRUCTURE:
           ```
           src/
           ├── main/
           │   ├── java/com/company/project/
           │   │   ├── ProjectApplication.java
           │   │   ├── config/ (Database, Security, Cache)
           │   │   ├── controller/ (REST endpoints)
           │   │   ├── service/ (Business logic)
           │   │   ├── repository/ (Data access)
           │   │   ├── entity/ (JPA entities)
           │   │   ├── dto/ (Data transfer objects)
           │   │   ├── exception/ (Custom exceptions)
           │   │   └── util/ (Utility classes)
           │   └── resources/
           │       ├── application.yml
           │       └── db/migration/
           └── test/ (Complete test structure)
           ```
        
        3. MODERN COMPONENTS:
           - Main application class with proper annotations
           - Configuration classes for all aspects
           - REST controllers with OpenAPI documentation
           - Service layer with transaction management
           - Repository layer with JPA specifications
           - Entity classes with Lombok and validation
        
        4. CONFIGURATION FILES:
           - Comprehensive application.yml with profiles
           - Database migration scripts (Flyway)
           - Docker and Kubernetes configurations
        
        5. BUILD CONFIGURATION:
           - Modern Maven/Gradle with Spring Boot 3.x
           - Essential dependencies and plugins
           - Multi-environment build profiles
        
        6. TESTING STRATEGY:
           - Unit, integration, and architecture tests
           - TestContainers for database testing
           - Performance testing setup
        
        7. MONITORING & OBSERVABILITY:
           - Spring Boot Actuator configuration
           - Prometheus metrics and health checks
           - Structured logging with JSON
        
        Provide specific, implementable designs based on the legacy system analysis.
        Format as complete markdown document following GUIDELINE.md template.
        """
        
        try:
            response = self.client.messages.create(
                model=self.model,
                max_tokens=4000,
                messages=[{"role": "user", "content": prompt}]
            )
            
            # Track cost
            input_tokens = response.usage.input_tokens
            output_tokens = response.usage.output_tokens
            cost = self.cost_tracker.track_usage(
                model=self.model,
                input_tokens=input_tokens,
                output_tokens=output_tokens,
                operation="new_structure_design"
            )
            
            structure_content = extract_text_from_content(response.content)
            
            # Save to file
            structure_file = self.output_dir / "NEW_JAVA_STRUCTURE.md"
            with open(structure_file, 'w', encoding='utf-8') as f:
                f.write(f"""# NEW_JAVA_STRUCTURE.md

**Generated:** {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}  
**Session ID:** {self.session_id}  
**Cost:** ${cost:.6f}

---

{structure_content}

---

*Generated by Phase 3: Modern Implementation Designer*
""")
            
            result = {
                "timestamp": datetime.datetime.now().isoformat(),
                "file_path": str(structure_file),
                "content": structure_content,
                "cost_info": {
                    "input_tokens": input_tokens,
                    "output_tokens": output_tokens,
                    "cost": round(cost, 6)
                }
            }
            
            print(f"✅ NEW_JAVA_STRUCTURE.md generated - Cost: ${cost:.6f}")
            print(f"📄 Saved to: {structure_file}")
            
            return result
            
        except Exception as e:
            error_msg = f"Error designing new structure: {e}"
            print(f"❌ {error_msg}")
            return {"error": error_msg, "cost_info": {"cost": 0}}

    def analyze_new_architecture(self, legacy_analysis: Dict[str, Any],
                                transformation_plan: Dict[str, Any],
                                new_structure: Dict[str, Any]) -> Dict[str, Any]:
        """
        Generate ANALYTIC_NEW_JAVA.md analyzing the new architecture quality
        """
        print(f"\n🔍 Analyzing New Architecture")
        print("=" * 60)
        
        context = {
            "legacy_info": legacy_analysis,
            "transformation_plan": transformation_plan,
            "new_structure": new_structure.get("content", "")[:2000]
        }
        
        prompt = f"""
        As an expert software architect, create comprehensive ANALYTIC_NEW_JAVA.md:

        CONTEXT:
        {json.dumps(context, indent=2)[:4000]}
        
        Analyze and validate the new Spring Boot architecture including:
        
        1. ARCHITECTURE QUALITY ASSESSMENT:
           - Clean architecture adherence (✅/❌ with scores)
           - SOLID principles implementation 
           - Dependency direction validation
           - Layer separation effectiveness
        
        2. SPRING BOOT BEST PRACTICES:
           - Auto-configuration usage (score/10)
           - Dependency injection patterns (score/10)
           - Configuration management (score/10)
           - Exception handling strategy (score/10)
        
        3. CODE QUALITY METRICS:
           - Projected test coverage percentage
           - Maintainability improvements vs legacy
           - Technical debt reduction estimates
           - Performance enhancement projections
        
        4. SECURITY ASSESSMENT:
           - Authentication/Authorization design
           - Input validation strategy
           - Security vulnerability mitigation
           - Data protection measures
        
        5. DATABASE DESIGN ANALYSIS:
           - JPA/Hibernate optimization
           - Query performance considerations
           - Connection pooling configuration
           - Transaction management strategy
        
        6. API DESIGN ASSESSMENT:
           - RESTful API compliance (score/10)
           - OpenAPI documentation coverage
           - Error handling patterns
           - Versioning and backward compatibility
        
        7. CONFIGURATION ANALYSIS:
           - Profile management effectiveness
           - External configuration flexibility
           - Environment variable usage
           - Feature flag implementation
        
        8. MONITORING & OBSERVABILITY:
           - Actuator endpoint configuration
           - Metrics collection setup
           - Structured logging implementation
           - Health check comprehensiveness
        
        9. TESTING STRATEGY EFFECTIVENESS:
           - Test pyramid compliance
           - Testing tool utilization
           - Integration test coverage
           - Performance testing approach
        
        10. MIGRATION SUCCESS METRICS:
            - Feature parity assessment (percentage)
            - Performance improvement projections
            - Maintainability enhancements
            - Development productivity gains
        
        11. QUALITY GATES STATUS:
            - [ ] All architectural rules enforced
            - [ ] Security requirements met
            - [ ] Performance benchmarks defined
            - [ ] Monitoring configured
            - [ ] Documentation complete
        
        12. RECOMMENDATIONS:
            - Immediate action items with timelines
            - Medium-term improvements
            - Long-term enhancements
            - Risk mitigation strategies
        
        13. OVERALL ASSESSMENT:
            - Migration Success Score: X/100
            - Readiness for Production: ✅/❌
            - Recommended next steps
        
        Provide specific metrics, actionable recommendations, and clear go/no-go decisions.
        Format as complete markdown document following GUIDELINE.md template.
        """
        
        try:
            response = self.client.messages.create(
                model=self.model,
                max_tokens=4000,
                messages=[{"role": "user", "content": prompt}]
            )
            
            # Track cost
            input_tokens = response.usage.input_tokens
            output_tokens = response.usage.output_tokens
            cost = self.cost_tracker.track_usage(
                model=self.model,
                input_tokens=input_tokens,
                output_tokens=output_tokens,
                operation="new_architecture_analysis"
            )
            
            analysis_content = extract_text_from_content(response.content)
            
            # Save to file
            analysis_file = self.output_dir / "ANALYTIC_NEW_JAVA.md"
            with open(analysis_file, 'w', encoding='utf-8') as f:
                f.write(f"""# ANALYTIC_NEW_JAVA.md

**Generated:** {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}  
**Session ID:** {self.session_id}  
**Cost:** ${cost:.6f}

---

{analysis_content}

---

*Generated by Phase 3: Modern Implementation Designer*
""")
            
            result = {
                "timestamp": datetime.datetime.now().isoformat(),
                "file_path": str(analysis_file),
                "content": analysis_content,
                "cost_info": {
                    "input_tokens": input_tokens,
                    "output_tokens": output_tokens,
                    "cost": round(cost, 6)
                }
            }
            
            print(f"✅ ANALYTIC_NEW_JAVA.md generated - Cost: ${cost:.6f}")
            print(f"📄 Saved to: {analysis_file}")
            
            return result
            
        except Exception as e:
            error_msg = f"Error analyzing new architecture: {e}"
            print(f"❌ {error_msg}")
            return {"error": error_msg, "cost_info": {"cost": 0}}

    def create_spring_boot_templates(self, new_structure: Dict[str, Any]) -> Dict[str, Any]:
        """
        Create Spring Boot project templates and code scaffolding
        """
        print(f"\n🚀 Creating Spring Boot Templates")
        print("=" * 60)
        
        # Create templates directory
        templates_dir = self.output_dir / "spring-boot-templates"
        templates_dir.mkdir(exist_ok=True)
        
        templates_created = []
        total_cost = 0.0
        
        # Template types to generate
        template_types = [
            ("pom.xml", "Maven build configuration"),
            ("application.yml", "Spring Boot configuration"),
            ("Application.java", "Main Spring Boot application class"),
            ("Entity template", "JPA entity template with annotations"),
            ("Repository template", "Spring Data JPA repository template"),
            ("Service template", "Service layer template with transactions"),
            ("Controller template", "REST controller template with OpenAPI"),
            ("Exception template", "Global exception handler template"),
            ("Configuration template", "Spring configuration class template")
        ]
        
        for template_name, description in template_types:
            try:
                print(f"🔄 Creating {template_name}...")
                template_result = self._generate_template(template_name, description, new_structure, templates_dir)
                
                if "error" not in template_result:
                    templates_created.append(template_name)
                    total_cost += template_result.get("cost_info", {}).get("cost", 0)
                    print(f"✅ {template_name} created")
                else:
                    print(f"❌ Failed to create {template_name}: {template_result['error']}")
                    
            except Exception as e:
                print(f"❌ Exception creating {template_name}: {e}")
                continue
        
        result = {
            "timestamp": datetime.datetime.now().isoformat(),
            "templates_directory": str(templates_dir),
            "templates_created": templates_created,
            "total_templates": len(template_types),
            "success_rate": len(templates_created) / len(template_types) * 100,
            "cost_info": {
                "total_cost": round(total_cost, 6)
            }
        }
        
        print(f"✅ Templates created: {len(templates_created)}/{len(template_types)} - Cost: ${total_cost:.6f}")
        return result

    def _generate_template(self, template_name: str, description: str, 
                          new_structure: Dict[str, Any], templates_dir: Path) -> Dict[str, Any]:
        """Generate individual template file"""
        prompt = f"""
        Create a {template_name} template for Spring Boot 3.x project.
        
        DESCRIPTION: {description}
        
        REQUIREMENTS:
        - Follow Spring Boot 3.x best practices
        - Include modern Java 21 features where appropriate
        - Add comprehensive comments for template usage
        - Include placeholder values that can be replaced
        - Follow clean architecture principles
        
        Generate clean, production-ready code with proper documentation.
        """
        
        try:
            response = self.client.messages.create(
                model=self.model,
                max_tokens=2000,
                messages=[{"role": "user", "content": prompt}]
            )
            
            # Track cost
            input_tokens = response.usage.input_tokens
            output_tokens = response.usage.output_tokens
            cost = self.cost_tracker.track_usage(
                model=self.model,
                input_tokens=input_tokens,
                output_tokens=output_tokens,
                operation=f"template_generation_{template_name}"
            )
            
            template_content = extract_text_from_content(response.content)
            
            # Determine file extension
            if template_name.endswith('.xml'):
                file_ext = '.xml'
            elif template_name.endswith('.yml'):
                file_ext = '.yml'
            elif template_name.endswith('.java'):
                file_ext = '.java'
            else:
                file_ext = '.java'  # Default to Java
            
            # Save template
            template_file = templates_dir / f"{template_name.replace(' ', '_').replace('.', '_')}_template{file_ext}"
            with open(template_file, 'w', encoding='utf-8') as f:
                f.write(f"""/*
 * {template_name} Template
 * Generated: {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
 * Description: {description}
 * 
 * Instructions:
 * 1. Replace placeholder values with actual project values
 * 2. Customize according to specific requirements
 * 3. Follow the established patterns and conventions
 */

{template_content}
""")
            
            return {
                "template": template_name,
                "file_path": str(template_file),
                "cost_info": {
                    "input_tokens": input_tokens,
                    "output_tokens": output_tokens,
                    "cost": round(cost, 6)
                }
            }
            
        except Exception as e:
            return {"error": str(e), "template": template_name}

    def execute_phase3_complete(self, legacy_analysis_file: Optional[str] = None, 
                               transformation_plan_file: Optional[str] = None) -> Dict[str, Any]:
        """
        Execute complete Phase 3: Modern Implementation
        """
        print("\n" + "="*80)
        print("🏗️ PHASE 3: MODERN IMPLEMENTATION - COMPLETE EXECUTION")
        print("="*80)
        
        # Load previous phase results
        legacy_analysis = self._load_phase_results(legacy_analysis_file, "phase1")
        transformation_plan = self._load_phase_results(transformation_plan_file, "phase2")
        
        if not legacy_analysis or not transformation_plan:
            print("❌ Cannot proceed without Phase 1 and Phase 2 results")
            return {"error": "Missing prerequisite phase results"}
        
        phase3_results = {
            "phase": "Phase 3: Modern Implementation",
            "start_time": datetime.datetime.now().isoformat(),
            "artifacts": [],
            "total_cost": 0.0
        }
        
        try:
            # Step 1: Design new Java structure
            print("\n📋 Step 1: Designing New Java Structure")
            structure_result = self.design_new_java_structure(legacy_analysis, transformation_plan)
            phase3_results["new_structure"] = structure_result
            phase3_results["total_cost"] += structure_result.get("cost_info", {}).get("cost", 0)
            phase3_results["artifacts"].append("NEW_JAVA_STRUCTURE.md")
            
            # Step 2: Analyze new architecture
            print("\n🔍 Step 2: Analyzing New Architecture")
            analysis_result = self.analyze_new_architecture(legacy_analysis, transformation_plan, structure_result)
            phase3_results["architecture_analysis"] = analysis_result
            phase3_results["total_cost"] += analysis_result.get("cost_info", {}).get("cost", 0)
            phase3_results["artifacts"].append("ANALYTIC_NEW_JAVA.md")
            
            # Step 3: Create Spring Boot templates
            print("\n🚀 Step 3: Creating Spring Boot Templates")
            templates_result = self.create_spring_boot_templates(structure_result)
            phase3_results["templates"] = templates_result
            phase3_results["total_cost"] += templates_result.get("cost_info", {}).get("total_cost", 0)
            phase3_results["artifacts"].extend(templates_result.get("templates_created", []))
            
            phase3_results["end_time"] = datetime.datetime.now().isoformat()
            phase3_results["success"] = True
            
            # Save phase results
            self._save_phase_results(phase3_results)
            
            print(f"\n🎉 PHASE 3 COMPLETE!")
            print(f"💰 Total Cost: ${phase3_results['total_cost']:.6f}")
            print(f"📁 Artifacts: {len(phase3_results['artifacts'])}")
            print(f"📄 Output Directory: {self.output_dir}")
            
            return phase3_results
            
        except Exception as e:
            error_msg = f"Phase 3 execution failed: {e}"
            print(f"❌ {error_msg}")
            phase3_results["error"] = error_msg
            phase3_results["success"] = False
            return phase3_results

    def _load_phase_results(self, file_path: Optional[str] = None, phase_name: str = "") -> Dict[str, Any]:
        """Load results from previous phases"""
        if file_path and Path(file_path).exists():
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except Exception as e:
                print(f"⚠️ Warning: Could not load {file_path}: {e}")
        
        # Try to find phase results in transformation-outputs
        phase_dirs = {
            "phase1": "phase1-legacy-analysis",
            "phase2": "phase2-transformation-planning"
        }
        
        if phase_name in phase_dirs:
            phase_dir = Path("transformation-outputs") / phase_dirs[phase_name]
            if phase_dir.exists():
                # Look for JSON results files
                for json_file in phase_dir.glob("*.json"):
                    try:
                        with open(json_file, 'r', encoding='utf-8') as f:
                            results = json.load(f)
                            print(f"✅ Loaded {phase_name} results from {json_file}")
                            return results
                    except Exception:
                        continue
        
        print(f"⚠️ Warning: Could not load {phase_name} results, using empty context")
        return {}

    def _save_phase_results(self, results: Dict[str, Any]):
        """Save phase results to JSON file"""
        results_file = self.output_dir / f"phase3_results_{self.session_id}.json"
        try:
            with open(results_file, 'w', encoding='utf-8') as f:
                json.dump(results, f, indent=2)
            print(f"💾 Phase 3 results saved to: {results_file}")
        except Exception as e:
            print(f"⚠️ Warning: Could not save results: {e}")


def main():
    """Main function to run Phase 3: Modern Implementation"""
    print("🏗️ Phase 3: Modern Implementation Designer")
    print("=" * 60)
    
    try:
        # Check API key
        if not os.getenv("ANTHROPIC_API_KEY"):
            print("❌ Error: ANTHROPIC_API_KEY environment variable is required")
            print("   Set your API key: $env:ANTHROPIC_API_KEY = 'your-key-here'")
            return
        
        designer = ModernImplementationDesigner()
        
        # Execute complete Phase 3
        results = designer.execute_phase3_complete()
        
        if results.get("success"):
            print("\n" + "="*60)
            print("✅ PHASE 3: MODERN IMPLEMENTATION COMPLETED SUCCESSFULLY")
            print("=" * 60)
            print("🎯 Key Accomplishments:")
            print("  ✅ New Java structure designed")
            print("  ✅ Architecture quality analyzed")
            print("  ✅ Spring Boot templates created")
            print("  ✅ Implementation plan ready")
            print(f"\n💰 Total investment: ${results['total_cost']:.6f}")
            print(f"📁 All outputs in: {designer.output_dir}")
            print("\n🚀 Ready for Phase 4: Code Generation!")
        else:
            print(f"\n❌ Phase 3 completed with errors: {results.get('error', 'Unknown error')}")
            
    except Exception as e:
        print(f"❌ Critical error in Phase 3: {e}")
        traceback.print_exc()


if __name__ == "__main__":
    main()
