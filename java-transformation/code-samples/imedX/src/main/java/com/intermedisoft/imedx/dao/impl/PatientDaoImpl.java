package com.intermedisoft.imedx.dao.impl;

import com.intermedisoft.imedx.dao.PatientDao;
import com.intermedisoft.imedx.model.Patient;
import com.intermedisoft.imedx.util.DatabaseConnection;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.ArrayList;
import java.util.Date;
import java.util.List;
import java.util.logging.Logger;

/**
 * Patient DAO Implementation - Legacy Java 8 style with JDBC
 * Demonstrates old-style database access with manual connection management
 */
public class PatientDaoImpl implements PatientDao {

  private static final Logger logger = Logger.getLogger(
    PatientDaoImpl.class.getName()
  );

  private static final String INSERT_PATIENT =
    "INSERT INTO patients (first_name, last_name, date_of_birth, gender, phone_number, " +
    "email, address, national_id, registration_date, emergency_contact, " +
    "emergency_contact_phone, blood_type, allergies, active) " +
    "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)";

  private static final String SELECT_PATIENT_BY_ID =
    "SELECT * FROM patients WHERE patient_id = ?";

  private static final String SELECT_ALL_PATIENTS =
    "SELECT * FROM patients ORDER BY last_name, first_name";

  private static final String UPDATE_PATIENT =
    "UPDATE patients SET first_name = ?, last_name = ?, date_of_birth = ?, gender = ?, " +
    "phone_number = ?, email = ?, address = ?, national_id = ?, emergency_contact = ?, " +
    "emergency_contact_phone = ?, blood_type = ?, allergies = ?, active = ? " +
    "WHERE patient_id = ?";

  private static final String DELETE_PATIENT =
    "DELETE FROM patients WHERE patient_id = ?";

  private static final String SELECT_BY_NAME =
    "SELECT * FROM patients WHERE first_name = ? AND last_name = ?";

  private static final String SELECT_BY_NATIONAL_ID =
    "SELECT * FROM patients WHERE national_id = ?";

  private static final String COUNT_PATIENTS = "SELECT COUNT(*) FROM patients";

  @Override
  public Patient save(Patient patient) {
    Connection conn = null;
    PreparedStatement stmt = null;
    ResultSet rs = null;

    try {
      conn = DatabaseConnection.getConnection();
      stmt =
        conn.prepareStatement(INSERT_PATIENT, Statement.RETURN_GENERATED_KEYS);

      stmt.setString(1, patient.getFirstName());
      stmt.setString(2, patient.getLastName());
      stmt.setDate(3, new java.sql.Date(patient.getDateOfBirth().getTime()));
      stmt.setString(4, patient.getGender());
      stmt.setString(5, patient.getPhoneNumber());
      stmt.setString(6, patient.getEmail());
      stmt.setString(7, patient.getAddress());
      stmt.setString(8, patient.getNationalId());
      stmt.setDate(
        9,
        new java.sql.Date(patient.getRegistrationDate().getTime())
      );
      stmt.setString(10, patient.getEmergencyContact());
      stmt.setString(11, patient.getEmergencyContactPhone());
      stmt.setString(12, patient.getBloodType());
      stmt.setString(13, patient.getAllergies());
      stmt.setBoolean(14, patient.isActive());

      int rowsAffected = stmt.executeUpdate();

      if (rowsAffected > 0) {
        rs = stmt.getGeneratedKeys();
        if (rs.next()) {
          patient.setPatientId(rs.getLong(1));
        }
      }

      logger.info("Patient saved successfully: " + patient.getFullName());
      return patient;
    } catch (SQLException e) {
      logger.severe("Error saving patient: " + e.getMessage());
      throw new RuntimeException("Failed to save patient", e);
    } finally {
      DatabaseConnection.closeResources(conn, stmt, rs);
    }
  }

  @Override
  public Patient findById(Long id) {
    Connection conn = null;
    PreparedStatement stmt = null;
    ResultSet rs = null;

    try {
      conn = DatabaseConnection.getConnection();
      stmt = conn.prepareStatement(SELECT_PATIENT_BY_ID);
      stmt.setLong(1, id);

      rs = stmt.executeQuery();

      if (rs.next()) {
        return mapResultSetToPatient(rs);
      }

      return null;
    } catch (SQLException e) {
      logger.severe("Error finding patient by ID: " + e.getMessage());
      throw new RuntimeException("Failed to find patient", e);
    } finally {
      DatabaseConnection.closeResources(conn, stmt, rs);
    }
  }

  @Override
  public List<Patient> findAll() {
    Connection conn = null;
    PreparedStatement stmt = null;
    ResultSet rs = null;
    List<Patient> patients = new ArrayList<>();

    try {
      conn = DatabaseConnection.getConnection();
      stmt = conn.prepareStatement(SELECT_ALL_PATIENTS);
      rs = stmt.executeQuery();

      while (rs.next()) {
        patients.add(mapResultSetToPatient(rs));
      }

      logger.info("Found " + patients.size() + " patients");
      return patients;
    } catch (SQLException e) {
      logger.severe("Error finding all patients: " + e.getMessage());
      throw new RuntimeException("Failed to find patients", e);
    } finally {
      DatabaseConnection.closeResources(conn, stmt, rs);
    }
  }

  @Override
  public Patient update(Patient patient) {
    Connection conn = null;
    PreparedStatement stmt = null;

    try {
      conn = DatabaseConnection.getConnection();
      stmt = conn.prepareStatement(UPDATE_PATIENT);

      stmt.setString(1, patient.getFirstName());
      stmt.setString(2, patient.getLastName());
      stmt.setDate(3, new java.sql.Date(patient.getDateOfBirth().getTime()));
      stmt.setString(4, patient.getGender());
      stmt.setString(5, patient.getPhoneNumber());
      stmt.setString(6, patient.getEmail());
      stmt.setString(7, patient.getAddress());
      stmt.setString(8, patient.getNationalId());
      stmt.setString(9, patient.getEmergencyContact());
      stmt.setString(10, patient.getEmergencyContactPhone());
      stmt.setString(11, patient.getBloodType());
      stmt.setString(12, patient.getAllergies());
      stmt.setBoolean(13, patient.isActive());
      stmt.setLong(14, patient.getPatientId());

      int rowsAffected = stmt.executeUpdate();

      if (rowsAffected > 0) {
        logger.info("Patient updated successfully: " + patient.getFullName());
        return patient;
      } else {
        logger.warning("No patient found with ID: " + patient.getPatientId());
        return null;
      }
    } catch (SQLException e) {
      logger.severe("Error updating patient: " + e.getMessage());
      throw new RuntimeException("Failed to update patient", e);
    } finally {
      DatabaseConnection.closeResources(conn, stmt, null);
    }
  }

  @Override
  public boolean deleteById(Long id) {
    Connection conn = null;
    PreparedStatement stmt = null;

    try {
      conn = DatabaseConnection.getConnection();
      stmt = conn.prepareStatement(DELETE_PATIENT);
      stmt.setLong(1, id);

      int rowsAffected = stmt.executeUpdate();

      if (rowsAffected > 0) {
        logger.info("Patient deleted successfully with ID: " + id);
        return true;
      } else {
        logger.warning("No patient found with ID: " + id);
        return false;
      }
    } catch (SQLException e) {
      logger.severe("Error deleting patient: " + e.getMessage());
      throw new RuntimeException("Failed to delete patient", e);
    } finally {
      DatabaseConnection.closeResources(conn, stmt, null);
    }
  }

  @Override
  public boolean delete(Patient patient) {
    return deleteById(patient.getPatientId());
  }

  @Override
  public boolean existsById(Long id) {
    return findById(id) != null;
  }

  @Override
  public long count() {
    Connection conn = null;
    PreparedStatement stmt = null;
    ResultSet rs = null;

    try {
      conn = DatabaseConnection.getConnection();
      stmt = conn.prepareStatement(COUNT_PATIENTS);
      rs = stmt.executeQuery();

      if (rs.next()) {
        return rs.getLong(1);
      }

      return 0;
    } catch (SQLException e) {
      logger.severe("Error counting patients: " + e.getMessage());
      throw new RuntimeException("Failed to count patients", e);
    } finally {
      DatabaseConnection.closeResources(conn, stmt, rs);
    }
  }

  @Override
  public List<Patient> findByName(String firstName, String lastName) {
    Connection conn = null;
    PreparedStatement stmt = null;
    ResultSet rs = null;
    List<Patient> patients = new ArrayList<>();

    try {
      conn = DatabaseConnection.getConnection();
      stmt = conn.prepareStatement(SELECT_BY_NAME);
      stmt.setString(1, firstName);
      stmt.setString(2, lastName);

      rs = stmt.executeQuery();

      while (rs.next()) {
        patients.add(mapResultSetToPatient(rs));
      }

      return patients;
    } catch (SQLException e) {
      logger.severe("Error finding patients by name: " + e.getMessage());
      throw new RuntimeException("Failed to find patients by name", e);
    } finally {
      DatabaseConnection.closeResources(conn, stmt, rs);
    }
  }

  @Override
  public Patient findByNationalId(String nationalId) {
    Connection conn = null;
    PreparedStatement stmt = null;
    ResultSet rs = null;

    try {
      conn = DatabaseConnection.getConnection();
      stmt = conn.prepareStatement(SELECT_BY_NATIONAL_ID);
      stmt.setString(1, nationalId);

      rs = stmt.executeQuery();

      if (rs.next()) {
        return mapResultSetToPatient(rs);
      }

      return null;
    } catch (SQLException e) {
      logger.severe("Error finding patient by national ID: " + e.getMessage());
      throw new RuntimeException("Failed to find patient by national ID", e);
    } finally {
      DatabaseConnection.closeResources(conn, stmt, rs);
    }
  }

  // Simplified implementations for other methods (would be similar patterns)
  @Override
  public List<Patient> findByDateOfBirthBetween(Date fromDate, Date toDate) {
    // Implementation would be similar to above with date range query
    return new ArrayList<>(); // Placeholder
  }

  @Override
  public List<Patient> findByGender(String gender) {
    // Implementation would be similar to above with gender filter
    return new ArrayList<>(); // Placeholder
  }

  @Override
  public List<Patient> findByActiveStatus(boolean active) {
    // Implementation would be similar to above with active status filter
    return new ArrayList<>(); // Placeholder
  }

  @Override
  public List<Patient> searchByName(String searchTerm) {
    // Implementation would use LIKE operator for partial matching
    return new ArrayList<>(); // Placeholder
  }

  @Override
  public List<Patient> findByRegistrationDateBetween(
    Date fromDate,
    Date toDate
  ) {
    // Implementation would be similar to date of birth range
    return new ArrayList<>(); // Placeholder
  }

  @Override
  public List<Patient> findByBloodType(String bloodType) {
    // Implementation would filter by blood type
    return new ArrayList<>(); // Placeholder
  }

  @Override
  public long countByGender(String gender) {
    // Implementation would count patients by gender
    return 0; // Placeholder
  }

  @Override
  public long countActivePatients() {
    // Implementation would count active patients
    return 0; // Placeholder
  }

  /**
   * Map ResultSet to Patient object - Legacy style mapping
   */
  private Patient mapResultSetToPatient(ResultSet rs) throws SQLException {
    Patient patient = new Patient();

    patient.setPatientId(rs.getLong("patient_id"));
    patient.setFirstName(rs.getString("first_name"));
    patient.setLastName(rs.getString("last_name"));
    patient.setDateOfBirth(rs.getDate("date_of_birth"));
    patient.setGender(rs.getString("gender"));
    patient.setPhoneNumber(rs.getString("phone_number"));
    patient.setEmail(rs.getString("email"));
    patient.setAddress(rs.getString("address"));
    patient.setNationalId(rs.getString("national_id"));
    patient.setRegistrationDate(rs.getDate("registration_date"));
    patient.setEmergencyContact(rs.getString("emergency_contact"));
    patient.setEmergencyContactPhone(rs.getString("emergency_contact_phone"));
    patient.setBloodType(rs.getString("blood_type"));
    patient.setAllergies(rs.getString("allergies"));
    patient.setActive(rs.getBoolean("active"));

    return patient;
  }
}
