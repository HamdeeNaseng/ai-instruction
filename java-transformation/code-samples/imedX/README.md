# ImedX EHR System - Legacy Java Demo Project

## Overview

ImedX is a **demo Electronic Health Records (EHR) system** built with legacy Java 8 technologies. This project serves as an example of older Java architectures that are commonly found in enterprise environments and are candidates for modernization to Spring Boot.

## Project Purpose

🎯 **This is a demonstration project created for:**
- Java migration R&D and analysis
- Showcasing legacy Java patterns and practices
- Providing a realistic example for modernization planning
- Educational purposes for understanding legacy system challenges

## Architecture & Technologies

### Current Technology Stack (Legacy)
- **Java Version:** Java 8
- **Build Tool:** Maven 3.x
- **Database Access:** Raw JDBC with manual connection management
- **Logging:** Log4j 1.2.x (legacy)
- **Testing:** JUnit 4
- **Configuration:** Properties files
- **Dependency Management:** Manual instantiation (no DI framework)

### Architecture Patterns
- **Layered Architecture:** Model → DAO → Service → Application
- **Design Patterns:** Factory, Singleton, DAO
- **Database Pattern:** Traditional JDBC with manual resource management
- **Configuration:** Properties-based configuration

## Project Structure

```
imedX/
├── src/main/java/com/intermedisoft/imedx/
│   ├── model/              # Domain entities (Patient, Doctor, MedicalRecord)
│   ├── dao/                # Data Access Objects with JDBC
│   │   └── impl/           # DAO implementations
│   ├── service/            # Business logic layer
│   │   └── impl/           # Service implementations
│   ├── util/               # Utility classes (DatabaseConnection)
│   └── ImedXApplication.java   # Main application class
├── src/main/resources/
│   ├── application.properties  # Application configuration
│   └── log4j.properties       # Logging configuration
├── src/test/java/          # JUnit 4 tests
└── pom.xml                 # Maven configuration
```

## Domain Model

### Core Entities

1. **Patient**
   - Personal information (name, DOB, gender, contact)
   - Medical information (blood type, allergies)
   - Emergency contact details
   - Registration and status tracking

2. **Doctor**
   - Professional information (specialization, license)
   - Contact and employment details
   - Experience and qualifications

3. **MedicalRecord**
   - Visit information and medical history
   - Vital signs and measurements
   - Diagnosis and treatment records
   - Patient-doctor relationship

## Legacy Patterns Demonstrated

### 1. Manual Dependency Management
```java
// No dependency injection framework
private final PatientDao patientDao = new PatientDaoImpl();
```

### 2. JDBC Resource Management
```java
// Manual connection handling
Connection conn = null;
PreparedStatement stmt = null;
ResultSet rs = null;
try {
    conn = DatabaseConnection.getConnection();
    // ... database operations
} finally {
    DatabaseConnection.closeResources(conn, stmt, rs);
}
```

### 3. Properties-Based Configuration
```properties
database.url=jdbc:mysql://localhost:3306/imedx_ehr
database.username=imedx_user
database.password=imedx_password
```

### 4. Manual Entity Mapping
```java
private Patient mapResultSetToPatient(ResultSet rs) throws SQLException {
    Patient patient = new Patient();
    patient.setPatientId(rs.getLong("patient_id"));
    patient.setFirstName(rs.getString("first_name"));
    // ... manual mapping for all fields
}
```

## Database Schema

The system uses MySQL with the following main tables:

- `patients` - Patient demographic and contact information
- `doctors` - Healthcare provider information
- `medical_records` - Patient visit records and medical data

## Getting Started

### Prerequisites
- Java 8 or higher
- Maven 3.x
- MySQL 5.7+ or 8.0+

### Database Setup
1. Create MySQL database: `imedx_ehr`
2. Create user with appropriate permissions
3. Update database configuration in `application.properties`

### Running the Application
```bash
# Compile the project
mvn compile

# Run tests
mvn test

# Run the application
mvn exec:java -Dexec.mainClass="com.intermedisoft.imedx.ImedXApplication"

# Or create JAR and run
mvn package
java -jar target/imedx-ehr-system-1.0.0-LEGACY.jar
```

## Sample Data

The application automatically creates sample patients on startup:
- John Doe (Male, O+ blood type, Penicillin allergy)
- Sarah Johnson (Female, A- blood type)
- Michael Chen (Male, B+ blood type, multiple allergies)

## Modernization Opportunities

This legacy system demonstrates several areas that would benefit from modernization:

### 1. Spring Boot Migration
- **Auto-configuration** instead of manual setup
- **Dependency injection** instead of manual instantiation
- **Spring Data JPA** instead of raw JDBC
- **Spring Boot Actuator** for monitoring

### 2. Modern Java Features
- **Lombok** to reduce boilerplate code
- **Java 21+** features (records, pattern matching, etc.)
- **Stream API** for data processing
- **Optional** for null safety

### 3. Database Layer Improvements
- **JPA/Hibernate** for ORM
- **Connection pooling** (HikariCP)
- **Database migrations** (Flyway/Liquibase)
- **Repository pattern** with Spring Data

### 4. Testing Enhancements
- **JUnit 5** with modern testing features
- **TestContainers** for integration testing
- **MockMvc** for web layer testing
- **AssertJ** for fluent assertions

### 5. Configuration Management
- **YAML configuration** instead of properties
- **Profiles** for environment-specific settings
- **Externalized configuration** for deployment flexibility

## Migration Strategy

For organizations looking to modernize similar legacy systems:

1. **Phase 1:** Update to modern Java version (8 → 21+)
2. **Phase 2:** Introduce Spring Boot framework
3. **Phase 3:** Migrate to Spring Data JPA
4. **Phase 4:** Add REST APIs and modern UI
5. **Phase 5:** Implement microservices architecture (if needed)

## Known Limitations

As a legacy system, this project includes several intentional limitations:

- No REST API (console interface only)
- Basic validation and error handling
- No authentication or authorization
- Limited transaction management
- Manual resource management
- Tight coupling between layers
- No caching strategy
- Basic logging implementation

## Contributing

This is a demonstration project. While not actively maintained for production use, it serves as an excellent example for:

- Java migration training
- Legacy system analysis
- Modernization planning workshops
- Architecture improvement discussions

## License

This project is created for educational and demonstration purposes.

---

**Note:** This is a demo project representing legacy Java patterns. It is not intended for production use but rather as a learning tool for understanding migration challenges and opportunities in enterprise Java applications.
