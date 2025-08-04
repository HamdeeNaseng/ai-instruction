"""
Claudefrom .basic_demo import ClaudeClient
from .advanced_demo import AdvancedClaudeDemo
from .interactive_demo import ClaudeDeveloperAssistant
from .real_world_demo import RealWorldClaudeDemo
from .rd_analytics_demo import RDAnalyticsAssistant

__all__ = [
    "ClaudeClient",
    "AdvancedClaudeDemo", 
    "ClaudeDeveloperAssistant",
    "RealWorldClaudeDemo",
    "RDAnalyticsAssistant"
]trations Package

A comprehensive suite of Claude API examples and demonstrations,
inspired by the DataCamp tutorial approach.
"""

__version__ = "1.0.0"
__author__ = "AI Instruction Team"
__email__ = "support@example.com"

from .basic_demo import ClaudeClient
from .advanced_demo import AdvancedClaudeDemo
from .interactive_demo import ClaudeDeveloperAssistant
from .real_world_demo import RealWorldClaudeDemo

__all__ = [
    "ClaudeClient",
    "AdvancedClaudeDemo", 
    "ClaudeDeveloperAssistant",
    "RealWorldClaudeDemo",
]
