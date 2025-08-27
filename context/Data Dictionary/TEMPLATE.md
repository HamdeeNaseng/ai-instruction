# Data Dictionary Template for Context Engineering & PRPs

## Overview

This Data Dictionary template provides a structured approach for documenting and managing data definitions within context engineering frameworks and Product Requirements Prompts (PRPs) methodologies. It ensures consistent terminology, clear data relationships, and comprehensive context for AI-powered analysis and decision-making.

## Template Structure

### 1. Metadata Header

```yaml
---
dictionary_version: "1.0"
project_name: "[PROJECT_NAME]"
domain: "[DOMAIN_AREA]"
created_date: "YYYY-MM-DD"
last_updated: "YYYY-MM-DD"
maintainer: "[MAINTAINER_NAME]"
review_cycle: "[QUARTERLY/ANNUALLY]"
context_framework: "PRPs"
ai_compatibility: ["Claude-3.5+", "GPT-4+"]
---
```

### 2. Context Engineering Data Categories

#### Business Context Data
| Term | Definition | Data Type | Format | Source | Usage Context |
|------|------------|-----------|---------|---------|---------------|
| **Business Objective** | High-level organizational goal | Text | Free text (max 500 chars) | Stakeholder interviews | PRPs Phase 1: Business Context |
| **Key Performance Indicator** | Measurable value demonstrating effectiveness | Numeric/Text | "[VALUE] [UNIT] [TIMEFRAME]" | Business metrics | Performance tracking |
| **Stakeholder** | Individual or group with interest in project | Text | "[NAME] - [ROLE] - [INFLUENCE_LEVEL]" | Stakeholder analysis | Requirements gathering |
| **Business Rule** | Constraint or guideline governing operations | Text | "IF [CONDITION] THEN [ACTION]" | Policy documents | System design |

#### Technical Context Data
| Term | Definition | Data Type | Format | Source | Usage Context |
|------|------------|-----------|---------|---------|---------------|
| **System Component** | Discrete functional unit of system | Text | "[COMPONENT_NAME].[VERSION]" | Architecture docs | System design |
| **API Endpoint** | Interface point for system communication | URL | "[METHOD] /[PATH]" | API documentation | Integration planning |
| **Data Entity** | Logical representation of business object | Text | "[ENTITY_NAME] {attributes}" | Data models | Database design |
| **Dependency** | Required relationship between components | Text | "[SOURCE] -> [TARGET] [TYPE]" | Architecture analysis | Impact assessment |

#### Requirements Context Data
| Term | Definition | Data Type | Format | Source | Usage Context |
|------|------------|-----------|---------|---------|---------------|
| **Functional Requirement** | What the system must do | Text | "The system SHALL [ACTION]" | Requirements analysis | PRPs Phase 3: Requirement Extraction |
| **Non-Functional Requirement** | How the system must perform | Text | "[ATTRIBUTE]: [CRITERIA]" | Quality standards | System specifications |
| **User Story** | Feature description from user perspective | Text | "As a [USER] I want [GOAL] so that [BENEFIT]" | User research | Development planning |
| **Acceptance Criteria** | Conditions for story completion | Text | "GIVEN [CONTEXT] WHEN [ACTION] THEN [OUTCOME]" | Requirements refinement | Testing criteria |

### 3. PRPs-Specific Data Definitions

#### Phase 1: Business Context
| Data Element | Definition | Context Usage | AI Prompt Integration |
|--------------|------------|---------------|----------------------|
| **Domain Knowledge** | Industry-specific information and best practices | Establishes AI expertise baseline | "Acting as a [DOMAIN] expert with knowledge of [DOMAIN_KNOWLEDGE]..." |
| **Business Environment** | Market conditions, regulatory constraints, competitive landscape | Provides decision-making context | "Considering the current [BUSINESS_ENVIRONMENT]..." |
| **Organizational Context** | Company structure, culture, processes, and constraints | Frames solution appropriateness | "Within the context of [ORGANIZATIONAL_CONTEXT]..." |

#### Phase 2: Stakeholder Analysis
| Data Element | Definition | Context Usage | AI Prompt Integration |
|--------------|------------|---------------|----------------------|
| **Stakeholder Profile** | Role, responsibilities, influence level, and interests | Identifies perspective requirements | "From the perspective of [STAKEHOLDER_PROFILE]..." |
| **Communication Preference** | Preferred formats, channels, and detail levels | Tailors output format | "Present findings in [COMMUNICATION_PREFERENCE] format..." |
| **Decision Authority** | Level of authority and approval requirements | Guides recommendation scope | "Considering [DECISION_AUTHORITY] approval requirements..." |

#### Phase 3: Requirement Extraction
| Data Element | Definition | Context Usage | AI Prompt Integration |
|--------------|------------|---------------|----------------------|
| **Requirement Category** | Functional, non-functional, technical, business | Organizes requirement types | "Focus on [REQUIREMENT_CATEGORY] requirements..." |
| **Priority Level** | Critical, high, medium, low priority classification | Guides analysis focus | "Prioritize [PRIORITY_LEVEL] requirements..." |
| **Constraint Type** | Technical, business, regulatory, resource constraints | Limits solution space | "Within the constraints of [CONSTRAINT_TYPE]..." |

#### Phase 4: Technical Translation
| Data Element | Definition | Context Usage | AI Prompt Integration |
|--------------|------------|---------------|----------------------|
| **Technical Specification** | Detailed technical requirements and parameters | Provides implementation guidance | "Translate to technical specifications considering [TECHNICAL_SPECIFICATION]..." |
| **Architecture Pattern** | Design patterns and architectural approaches | Guides solution design | "Apply [ARCHITECTURE_PATTERN] in the solution..." |
| **Integration Point** | System interfaces and data exchange requirements | Defines system boundaries | "Ensure compatibility with [INTEGRATION_POINT]..." |

#### Phase 5: Specification Output
| Data Element | Definition | Context Usage | AI Prompt Integration |
|--------------|------------|---------------|----------------------|
| **Output Format** | Documentation format and structure requirements | Standardizes deliverables | "Generate output in [OUTPUT_FORMAT] format..." |
| **Detail Level** | Required depth and granularity of information | Controls analysis scope | "Provide [DETAIL_LEVEL] analysis..." |
| **Audience Type** | Target audience characteristics and needs | Tailors communication style | "Tailor content for [AUDIENCE_TYPE]..." |

#### Phase 6: Validation Framework
| Data Element | Definition | Context Usage | AI Prompt Integration |
|--------------|------------|---------------|----------------------|
| **Validation Criteria** | Standards and metrics for requirement quality | Ensures completeness | "Validate against [VALIDATION_CRITERIA]..." |
| **Review Process** | Steps and participants in validation workflow | Guides review activities | "Follow [REVIEW_PROCESS] for validation..." |
| **Success Metrics** | Quantifiable measures of requirement quality | Measures effectiveness | "Measure success using [SUCCESS_METRICS]..." |

### 4. Context Engineering Data Patterns

#### Context Hierarchy
```
Enterprise Context
├── Domain Context
│   ├── Business Context
│   ├── Technical Context
│   └── Regulatory Context
├── Project Context
│   ├── Scope Context
│   ├── Resource Context
│   └── Timeline Context
└── Operational Context
    ├── User Context
    ├── System Context
    └── Environmental Context
```

#### Data Relationship Types
| Relationship Type | Definition | Notation | Usage Example |
|------------------|------------|----------|---------------|
| **Dependency** | One entity requires another | A → B | Component A requires Component B |
| **Composition** | Entity contains other entities | A ◊ B | System A contains Module B |
| **Association** | Entities are related | A ↔ B | User A interacts with System B |
| **Inheritance** | Entity inherits properties | A ⊂ B | Specific Requirement A inherits from General Requirement B |

### 5. AI Context Integration Patterns

#### Prompt Context Templates
```
ROLE_CONTEXT: "You are a [ROLE] with expertise in [DOMAIN] and [SPECIALIZATION]"
KNOWLEDGE_CONTEXT: "Your knowledge includes [KNOWLEDGE_AREAS] and understanding of [CONSTRAINTS]"
TASK_CONTEXT: "Your task is to [TASK_DESCRIPTION] within the context of [PROJECT_CONTEXT]"
OUTPUT_CONTEXT: "Provide output in [FORMAT] suitable for [AUDIENCE] with [DETAIL_LEVEL] detail"
VALIDATION_CONTEXT: "Ensure outputs meet [QUALITY_CRITERIA] and align with [STANDARDS]"
```

#### Context Chaining Patterns
```
PRIMARY_CONTEXT → DOMAIN_CONTEXT → TASK_CONTEXT → OUTPUT_CONTEXT
│                                                                │
└── VALIDATION_LOOP ← FEEDBACK_CONTEXT ← REVIEW_CONTEXT ←────────┘
```

### 6. Data Quality Standards

#### Completeness Criteria
- **Definition Clarity**: Each term has unambiguous definition
- **Context Coverage**: All relevant contexts are documented
- **Relationship Mapping**: Dependencies and associations are clear
- **Usage Examples**: Practical application examples provided

#### Consistency Standards
- **Terminology Alignment**: Consistent use across all contexts
- **Format Standardization**: Uniform data formats and structures
- **Version Control**: Change tracking and version management
- **Cross-Reference Validation**: Links and references are accurate

#### Accuracy Requirements
- **Source Verification**: All definitions traced to authoritative sources
- **Expert Review**: Domain expert validation of technical content
- **Stakeholder Approval**: Business stakeholder sign-off on definitions
- **Regular Updates**: Periodic review and update cycles

### 7. Implementation Guidelines

#### Data Dictionary Development Process
1. **Initial Assessment**: Identify all data elements in project scope
2. **Stakeholder Input**: Gather definitions from domain experts
3. **Context Mapping**: Map data elements to context engineering phases
4. **PRPs Integration**: Align definitions with PRPs methodology
5. **Quality Review**: Validate completeness, consistency, and accuracy
6. **Approval Process**: Obtain stakeholder sign-off
7. **Maintenance Plan**: Establish ongoing update procedures

#### Usage in Context Engineering
```
1. Context Setup Phase:
   - Reference business context data
   - Load stakeholder definitions
   - Establish domain terminology

2. Analysis Phase:
   - Apply technical context data
   - Use requirement definitions
   - Reference architectural patterns

3. Output Generation:
   - Follow format specifications
   - Apply audience-specific terminology
   - Ensure consistency with definitions

4. Validation Phase:
   - Check against quality criteria
   - Validate completeness
   - Confirm stakeholder alignment
```

### 8. Maintenance and Governance

#### Version Control
- **Change Log**: Document all modifications with rationale
- **Impact Assessment**: Analyze effects of definition changes
- **Communication Plan**: Notify stakeholders of updates
- **Rollback Procedures**: Ability to revert problematic changes

#### Governance Framework
- **Data Stewardship**: Assign ownership for each data category
- **Review Cycles**: Regular validation and update schedules
- **Approval Authority**: Clear authority for definition changes
- **Compliance Monitoring**: Ensure adherence to standards

#### Quality Assurance
- **Automated Checks**: Consistency and format validation
- **Peer Review**: Cross-validation by team members
- **Expert Validation**: Domain expert review of specialized terms
- **User Feedback**: Incorporation of user experience feedback

### 9. Integration with AI Systems

#### Context Injection Patterns
```python
# Example context injection for AI prompts
context_data = {
    "business_context": load_business_definitions(),
    "technical_context": load_technical_definitions(),
    "stakeholder_context": load_stakeholder_definitions(),
    "requirement_context": load_requirement_definitions()
}

prompt = f"""
Given the following context:
Business Context: {context_data['business_context']}
Technical Context: {context_data['technical_context']}
Stakeholder Perspective: {context_data['stakeholder_context']}
Requirements Framework: {context_data['requirement_context']}

Please analyze and provide recommendations for...
"""
```

#### Validation Automation
```python
# Example validation framework
def validate_context_completeness(data_dictionary, context_phase):
    required_elements = get_required_elements(context_phase)
    missing_elements = []
    
    for element in required_elements:
        if element not in data_dictionary:
            missing_elements.append(element)
    
    return {
        "complete": len(missing_elements) == 0,
        "missing": missing_elements,
        "coverage": (len(required_elements) - len(missing_elements)) / len(required_elements)
    }
```

### 10. Customization Framework

#### Project-Specific Adaptations
Replace the following placeholders with project-specific information:

- **[PROJECT_NAME]**: Actual project identifier
- **[DOMAIN_AREA]**: Specific domain or industry
- **[MAINTAINER_NAME]**: Responsible individual or team
- **[ROLE]**: Specific AI role for context
- **[SPECIALIZATION]**: Area of expertise
- **[KNOWLEDGE_AREAS]**: Relevant knowledge domains

#### Domain-Specific Extensions
Add domain-specific data categories:

- **Healthcare**: Patient data, medical terminology, compliance requirements
- **Finance**: Financial instruments, regulatory data, risk categories
- **Manufacturing**: Process data, quality metrics, safety standards
- **Software**: Technical specifications, architecture patterns, development standards

#### Organization-Specific Standards
Adapt to organizational requirements:

- **Terminology Standards**: Company-specific language and definitions
- **Process Integration**: Alignment with existing workflows
- **Tool Compatibility**: Integration with current tools and systems
- **Compliance Requirements**: Industry or regulatory compliance needs

---

**Template Version**: 1.0  
**Last Updated**: August 27, 2025  
**Compatible Frameworks**: Context Engineering, PRPs  
**AI Models**: Claude 3.5+, GPT-4+  
**Methodology**: Data-Driven Context Engineering
