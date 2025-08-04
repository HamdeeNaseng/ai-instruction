#!/usr/bin/env python3
"""
R&D Analytics Demo for Claude API
Specialized demonstrations for Research & Development engineers focusing on:
- Data analysis and interpretation
- Results logging and tracking
- Decision support systems
- Experimental design guidance
- Technical report generation
"""

import os
import json
import csv
import datetime
from pathlib import Path
from typing import Dict, List, Any, Optional, Union
import anthropic
from anthropic.types import TextBlock


def extract_text_from_content(content_blocks):
    """
    Extract text content from Claude API response content blocks.
    Only TextBlock objects have a .text attribute.
    """
    for content_block in content_blocks:
        if isinstance(content_block, TextBlock):
            return content_block.text
    return "No text content found in response"


class RDAnalyticsAssistant:
    """
    R&D Analytics Assistant powered by Claude API
    Specialized for research and development workflows
    """
    
    def __init__(self):
        self.client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
        self.model = "claude-3-5-sonnet-20241022"
        self.results_log = []
        self.session_id = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        
        # Create directories for outputs
        self.output_dir = Path("rd_analytics_outputs")
        self.output_dir.mkdir(exist_ok=True)
        
        self.logs_dir = self.output_dir / "logs"
        self.logs_dir.mkdir(exist_ok=True)
        
        self.reports_dir = self.output_dir / "reports"
        self.reports_dir.mkdir(exist_ok=True)
        
        self.data_dir = self.output_dir / "data"
        self.data_dir.mkdir(exist_ok=True)

    def analyze_experimental_data(self, data: Union[str, Dict, List], 
                                context: str = "", 
                                analysis_type: str = "general") -> Dict[str, Any]:
        """
        Analyze experimental data and provide insights
        
        Args:
            data: Raw data (CSV string, dict, or list)
            context: Experimental context and background
            analysis_type: Type of analysis (statistical, trend, comparative, etc.)
        """
        print(f"\n🔬 Analyzing Experimental Data - {analysis_type.title()} Analysis")
        print("=" * 60)
        
        # Prepare data for analysis
        if isinstance(data, (dict, list)):
            data_str = json.dumps(data, indent=2)
        else:
            data_str = str(data)
        
        prompt = f"""
        As an expert R&D data analyst, please analyze the following experimental data:

        CONTEXT: {context}
        ANALYSIS TYPE: {analysis_type}
        
        DATA:
        {data_str}
        
        Please provide:
        1. Data Overview: Key metrics and patterns
        2. Statistical Analysis: Trends, correlations, outliers
        3. Key Insights: Important findings and observations
        4. Potential Issues: Data quality concerns or anomalies
        5. Recommendations: Next steps and suggestions for further investigation
        6. Decision Support: Actionable recommendations based on findings
        
        Format as structured analysis with clear sections.
        """
        
        try:
            response = self.client.messages.create(
                model=self.model,
                max_tokens=4000,
                messages=[{"role": "user", "content": prompt}]
            )
            
            analysis_result = {
                "timestamp": datetime.datetime.now().isoformat(),
                "analysis_type": analysis_type,
                "context": context,
                "raw_data": data_str[:500] + "..." if len(data_str) > 500 else data_str,
                "analysis": extract_text_from_content(response.content),
                "session_id": self.session_id
            }
            
            # Log the analysis
            self._log_result("data_analysis", analysis_result)
            
            print("📊 Analysis Results:")
            print("-" * 40)
            print(extract_text_from_content(response.content))
            
            # Save detailed report
            self._save_analysis_report(analysis_result)
            
            return analysis_result
            
        except Exception as e:
            error_msg = f"Error analyzing data: {e}"
            print(f"❌ {error_msg}")
            return {"error": error_msg, "timestamp": datetime.datetime.now().isoformat()}

    def interpret_results(self, results: Dict[str, Any], 
                         hypothesis: str = "", 
                         success_criteria: str = "") -> Dict[str, Any]:
        """
        Interpret experimental results against hypothesis and success criteria
        """
        print(f"\n🎯 Interpreting Experimental Results")
        print("=" * 60)
        
        results_str = json.dumps(results, indent=2)
        
        prompt = f"""
        As an expert R&D analyst, please interpret these experimental results:

        HYPOTHESIS: {hypothesis}
        SUCCESS CRITERIA: {success_criteria}
        
        RESULTS:
        {results_str}
        
        Please provide:
        1. Hypothesis Validation: Does the data support or reject the hypothesis?
        2. Success Assessment: How well do results meet the defined criteria?
        3. Statistical Significance: Confidence level and reliability of findings
        4. Practical Implications: Real-world impact and applications
        5. Risk Assessment: Potential risks and limitations
        6. Recommendations: Should we proceed, modify approach, or investigate further?
        7. Next Steps: Specific actions recommended based on these results
        
        Provide a clear GO/NO-GO recommendation with reasoning.
        """
        
        try:
            response = self.client.messages.create(
                model=self.model,
                max_tokens=4000,
                messages=[{"role": "user", "content": prompt}]
            )
            
            interpretation = {
                "timestamp": datetime.datetime.now().isoformat(),
                "hypothesis": hypothesis,
                "success_criteria": success_criteria,
                "results_summary": results_str[:500] + "..." if len(results_str) > 500 else results_str,
                "interpretation": extract_text_from_content(response.content),
                "session_id": self.session_id
            }
            
            # Log the interpretation
            self._log_result("results_interpretation", interpretation)
            
            print("🔍 Results Interpretation:")
            print("-" * 40)
            print(extract_text_from_content(response.content))
            
            return interpretation
            
        except Exception as e:
            error_msg = f"Error interpreting results: {e}"
            print(f"❌ {error_msg}")
            return {"error": error_msg, "timestamp": datetime.datetime.now().isoformat()}

    def generate_decision_matrix(self, options: List[str], 
                               criteria: List[str], 
                               context: str = "") -> Dict[str, Any]:
        """
        Generate a decision matrix for R&D project decisions
        """
        print(f"\n⚖️ Generating Decision Matrix")
        print("=" * 60)
        
        prompt = f"""
        As an expert R&D decision analyst, create a comprehensive decision matrix:

        CONTEXT: {context}
        
        OPTIONS TO EVALUATE:
        {chr(10).join([f"- {option}" for option in options])}
        
        EVALUATION CRITERIA:
        {chr(10).join([f"- {criterion}" for criterion in criteria])}
        
        Please provide:
        1. Decision Matrix: Score each option (1-10) against each criterion
        2. Weighted Analysis: Assign importance weights to criteria
        3. Risk Assessment: Identify risks for each option
        4. Cost-Benefit Analysis: Rough estimates where applicable
        5. Timeline Considerations: Development/implementation timeframes
        6. Resource Requirements: Personnel, equipment, budget needs
        7. Recommendation: Top choice with detailed reasoning
        8. Sensitivity Analysis: How robust is the recommendation?
        
        Present in a clear, structured format suitable for executive review.
        """
        
        try:
            response = self.client.messages.create(
                model=self.model,
                max_tokens=4000,
                messages=[{"role": "user", "content": prompt}]
            )
            
            decision_matrix = {
                "timestamp": datetime.datetime.now().isoformat(),
                "context": context,
                "options": options,
                "criteria": criteria,
                "analysis": extract_text_from_content(response.content),
                "session_id": self.session_id
            }
            
            # Log the decision matrix
            self._log_result("decision_matrix", decision_matrix)
            
            print("📋 Decision Matrix Analysis:")
            print("-" * 40)
            print(extract_text_from_content(response.content))
            
            # Save as structured report
            self._save_decision_report(decision_matrix)
            
            return decision_matrix
            
        except Exception as e:
            error_msg = f"Error generating decision matrix: {e}"
            print(f"❌ {error_msg}")
            return {"error": error_msg, "timestamp": datetime.datetime.now().isoformat()}

    def design_experiment(self, objective: str, 
                         variables: List[str], 
                         constraints: str = "",
                         budget: str = "") -> Dict[str, Any]:
        """
        Design an experimental approach for R&D objectives
        """
        print(f"\n🧪 Designing Experimental Approach")
        print("=" * 60)
        
        prompt = f"""
        As an expert experimental design consultant, help design an experiment:

        OBJECTIVE: {objective}
        
        VARIABLES TO STUDY:
        {chr(10).join([f"- {var}" for var in variables])}
        
        CONSTRAINTS: {constraints}
        BUDGET CONSIDERATIONS: {budget}
        
        Please provide:
        1. Experimental Design: Type of experiment (factorial, DOE, etc.)
        2. Sample Size: Statistical requirements and power analysis
        3. Control Strategy: What controls are needed
        4. Measurement Plan: What metrics to collect and how
        5. Timeline: Phases and milestones
        6. Resource Requirements: Equipment, materials, personnel
        7. Risk Mitigation: Potential issues and contingencies
        8. Success Metrics: How to measure success
        9. Analysis Plan: How to analyze the results
        10. Expected Outcomes: What we expect to learn
        
        Focus on practical, actionable experimental design.
        """
        
        try:
            response = self.client.messages.create(
                model=self.model,
                max_tokens=4000,
                messages=[{"role": "user", "content": prompt}]
            )
            
            experiment_design = {
                "timestamp": datetime.datetime.now().isoformat(),
                "objective": objective,
                "variables": variables,
                "constraints": constraints,
                "budget": budget,
                "design": extract_text_from_content(response.content),
                "session_id": self.session_id
            }
            
            # Log the experiment design
            self._log_result("experiment_design", experiment_design)
            
            print("🔬 Experimental Design:")
            print("-" * 40)
            print(extract_text_from_content(response.content))
            
            return experiment_design
            
        except Exception as e:
            error_msg = f"Error designing experiment: {e}"
            print(f"❌ {error_msg}")
            return {"error": error_msg, "timestamp": datetime.datetime.now().isoformat()}

    def generate_technical_report(self, data: Dict[str, Any], 
                                audience: str = "technical",
                                report_type: str = "progress") -> Dict[str, Any]:
        """
        Generate a comprehensive technical report
        """
        print(f"\n📄 Generating Technical Report")
        print("=" * 60)
        
        data_str = json.dumps(data, indent=2)
        
        prompt = f"""
        As an expert technical writer, create a comprehensive R&D report:

        AUDIENCE: {audience} (technical/executive/regulatory)
        REPORT TYPE: {report_type} (progress/final/feasibility/regulatory)
        
        DATA AND FINDINGS:
        {data_str}
        
        Please structure the report with:
        1. Executive Summary: Key findings and recommendations
        2. Introduction: Background and objectives
        3. Methodology: Approach and methods used
        4. Results: Detailed findings with data presentation
        5. Analysis: Interpretation and implications
        6. Conclusions: Main outcomes and significance
        7. Recommendations: Next steps and actions
        8. Appendices: Supporting data and references
        
        Adapt the technical depth and language to the specified audience.
        Include specific metrics, charts descriptions, and actionable insights.
        """
        
        try:
            response = self.client.messages.create(
                model=self.model,
                max_tokens=4000,
                messages=[{"role": "user", "content": prompt}]
            )
            
            report = {
                "timestamp": datetime.datetime.now().isoformat(),
                "audience": audience,
                "report_type": report_type,
                "data_summary": data_str[:500] + "..." if len(data_str) > 500 else data_str,
                "report_content": extract_text_from_content(response.content),
                "session_id": self.session_id
            }
            
            # Log and save the report
            self._log_result("technical_report", report)
            self._save_technical_report(report)
            
            print("📋 Technical Report Generated:")
            print("-" * 40)
            report_text = extract_text_from_content(response.content)
            print(report_text[:1000] + "..." if len(report_text) > 1000 else report_text)
            print(f"\n💾 Full report saved to: {self.reports_dir}/technical_report_{self.session_id}.md")
            
            return report
            
        except Exception as e:
            error_msg = f"Error generating report: {e}"
            print(f"❌ {error_msg}")
            return {"error": error_msg, "timestamp": datetime.datetime.now().isoformat()}

    def track_project_metrics(self, metrics: Dict[str, Any], 
                            targets: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Track and analyze project metrics against targets
        """
        print(f"\n📈 Tracking Project Metrics")
        print("=" * 60)
        
        metrics_str = json.dumps(metrics, indent=2)
        targets_str = json.dumps(targets or {}, indent=2)
        
        prompt = f"""
        As an R&D project analyst, evaluate these project metrics:

        CURRENT METRICS:
        {metrics_str}
        
        TARGETS/GOALS:
        {targets_str}
        
        Please provide:
        1. Performance Summary: How are we doing overall?
        2. Target Analysis: Which targets are met/missed and by how much?
        3. Trend Analysis: Are metrics improving or declining?
        4. Risk Indicators: Warning signs that need attention
        5. Bottleneck Identification: What's limiting progress?
        6. Recommendations: Specific actions to improve performance
        7. Forecasting: Projected outcomes based on current trends
        8. Resource Optimization: How to better allocate resources
        
        Provide actionable insights for project management.
        """
        
        try:
            response = self.client.messages.create(
                model=self.model,
                max_tokens=3000,
                messages=[{"role": "user", "content": prompt}]
            )
            
            metrics_analysis = {
                "timestamp": datetime.datetime.now().isoformat(),
                "metrics": metrics,
                "targets": targets,
                "analysis": extract_text_from_content(response.content),
                "session_id": self.session_id
            }
            
            # Log the metrics analysis
            self._log_result("metrics_tracking", metrics_analysis)
            
            print("📊 Metrics Analysis:")
            print("-" * 40)
            print(extract_text_from_content(response.content))
            
            # Save metrics data
            self._save_metrics_data(metrics_analysis)
            
            return metrics_analysis
            
        except Exception as e:
            error_msg = f"Error tracking metrics: {e}"
            print(f"❌ {error_msg}")
            return {"error": error_msg, "timestamp": datetime.datetime.now().isoformat()}

    def _log_result(self, operation_type: str, result: Dict[str, Any]):
        """Log operation results to session log"""
        log_entry = {
            "timestamp": datetime.datetime.now().isoformat(),
            "session_id": self.session_id,
            "operation": operation_type,
            "result": result
        }
        
        self.results_log.append(log_entry)
        
        # Save to file
        log_file = self.logs_dir / f"session_{self.session_id}.json"
        with open(log_file, 'w') as f:
            json.dump(self.results_log, f, indent=2)

    def _save_analysis_report(self, analysis: Dict[str, Any]):
        """Save detailed analysis report"""
        filename = f"analysis_{analysis['analysis_type']}_{self.session_id}.md"
        filepath = self.reports_dir / filename
        
        content = f"""# Data Analysis Report
        
**Session ID:** {self.session_id}
**Timestamp:** {analysis['timestamp']}
**Analysis Type:** {analysis['analysis_type']}
**Context:** {analysis['context']}

## Analysis Results

{analysis['analysis']}

## Raw Data Summary
```
{analysis['raw_data']}
```
"""
        
        with open(filepath, 'w') as f:
            f.write(content)

    def _save_decision_report(self, decision: Dict[str, Any]):
        """Save decision matrix report"""
        filename = f"decision_matrix_{self.session_id}.md"
        filepath = self.reports_dir / filename
        
        content = f"""# Decision Matrix Report
        
**Session ID:** {self.session_id}
**Timestamp:** {decision['timestamp']}
**Context:** {decision['context']}

## Options Evaluated
{chr(10).join([f"- {option}" for option in decision['options']])}

## Evaluation Criteria
{chr(10).join([f"- {criterion}" for criterion in decision['criteria']])}

## Analysis Results

{decision['analysis']}
"""
        
        with open(filepath, 'w') as f:
            f.write(content)

    def _save_technical_report(self, report: Dict[str, Any]):
        """Save technical report"""
        filename = f"technical_report_{self.session_id}.md"
        filepath = self.reports_dir / filename
        
        content = f"""# Technical Report
        
**Session ID:** {self.session_id}
**Timestamp:** {report['timestamp']}
**Audience:** {report['audience']}
**Report Type:** {report['report_type']}

{report['report_content']}

## Data Summary
```
{report['data_summary']}
```
"""
        
        with open(filepath, 'w') as f:
            f.write(content)

    def _save_metrics_data(self, metrics: Dict[str, Any]):
        """Save metrics data to CSV"""
        filename = f"metrics_{self.session_id}.csv"
        filepath = self.data_dir / filename
        
        # Extract metrics for CSV
        if isinstance(metrics.get('metrics'), dict):
            with open(filepath, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(['Metric', 'Value', 'Target', 'Timestamp'])
                for metric, value in metrics['metrics'].items():
                    target = metrics.get('targets', {}).get(metric, 'N/A')
                    writer.writerow([metric, value, target, metrics['timestamp']])

    def get_session_summary(self) -> Dict[str, Any]:
        """Get summary of current session activities"""
        print(f"\n📋 Session Summary - {self.session_id}")
        print("=" * 60)
        
        summary = {
            "session_id": self.session_id,
            "total_operations": len(self.results_log),
            "operation_types": {},
            "files_created": [],
            "timestamp": datetime.datetime.now().isoformat()
        }
        
        # Count operation types
        for entry in self.results_log:
            op_type = entry['operation']
            summary['operation_types'][op_type] = summary['operation_types'].get(op_type, 0) + 1
        
        # List created files
        for dir_path in [self.logs_dir, self.reports_dir, self.data_dir]:
            for file_path in dir_path.glob(f"*{self.session_id}*"):
                summary['files_created'].append(str(file_path.relative_to(self.output_dir)))
        
        print(f"📊 Operations performed: {summary['total_operations']}")
        for op_type, count in summary['operation_types'].items():
            print(f"  - {op_type}: {count}")
        
        print(f"📁 Files created: {len(summary['files_created'])}")
        for file_path in summary['files_created']:
            print(f"  - {file_path}")
        
        return summary


def demonstrate_rd_analytics():
    """Demonstrate R&D Analytics capabilities"""
    print("🔬 R&D Analytics Demo - Advanced Decision Support")
    print("=" * 70)
    
    rd = RDAnalyticsAssistant()
    
    # Demo 1: Analyze experimental data
    print("\n1️⃣ EXPERIMENTAL DATA ANALYSIS")
    sample_data = {
        "temperature": [25, 30, 35, 40, 45],
        "yield": [78.5, 82.1, 85.3, 88.7, 85.2],
        "purity": [95.2, 96.1, 97.8, 96.5, 94.8],
        "reaction_time": [2.5, 2.3, 2.1, 2.0, 2.2]  # hours
    }
    
    analysis = rd.analyze_experimental_data(
        data=sample_data,
        context="Optimization of synthesis reaction conditions for new pharmaceutical compound",
        analysis_type="optimization"
    )
    
    # Demo 2: Interpret results
    print("\n2️⃣ RESULTS INTERPRETATION")
    results = {
        "optimal_temperature": 40,
        "max_yield": 88.7,
        "target_purity": 97.8,
        "cost_per_batch": 15000,
        "quality_score": 9.2
    }
    
    interpretation = rd.interpret_results(
        results=results,
        hypothesis="Optimal temperature around 40°C will maximize both yield and purity",
        success_criteria="Yield >85%, Purity >95%, Cost <$20K per batch"
    )
    
    # Demo 3: Decision matrix
    print("\n3️⃣ DECISION MATRIX GENERATION")
    options = [
        "Scale up current process",
        "Optimize further with DoE",
        "Investigate alternative catalyst",
        "Implement continuous flow process"
    ]
    
    criteria = [
        "Technical feasibility",
        "Cost effectiveness",
        "Time to market",
        "Risk level",
        "Scalability potential"
    ]
    
    decision_matrix = rd.generate_decision_matrix(
        options=options,
        criteria=criteria,
        context="Next phase decision for pharmaceutical synthesis project"
    )
    
    # Demo 4: Design new experiment
    print("\n4️⃣ EXPERIMENTAL DESIGN")
    experiment = rd.design_experiment(
        objective="Validate scalability of optimized process from lab to pilot scale",
        variables=["Temperature", "Pressure", "Flow rate", "Catalyst concentration"],
        constraints="Pilot plant available for 2 weeks, safety temperature limit 60°C",
        budget="$100K for pilot testing"
    )
    
    # Demo 5: Track project metrics
    print("\n5️⃣ PROJECT METRICS TRACKING")
    metrics = {
        "completion_percentage": 75,
        "budget_used": 850000,
        "milestones_achieved": 8,
        "quality_score": 8.7,
        "team_utilization": 92,
        "risk_score": 3.2
    }
    
    targets = {
        "completion_percentage": 80,
        "budget_used": 900000,
        "milestones_achieved": 10,
        "quality_score": 9.0,
        "team_utilization": 90,
        "risk_score": 3.0
    }
    
    metrics_analysis = rd.track_project_metrics(metrics=metrics, targets=targets)
    
    # Demo 6: Generate technical report
    print("\n6️⃣ TECHNICAL REPORT GENERATION")
    report_data = {
        "project": "Advanced Pharmaceutical Synthesis",
        "phase": "Optimization Complete",
        "results": analysis,
        "interpretation": interpretation,
        "decision": decision_matrix,
        "next_steps": experiment,
        "metrics": metrics_analysis
    }
    
    technical_report = rd.generate_technical_report(
        data=report_data,
        audience="executive",
        report_type="progress"
    )
    
    # Session summary
    print("\n7️⃣ SESSION SUMMARY")
    session_summary = rd.get_session_summary()
    
    print(f"\n🎉 R&D Analytics Demo Complete!")
    print(f"📁 All outputs saved to: {rd.output_dir}")
    print(f"📊 Session ID: {rd.session_id}")


def main():
    """Main function to run R&D Analytics demonstration"""
    try:
        demonstrate_rd_analytics()
        
        print("\n" + "="*70)
        print("🎓 R&D Analytics Features Demonstrated:")
        print("  ✅ Experimental data analysis and interpretation")
        print("  ✅ Results validation against hypothesis")
        print("  ✅ Multi-criteria decision matrix generation")
        print("  ✅ Experimental design recommendations")
        print("  ✅ Project metrics tracking and analysis")
        print("  ✅ Technical report generation")
        print("  ✅ Comprehensive logging and documentation")
        print("\n💡 Use these tools for:")
        print("  - Data-driven R&D decisions")
        print("  - Experimental planning and optimization")
        print("  - Project progress monitoring")
        print("  - Technical documentation")
        print("  - Risk assessment and mitigation")
        
    except Exception as e:
        print(f"❌ Error running R&D Analytics demo: {e}")
        print("Make sure your ANTHROPIC_API_KEY is set correctly")


if __name__ == "__main__":
    main()
