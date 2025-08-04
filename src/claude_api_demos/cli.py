#!/usr/bin/env python3
"""
Command-line interface for Claude API Demonstrations
"""

import sys
import os
from pathlib import Path

# Add package to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

def check_api_key():
    """Check if API key is configured"""
    try:
        from dotenv import load_dotenv
        
        # Load environment variables
        load_dotenv()
        
        api_key = os.getenv("ANTHROPIC_API_KEY")
        if not api_key:
            print("❌ ANTHROPIC_API_KEY not found!")
            print("\n📋 Setup instructions:")
            print("1. Copy .env.example to .env")
            print("2. Edit .env and add your API key from https://console.anthropic.com/")
            print("3. Run the demo again")
            return False
        
        # Mask the key for display
        masked_key = api_key[:8] + "..." + api_key[-4:] if len(api_key) > 12 else "***"
        print(f"✅ API Key configured: {masked_key}")
        return True
    except ImportError:
        print("❌ python-dotenv not installed. Run: pip install python-dotenv")
        return False

def run_basic_demo():
    """Run basic demonstrations"""
    print("\n🚀 Running Basic Claude API Demo...")
    print("="*60)
    
    try:
        from claude_api_demos.basic_demo import main
        main()
    except Exception as e:
        print(f"❌ Error running basic demo: {e}")

def run_advanced_demo():
    """Run advanced demonstrations"""
    print("\n🔧 Running Advanced Development Demo...")
    print("="*60)
    
    try:
        from claude_api_demos.advanced_demo import main
        main()
    except Exception as e:
        print(f"❌ Error running advanced demo: {e}")

def run_interactive_demo():
    """Run interactive demonstration"""
    print("\n💬 Running Interactive Assistant Demo...")
    print("="*60)
    
    try:
        from claude_api_demos.interactive_demo import main
        main()
    except Exception as e:
        print(f"❌ Error running interactive demo: {e}")

def run_realworld_demo():
    """Run real-world demonstrations"""
    print("\n🌟 Running Real-World Applications Demo...")
    print("="*60)
    
    try:
        from claude_api_demos.real_world_demo import main
        main()
    except Exception as e:
        print(f"❌ Error running real-world demo: {e}")

def run_rd_analytics_demo():
    """Run R&D Analytics demonstrations"""
    print("\n🔬 Running R&D Analytics Demo...")
    print("="*60)
    
    try:
        from claude_api_demos.rd_analytics_demo import main
        main()
    except Exception as e:
        print(f"❌ Error running R&D analytics demo: {e}")

def show_menu():
    """Show main menu"""
    print("\n🤖 Claude API Demonstration Suite")
    print("="*50)
    print("Choose a demonstration to run:")
    print()
    print("1. 🚀 Basic Demo - Simple API usage examples")
    print("2. 🔧 Advanced Demo - Code analysis and refactoring")
    print("3. 💬 Interactive Demo - Chat-based development assistant")
    print("4. 🌟 Real-World Demo - Practical applications")
    print("5. 🔬 R&D Analytics Demo - Data analysis & decision support")
    print("6. 🎯 Run All Demos - Complete demonstration suite")
    print("7. ❓ Show Help - More information")
    print("0. 👋 Exit")
    print()
    print()

def show_help():
    """Show help information"""
    print("\n📚 Claude API Demo Help")
    print("="*50)
    print()
    print("This demonstration suite showcases various Claude API capabilities:")
    print()
    print("🚀 BASIC DEMO:")
    print("   • Simple chat interactions")
    print("   • Code analysis and refactoring")
    print("   • Multi-turn conversations")
    print("   • Creative coding tasks")
    print()
    print("🔧 ADVANCED DEMO:")
    print("   • Comprehensive file analysis")
    print("   • Automatic test generation")
    print("   • Performance optimization")
    print("   • Complex code explanations")
    print()
    print("💬 INTERACTIVE DEMO:")
    print("   • Command-based interface")
    print("   • Real-time coding assistance")
    print("   • Concept explanations")
    print("   • Debug help")
    print()
    print("🌟 REAL-WORLD DEMO:")
    print("   • Documentation generation")
    print("   • API client building")
    print("   • Bug analysis and fixing")
    print("   • Architecture review")
    print()
    print("💡 Requirements:")
    print("   • Python 3.8+")
    print("   • Anthropic API key")
    print("   • Internet connection")
    print()
    print("🔗 Resources:")
    print("   • API Key: https://console.anthropic.com/")
    print("   • Documentation: https://docs.anthropic.com/")
    print("   • DataCamp Tutorial: https://www.datacamp.com/tutorial/claude-code")

def main():
    """Main CLI function"""
    print("🎯 Claude API Demonstration Suite")
    print("Inspired by DataCamp's Claude tutorial")
    print("="*60)
    
    # Check API key first
    if not check_api_key():
        return
    
    # If command line argument provided, run specific demo
    if len(sys.argv) > 1:
        demo_type = sys.argv[1].lower()
        
        if demo_type == "basic":
            run_basic_demo()
        elif demo_type == "advanced":
            run_advanced_demo()
        elif demo_type == "interactive":
            run_interactive_demo()
        elif demo_type == "realworld":
            run_realworld_demo()
        elif demo_type == "rdanalytics" or demo_type == "rd":
            run_rd_analytics_demo()
        elif demo_type == "all":
            run_basic_demo()
            run_advanced_demo()
            run_interactive_demo()
            run_realworld_demo()
            run_rd_analytics_demo()
        else:
            print(f"❌ Unknown demo type: {demo_type}")
            print("Available options: basic, advanced, interactive, realworld, rdanalytics, all")
        return
    
    # Interactive menu
    while True:
        show_menu()
        
        try:
            choice = input("Enter your choice (0-7): ").strip()
            
            if choice == "0":
                print("\n👋 Thank you for using Claude API demos!")
                break
            elif choice == "1":
                run_basic_demo()
            elif choice == "2":
                run_advanced_demo()
            elif choice == "3":
                run_interactive_demo()
            elif choice == "4":
                run_realworld_demo()
            elif choice == "5":
                run_rd_analytics_demo()
            elif choice == "6":
                print("\n🎯 Running all demonstrations...")
                run_basic_demo()
                run_advanced_demo()
                run_interactive_demo()
                run_realworld_demo()
                run_rd_analytics_demo()
                print("\n🎉 All demonstrations completed!")
            elif choice == "7":
                show_help()
            else:
                print("❌ Invalid choice. Please enter a number between 0-7.")
                
        except KeyboardInterrupt:
            print("\n\n👋 Demo interrupted. Goodbye!")
            break
        except Exception as e:
            print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()
