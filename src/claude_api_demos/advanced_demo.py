"""
Advanced Claude API Demonstrations
Showcasing sophisticated use cases similar to DataCamp's tutorial
"""

import anthropic
import os
import json
from typing import List, Dict, Any, Optional
from pathlib import Path

class AdvancedClaudeDemo:
    def __init__(self, api_key: Optional[str] = None):
        """Initialize with Claude client"""
        self.client = anthropic.Anthropic(
            api_key=api_key or os.getenv("ANTHROPIC_API_KEY")
        )
    
    def code_review_and_refactor(self, file_path: str) -> Dict[str, str]:
        """
        Perform comprehensive code review and refactoring
        Similar to the DataCamp tutorial's approach
        """
        try:
            # Read the file
            with open(file_path, 'r', encoding='utf-8') as f:
                code_content = f.read()
            
            # Define different analysis tasks
            tasks = {
                "review": "Review this code for best practices, potential bugs, and areas of improvement:",
                "refactor": "Refactor this code to improve readability, maintainability, and performance. Provide the complete refactored code:",
                "document": "Add comprehensive documentation, docstrings, and inline comments to this code:",
                "security": "Analyze this code for potential security vulnerabilities and suggest fixes:"
            }
            
            results = {}
            
            for task_name, prompt in tasks.items():
                print(f"🔍 Running {task_name.title()} Analysis...")
                
                full_prompt = f"{prompt}\n\n```python\n{code_content}\n```"
                
                response = self.client.messages.create(
                    model="claude-3-5-sonnet-20241022",
                    max_tokens=2000,
                    messages=[{"role": "user", "content": full_prompt}]
                )
                
                results[task_name] = response.content[0].text
                print(f"✅ {task_name.title()} completed")
            
            return results
            
        except Exception as e:
            return {"error": f"Failed to analyze file: {e}"}
    
    def generate_test_cases(self, function_code: str) -> str:
        """Generate comprehensive test cases for a function"""
        prompt = f"""
        Generate comprehensive unit tests for this Python function using pytest.
        Include edge cases, error handling, and various input scenarios:
        
        ```python
        {function_code}
        ```
        
        Provide complete test code that I can run directly.
        """
        
        try:
            response = self.client.messages.create(
                model="claude-3-5-sonnet-20241022",
                max_tokens=1500,
                messages=[{"role": "user", "content": prompt}]
            )
            return response.content[0].text
        except Exception as e:
            return f"Error generating tests: {e}"
    
    def explain_complex_code(self, code: str) -> str:
        """Provide detailed explanation of complex code"""
        prompt = f"""
        Explain this code in detail, breaking down:
        1. What it does (high-level purpose)
        2. How it works (step-by-step logic)
        3. Key concepts and patterns used
        4. Potential improvements or alternatives
        
        Code to explain:
        ```python
        {code}
        ```
        """
        
        try:
            response = self.client.messages.create(
                model="claude-3-5-sonnet-20241022",
                max_tokens=1500,
                messages=[{"role": "user", "content": prompt}]
            )
            return response.content[0].text
        except Exception as e:
            return f"Error explaining code: {e}"
    
    def optimize_performance(self, code: str) -> str:
        """Analyze and optimize code performance"""
        prompt = f"""
        Analyze this code for performance bottlenecks and provide optimized versions:
        
        1. Identify performance issues
        2. Suggest specific optimizations
        3. Provide optimized code with explanations
        4. Compare time/space complexity before and after
        
        Code to optimize:
        ```python
        {code}
        ```
        """
        
        try:
            response = self.client.messages.create(
                model="claude-3-5-sonnet-20241022",
                max_tokens=2000,
                messages=[{"role": "user", "content": prompt}]
            )
            return response.content[0].text
        except Exception as e:
            return f"Error optimizing code: {e}"

def demo_file_analysis():
    """Demonstrate file analysis similar to DataCamp's client.py example"""
    print("=== File Analysis Demo (DataCamp Style) ===")
    
    # Create a sample file to analyze
    sample_file_content = '''
import requests
import json

class APIClient:
    def __init__(self, base_url, api_key):
        self.base_url = base_url
        self.api_key = api_key
        self.session = requests.Session()
    
    def get_data(self, endpoint):
        url = self.base_url + endpoint
        headers = {'Authorization': f'Bearer {self.api_key}'}
        response = self.session.get(url, headers=headers)
        if response.status_code == 200:
            return json.loads(response.text)
        else:
            return None
    
    def post_data(self, endpoint, data):
        url = self.base_url + endpoint
        headers = {'Authorization': f'Bearer {self.api_key}', 'Content-Type': 'application/json'}
        response = self.session.post(url, headers=headers, data=json.dumps(data))
        return response.status_code == 201
'''
    
    # Write sample file
    with open('sample_api_client.py', 'w') as f:
        f.write(sample_file_content)
    
    demo = AdvancedClaudeDemo()
    
    print("📁 Analyzing sample_api_client.py...")
    results = demo.code_review_and_refactor('sample_api_client.py')
    
    for task_name, result in results.items():
        if task_name != "error":
            print(f"\n{'='*60}")
            print(f"🔧 {task_name.upper()} RESULTS:")
            print('='*60)
            print(result)
    
    # Clean up
    os.remove('sample_api_client.py')
    print("\n✅ File analysis demonstration completed!")

def demo_test_generation():
    """Demonstrate automatic test generation"""
    print("\n=== Test Generation Demo ===")
    
    function_code = '''
def binary_search(arr, target):
    """
    Perform binary search on a sorted array
    """
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1
'''
    
    demo = AdvancedClaudeDemo()
    
    print("🧪 Generating tests for binary_search function...")
    tests = demo.generate_test_cases(function_code)
    
    print("\n📝 Generated Test Cases:")
    print("="*60)
    print(tests)

def demo_performance_optimization():
    """Demonstrate performance optimization"""
    print("\n=== Performance Optimization Demo ===")
    
    slow_code = '''
def find_duplicates(numbers):
    """Find duplicate numbers in a list - inefficient version"""
    duplicates = []
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] == numbers[j] and numbers[i] not in duplicates:
                duplicates.append(numbers[i])
    return duplicates

def fibonacci_slow(n):
    """Compute fibonacci number - recursive version"""
    if n <= 1:
        return n
    return fibonacci_slow(n-1) + fibonacci_slow(n-2)
'''
    
    demo = AdvancedClaudeDemo()
    
    print("⚡ Optimizing performance-critical code...")
    optimization = demo.optimize_performance(slow_code)
    
    print("\n🚀 Performance Optimization Results:")
    print("="*60)
    print(optimization)

def demo_code_explanation():
    """Demonstrate complex code explanation"""
    print("\n=== Code Explanation Demo ===")
    
    complex_code = '''
from functools import wraps
from threading import Lock
from typing import Dict, Any, Callable
import time

class Memoize:
    def __init__(self, ttl: int = 300):
        self.ttl = ttl
        self.cache: Dict[str, Dict[str, Any]] = {}
        self.lock = Lock()
    
    def __call__(self, func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            key = f"{func.__name__}:{hash(str(args) + str(sorted(kwargs.items())))}"
            
            with self.lock:
                if key in self.cache:
                    cached_time, result = self.cache[key]['time'], self.cache[key]['result']
                    if time.time() - cached_time < self.ttl:
                        return result
                
                result = func(*args, **kwargs)
                self.cache[key] = {'time': time.time(), 'result': result}
                return result
        
        return wrapper
'''
    
    demo = AdvancedClaudeDemo()
    
    print("📚 Explaining complex memoization decorator...")
    explanation = demo.explain_complex_code(complex_code)
    
    print("\n💡 Detailed Code Explanation:")
    print("="*60)
    print(explanation)

def main():
    """Run all advanced demonstrations"""
    print("🚀 Advanced Claude API Demonstrations")
    print("=" * 60)
    print("Showcasing sophisticated use cases similar to DataCamp's tutorial")
    print("=" * 60)
    
    try:
        # Run all demonstrations
        demo_file_analysis()
        demo_test_generation()
        demo_performance_optimization()
        demo_code_explanation()
        
        print("\n" + "="*60)
        print("🎉 All advanced demonstrations completed successfully!")
        print("🔧 Try modifying the examples to explore more capabilities!")
        print("="*60)
        
    except Exception as e:
        print(f"❌ Error running demonstrations: {e}")
        print("Make sure your ANTHROPIC_API_KEY is set correctly in your .env file")

if __name__ == "__main__":
    main()
