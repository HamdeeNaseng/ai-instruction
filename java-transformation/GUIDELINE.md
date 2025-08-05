# Java Transformation AI Guidelines

## Overview

This guideline provides a structured approach for AI agents to analyze, transform, and modernize legacy Java projects to modern Spring Boot applications. The workflow is designed to handle large Java projects systematically with proper documentation and state management.

## AI Workflow Process

### Phase 1: Legacy Analysis
1. **Scan Legacy Project** → Generate `OLD_JAVA_STRUCTURE.md`
2. **Analyze Legacy Code** → Generate `ANALYTIC_OLD_JAVA.md`

### Phase 2: Transformation Planning
3. **Create Transformation Guidelines** → Generate `GUILDLINE_TO_TRANSFORM.md`
4. **Define Code Rules** → Generate `RULE_CODE.md`
5. **Design Clean Architecture** → Generate `CLEAN_ARCHITECH.md`

### Phase 3: Modern Implementation
6. **Design New Structure** → Generate `NEW_JAVA_STRUCTURE.md`
7. **Analyze New Architecture** → Generate `ANALYTIC_NEW_JAVA.md`

## Phase 4: Check error after generate code java
8. **Read Project of Generated**
9. **Fix error it can CRUD file of generated**
10. **Test running**

## Phase 5: Test Performances
11. **Install project**
12. **Running**
13. **Report Performances as logs metric cost** 

## Document Templates

### 1. OLD_JAVA_STRUCTURE.md

**Purpose:** Document the complete structure of the legacy Java project

**AI Task:**
```markdown
# Legacy Java Project Structure Analysis

## Project Overview
- Project Name: [NAME]
- Java Version: [VERSION] 
- Build Tool: [MAVEN/GRADLE]
- Framework: [FRAMEWORK OR NONE]
- Estimated LOC: [NUMBER]

## Directory Structure
```
[FULL DIRECTORY TREE]
```

## Package Analysis
### Core Packages
- Package: [PACKAGE_NAME]
  - Purpose: [DESCRIPTION]
  - Classes: [LIST]
  - Dependencies: [LIST]

## Dependencies Analysis
### External Dependencies
- [DEPENDENCY]: [VERSION] - [PURPOSE]

### Internal Dependencies
- [PACKAGE] → [DEPENDENT_PACKAGES]

## Configuration Files
- [FILE]: [PURPOSE AND CONTENT SUMMARY]

## Database Schema (if applicable)
- Tables: [LIST]
- Relationships: [DESCRIPTION]

## Build Configuration
- Build file analysis
- Compilation targets
- Test configuration

## Entry Points
- Main classes: [LIST]
- Web endpoints: [LIST IF APPLICABLE]
```

### 2. ANALYTIC_OLD_JAVA.md

**Purpose:** Deep analysis of legacy code quality, patterns, and issues

**AI Task:**
```markdown
# Legacy Java Code Analysis

## Architecture Patterns
### Design Patterns Used
- [PATTERN]: [USAGE_DESCRIPTION]

### Anti-Patterns Identified
- [ANTI_PATTERN]: [DESCRIPTION_AND_LOCATION]

## Code Quality Metrics
### Maintainability Issues
- [ISSUE]: [DESCRIPTION_AND_IMPACT]

### Technical Debt
- [DEBT_ITEM]: [PRIORITY] - [DESCRIPTION]

### Security Vulnerabilities
- [VULNERABILITY]: [RISK_LEVEL] - [DESCRIPTION]

## Dependencies Analysis
### Outdated Dependencies
- [DEPENDENCY]: [CURRENT_VERSION] → [RECOMMENDED_VERSION]

### Unused Dependencies
- [DEPENDENCY]: [REASON_FOR_REMOVAL]

## Performance Bottlenecks
- [BOTTLENECK]: [DESCRIPTION_AND_SOLUTION]

## Testing Coverage
- Test Coverage: [PERCENTAGE]
- Missing Tests: [AREAS]
- Test Quality: [ASSESSMENT]

## Configuration Management
- Configuration Style: [PROPERTIES/XML/ANNOTATION]
- Configuration Issues: [LIST]

## Logging Analysis
- Logging Framework: [FRAMEWORK]
- Logging Issues: [LIST]

## Database Access Patterns
- Access Method: [JDBC/ORM/HYBRID]
- Connection Management: [ANALYSIS]
- Query Patterns: [ANALYSIS]
```

### 3. GUILDLINE_TO_TRANSFORM.md

**Purpose:** Transformation strategy and guidelines

**AI Task:**
```markdown
# Java Transformation Guidelines

## Transformation Strategy
### Migration Approach
- Strategy: [BIG_BANG/PHASED/STRANGLER_FIG]
- Rationale: [EXPLANATION]

### Phased Migration Plan
#### Phase 1: [NAME]
- Duration: [TIMEFRAME]
- Scope: [DESCRIPTION]
- Deliverables: [LIST]
- Risks: [LIST]

## Technology Stack Migration
### From → To
- Java Version: [OLD] → [NEW]
- Framework: [OLD] → Spring Boot 3.x
- Database Access: [OLD] → Spring Data JPA
- Testing: [OLD] → JUnit 5 + TestContainers
- Build Tool: [OLD] → [NEW_IF_CHANGED]

## Transformation Rules
### Code Transformation
1. **Entity Classes**
   - Add JPA annotations
   - Replace getters/setters with Lombok
   - Add validation annotations

2. **Data Access Layer**
   - Replace DAO with Repository interfaces
   - Convert JDBC to JPA queries
   - Implement custom queries where needed

3. **Service Layer**
   - Add @Service annotations
   - Implement proper transaction management
   - Add validation and error handling

4. **Configuration**
   - Convert to application.yml
   - Use Spring profiles
   - Implement environment-specific configs

### Architecture Principles
- Separation of Concerns
- Dependency Injection
- Single Responsibility
- Open/Closed Principle

## Quality Gates
### Code Quality Requirements
- Test Coverage: >80%
- Code Duplication: <5%
- Cyclomatic Complexity: <10
- Technical Debt: <2 hours per file

### Performance Requirements
- Response Time: <200ms (95th percentile)
- Throughput: >1000 RPS
- Memory Usage: <2GB heap

## Risk Mitigation
### High-Risk Areas
- [AREA]: [MITIGATION_STRATEGY]

### Rollback Plan
- [ROLLBACK_STRATEGY]
```

### 4. RULE_CODE.md

**Purpose:** Specific coding rules and conventions for transformation

**AI Task:**
```markdown
# Java Transformation Code Rules

## General Coding Standards
### Java Version Features
- Use Java 21+ features (records, pattern matching, text blocks)
- Replace old constructs with modern equivalents
- Use var for local variables where appropriate

### Package Structure
```
com.company.project/
├── config/          # Configuration classes
├── controller/      # REST controllers
├── service/         # Business logic
├── repository/      # Data access
├── entity/          # JPA entities
├── dto/             # Data transfer objects
├── exception/       # Custom exceptions
└── util/            # Utility classes
```

## Spring Boot Conventions
### Annotations Usage
- `@SpringBootApplication` for main class
- `@RestController` for REST endpoints
- `@Service` for business logic
- `@Repository` for data access
- `@Entity` for JPA entities
- `@Configuration` for config classes

### Dependency Injection
- Use constructor injection (preferred)
- Avoid field injection
- Use `@Autowired` only when necessary

## JPA/Hibernate Rules
### Entity Design
```java
@Entity
@Table(name = "patients")
@Data
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class Patient {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    
    @Column(nullable = false)
    private String firstName;
    
    // ... other fields
}
```

### Repository Pattern
```java
@Repository
public interface PatientRepository extends JpaRepository<Patient, Long> {
    List<Patient> findByActiveTrue();
    
    @Query("SELECT p FROM Patient p WHERE p.firstName LIKE %:name%")
    List<Patient> findByNameContaining(@Param("name") String name);
}
```

## Error Handling Rules
### Exception Hierarchy
```java
@ResponseStatus(HttpStatus.NOT_FOUND)
public class EntityNotFoundException extends RuntimeException {
    public EntityNotFoundException(String message) {
        super(message);
    }
}
```

### Global Exception Handler
```java
@ControllerAdvice
public class GlobalExceptionHandler {
    @ExceptionHandler(EntityNotFoundException.class)
    public ResponseEntity<ErrorResponse> handleNotFound(EntityNotFoundException ex) {
        // Handle exception
    }
}
```

## Testing Rules
### Unit Tests
- Use JUnit 5
- Use AssertJ for assertions
- Mock dependencies with Mockito
- Follow AAA pattern (Arrange, Act, Assert)

### Integration Tests
- Use TestContainers for database tests
- Use @SpringBootTest for full context tests
- Separate test configurations

## Configuration Rules
### Application Properties
```yaml
spring:
  application:
    name: project-name
  profiles:
    active: dev
  datasource:
    url: jdbc:postgresql://localhost:5432/db
    username: ${DB_USERNAME:user}
    password: ${DB_PASSWORD:password}
  jpa:
    hibernate:
      ddl-auto: validate
    show-sql: false
```

## Security Rules
### Authentication & Authorization
- Use Spring Security
- JWT for stateless authentication
- Role-based access control
- Secure sensitive endpoints

### Data Validation
- Use Bean Validation annotations
- Validate input at controller level
- Sanitize output data

## Performance Rules
### Database Optimization
- Use connection pooling (HikariCP)
- Implement proper indexing
- Use pagination for large datasets
- Avoid N+1 queries

### Caching Strategy
- Use Spring Cache abstraction
- Cache expensive operations
- Implement cache eviction policies

## Logging Rules
### Logging Framework
- Use SLF4J with Logback
- Use structured logging (JSON)
- Implement proper log levels

### Logging Patterns
```java
@Slf4j
@Service
public class PatientService {
    public Patient createPatient(Patient patient) {
        log.info("Creating patient: {}", patient.getId());
        try {
            // business logic
            log.debug("Patient created successfully: {}", patient.getId());
            return patient;
        } catch (Exception e) {
            log.error("Error creating patient: {}", patient.getId(), e);
            throw e;
        }
    }
}
```
```

### 5. CLEAN_ARCHITECH.md

**Purpose:** Clean architecture principles and implementation guidelines

**AI Task:**
```markdown
# Clean Architecture for Java Spring Boot

## Architecture Overview
### Layered Architecture
```
┌─────────────────────────────────────┐
│           Presentation Layer        │
│         (Controllers, DTOs)         │
├─────────────────────────────────────┤
│            Service Layer            │
│         (Business Logic)            │
├─────────────────────────────────────┤
│          Repository Layer           │
│          (Data Access)              │
├─────────────────────────────────────┤
│            Entity Layer             │
│          (Domain Models)            │
└─────────────────────────────────────┘
```

## Dependency Direction
- **Rule:** Dependencies point inward
- **Principle:** Inner layers should not know about outer layers
- **Implementation:** Use interfaces and dependency injection

## Layer Responsibilities

### 1. Entity Layer (Domain)
**Purpose:** Core business entities and domain logic
**Rules:**
- No external dependencies
- Contains business rules
- Immutable where possible
- Rich domain models

**Example:**
```java
@Entity
@Table(name = "patients")
@Data
@Builder
@NoArgsConstructor
@AllArgsConstructor
public class Patient {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    
    @Column(nullable = false)
    private String firstName;
    
    @Column(nullable = false)
    private String lastName;
    
    // Business logic methods
    public String getFullName() {
        return firstName + " " + lastName;
    }
    
    public boolean isAdult() {
        return calculateAge() >= 18;
    }
}
```

### 2. Repository Layer (Data Access)
**Purpose:** Data persistence abstraction
**Rules:**
- Interface-based design
- No business logic
- Database agnostic
- Single responsibility per repository

**Example:**
```java
@Repository
public interface PatientRepository extends JpaRepository<Patient, Long> {
    List<Patient> findByActiveTrue();
    Optional<Patient> findByEmail(String email);
    
    @Query("SELECT p FROM Patient p WHERE p.registrationDate BETWEEN :start AND :end")
    List<Patient> findByRegistrationDateBetween(
        @Param("start") LocalDateTime start,
        @Param("end") LocalDateTime end
    );
}
```

### 3. Service Layer (Business Logic)
**Purpose:** Orchestrate business operations
**Rules:**
- Contains business logic
- Coordinates between repositories
- Handles transactions
- Validates business rules

**Example:**
```java
@Service
@Transactional
@RequiredArgsConstructor
@Slf4j
public class PatientService {
    private final PatientRepository patientRepository;
    private final PatientMapper patientMapper;
    
    public PatientDTO createPatient(CreatePatientRequest request) {
        log.info("Creating patient with email: {}", request.getEmail());
        
        // Business validation
        validatePatientData(request);
        
        // Check for duplicates
        if (patientRepository.findByEmail(request.getEmail()).isPresent()) {
            throw new DuplicatePatientException("Patient with email already exists");
        }
        
        // Create and save entity
        Patient patient = patientMapper.toEntity(request);
        Patient savedPatient = patientRepository.save(patient);
        
        log.info("Patient created with ID: {}", savedPatient.getId());
        return patientMapper.toDTO(savedPatient);
    }
}
```

### 4. Presentation Layer (Controllers)
**Purpose:** Handle HTTP requests and responses
**Rules:**
- Thin controllers
- Input validation
- Response mapping
- Exception handling

**Example:**
```java
@RestController
@RequestMapping("/api/patients")
@RequiredArgsConstructor
@Validated
@Slf4j
public class PatientController {
    private final PatientService patientService;
    
    @PostMapping
    public ResponseEntity<PatientDTO> createPatient(
            @Valid @RequestBody CreatePatientRequest request) {
        log.info("Received request to create patient");
        PatientDTO patient = patientService.createPatient(request);
        return ResponseEntity.status(HttpStatus.CREATED).body(patient);
    }
}
```

## Cross-Cutting Concerns

### 1. Configuration
**Location:** `config/` package
**Purpose:** Application configuration and beans

```java
@Configuration
@EnableJpaRepositories(basePackages = "com.company.repository")
public class DatabaseConfig {
    
    @Bean
    @Primary
    public DataSource primaryDataSource() {
        return DataSourceBuilder.create()
            .url("${spring.datasource.url}")
            .username("${spring.datasource.username}")
            .password("${spring.datasource.password}")
            .build();
    }
}
```

### 2. Exception Handling
**Location:** `exception/` package
**Purpose:** Centralized error handling

```java
@ControllerAdvice
@Slf4j
public class GlobalExceptionHandler {
    
    @ExceptionHandler(EntityNotFoundException.class)
    public ResponseEntity<ErrorResponse> handleEntityNotFound(EntityNotFoundException ex) {
        log.warn("Entity not found: {}", ex.getMessage());
        ErrorResponse error = ErrorResponse.builder()
            .code("ENTITY_NOT_FOUND")
            .message(ex.getMessage())
            .timestamp(LocalDateTime.now())
            .build();
        return ResponseEntity.status(HttpStatus.NOT_FOUND).body(error);
    }
}
```

### 3. Data Transfer Objects
**Location:** `dto/` package
**Purpose:** API request/response models

```java
@Data
@Builder
@NoArgsConstructor
@AllArgsConstructor
public class PatientDTO {
    private Long id;
    private String firstName;
    private String lastName;
    private String email;
    private LocalDateTime registrationDate;
    private boolean active;
}
```

## SOLID Principles Implementation

### Single Responsibility Principle (SRP)
- Each class has one reason to change
- Separate concerns into different classes
- Use composition over inheritance

### Open/Closed Principle (OCP)
- Open for extension, closed for modification
- Use interfaces and abstract classes
- Strategy pattern for varying behavior

### Liskov Substitution Principle (LSP)
- Subtypes must be substitutable for base types
- Honor contracts defined by interfaces
- Avoid strengthening preconditions

### Interface Segregation Principle (ISP)
- Many specific interfaces are better than one general interface
- Clients shouldn't depend on interfaces they don't use
- Create focused, cohesive interfaces

### Dependency Inversion Principle (DIP)
- Depend on abstractions, not concretions
- High-level modules shouldn't depend on low-level modules
- Use dependency injection

## Testing Strategy

### Unit Tests
- Test business logic in isolation
- Mock external dependencies
- Focus on behavior, not implementation

### Integration Tests
- Test layer interactions
- Use TestContainers for database tests
- Test complete user scenarios

### Architecture Tests
- Use ArchUnit to enforce architecture rules
- Verify dependency directions
- Ensure package organization

```java
@ArchTest
static final ArchRule services_should_only_be_accessed_by_controllers =
    classes()
        .that().resideInAPackage("..service..")
        .should().onlyBeAccessed().byAnyPackage("..controller..", "..service..");
```
```

### 6. NEW_JAVA_STRUCTURE.md

**Purpose:** Document the new Spring Boot project structure

**AI Task:**
```markdown
# Modern Spring Boot Project Structure

## Project Overview
- Project Name: [NAME]
- Java Version: 21+
- Spring Boot Version: 3.x
- Build Tool: Maven/Gradle
- Database: PostgreSQL/MySQL
- Testing: JUnit 5 + TestContainers

## Directory Structure
```
src/
├── main/
│   ├── java/com/company/project/
│   │   ├── ProjectApplication.java
│   │   ├── config/
│   │   │   ├── DatabaseConfig.java
│   │   │   ├── SecurityConfig.java
│   │   │   └── SwaggerConfig.java
│   │   ├── controller/
│   │   │   ├── PatientController.java
│   │   │   └── DoctorController.java
│   │   ├── service/
│   │   │   ├── PatientService.java
│   │   │   └── DoctorService.java
│   │   ├── repository/
│   │   │   ├── PatientRepository.java
│   │   │   └── DoctorRepository.java
│   │   ├── entity/
│   │   │   ├── Patient.java
│   │   │   └── Doctor.java
│   │   ├── dto/
│   │   │   ├── request/
│   │   │   └── response/
│   │   ├── mapper/
│   │   │   ├── PatientMapper.java
│   │   │   └── DoctorMapper.java
│   │   ├── exception/
│   │   │   ├── GlobalExceptionHandler.java
│   │   │   └── CustomExceptions.java
│   │   └── util/
│   │       └── DateUtils.java
│   └── resources/
│       ├── application.yml
│       ├── application-dev.yml
│       ├── application-prod.yml
│       └── db/migration/
│           └── V1__Initial_schema.sql
└── test/
    ├── java/com/company/project/
    │   ├── integration/
    │   ├── service/
    │   ├── controller/
    │   └── repository/
    └── resources/
        └── application-test.yml
```

## Modern Components

### 1. Main Application Class
```java
@SpringBootApplication
@EnableJpaRepositories
@EnableScheduling
public class ProjectApplication {
    public static void main(String[] args) {
        SpringApplication.run(ProjectApplication.class, args);
    }
}
```

### 2. Configuration Classes
#### Database Configuration
```java
@Configuration
@EnableTransactionManagement
public class DatabaseConfig {
    // HikariCP configuration
    // Transaction management
    // JPA configuration
}
```

#### Security Configuration
```java
@Configuration
@EnableWebSecurity
@EnableMethodSecurity
public class SecurityConfig {
    // JWT configuration
    // CORS configuration
    // Authentication/Authorization
}
```

### 3. REST Controllers
```java
@RestController
@RequestMapping("/api/v1/patients")
@RequiredArgsConstructor
@Validated
@Tag(name = "Patient Management")
public class PatientController {
    // CRUD operations
    // Pagination support
    // Search functionality
    // OpenAPI documentation
}
```

### 4. Service Layer
```java
@Service
@Transactional
@RequiredArgsConstructor
@Slf4j
public class PatientService {
    // Business logic
    // Transaction management
    // Validation
    // Error handling
}
```

### 5. Repository Layer
```java
@Repository
public interface PatientRepository extends JpaRepository<Patient, Long>, 
                                           JpaSpecificationExecutor<Patient> {
    // Custom queries
    // Native queries
    // Specifications for complex queries
}
```

### 6. Entity Classes
```java
@Entity
@Table(name = "patients")
@Data
@Builder
@NoArgsConstructor
@AllArgsConstructor
@EntityListeners(AuditingEntityListener.class)
public class Patient {
    // JPA annotations
    // Lombok annotations
    // Validation annotations
    // Audit fields
}
```

## Configuration Files

### application.yml
```yaml
spring:
  application:
    name: project-name
  profiles:
    active: ${SPRING_PROFILES_ACTIVE:dev}
  
  datasource:
    url: jdbc:postgresql://localhost:5432/${DB_NAME:project_db}
    username: ${DB_USERNAME:project_user}
    password: ${DB_PASSWORD:project_pass}
    hikari:
      maximum-pool-size: 20
      minimum-idle: 5
  
  jpa:
    hibernate:
      ddl-auto: validate
    show-sql: false
    properties:
      hibernate:
        format_sql: true
        use_sql_comments: true
  
  flyway:
    enabled: true
    locations: classpath:db/migration
  
  cache:
    type: redis
    redis:
      host: localhost
      port: 6379

server:
  port: 8080
  servlet:
    context-path: /api

logging:
  level:
    com.company.project: INFO
  pattern:
    console: "%d{yyyy-MM-dd HH:mm:ss} - %msg%n"
  file:
    name: logs/application.log

management:
  endpoints:
    web:
      exposure:
        include: health,info,metrics,prometheus
  endpoint:
    health:
      show-details: always
```

## Testing Structure

### Unit Tests
- Service layer tests with mocked dependencies
- Repository tests with @DataJpaTest
- Controller tests with @WebMvcTest

### Integration Tests
- Full application context tests
- TestContainers for database integration
- End-to-end API tests

### Architecture Tests
- Package dependency rules
- Naming conventions
- Layer architecture validation

## Build Configuration

### Maven (pom.xml)
```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0">
    <parent>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-parent</artifactId>
        <version>3.1.0</version>
    </parent>

    <dependencies>
        <!-- Spring Boot Starters -->
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-data-jpa</artifactId>
        </dependency>
        <!-- Other dependencies -->
    </dependencies>
</project>
```

## Performance Optimizations
- Connection pooling with HikariCP
- Redis caching for frequently accessed data
- Database indexing strategy
- Pagination for large datasets
- Async processing where appropriate

## Monitoring and Observability
- Spring Boot Actuator endpoints
- Prometheus metrics
- Structured logging with JSON format
- Health checks for dependencies
- Custom metrics for business KPIs
```

### 7. ANALYTIC_NEW_JAVA.md

**Purpose:** Analysis and validation of the new Spring Boot architecture

**AI Task:**
```markdown
# Modern Spring Boot Architecture Analysis

## Architecture Quality Assessment

### Adherence to Clean Architecture
- **Layered Structure:** ✅/❌ - [ANALYSIS]
- **Dependency Direction:** ✅/❌ - [ANALYSIS]  
- **Separation of Concerns:** ✅/❌ - [ANALYSIS]
- **SOLID Principles:** ✅/❌ - [ANALYSIS]

### Spring Boot Best Practices
- **Auto-configuration Usage:** [SCORE/10] - [COMMENTS]
- **Dependency Injection:** [SCORE/10] - [COMMENTS]
- **Configuration Management:** [SCORE/10] - [COMMENTS]
- **Exception Handling:** [SCORE/10] - [COMMENTS]

## Code Quality Metrics

### Test Coverage
- **Unit Tests:** [PERCENTAGE]%
- **Integration Tests:** [PERCENTAGE]%
- **Overall Coverage:** [PERCENTAGE]%
- **Missing Test Areas:** [LIST]

### Code Quality
- **Cyclomatic Complexity:** [AVERAGE] (Target: <10)
- **Code Duplication:** [PERCENTAGE]% (Target: <5%)
- **Technical Debt:** [HOURS] (Target: <2h per file)
- **Maintainability Index:** [SCORE] (Target: >70)

### Performance Analysis
- **Startup Time:** [SECONDS]
- **Memory Usage:** [MB] (Heap: [X]MB, Non-heap: [Y]MB)
- **Response Time (95th percentile):** [MS]
- **Throughput:** [RPS]

## Security Assessment

### Security Features Implemented
- **Authentication:** [MECHANISM] - [STATUS]
- **Authorization:** [RBAC/ATTRIBUTE-BASED] - [STATUS]
- **Input Validation:** [STATUS] - [COVERAGE]
- **SQL Injection Protection:** [STATUS] - [METHOD]
- **XSS Protection:** [STATUS] - [METHOD]
- **CSRF Protection:** [STATUS] - [METHOD]

### Security Scan Results
- **High Severity:** [COUNT] issues
- **Medium Severity:** [COUNT] issues
- **Low Severity:** [COUNT] issues
- **Recommendations:** [LIST]

## Database Design Analysis

### JPA/Hibernate Implementation
- **Entity Relationships:** [ANALYSIS]
- **Query Performance:** [ANALYSIS]
- **Connection Pooling:** [CONFIGURATION]
- **Transaction Management:** [ANALYSIS]

### Database Schema
- **Normalization:** [LEVEL] - [COMMENTS]
- **Indexing Strategy:** [ANALYSIS]
- **Migration Scripts:** [STATUS]
- **Data Integrity:** [CONSTRAINTS_ANALYSIS]

## API Design Assessment

### RESTful API Design
- **Resource Naming:** [SCORE/10] - [COMMENTS]
- **HTTP Methods Usage:** [SCORE/10] - [COMMENTS]
- **Status Codes:** [SCORE/10] - [COMMENTS]
- **Error Handling:** [SCORE/10] - [COMMENTS]

### API Documentation
- **OpenAPI/Swagger:** [STATUS] - [COVERAGE]
- **Examples:** [STATUS] - [QUALITY]
- **Authentication Docs:** [STATUS]

## Configuration Analysis

### Application Configuration
- **Profile Management:** [DEV/PROD/TEST] - [STATUS]
- **External Configuration:** @ConfigurationProperties usage
- **Environment Variables:** Security and flexibility
- **Feature Flags:** Implementation status

### Deployment Configuration
- **Docker:** [STATUS] - [OPTIMIZATION_LEVEL]
- **Kubernetes:** [STATUS] - [RESOURCE_LIMITS]
- **Health Checks:** [ENDPOINT_STATUS]
- **Monitoring:** [ACTUATOR_ENDPOINTS]

## Logging and Monitoring

### Logging Implementation
- **Framework:** [SLF4J/LOGBACK] - [CONFIGURATION]
- **Log Levels:** [APPROPRIATE_USAGE]
- **Structured Logging:** [JSON/TEXT] - [STATUS]
- **Log Aggregation:** [SYSTEM_READY]

### Monitoring Setup
- **Metrics Collection:** [PROMETHEUS/MICROMETER] - [STATUS]
- **Health Endpoints:** [COVERAGE]
- **Custom Metrics:** [BUSINESS_METRICS_COUNT]
- **Alerting:** [CONFIGURATION_STATUS]

## Testing Strategy Effectiveness

### Test Pyramid Compliance
- **Unit Tests (70%):** [ACTUAL_PERCENTAGE]% - [GAP_ANALYSIS]
- **Integration Tests (20%):** [ACTUAL_PERCENTAGE]% - [GAP_ANALYSIS]
- **E2E Tests (10%):** [ACTUAL_PERCENTAGE]% - [GAP_ANALYSIS]

### Testing Tools Usage
- **JUnit 5:** [USAGE_EFFECTIVENESS]
- **Mockito:** [MOCKING_QUALITY]
- **TestContainers:** [INTEGRATION_TEST_QUALITY]
- **AssertJ:** [ASSERTION_QUALITY]

## Performance Benchmarks

### Load Testing Results
- **Concurrent Users:** [NUMBER]
- **Average Response Time:** [MS]
- **Error Rate:** [PERCENTAGE]%
- **Resource Utilization:** CPU: [%], Memory: [MB]

### Optimization Recommendations
1. **Database Optimization:** [RECOMMENDATIONS]
2. **Caching Strategy:** [RECOMMENDATIONS]
3. **Connection Pooling:** [RECOMMENDATIONS]
4. **JVM Tuning:** [RECOMMENDATIONS]

## Migration Success Metrics

### Functionality Parity
- **Feature Completeness:** [PERCENTAGE]%
- **Data Migration:** [SUCCESS_RATE]%
- **Integration Points:** [STATUS]
- **Business Logic Preservation:** [VERIFICATION_STATUS]

### Improvement Metrics
- **Code Reduction:** [PERCENTAGE]% fewer lines
- **Build Time:** [OLD_TIME] → [NEW_TIME]
- **Deployment Time:** [OLD_TIME] → [NEW_TIME]
- **Developer Productivity:** [METRIC_IMPROVEMENT]

## Recommendations

### Immediate Actions
1. [HIGH_PRIORITY_ITEM] - [TIMELINE]
2. [HIGH_PRIORITY_ITEM] - [TIMELINE]

### Medium-term Improvements
1. [MEDIUM_PRIORITY_ITEM] - [TIMELINE]
2. [MEDIUM_PRIORITY_ITEM] - [TIMELINE]

### Long-term Enhancements
1. [LONG_TERM_ITEM] - [TIMELINE]
2. [LONG_TERM_ITEM] - [TIMELINE]

## Quality Gates Status
- [ ] All unit tests passing
- [ ] Integration tests passing
- [ ] Code coverage >80%
- [ ] Security scan passed
- [ ] Performance benchmarks met
- [ ] Documentation complete
- [ ] Ready for production deployment

## Overall Assessment
**Migration Success Score:** [SCORE]/100
**Readiness for Production:** ✅/❌
**Recommended Next Steps:** [PRIORITIZED_LIST]
```

## AI State Management for Large Projects

### Temporary Data Storage
The AI must maintain state across multiple sessions for large projects:

#### 1. Project Context File: `PROJECT_CONTEXT.json`
```json
{
  "project_info": {
    "name": "ProjectName",
    "java_version": "8",
    "target_java_version": "21",
    "framework": "Spring Boot 3.x",
    "database": "PostgreSQL",
    "estimated_size": "large"
  },
  "analysis_progress": {
    "old_structure_scanned": true,
    "old_analysis_complete": true,
    "transformation_guidelines_created": false,
    "new_structure_designed": false
  },
  "current_phase": "transformation_planning",
  "next_tasks": [
    "Create transformation guidelines",
    "Design new architecture"
  ],
  "key_findings": {
    "critical_issues": ["Manual dependency injection", "JDBC usage"],
    "complexity_score": 8,
    "estimated_effort": "6 months"
  }
}
```

#### 2. Session Memory File: `AI_SESSION_MEMORY.json`
```json
{
  "last_session": "2025-08-04T14:00:00Z",
  "files_analyzed": [
    "src/main/java/com/company/service/UserService.java",
    "src/main/java/com/company/dao/UserDao.java"
  ],
  "current_focus": "Service layer analysis",
  "pending_decisions": [
    {
      "decision": "Database migration approach",
      "options": ["Flyway", "Liquibase"],
      "recommendation": "Flyway"
    }
  ],
  "code_patterns_identified": [
    "DAO pattern with JDBC",
    "Manual transaction management",
    "Properties-based configuration"
  ]
}
```

### AI Workflow Instructions

#### For Each Session:
1. **Load Context:** Read `PROJECT_CONTEXT.json` and `AI_SESSION_MEMORY.json`
2. **Continue Work:** Based on `current_phase` and `next_tasks`
3. **Update Progress:** Save findings to appropriate `.md` files
4. **Save State:** Update context and memory files before ending session

#### Large Project Handling:
1. **Chunking Strategy:** Analyze project in logical chunks (package by package)
2. **Incremental Analysis:** Build analysis incrementally across sessions
3. **Consistency Checks:** Validate consistency between documents
4. **Progress Tracking:** Maintain clear progress indicators

### AI Collaboration Commands

When working on large projects, AI agents should:

#### Start Command:
```
AI_LOAD_PROJECT_CONTEXT: java-transformation/
```

#### Save Progress Command:
```
AI_SAVE_SESSION_STATE: {
  "current_file": "ANALYTIC_OLD_JAVA.md",
  "completion_percentage": 65,
  "next_focus": "Database layer analysis"
}
```

#### Resume Command:
```
AI_RESUME_FROM_LAST_SESSION: java-transformation/AI_SESSION_MEMORY.json
```

## Quality Assurance Checklist

Before completing each document:
- [ ] All sections completed according to template
- [ ] Specific examples provided (not generic)
- [ ] Actionable recommendations included
- [ ] Cross-references between documents maintained
- [ ] Technical accuracy verified
- [ ] Business impact assessed
- [ ] Timeline estimates provided
- [ ] Risk assessment included

## Document Maintenance

### Version Control
- Each document should include version and last updated timestamp
- Track changes between versions
- Maintain change log for major updates

### Review Process
- Technical review by senior developer
- Business review by stakeholder
- Architecture review by architect
- Final approval before implementation

---

**Note:** This guideline ensures systematic, thorough, and consistent Java transformation projects with proper AI state management for large-scale enterprise applications.
