import anthropic
import os
from typing import Optional

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
    
    def chat(self, message: str, model: str = "claude-3-sonnet-20240229") -> str:
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

def main():
    """
    Example usage of the Claude client
    """
    # Create client (make sure to set ANTHROPIC_API_KEY environment variable)
    client = ClaudeClient()
    
    # Example conversation
    response = client.chat("Hello! Can you help me understand what you can do?")
    print("Claude:", response)

if __name__ == "__main__":
    main()
