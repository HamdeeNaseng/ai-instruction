#!/usr/bin/env python3
"""
Test script to check Anthropic API response structure
"""

import anthropic
import os
from anthropic.types import TextBlock

def test_api_response():
    """Test the API response structure"""
    try:
        client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
        
        response = client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=100,
            messages=[{"role": "user", "content": "Just say 'Hello!'"}]
        )
        
        print("Response object type:", type(response))
        print("Content type:", type(response.content))
        print("Content length:", len(response.content))
        
        if response.content:
            first_content = response.content[0]
            print("First content type:", type(first_content))
            print("First content attributes:", [attr for attr in dir(first_content) if not attr.startswith('_')])
            
            # Try different ways to access text
            try:
                # Only access .text if the block is a TextBlock
                if isinstance(first_content, TextBlock):
                    print("Using .text:", first_content.text)
                else:
                    print(f"Block type {type(first_content).__name__} does not have .text attribute")
            except Exception as e:
                print("Error with .text:", e)
            
            try:
                print("String representation:", str(first_content))
            except Exception as e:
                print("Error with str():", e)
                
            # Check if it's a TextBlock
            if isinstance(first_content, TextBlock):
                print("Content text:", first_content.text)
            else:
                print("No .text attribute found")
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    test_api_response()
