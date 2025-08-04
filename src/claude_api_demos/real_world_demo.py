"""
Real-world use case demonstrations
Showing practical applications like the DataCamp tutorial
"""

import anthropic
import os
import json
from typing import Dict, List, Optional
from datetime import datetime

class RealWorldClaudeDemo:
    """Demonstrate real-world applications of Claude API"""
    
    def __init__(self, api_key: Optional[str] = None):
        self.client = anthropic.Anthropic(
            api_key=api_key or os.getenv("ANTHROPIC_API_KEY")
        )
    
    def code_documentation_generator(self, code: str, style: str = "google") -> str:
        """
        Generate comprehensive documentation for code
        Similar to DataCamp's documentation example
        """
        prompt = f"""
        Generate comprehensive documentation for this Python code using {style} style docstrings:
        
        Requirements:
        1. Add module-level docstring
        2. Add class and method docstrings
        3. Include parameter descriptions
        4. Add return value documentation
        5. Include usage examples
        6. Add type hints where missing
        
        Code to document:
        ```python
        {code}
        ```
        
        Return the fully documented code.
        """
        
        try:
            response = self.client.messages.create(
                model="claude-3-5-sonnet-20241022",
                max_tokens=2000,
                messages=[{"role": "user", "content": prompt}]
            )
            return response.content[0].text
        except Exception as e:
            return f"Error generating documentation: {e}"
    
    def api_client_builder(self, api_description: str) -> str:
        """
        Build a complete API client based on description
        """
        prompt = f"""
        Create a complete, production-ready Python API client based on this description:
        
        {api_description}
        
        Include:
        1. Proper class structure with initialization
        2. Authentication handling
        3. Error handling and retries
        4. Rate limiting considerations
        5. Logging
        6. Type hints
        7. Comprehensive docstrings
        8. Usage examples
        
        Make it robust and follow Python best practices.
        """
        
        try:
            response = self.client.messages.create(
                model="claude-3-5-sonnet-20241022",
                max_tokens=3000,
                messages=[{"role": "user", "content": prompt}]
            )
            return response.content[0].text
        except Exception as e:
            return f"Error building API client: {e}"
    
    def bug_reporter_and_fixer(self, code: str, error_message: str) -> Dict[str, str]:
        """
        Comprehensive bug analysis and fixing
        """
        analysis_prompt = f"""
        Analyze this bug report:
        
        Code:
        ```python
        {code}
        ```
        
        Error:
        {error_message}
        
        Provide:
        1. Root cause analysis
        2. Step-by-step explanation of why the error occurs
        3. Impact assessment
        4. Multiple solution approaches
        """
        
        fix_prompt = f"""
        Fix this buggy code:
        
        ```python
        {code}
        ```
        
        Error: {error_message}
        
        Provide:
        1. Fixed code with comments explaining changes
        2. Test cases to verify the fix
        3. Prevention strategies for similar bugs
        """
        
        try:
            # Get analysis
            analysis_response = self.client.messages.create(
                model="claude-3-5-sonnet-20241022",
                max_tokens=1500,
                messages=[{"role": "user", "content": analysis_prompt}]
            )
            
            # Get fix
            fix_response = self.client.messages.create(
                model="claude-3-5-sonnet-20241022",
                max_tokens=1500,
                messages=[{"role": "user", "content": fix_prompt}]
            )
            
            return {
                "analysis": analysis_response.content[0].text,
                "fix": fix_response.content[0].text
            }
        except Exception as e:
            return {"error": f"Error in bug analysis: {e}"}
    
    def architecture_reviewer(self, project_structure: str) -> str:
        """
        Review project architecture and suggest improvements
        """
        prompt = f"""
        Review this project structure and provide architectural recommendations:
        
        {project_structure}
        
        Analyze:
        1. Code organization and structure
        2. Separation of concerns
        3. Scalability considerations
        4. Maintainability issues
        5. Security considerations
        6. Performance implications
        7. Best practices compliance
        
        Provide specific, actionable recommendations.
        """
        
        try:
            response = self.client.messages.create(
                model="claude-3-5-sonnet-20241022",
                max_tokens=2000,
                messages=[{"role": "user", "content": prompt}]
            )
            return response.content[0].text
        except Exception as e:
            return f"Error in architecture review: {e}"

def demo_documentation_generation():
    """Demo automatic documentation generation"""
    print("📝 Documentation Generation Demo")
    print("=" * 50)
    
    # Sample undocumented code
    undocumented_code = '''
class DataProcessor:
    def __init__(self, config):
        self.config = config
        self.data = []
    
    def load_data(self, filepath):
        with open(filepath, 'r') as f:
            self.data = json.load(f)
    
    def process(self):
        processed = []
        for item in self.data:
            if item.get('active', False):
                processed.append({
                    'id': item['id'],
                    'value': item['value'] * 2,
                    'timestamp': datetime.now().isoformat()
                })
        return processed
    
    def save_results(self, results, output_path):
        with open(output_path, 'w') as f:
            json.dump(results, f, indent=2)
'''
    
    demo = RealWorldClaudeDemo()
    
    print("🔍 Generating documentation for DataProcessor class...")
    documented_code = demo.code_documentation_generator(undocumented_code)
    
    print("\n📚 Generated Documentation:")
    print("-" * 50)
    print(documented_code)

def demo_api_client_generation():
    """Demo API client generation"""
    print("\n🌐 API Client Generation Demo")
    print("=" * 50)
    
    api_description = """
    Create a client for a REST API that manages user profiles:
    - Base URL: https://api.example.com/v1
    - Authentication: Bearer token
    - Endpoints:
      - GET /users - List all users
      - GET /users/{id} - Get user by ID
      - POST /users - Create new user
      - PUT /users/{id} - Update user
      - DELETE /users/{id} - Delete user
    - Rate limit: 100 requests per minute
    - Responses are JSON format
    - Handle common HTTP errors (400, 401, 404, 500)
    """
    
    demo = RealWorldClaudeDemo()
    
    print("🔧 Building API client...")
    api_client = demo.api_client_builder(api_description)
    
    print("\n💻 Generated API Client:")
    print("-" * 50)
    print(api_client[:1000] + "..." if len(api_client) > 1000 else api_client)

def demo_bug_fixing():
    """Demo comprehensive bug fixing"""
    print("\n🐛 Bug Analysis and Fixing Demo")
    print("=" * 50)
    
    buggy_code = '''
def calculate_average(numbers):
    total = 0
    for num in numbers:
        total += num
    return total / len(numbers)

def process_data(data_list):
    results = []
    for data in data_list:
        if data['value'] > 0:
            avg = calculate_average(data['numbers'])
            results.append({
                'id': data['id'],
                'average': avg,
                'category': data['category'].upper()
            })
    return results

# Usage that causes error
test_data = [
    {'id': 1, 'numbers': [1, 2, 3], 'value': 5, 'category': 'type_a'},
    {'id': 2, 'numbers': [], 'value': 3, 'category': None},
    {'id': 3, 'numbers': [4, 5], 'value': 0, 'category': 'type_b'}
]

result = process_data(test_data)
'''
    
    error_message = """
    ZeroDivisionError: division by zero at line 5 in calculate_average
    AttributeError: 'NoneType' object has no attribute 'upper' at line 15
    """
    
    demo = RealWorldClaudeDemo()
    
    print("🔍 Analyzing and fixing bugs...")
    bug_report = demo.bug_reporter_and_fixer(buggy_code, error_message)
    
    if "error" not in bug_report:
        print("\n📊 Bug Analysis:")
        print("-" * 30)
        print(bug_report["analysis"][:800] + "..." if len(bug_report["analysis"]) > 800 else bug_report["analysis"])
        
        print("\n🔧 Bug Fix:")
        print("-" * 30)
        print(bug_report["fix"][:800] + "..." if len(bug_report["fix"]) > 800 else bug_report["fix"])
    else:
        print(f"Error: {bug_report['error']}")

def demo_architecture_review():
    """Demo architecture review"""
    print("\n🏗️ Architecture Review Demo")
    print("=" * 50)
    
    project_structure = '''
    Project Structure:
    /my_project
    ├── main.py (contains everything - API routes, database logic, business logic)
    ├── config.py (hardcoded values)
    ├── utils.py (mixed utility functions)
    └── data/
        └── users.json (file-based storage)
    
    main.py contains:
    - Flask app initialization
    - All API route handlers
    - Database connection and queries
    - Business logic
    - Email sending functionality
    - File upload handling
    - Authentication logic
    - Logging setup
    
    Current issues:
    - No separation of concerns
    - No error handling
    - Hardcoded secrets in code
    - No testing structure
    - Single file with 500+ lines
    '''
    
    demo = RealWorldClaudeDemo()
    
    print("🔍 Reviewing project architecture...")
    review = demo.architecture_reviewer(project_structure)
    
    print("\n📋 Architecture Review:")
    print("-" * 50)
    print(review)

def main():
    """Run all real-world demonstrations"""
    print("🌟 Real-World Claude API Use Cases")
    print("=" * 60)
    print("Practical applications similar to DataCamp's tutorial")
    print("=" * 60)
    
    try:
        demo_documentation_generation()
        demo_api_client_generation()
        demo_bug_fixing()
        demo_architecture_review()
        
        print("\n" + "="*60)
        print("🎉 All real-world demonstrations completed successfully!")
        print("💡 These examples show how Claude can assist in:")
        print("   • Code documentation and commenting")
        print("   • API client generation")
        print("   • Bug analysis and fixing")
        print("   • Architecture review and recommendations")
        print("="*60)
        
    except Exception as e:
        print(f"❌ Error running demonstrations: {e}")
        print("Make sure your ANTHROPIC_API_KEY is set correctly")

if __name__ == "__main__":
    main()
