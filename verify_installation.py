#!/usr/bin/env python3
"""
Installation verification script for claude-api-demos package
"""

def test_package_installation():
    """Test that the package is properly installed"""
    print("🔍 Testing Claude API Demos Package Installation...")
    print("=" * 60)
    
    # Test 1: Import package
    try:
        import claude_api_demos
        print("✅ Package import: SUCCESS")
        print(f"   Version: {claude_api_demos.__version__}")
    except ImportError as e:
        print(f"❌ Package import: FAILED - {e}")
        return False
    
    # Test 2: Import main classes
    try:
        from claude_api_demos import (
            ClaudeClient,
            AdvancedClaudeDemo,
            ClaudeDeveloperAssistant,
            RealWorldClaudeDemo
        )
        print("✅ Main classes import: SUCCESS")
    except ImportError as e:
        print(f"❌ Main classes import: FAILED - {e}")
        return False
    
    # Test 3: Test CLI module
    try:
        from claude_api_demos import cli
        print("✅ CLI module import: SUCCESS")
    except ImportError as e:
        print(f"❌ CLI module import: FAILED - {e}")
        return False
    
    # Test 4: Test individual demo modules
    demo_modules = ["basic_demo", "advanced_demo", "interactive_demo", "real_world_demo"]
    for module_name in demo_modules:
        try:
            module = getattr(claude_api_demos, module_name)
            print(f"✅ {module_name} module: SUCCESS")
        except AttributeError as e:
            print(f"❌ {module_name} module: FAILED - {e}")
            return False
    
    # Test 5: Check available functions
    try:
        from claude_api_demos.basic_demo import ClaudeClient
        from claude_api_demos.advanced_demo import AdvancedClaudeDemo
        from claude_api_demos.interactive_demo import ClaudeDeveloperAssistant
        from claude_api_demos.real_world_demo import RealWorldClaudeDemo
        print("✅ Direct class imports: SUCCESS")
    except ImportError as e:
        print(f"❌ Direct class imports: FAILED - {e}")
        return False
    
    print("\n" + "=" * 60)
    print("🎉 Package installation verification: SUCCESS!")
    print("\n📋 Available commands:")
    print("• claude-demos                    - Interactive menu")
    print("• claude-demos basic              - Basic demonstrations")
    print("• claude-demos advanced           - Advanced demonstrations")
    print("• claude-demos interactive        - Interactive assistant")
    print("• claude-demos realworld          - Real-world applications")
    print("• claude-demos all                - Run all demonstrations")
    print("\n📚 Python usage:")
    print(">>> from claude_api_demos import ClaudeClient")
    print(">>> client = ClaudeClient()")
    print(">>> response = client.chat('Hello!')")
    print("\n⚠️  Note: Set ANTHROPIC_API_KEY environment variable to use demos")
    
    return True

if __name__ == "__main__":
    success = test_package_installation()
    exit(0 if success else 1)
