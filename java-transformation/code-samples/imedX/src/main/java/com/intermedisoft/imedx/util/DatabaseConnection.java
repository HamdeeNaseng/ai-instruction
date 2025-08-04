package com.intermedisoft.imedx.util;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.Properties;
import java.util.logging.Logger;

/**
 * Database Connection Utility - Legacy Java 8 style
 * Manages database connections using traditional JDBC patterns
 * This represents the old-style connection management that would be replaced
 * by Spring Boot's auto-configuration and connection pooling
 */
public class DatabaseConnection {

  private static final Logger logger = Logger.getLogger(
    DatabaseConnection.class.getName()
  );

  // Database configuration - would typically be in properties file
  private static final String DB_URL = "jdbc:mysql://localhost:3306/imedx_ehr";
  private static final String DB_USERNAME = "imedx_user";
  private static final String DB_PASSWORD = "imedx_password";
  private static final String DB_DRIVER = "com.mysql.cj.jdbc.Driver";

  // Connection pool simulation - very basic (Spring Boot would handle this better)
  private static final int MAX_CONNECTIONS = 10;
  private static int activeConnections = 0;

  static {
    // Load MySQL JDBC driver - legacy approach
    try {
      Class.forName(DB_DRIVER);
      logger.info("MySQL JDBC Driver loaded successfully");
    } catch (ClassNotFoundException e) {
      logger.severe("Failed to load MySQL JDBC Driver: " + e.getMessage());
      throw new RuntimeException("Database driver not found", e);
    }
  }

  /**
   * Get database connection - Legacy style connection management
   * In modern Spring Boot, this would be handled by DataSource auto-configuration
   * @return Database connection
   * @throws SQLException if connection fails
   */
  public static Connection getConnection() throws SQLException {
    if (activeConnections >= MAX_CONNECTIONS) {
      throw new SQLException("Maximum connections reached: " + MAX_CONNECTIONS);
    }

    try {
      Properties props = new Properties();
      props.setProperty("user", DB_USERNAME);
      props.setProperty("password", DB_PASSWORD);
      props.setProperty("useSSL", "false");
      props.setProperty("serverTimezone", "UTC");
      props.setProperty("allowPublicKeyRetrieval", "true");

      Connection connection = DriverManager.getConnection(DB_URL, props);
      connection.setAutoCommit(true); // Legacy approach - would use transactions in modern code

      activeConnections++;
      logger.info(
        "Database connection established. Active connections: " +
        activeConnections
      );

      return connection;
    } catch (SQLException e) {
      logger.severe(
        "Failed to establish database connection: " + e.getMessage()
      );
      throw e;
    }
  }

  /**
   * Close database connection - Legacy style resource management
   * In modern Spring Boot, this would be handled automatically by connection pooling
   * @param connection Connection to close
   */
  public static void closeConnection(Connection connection) {
    if (connection != null) {
      try {
        connection.close();
        activeConnections--;
        logger.info(
          "Database connection closed. Active connections: " + activeConnections
        );
      } catch (SQLException e) {
        logger.severe("Error closing database connection: " + e.getMessage());
      }
    }
  }

  /**
   * Close all database resources - Legacy style resource management
   * This is a common pattern in legacy JDBC code that would be eliminated
   * with Spring Boot's automatic resource management
   * @param connection Database connection
   * @param statement Prepared statement
   * @param resultSet Result set
   */
  public static void closeResources(
    Connection connection,
    PreparedStatement statement,
    ResultSet resultSet
  ) {
    // Close ResultSet
    if (resultSet != null) {
      try {
        resultSet.close();
      } catch (SQLException e) {
        logger.warning("Error closing ResultSet: " + e.getMessage());
      }
    }

    // Close PreparedStatement
    if (statement != null) {
      try {
        statement.close();
      } catch (SQLException e) {
        logger.warning("Error closing PreparedStatement: " + e.getMessage());
      }
    }

    // Close Connection
    closeConnection(connection);
  }

  /**
   * Test database connectivity - Legacy style connection testing
   * @return true if connection successful, false otherwise
   */
  public static boolean testConnection() {
    Connection conn = null;
    try {
      conn = getConnection();
      logger.info("Database connection test successful");
      return true;
    } catch (SQLException e) {
      logger.severe("Database connection test failed: " + e.getMessage());
      return false;
    } finally {
      closeConnection(conn);
    }
  }

  /**
   * Get current active connections count
   * @return Number of active connections
   */
  public static int getActiveConnectionsCount() {
    return activeConnections;
  }

  /**
   * Initialize database - Legacy style database setup
   * In modern Spring Boot, this would be handled by Flyway or Liquibase migrations
   * @return true if initialization successful
   */
  public static boolean initializeDatabase() {
    Connection conn = null;
    PreparedStatement stmt = null;

    try {
      conn = getConnection();

      // Create patients table if not exists
      String createPatientsTable =
        "CREATE TABLE IF NOT EXISTS patients (" +
        "patient_id BIGINT AUTO_INCREMENT PRIMARY KEY, " +
        "first_name VARCHAR(100) NOT NULL, " +
        "last_name VARCHAR(100) NOT NULL, " +
        "date_of_birth DATE NOT NULL, " +
        "gender VARCHAR(10) NOT NULL, " +
        "phone_number VARCHAR(20), " +
        "email VARCHAR(150), " +
        "address TEXT, " +
        "national_id VARCHAR(50) UNIQUE, " +
        "registration_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, " +
        "emergency_contact VARCHAR(100), " +
        "emergency_contact_phone VARCHAR(20), " +
        "blood_type VARCHAR(10), " +
        "allergies TEXT, " +
        "active BOOLEAN DEFAULT TRUE, " +
        "INDEX idx_national_id (national_id), " +
        "INDEX idx_name (last_name, first_name), " +
        "INDEX idx_registration_date (registration_date)" +
        ")";

      stmt = conn.prepareStatement(createPatientsTable);
      stmt.executeUpdate();

      // Create doctors table if not exists
      String createDoctorsTable =
        "CREATE TABLE IF NOT EXISTS doctors (" +
        "doctor_id BIGINT AUTO_INCREMENT PRIMARY KEY, " +
        "first_name VARCHAR(100) NOT NULL, " +
        "last_name VARCHAR(100) NOT NULL, " +
        "specialization VARCHAR(100) NOT NULL, " +
        "license_number VARCHAR(50) UNIQUE NOT NULL, " +
        "email VARCHAR(150), " +
        "phone_number VARCHAR(20), " +
        "department VARCHAR(100), " +
        "hire_date DATE, " +
        "qualification TEXT, " +
        "experience_years INT, " +
        "active BOOLEAN DEFAULT TRUE, " +
        "working_hours VARCHAR(100), " +
        "consultation_fee DECIMAL(10,2), " +
        "INDEX idx_license (license_number), " +
        "INDEX idx_specialization (specialization)" +
        ")";

      stmt.close();
      stmt = conn.prepareStatement(createDoctorsTable);
      stmt.executeUpdate();

      // Create medical_records table if not exists
      String createMedicalRecordsTable =
        "CREATE TABLE IF NOT EXISTS medical_records (" +
        "record_id BIGINT AUTO_INCREMENT PRIMARY KEY, " +
        "patient_id BIGINT NOT NULL, " +
        "doctor_id BIGINT NOT NULL, " +
        "visit_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, " +
        "chief_complaint TEXT, " +
        "present_illness TEXT, " +
        "physical_examination TEXT, " +
        "diagnosis TEXT, " +
        "treatment TEXT, " +
        "medications TEXT, " +
        "notes TEXT, " +
        "record_type VARCHAR(50), " +
        "temperature DECIMAL(4,1), " +
        "blood_pressure_systolic INT, " +
        "blood_pressure_diastolic INT, " +
        "heart_rate INT, " +
        "weight DECIMAL(5,2), " +
        "height DECIMAL(5,2), " +
        "created_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, " +
        "updated_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, " +
        "status VARCHAR(50) DEFAULT 'DRAFT', " +
        "FOREIGN KEY (patient_id) REFERENCES patients(patient_id), " +
        "FOREIGN KEY (doctor_id) REFERENCES doctors(doctor_id), " +
        "INDEX idx_patient_id (patient_id), " +
        "INDEX idx_doctor_id (doctor_id), " +
        "INDEX idx_visit_date (visit_date)" +
        ")";

      stmt.close();
      stmt = conn.prepareStatement(createMedicalRecordsTable);
      stmt.executeUpdate();

      logger.info("Database tables initialized successfully");
      return true;
    } catch (SQLException e) {
      logger.severe("Failed to initialize database: " + e.getMessage());
      return false;
    } finally {
      closeResources(conn, stmt, null);
    }
  }
}
