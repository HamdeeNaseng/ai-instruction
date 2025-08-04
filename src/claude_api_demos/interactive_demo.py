"""
Interactive Claude Development Assistant
Similar to the DataCamp tutorial's hands-on approach
"""

import anthropic
import os
from typing import Optional, List, Dict
import sys
import traceback

class ClaudeDeveloperAssistant:
    def __init__(self, api_key: Optional[str] = None):
        """Initialize the developer assistant"""
        self.client = anthropic.Anthropic(
            api_key=api_key or os.getenv("ANTHROPIC_API_KEY")
        )
        self.conversation_history = []
    
    def interactive_session(self):
        """Start an interactive development session with Claude"""
        print("🤖 Claude Developer Assistant")
        print("=" * 50)
        print("Available commands:")
        print("• 'analyze [filename]' - Analyze a Python file")
        print("• 'refactor [code]' - Refactor code snippet")
        print("• 'debug [error]' - Help debug an error")
        print("• 'explain [concept]' - Explain programming concept")
        print("• 'optimize [code]' - Optimize code performance")
        print("• 'test [function]' - Generate tests for function")
        print("• 'quit' - Exit the session")
        print("=" * 50)
        
        while True:
            try:
                user_input = input("\n🔧 What can I help you with? ").strip()
                
                if user_input.lower() in ['quit', 'exit', 'q']:
                    print("👋 Thanks for using Claude Developer Assistant!")
                    break
                
                if not user_input:
                    continue
                
                # Process the command
                response = self.process_command(user_input)
                print(f"\n🤖 Claude: {response}")
                
            except KeyboardInterrupt:
                print("\n👋 Session interrupted. Goodbye!")
                break
            except Exception as e:
                print(f"❌ Error: {e}")
    
    def process_command(self, command: str) -> str:
        """Process user commands"""
        parts = command.split(' ', 1)
        cmd = parts[0].lower()
        content = parts[1] if len(parts) > 1 else ""
        
        if cmd == 'analyze':
            return self.analyze_file(content)
        elif cmd == 'refactor':
            return self.refactor_code(content)
        elif cmd == 'debug':
            return self.debug_help(content)
        elif cmd == 'explain':
            return self.explain_concept(content)
        elif cmd == 'optimize':
            return self.optimize_code(content)
        elif cmd == 'test':
            return self.generate_tests(content)
        else:
            # General conversation
            return self.chat(command)
    
    def analyze_file(self, filename: str) -> str:
        """Analyze a Python file"""
        try:
            if not filename:
                return "Please specify a filename to analyze."
            
            if not os.path.exists(filename):
                return f"File '{filename}' not found."
            
            with open(filename, 'r', encoding='utf-8') as f:
                code = f.read()
            
            prompt = f"""
            Analyze this Python file and provide insights about:
            1. Code structure and organization
            2. Potential improvements
            3. Best practices compliance
            4. Possible bugs or issues
            
            File: {filename}
            ```python
            {code}
            ```
            """
            
            return self.chat(prompt)
            
        except Exception as e:
            return f"Error analyzing file: {e}"
    
    def refactor_code(self, code: str) -> str:
        """Refactor code for better quality"""
        if not code:
            return "Please provide code to refactor."
        
        prompt = f"""
        Refactor this code to improve:
        - Readability and maintainability
        - Performance
        - Error handling
        - Code organization
        
        Original code:
        ```python
        {code}
        ```
        
        Provide the refactored version with explanations.
        """
        
        return self.chat(prompt)
    
    def debug_help(self, error_info: str) -> str:
        """Help debug errors"""
        if not error_info:
            return "Please describe the error or provide error message."
        
        prompt = f"""
        Help me debug this issue:
        {error_info}
        
        Please provide:
        1. Possible causes of this error
        2. Step-by-step debugging approach
        3. Code fixes or solutions
        4. Prevention strategies
        """
        
        return self.chat(prompt)
    
    def explain_concept(self, concept: str) -> str:
        """Explain programming concepts"""
        if not concept:
            return "Please specify a concept to explain."
        
        prompt = f"""
        Explain the programming concept: {concept}
        
        Please include:
        1. Clear definition
        2. When and why to use it
        3. Practical examples with code
        4. Common pitfalls to avoid
        """
        
        return self.chat(prompt)
    
    def optimize_code(self, code: str) -> str:
        """Optimize code performance"""
        if not code:
            return "Please provide code to optimize."
        
        prompt = f"""
        Optimize this code for better performance:
        
        ```python
        {code}
        ```
        
        Provide:
        1. Performance analysis
        2. Bottlenecks identification
        3. Optimized version
        4. Performance comparison
        """
        
        return self.chat(prompt)
    
    def generate_tests(self, function_code: str) -> str:
        """Generate test cases"""
        if not function_code:
            return "Please provide function code to generate tests for."
        
        prompt = f"""
        Generate comprehensive unit tests for this function:
        
        ```python
        {function_code}
        ```
        
        Include:
        1. Normal use cases
        2. Edge cases
        3. Error conditions
        4. Mock requirements if needed
        """
        
        return self.chat(prompt)
    
    def chat(self, message: str) -> str:
        """General chat with Claude"""
        try:
            # Add to conversation history
            self.conversation_history.append({"role": "user", "content": message})
            
            # Keep only last 10 exchanges to manage context
            if len(self.conversation_history) > 20:
                self.conversation_history = self.conversation_history[-20:]
            
            response = self.client.messages.create(
                model="claude-3-5-sonnet-20241022",
                max_tokens=2000,
                messages=self.conversation_history
            )
            
            assistant_response = response.content[0].text
            self.conversation_history.append({"role": "assistant", "content": assistant_response})
            
            return assistant_response
            
        except Exception as e:
            return f"Error: {e}"

def demo_interactive_features():
    """Demonstrate key features without full interactive mode"""
    print("🎯 Claude Developer Assistant - Feature Demo")
    print("=" * 60)
    
    assistant = ClaudeDeveloperAssistant()
    
    # Demo 1: Concept Explanation
    print("\n📚 Demo 1: Explaining Python Decorators")
    print("-" * 40)
    response = assistant.explain_concept("Python decorators")
    print(response[:500] + "..." if len(response) > 500 else response)
    
    # Demo 2: Code Refactoring
    print("\n🔧 Demo 2: Code Refactoring")
    print("-" * 40)
    messy_code = """
def calc(x,y,op):
    if op=='+':return x+y
    elif op=='-':return x-y
    elif op=='*':return x*y
    elif op=='/':return x/y if y!=0 else None
    """
    response = assistant.refactor_code(messy_code)
    print(response[:500] + "..." if len(response) > 500 else response)
    
    # Demo 3: Debug Help
    print("\n🐛 Demo 3: Debug Assistance")
    print("-" * 40)
    error_msg = "AttributeError: 'NoneType' object has no attribute 'split' when processing user input"
    response = assistant.debug_help(error_msg)
    print(response[:500] + "..." if len(response) > 500 else response)
    
    print("\n✅ Feature demonstration completed!")
    print("Run the script and use 'interactive' mode for full experience!")

def main():
    """Main function"""
    if len(sys.argv) > 1 and sys.argv[1] == 'interactive':
        # Start interactive session
        assistant = ClaudeDeveloperAssistant()
        assistant.interactive_session()
    else:
        # Run demonstration
        demo_interactive_features()
        print("\n💡 To start interactive mode, run:")
        print("   python interactive_demo.py interactive")

if __name__ == "__main__":
    main()
