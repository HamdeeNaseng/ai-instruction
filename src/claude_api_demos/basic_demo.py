import anthropic
import os
from typing import Optional, List, Dict, Any
import json

class ClaudeClient:
    def __init__(self, api_key: Optional[str] = None):
        """
        Initialize Claude client
        
        Args:
            api_key: Your Anthropic API key. If not provided, will look for ANTHROPIC_API_KEY env var
        """
        self.client = anthropic.Anthropic(
            api_key=api_key or os.getenv("ANTHROPIC_API_KEY")
        )
    
    def chat(self, message: str, model: str = "claude-3-5-sonnet-20241022") -> str:
        """
        Send a message to Claude and get a response
        
        Args:
            message: The message to send to Claude
            model: The Claude model to use
            
        Returns:
            Claude's response
        """
        try:
            message_obj = self.client.messages.create(
                model=model,
                max_tokens=1000,
                messages=[
                    {"role": "user", "content": message}
                ]
            )
            return message_obj.content[0].text
        except Exception as e:
            return f"Error: {e}"
    
    def multi_turn_conversation(self, messages: List[Dict[str, str]], model: str = "claude-3-5-sonnet-20241022") -> str:
        """
        Have a multi-turn conversation with Claude
        
        Args:
            messages: List of message dictionaries with 'role' and 'content' keys
            model: The Claude model to use
            
        Returns:
            Claude's response
        """
        try:
            message_obj = self.client.messages.create(
                model=model,
                max_tokens=1000,
                messages=messages
            )
            return message_obj.content[0].text
        except Exception as e:
            return f"Error: {e}"
    
    def analyze_code(self, code: str, task: str = "analyze") -> str:
        """
        Analyze code using Claude
        
        Args:
            code: The code to analyze
            task: The task to perform (analyze, refactor, document, debug)
            
        Returns:
            Claude's analysis
        """
        prompts = {
            "analyze": "Analyze this code and provide insights about its structure, functionality, and potential improvements:",
            "refactor": "Refactor this code to improve readability, maintainability, and performance:",
            "document": "Add comprehensive documentation and comments to this code:",
            "debug": "Identify potential bugs or issues in this code and suggest fixes:"
        }
        
        prompt = prompts.get(task, prompts["analyze"])
        full_message = f"{prompt}\n\n```python\n{code}\n```"
        
        return self.chat(full_message)

def demonstrate_basic_chat():
    """Demonstrate basic chat functionality"""
    print("=== Basic Chat Demo ===")
    client = ClaudeClient()
    
    response = client.chat("Hello! Can you help me understand what you can do?")
    print("Claude:", response)
    print("\n" + "="*50 + "\n")

def demonstrate_code_analysis():
    """Demonstrate code analysis capabilities"""
    print("=== Code Analysis Demo ===")
    client = ClaudeClient()
    
    # Sample code to analyze
    sample_code = '''
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

for i in range(10):
    print(fibonacci(i))
'''
    
    print("Analyzing this code:")
    print(sample_code)
    print("\nClaude's Analysis:")
    analysis = client.analyze_code(sample_code, "analyze")
    print(analysis)
    print("\n" + "="*50 + "\n")

def demonstrate_code_refactoring():
    """Demonstrate code refactoring"""
    print("=== Code Refactoring Demo ===")
    client = ClaudeClient()
    
    # Code that needs refactoring
    messy_code = '''
def calc(a,b,op):
    if op=='+':
        return a+b
    elif op=='-':
        return a-b
    elif op=='*':
        return a*b
    elif op=='/':
        if b!=0:
            return a/b
        else:
            return 'Error'
    else:
        return 'Invalid'
'''
    
    print("Refactoring this code:")
    print(messy_code)
    print("\nClaude's Refactored Version:")
    refactored = client.analyze_code(messy_code, "refactor")
    print(refactored)
    print("\n" + "="*50 + "\n")

def demonstrate_multi_turn_conversation():
    """Demonstrate multi-turn conversation"""
    print("=== Multi-turn Conversation Demo ===")
    client = ClaudeClient()
    
    messages = [
        {"role": "user", "content": "I'm learning Python. Can you explain what a list comprehension is?"},
    ]
    
    # First exchange
    response1 = client.multi_turn_conversation(messages)
    print("User: I'm learning Python. Can you explain what a list comprehension is?")
    print("Claude:", response1)
    
    # Add Claude's response and continue conversation
    messages.append({"role": "assistant", "content": response1})
    messages.append({"role": "user", "content": "Can you show me a practical example with filtering?"})
    
    response2 = client.multi_turn_conversation(messages)
    print("\nUser: Can you show me a practical example with filtering?")
    print("Claude:", response2)
    print("\n" + "="*50 + "\n")

def demonstrate_creative_tasks():
    """Demonstrate creative and analytical tasks"""
    print("=== Creative Tasks Demo ===")
    client = ClaudeClient()
    
    # Creative writing
    print("Creative Writing Task:")
    creative_response = client.chat("Write a short Python function that generates a haiku about programming. Include both the function and sample output.")
    print(creative_response)
    
    print("\n" + "-"*30 + "\n")
    
    # Problem solving
    print("Problem Solving Task:")
    problem_response = client.chat("I have a list of numbers [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]. I want to find all pairs that sum to 10. Write a Python solution and explain the approach.")
    print(problem_response)
    print("\n" + "="*50 + "\n")

def main():
    """
    Run all demonstrations
    """
    print("Claude API Practical Demonstrations")
    print("=" * 50)
    print("Make sure you have set your ANTHROPIC_API_KEY environment variable!")
    print("=" * 50 + "\n")
    
    try:
        # Run all demonstrations
        demonstrate_basic_chat()
        demonstrate_code_analysis()
        demonstrate_code_refactoring()
        demonstrate_multi_turn_conversation()
        demonstrate_creative_tasks()
        
        print("🎉 All demonstrations completed successfully!")
        print("\nTry running individual functions or modify the examples to explore more capabilities!")
        
    except Exception as e:
        print(f"❌ Error running demonstrations: {e}")
        print("Make sure your ANTHROPIC_API_KEY is set correctly in your .env file")

if __name__ == "__main__":
    main()
