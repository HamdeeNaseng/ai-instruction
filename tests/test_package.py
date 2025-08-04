"""
Test suite for Claude API Demonstrations package
"""

import pytest
import os
from unittest.mock import Mock, patch, MagicMock

def test_package_imports():
    """Test that all main classes can be imported"""
    try:
        from claude_api_demos import (
            ClaudeClient,
            AdvancedClaudeDemo,
            ClaudeDeveloperAssistant,
            RealWorldClaudeDemo
        )
        assert ClaudeClient is not None
        assert AdvancedClaudeDemo is not None
        assert ClaudeDeveloperAssistant is not None
        assert RealWorldClaudeDemo is not None
    except ImportError as e:
        pytest.fail(f"Failed to import package components: {e}")

def test_package_version():
    """Test that package version is accessible"""
    import claude_api_demos
    assert hasattr(claude_api_demos, '__version__')
    assert claude_api_demos.__version__ == "1.0.0"

@patch.dict(os.environ, {'ANTHROPIC_API_KEY': 'test_key'})
def test_claude_client_initialization():
    """Test ClaudeClient can be initialized"""
    from claude_api_demos import ClaudeClient
    
    # Mock the anthropic client to avoid actual API calls
    with patch('anthropic.Anthropic') as mock_anthropic:
        client = ClaudeClient()
        assert client is not None
        mock_anthropic.assert_called_once()

@patch.dict(os.environ, {'ANTHROPIC_API_KEY': 'test_key'})
def test_advanced_demo_initialization():
    """Test AdvancedClaudeDemo can be initialized"""
    from claude_api_demos import AdvancedClaudeDemo
    
    with patch('anthropic.Anthropic') as mock_anthropic:
        demo = AdvancedClaudeDemo()
        assert demo is not None
        mock_anthropic.assert_called_once()

@patch.dict(os.environ, {'ANTHROPIC_API_KEY': 'test_key'})
def test_interactive_demo_initialization():
    """Test ClaudeDeveloperAssistant can be initialized"""
    from claude_api_demos import ClaudeDeveloperAssistant
    
    with patch('anthropic.Anthropic') as mock_anthropic:
        assistant = ClaudeDeveloperAssistant()
        assert assistant is not None
        mock_anthropic.assert_called_once()

@patch.dict(os.environ, {'ANTHROPIC_API_KEY': 'test_key'})
def test_real_world_demo_initialization():
    """Test RealWorldClaudeDemo can be initialized"""
    from claude_api_demos import RealWorldClaudeDemo
    
    with patch('anthropic.Anthropic') as mock_anthropic:
        demo = RealWorldClaudeDemo()
        assert demo is not None
        mock_anthropic.assert_called_once()

def test_rd_analytics_demo_initialization():
    """Test that RDAnalyticsAssistant can be imported and initialized"""
    from claude_api_demos import RDAnalyticsAssistant
    
    # Test import
    assert RDAnalyticsAssistant is not None
    
    # Mock the Anthropic client to avoid needing API key
    with patch('anthropic.Anthropic') as mock_anthropic:
        mock_client = MagicMock()
        mock_anthropic.return_value = mock_client
        
        # Test initialization
        rd_assistant = RDAnalyticsAssistant()
        assert rd_assistant is not None
        assert rd_assistant.model == "claude-3-5-sonnet-20241022"
        assert rd_assistant.results_log == []

def test_cli_module_exists():
    """Test that CLI module exists and can be imported"""
    try:
        from claude_api_demos import cli
        assert hasattr(cli, 'main')
    except ImportError as e:
        pytest.fail(f"Failed to import CLI module: {e}")

if __name__ == "__main__":
    pytest.main([__file__])
