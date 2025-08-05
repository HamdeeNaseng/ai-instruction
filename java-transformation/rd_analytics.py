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
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


def extract_text_from_content(content_blocks):
    """
    Extract text content from Claude API response content blocks.
    Only TextBlock objects have a .text attribute.
    """
    for content_block in content_blocks:
        if isinstance(content_block, TextBlock):
            return content_block.text
    return "No text content found in response"


class CostTracker:
    """
    Track and calculate costs for Claude API usage
    Pricing as of Claude 3.5 Sonnet (20241022) - Update as needed
    """
    
    # Pricing per 1M tokens (as of latest pricing - January 2025)
    PRICING = {
        "claude-4-opus-20250120": {
            "input": 15.00,  # $15.00 per 1M input tokens
            "output": 75.00  # $75.00 per 1M output tokens
        },
        "claude-4-sonnet-20250120": {
            "input": 3.00,   # $3.00 per 1M input tokens
            "output": 15.00  # $15.00 per 1M output tokens
        },
        "claude-3-7-sonnet-20250120": {
            "input": 3.00,   # $3.00 per 1M input tokens
            "output": 15.00  # $15.00 per 1M output tokens
        },
        "claude-3-5-sonnet-20241022": {
            "input": 3.00,   # $3.00 per 1M input tokens
            "output": 15.00  # $15.00 per 1M output tokens
        },
        "claude-3-5-haiku-20241022": {
            "input": 0.80,   # $0.80 per 1M input tokens
            "output": 4.00   # $4.00 per 1M output tokens
        },
        "claude-3-opus-20240229": {
            "input": 15.00,  # $15.00 per 1M input tokens
            "output": 75.00  # $75.00 per 1M output tokens
        },
        "claude-3-haiku-20240307": {
            "input": 0.25,   # $0.25 per 1M input tokens
            "output": 1.25   # $1.25 per 1M output tokens
        }
    }
    
    def __init__(self):
        self.total_input_tokens = 0
        self.total_output_tokens = 0
        self.total_cost = 0.0
        self.api_calls = []
    
    def track_usage(self, model: str, input_tokens: int, output_tokens: int, operation: str = "unknown"):
        """Track token usage and calculate cost for an API call"""
        if model not in self.PRICING:
            print(f"⚠️ Warning: Pricing not available for model {model}")
            return 0.0
        
        pricing = self.PRICING[model]
        input_cost = (input_tokens / 1_000_000) * pricing["input"]
        output_cost = (output_tokens / 1_000_000) * pricing["output"]
        call_cost = input_cost + output_cost
        
        # Track totals
        self.total_input_tokens += input_tokens
        self.total_output_tokens += output_tokens
        self.total_cost += call_cost
        
        # Record individual call
        call_record = {
            "timestamp": datetime.datetime.now().isoformat(),
            "operation": operation,
            "model": model,
            "input_tokens": input_tokens,
            "output_tokens": output_tokens,
            "input_cost": round(input_cost, 6),
            "output_cost": round(output_cost, 6),
            "total_cost": round(call_cost, 6)
        }
        self.api_calls.append(call_record)
        
        return call_cost
    
    def get_summary(self) -> Dict[str, Any]:
        """Get cost summary"""
        return {
            "total_api_calls": len(self.api_calls),
            "total_input_tokens": self.total_input_tokens,
            "total_output_tokens": self.total_output_tokens,
            "total_tokens": self.total_input_tokens + self.total_output_tokens,
            "total_cost": round(self.total_cost, 6),
            "average_cost_per_call": round(self.total_cost / len(self.api_calls), 6) if self.api_calls else 0,
            "calls": self.api_calls
        }
    
    def print_call_summary(self, operation: str, cost: float, input_tokens: int, output_tokens: int):
        """Print a formatted summary of the API call cost"""
        print(f"💰 Cost Summary for {operation}:")
        print(f"   Input tokens: {input_tokens:,} (${(input_tokens/1_000_000)*3.00:.6f})")
        print(f"   Output tokens: {output_tokens:,} (${(output_tokens/1_000_000)*15.00:.6f})")
        print(f"   Total cost: ${cost:.6f}")
        print(f"   Running total: ${self.total_cost:.6f}")


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
        self.cost_tracker = CostTracker()  # Add cost tracking
        
        # Create directories for outputs
        self.output_dir = Path("rd_analytics_outputs")
        self.output_dir.mkdir(exist_ok=True)
        
        self.logs_dir = self.output_dir / "logs"
        self.logs_dir.mkdir(exist_ok=True)
        
        self.reports_dir = self.output_dir / "reports"
        self.reports_dir.mkdir(exist_ok=True)
        
        self.data_dir = self.output_dir / "data"
        self.data_dir.mkdir(exist_ok=True)
        
        # Create information directories for multilingual reports
        self.info_dir = self.output_dir / "information"
        self.info_dir.mkdir(exist_ok=True)
        
        self.info_en_dir = self.info_dir / "en"
        self.info_en_dir.mkdir(exist_ok=True)
        
        self.info_th_dir = self.info_dir / "th"
        self.info_th_dir.mkdir(exist_ok=True)

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
            
            # Track cost and usage
            input_tokens = response.usage.input_tokens
            output_tokens = response.usage.output_tokens
            cost = self.cost_tracker.track_usage(
                model=self.model, 
                input_tokens=input_tokens, 
                output_tokens=output_tokens,
                operation="experimental_data_analysis"
            )
            
            analysis_result = {
                "timestamp": datetime.datetime.now().isoformat(),
                "analysis_type": analysis_type,
                "context": context,
                "raw_data": data_str[:500] + "..." if len(data_str) > 500 else data_str,
                "analysis": extract_text_from_content(response.content),
                "session_id": self.session_id,
                "cost_info": {
                    "input_tokens": input_tokens,
                    "output_tokens": output_tokens,
                    "cost": round(cost, 6)
                }
            }
            
            # Log the analysis
            self._log_result("data_analysis", analysis_result)
            
            print("📊 Analysis Results:")
            print("-" * 40)
            print(extract_text_from_content(response.content))
            
            # Print cost summary
            self.cost_tracker.print_call_summary("Data Analysis", cost, input_tokens, output_tokens)
            
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
            
            # Track cost and usage
            input_tokens = response.usage.input_tokens
            output_tokens = response.usage.output_tokens
            cost = self.cost_tracker.track_usage(
                model=self.model, 
                input_tokens=input_tokens, 
                output_tokens=output_tokens,
                operation="results_interpretation"
            )
            
            interpretation = {
                "timestamp": datetime.datetime.now().isoformat(),
                "hypothesis": hypothesis,
                "success_criteria": success_criteria,
                "results_summary": results_str[:500] + "..." if len(results_str) > 500 else results_str,
                "interpretation": extract_text_from_content(response.content),
                "session_id": self.session_id,
                "cost_info": {
                    "input_tokens": input_tokens,
                    "output_tokens": output_tokens,
                    "cost": round(cost, 6)
                }
            }
            
            # Log the interpretation
            self._log_result("results_interpretation", interpretation)
            
            print("🔍 Results Interpretation:")
            print("-" * 40)
            print(extract_text_from_content(response.content))
            
            # Print cost summary
            self.cost_tracker.print_call_summary("Results Interpretation", cost, input_tokens, output_tokens)
            
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
            
            # Track cost and usage
            input_tokens = response.usage.input_tokens
            output_tokens = response.usage.output_tokens
            cost = self.cost_tracker.track_usage(
                model=self.model, 
                input_tokens=input_tokens, 
                output_tokens=output_tokens,
                operation="decision_matrix_generation"
            )
            
            decision_matrix = {
                "timestamp": datetime.datetime.now().isoformat(),
                "context": context,
                "options": options,
                "criteria": criteria,
                "analysis": extract_text_from_content(response.content),
                "session_id": self.session_id,
                "cost_info": {
                    "input_tokens": input_tokens,
                    "output_tokens": output_tokens,
                    "cost": round(cost, 6)
                }
            }
            
            # Log the decision matrix
            self._log_result("decision_matrix", decision_matrix)
            
            print("📋 Decision Matrix Analysis:")
            print("-" * 40)
            print(extract_text_from_content(response.content))
            
            # Print cost summary
            self.cost_tracker.print_call_summary("Decision Matrix", cost, input_tokens, output_tokens)
            
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
            
            # Track cost and usage
            input_tokens = response.usage.input_tokens
            output_tokens = response.usage.output_tokens
            cost = self.cost_tracker.track_usage(
                model=self.model, 
                input_tokens=input_tokens, 
                output_tokens=output_tokens,
                operation="experiment_design"
            )
            
            experiment_design = {
                "timestamp": datetime.datetime.now().isoformat(),
                "objective": objective,
                "variables": variables,
                "constraints": constraints,
                "budget": budget,
                "design": extract_text_from_content(response.content),
                "session_id": self.session_id,
                "cost_info": {
                    "input_tokens": input_tokens,
                    "output_tokens": output_tokens,
                    "cost": round(cost, 6)
                }
            }
            
            # Log the experiment design
            self._log_result("experiment_design", experiment_design)
            
            print("🔬 Experimental Design:")
            print("-" * 40)
            print(extract_text_from_content(response.content))
            
            # Print cost summary
            self.cost_tracker.print_call_summary("Experiment Design", cost, input_tokens, output_tokens)
            
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
            
            # Track cost and usage
            input_tokens = response.usage.input_tokens
            output_tokens = response.usage.output_tokens
            cost = self.cost_tracker.track_usage(
                model=self.model, 
                input_tokens=input_tokens, 
                output_tokens=output_tokens,
                operation="technical_report_generation"
            )
            
            report = {
                "timestamp": datetime.datetime.now().isoformat(),
                "audience": audience,
                "report_type": report_type,
                "data_summary": data_str[:500] + "..." if len(data_str) > 500 else data_str,
                "report_content": extract_text_from_content(response.content),
                "session_id": self.session_id,
                "cost_info": {
                    "input_tokens": input_tokens,
                    "output_tokens": output_tokens,
                    "cost": round(cost, 6)
                }
            }
            
            # Log and save the report
            self._log_result("technical_report", report)
            self._save_technical_report(report)
            
            print("📋 Technical Report Generated:")
            print("-" * 40)
            report_text = extract_text_from_content(response.content)
            print(report_text[:1000] + "..." if len(report_text) > 1000 else report_text)
            print(f"\n💾 Full report saved to: {self.reports_dir}/technical_report_{self.session_id}.md")
            
            # Print cost summary
            self.cost_tracker.print_call_summary("Technical Report", cost, input_tokens, output_tokens)
            
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
            
            # Track cost and usage
            input_tokens = response.usage.input_tokens
            output_tokens = response.usage.output_tokens
            cost = self.cost_tracker.track_usage(
                model=self.model, 
                input_tokens=input_tokens, 
                output_tokens=output_tokens,
                operation="metrics_tracking"
            )
            
            metrics_analysis = {
                "timestamp": datetime.datetime.now().isoformat(),
                "metrics": metrics,
                "targets": targets,
                "analysis": extract_text_from_content(response.content),
                "session_id": self.session_id,
                "cost_info": {
                    "input_tokens": input_tokens,
                    "output_tokens": output_tokens,
                    "cost": round(cost, 6)
                }
            }
            
            # Log the metrics analysis
            self._log_result("metrics_tracking", metrics_analysis)
            
            print("📊 Metrics Analysis:")
            print("-" * 40)
            print(extract_text_from_content(response.content))
            
            # Print cost summary
            self.cost_tracker.print_call_summary("Metrics Tracking", cost, input_tokens, output_tokens)
            
            # Save metrics data
            self._save_metrics_data(metrics_analysis)
            
            return metrics_analysis
            
        except Exception as e:
            error_msg = f"Error tracking metrics: {e}"
            print(f"❌ {error_msg}")
            return {"error": error_msg, "timestamp": datetime.datetime.now().isoformat()}

    def generate_multilingual_summary(self, session_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Generate summary reports in both English and Thai
        """
        print(f"\n🌐 Generating Multilingual Summary Reports")
        print("=" * 60)
        
        # Prepare session data for the prompt
        session_str = json.dumps(session_data, indent=2)
        
        # Generate English summary
        english_prompt = f"""
        As an expert R&D report writer, create a comprehensive executive summary report in ENGLISH:

        SESSION DATA:
        {session_str}
        
        Please create a professional executive summary with:
        1. PROJECT OVERVIEW: Brief description of R&D activities performed
        2. KEY FINDINGS: Most important discoveries and insights
        3. COST ANALYSIS: Token usage and financial summary
        4. PERFORMANCE METRICS: Success indicators and KPIs
        5. RECOMMENDATIONS: Next steps and strategic recommendations
        6. TECHNICAL SUMMARY: Brief technical highlights
        7. RISK ASSESSMENT: Identified risks and mitigation strategies
        8. CONCLUSION: Overall project status and outlook
        
        Format as a professional executive summary suitable for management review.
        Use clear headings, bullet points, and executive-level language.
        """
        
        # Generate Thai summary
        thai_prompt = f"""
        As an expert R&D report writer, create a comprehensive executive summary report in THAI language:

        SESSION DATA:
        {session_str}
        
        Please create a professional executive summary IN THAI with:
        1. ภาพรวมโครงการ: คำอธิบายสั้นๆ เกี่ยวกับกิจกรรม R&D ที่ดำเนินการ
        2. ผลการค้นพบที่สำคัญ: การค้นพบและข้อมูลเชิงลึกที่สำคัญที่สุด
        3. การวิเคราะห์ต้นทุน: การใช้โทเค็นและสรุปทางการเงิน
        4. ตัวชี้วัดประสิทธิภาพ: ตัวบ่งชี้ความสำเร็จและ KPI
        5. ข้อเสนอแนะ: ขั้นตอนต่อไปและข้อเสนอแนะเชิงกลยุทธ์
        6. สรุปทางเทคนิค: จุดเด่นทางเทคนิคโดยย่อ
        7. การประเมินความเสี่ยง: ความเสี่ยงที่ระบุและกลยุทธ์การลดความเสี่ยง
        8. บทสรุป: สถานะโครงการโดยรวมและแนวโน้ม
        
        จัดรูปแบบเป็นสรุปผู้บริหารระดับมืออาชีพที่เหมาะสำหรับการทบทวนของผู้บริหาร
        ใช้หัวข้อที่ชัดเจน จุดย่อย และภาษาระดับผู้บริหาร
        """
        
        summaries = {}
        
        try:
            # Generate English summary
            print("📝 Generating English summary...")
            en_response = self.client.messages.create(
                model=self.model,
                max_tokens=4000,
                messages=[{"role": "user", "content": english_prompt}]
            )
            
            # Track cost for English summary
            en_input_tokens = en_response.usage.input_tokens
            en_output_tokens = en_response.usage.output_tokens
            en_cost = self.cost_tracker.track_usage(
                model=self.model, 
                input_tokens=en_input_tokens, 
                output_tokens=en_output_tokens,
                operation="multilingual_summary_english"
            )
            
            summaries['english'] = {
                "content": extract_text_from_content(en_response.content),
                "cost_info": {
                    "input_tokens": en_input_tokens,
                    "output_tokens": en_output_tokens,
                    "cost": round(en_cost, 6)
                }
            }
            
            # Generate Thai summary
            print("📝 Generating Thai summary...")
            th_response = self.client.messages.create(
                model=self.model,
                max_tokens=4000,
                messages=[{"role": "user", "content": thai_prompt}]
            )
            
            # Track cost for Thai summary
            th_input_tokens = th_response.usage.input_tokens
            th_output_tokens = th_response.usage.output_tokens
            th_cost = self.cost_tracker.track_usage(
                model=self.model, 
                input_tokens=th_input_tokens, 
                output_tokens=th_output_tokens,
                operation="multilingual_summary_thai"
            )
            
            summaries['thai'] = {
                "content": extract_text_from_content(th_response.content),
                "cost_info": {
                    "input_tokens": th_input_tokens,
                    "output_tokens": th_output_tokens,
                    "cost": round(th_cost, 6)
                }
            }
            
            # Save both summaries
            self._save_multilingual_summaries(summaries)
            
            # Print cost summary
            total_cost = en_cost + th_cost
            total_tokens = en_input_tokens + en_output_tokens + th_input_tokens + th_output_tokens
            print(f"💰 Multilingual Summary Cost:")
            print(f"   English: ${en_cost:.6f} ({en_input_tokens + en_output_tokens:,} tokens)")
            print(f"   Thai: ${th_cost:.6f} ({th_input_tokens + th_output_tokens:,} tokens)")
            print(f"   Total: ${total_cost:.6f} ({total_tokens:,} tokens)")
            
            result = {
                "timestamp": datetime.datetime.now().isoformat(),
                "session_id": self.session_id,
                "summaries": summaries,
                "total_cost": round(total_cost, 6),
                "total_tokens": total_tokens
            }
            
            self._log_result("multilingual_summary", result)
            
            print("✅ Multilingual summaries generated successfully!")
            print(f"   📁 English: information/en/summary_{self.session_id}.md")
            print(f"   📁 Thai: information/th/summary_{self.session_id}.md")
            
            return result
            
        except Exception as e:
            error_msg = f"Error generating multilingual summary: {e}"
            print(f"❌ {error_msg}")
            return {"error": error_msg, "timestamp": datetime.datetime.now().isoformat()}

    def _save_multilingual_summaries(self, summaries: Dict[str, Any]):
        """Save multilingual summary reports to appropriate directories"""
        
        # Save English summary
        en_filename = f"summary_{self.session_id}.md"
        en_filepath = self.info_en_dir / en_filename
        
        en_content = f"""# R&D Analytics Executive Summary
        
**Session ID:** {self.session_id}  
**Generated:** {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}  
**Language:** English  
**Cost:** ${summaries['english']['cost_info']['cost']:.6f}  
**Tokens:** {summaries['english']['cost_info']['input_tokens'] + summaries['english']['cost_info']['output_tokens']:,}

---

{summaries['english']['content']}

---

*This report was generated using Claude AI for R&D Analytics*
"""
        
        with open(en_filepath, 'w', encoding='utf-8') as f:
            f.write(en_content)
        
        # Save Thai summary
        th_filename = f"summary_{self.session_id}.md"
        th_filepath = self.info_th_dir / th_filename
        
        th_content = f"""# สรุปผู้บริหาร - การวิเคราะห์ R&D
        
**รหัสเซสชัน:** {self.session_id}  
**สร้างเมื่อ:** {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}  
**ภาษา:** ไทย  
**ต้นทุน:** ${summaries['thai']['cost_info']['cost']:.6f}  
**โทเค็น:** {summaries['thai']['cost_info']['input_tokens'] + summaries['thai']['cost_info']['output_tokens']:,}

---

{summaries['thai']['content']}

---

*รายงานนี้สร้างโดยใช้ Claude AI สำหรับการวิเคราะห์ R&D*
"""
        
        with open(th_filepath, 'w', encoding='utf-8') as f:
            f.write(th_content)

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

    def _save_cost_data(self):
        """Save cost tracking data to CSV"""
        filename = f"costs_{self.session_id}.csv"
        filepath = self.data_dir / filename
        
        cost_summary = self.cost_tracker.get_summary()
        
        with open(filepath, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Timestamp', 'Operation', 'Model', 'Input_Tokens', 'Output_Tokens', 'Input_Cost', 'Output_Cost', 'Total_Cost'])
            
            for call in cost_summary['calls']:
                writer.writerow([
                    call['timestamp'],
                    call['operation'],
                    call['model'],
                    call['input_tokens'],
                    call['output_tokens'],
                    call['input_cost'],
                    call['output_cost'],
                    call['total_cost']
                ])
        
        # Also save summary as JSON
        summary_filename = f"cost_summary_{self.session_id}.json"
        summary_filepath = self.data_dir / summary_filename
        
        with open(summary_filepath, 'w') as f:
            json.dump(cost_summary, f, indent=2)

    def get_session_summary(self) -> Dict[str, Any]:
        """Get summary of current session activities"""
        print(f"\n📋 Session Summary - {self.session_id}")
        print("=" * 60)
        
        # Save cost data before generating summary
        self._save_cost_data()
        cost_summary = self.cost_tracker.get_summary()
        
        summary = {
            "session_id": self.session_id,
            "total_operations": len(self.results_log),
            "operation_types": {},
            "files_created": [],
            "cost_summary": cost_summary,
            "timestamp": datetime.datetime.now().isoformat()
        }
        
        # Count operation types
        for entry in self.results_log:
            op_type = entry['operation']
            summary['operation_types'][op_type] = summary['operation_types'].get(op_type, 0) + 1
        
        # List created files
        for dir_path in [self.logs_dir, self.reports_dir, self.data_dir, self.info_en_dir, self.info_th_dir]:
            for file_path in dir_path.glob(f"*{self.session_id}*"):
                summary['files_created'].append(str(file_path.relative_to(self.output_dir)))
        
        print(f"📊 Operations performed: {summary['total_operations']}")
        for op_type, count in summary['operation_types'].items():
            print(f"  - {op_type}: {count}")
        
        print(f"📁 Files created: {len(summary['files_created'])}")
        for file_path in summary['files_created']:
            print(f"  - {file_path}")
        
        # Print detailed cost summary
        print(f"\n💰 Cost Summary:")
        print(f"  - Total API calls: {cost_summary['total_api_calls']}")
        print(f"  - Total tokens used: {cost_summary['total_tokens']:,}")
        print(f"    • Input tokens: {cost_summary['total_input_tokens']:,}")
        print(f"    • Output tokens: {cost_summary['total_output_tokens']:,}")
        print(f"  - Total cost: ${cost_summary['total_cost']:.6f}")
        print(f"  - Average cost per call: ${cost_summary['average_cost_per_call']:.6f}")
        
        print(f"\n💡 Cost Breakdown by Operation:")
        operation_costs = {}
        for call in cost_summary['calls']:
            op = call['operation']
            if op not in operation_costs:
                operation_costs[op] = {'calls': 0, 'cost': 0.0, 'tokens': 0}
            operation_costs[op]['calls'] += 1
            operation_costs[op]['cost'] += call['total_cost']
            operation_costs[op]['tokens'] += call['input_tokens'] + call['output_tokens']
        
        for operation, data in operation_costs.items():
            print(f"  - {operation}: {data['calls']} calls, {data['tokens']:,} tokens, ${data['cost']:.6f}")
        
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
    
    # Generate multilingual summary
    print("\n8️⃣ MULTILINGUAL SUMMARY GENERATION")
    multilingual_summary = rd.generate_multilingual_summary(session_summary)
    
    print(f"\n🎉 R&D Analytics Demo Complete!")
    print(f"📁 All outputs saved to: {rd.output_dir}")
    print(f"📊 Session ID: {rd.session_id}")
    
    # Final cost summary
    final_cost = rd.cost_tracker.get_summary()
    print(f"\n💰 Final Cost Summary:")
    print(f"   Total API calls: {final_cost['total_api_calls']}")
    print(f"   Total tokens: {final_cost['total_tokens']:,}")
    print(f"   Total cost: ${final_cost['total_cost']:.6f}")
    print(f"   💡 Cost per operation: ${final_cost['average_cost_per_call']:.6f}")


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
        print("  ✅ Multilingual summary reports (English/Thai)")
        print("  ✅ Cost tracking and token usage analysis")
        print("\n💡 Use these tools for:")
        print("  - Data-driven R&D decisions")
        print("  - Experimental planning and optimization")
        print("  - Project progress monitoring")
        print("  - Technical documentation")
        print("  - Risk assessment and mitigation")
        print("  - Multilingual reporting for international teams")
        print("  - AI cost management and budgeting")
        
    except Exception as e:
        print(f"❌ Error running R&D Analytics demo: {e}")
        print("Make sure your ANTHROPIC_API_KEY is set correctly")


if __name__ == "__main__":
    main()
