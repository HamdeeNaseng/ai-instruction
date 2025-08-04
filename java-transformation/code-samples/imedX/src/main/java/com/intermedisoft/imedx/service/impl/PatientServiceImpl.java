package com.intermedisoft.imedx.service.impl;

import com.intermedisoft.imedx.dao.PatientDao;
import com.intermedisoft.imedx.dao.impl.PatientDaoImpl;
import com.intermedisoft.imedx.model.Patient;
import com.intermedisoft.imedx.service.PatientService;
import com.intermedisoft.imedx.service.PatientStatistics;
import java.util.Calendar;
import java.util.Date;
import java.util.List;
import java.util.logging.Logger;

/**
 * Patient Service Implementation - Legacy Java 8 style
 * Implements business logic for patient management
 * This represents the old-style service layer that would be modernized
 * with Spring Boot's dependency injection and transaction management
 */
public class PatientServiceImpl implements PatientService {

  private static final Logger logger = Logger.getLogger(
    PatientServiceImpl.class.getName()
  );

  // Manual dependency management - would be replaced by Spring's @Autowired
  private final PatientDao patientDao;

  // Constructor injection - primitive form of dependency injection
  public PatientServiceImpl() {
    this.patientDao = new PatientDaoImpl(); // Hard-coded dependency - bad practice
  }

  // Constructor for testing - allows dependency injection
  public PatientServiceImpl(PatientDao patientDao) {
    this.patientDao = patientDao;
  }

  @Override
  public Patient registerPatient(Patient patient) {
    logger.info("Registering new patient: " + patient.getFullName());

    // Validate patient data
    if (!validatePatientData(patient)) {
      throw new IllegalArgumentException("Invalid patient data");
    }

    // Check if national ID is unique (if provided)
    if (
      patient.getNationalId() != null &&
      !patient.getNationalId().trim().isEmpty()
    ) {
      if (!isNationalIdUnique(patient.getNationalId(), null)) {
        throw new IllegalArgumentException(
          "National ID already exists: " + patient.getNationalId()
        );
      }
    }

    // Set registration date if not already set
    if (patient.getRegistrationDate() == null) {
      patient.setRegistrationDate(new Date());
    }

    // Set active status if not already set
    patient.setActive(true);

    try {
      Patient savedPatient = patientDao.save(patient);
      logger.info(
        "Patient registered successfully with ID: " +
        savedPatient.getPatientId()
      );
      return savedPatient;
    } catch (Exception e) {
      logger.severe("Error registering patient: " + e.getMessage());
      throw new RuntimeException("Failed to register patient", e);
    }
  }

  @Override
  public Patient updatePatient(Patient patient) {
    logger.info("Updating patient: " + patient.getPatientId());

    // Validate patient data
    if (!validatePatientData(patient)) {
      throw new IllegalArgumentException("Invalid patient data");
    }

    // Check if patient exists
    Patient existingPatient = patientDao.findById(patient.getPatientId());
    if (existingPatient == null) {
      throw new IllegalArgumentException(
        "Patient not found with ID: " + patient.getPatientId()
      );
    }

    // Check if national ID is unique (excluding current patient)
    if (
      patient.getNationalId() != null &&
      !patient.getNationalId().trim().isEmpty()
    ) {
      if (
        !isNationalIdUnique(patient.getNationalId(), patient.getPatientId())
      ) {
        throw new IllegalArgumentException(
          "National ID already exists: " + patient.getNationalId()
        );
      }
    }

    try {
      Patient updatedPatient = patientDao.update(patient);
      logger.info(
        "Patient updated successfully: " + updatedPatient.getPatientId()
      );
      return updatedPatient;
    } catch (Exception e) {
      logger.severe("Error updating patient: " + e.getMessage());
      throw new RuntimeException("Failed to update patient", e);
    }
  }

  @Override
  public Patient findPatientById(Long patientId) {
    if (patientId == null) {
      throw new IllegalArgumentException("Patient ID cannot be null");
    }

    try {
      return patientDao.findById(patientId);
    } catch (Exception e) {
      logger.severe("Error finding patient by ID: " + e.getMessage());
      throw new RuntimeException("Failed to find patient", e);
    }
  }

  @Override
  public Patient findPatientByNationalId(String nationalId) {
    if (nationalId == null || nationalId.trim().isEmpty()) {
      throw new IllegalArgumentException("National ID cannot be null or empty");
    }

    try {
      return patientDao.findByNationalId(nationalId.trim());
    } catch (Exception e) {
      logger.severe("Error finding patient by national ID: " + e.getMessage());
      throw new RuntimeException("Failed to find patient", e);
    }
  }

  @Override
  public List<Patient> searchPatientsByName(String searchTerm) {
    if (searchTerm == null || searchTerm.trim().isEmpty()) {
      throw new IllegalArgumentException("Search term cannot be null or empty");
    }

    try {
      return patientDao.searchByName(searchTerm.trim());
    } catch (Exception e) {
      logger.severe("Error searching patients by name: " + e.getMessage());
      throw new RuntimeException("Failed to search patients", e);
    }
  }

  @Override
  public List<Patient> getAllActivePatients() {
    try {
      return patientDao.findByActiveStatus(true);
    } catch (Exception e) {
      logger.severe("Error getting active patients: " + e.getMessage());
      throw new RuntimeException("Failed to get active patients", e);
    }
  }

  @Override
  public List<Patient> getAllPatients() {
    try {
      return patientDao.findAll();
    } catch (Exception e) {
      logger.severe("Error getting all patients: " + e.getMessage());
      throw new RuntimeException("Failed to get patients", e);
    }
  }

  @Override
  public boolean deactivatePatient(Long patientId) {
    if (patientId == null) {
      throw new IllegalArgumentException("Patient ID cannot be null");
    }

    try {
      Patient patient = patientDao.findById(patientId);
      if (patient == null) {
        logger.warning("Patient not found with ID: " + patientId);
        return false;
      }

      patient.setActive(false);
      Patient updatedPatient = patientDao.update(patient);

      if (updatedPatient != null) {
        logger.info("Patient deactivated successfully: " + patientId);
        return true;
      } else {
        logger.warning("Failed to deactivate patient: " + patientId);
        return false;
      }
    } catch (Exception e) {
      logger.severe("Error deactivating patient: " + e.getMessage());
      throw new RuntimeException("Failed to deactivate patient", e);
    }
  }

  @Override
  public boolean reactivatePatient(Long patientId) {
    if (patientId == null) {
      throw new IllegalArgumentException("Patient ID cannot be null");
    }

    try {
      Patient patient = patientDao.findById(patientId);
      if (patient == null) {
        logger.warning("Patient not found with ID: " + patientId);
        return false;
      }

      patient.setActive(true);
      Patient updatedPatient = patientDao.update(patient);

      if (updatedPatient != null) {
        logger.info("Patient reactivated successfully: " + patientId);
        return true;
      } else {
        logger.warning("Failed to reactivate patient: " + patientId);
        return false;
      }
    } catch (Exception e) {
      logger.severe("Error reactivating patient: " + e.getMessage());
      throw new RuntimeException("Failed to reactivate patient", e);
    }
  }

  @Override
  public List<Patient> getPatientsByAgeRange(int minAge, int maxAge) {
    if (minAge < 0 || maxAge < 0 || minAge > maxAge) {
      throw new IllegalArgumentException(
        "Invalid age range: " + minAge + " - " + maxAge
      );
    }

    // Calculate date range based on ages - legacy approach
    Calendar cal = Calendar.getInstance();
    cal.add(Calendar.YEAR, -maxAge - 1);
    Date fromDate = cal.getTime();

    cal = Calendar.getInstance();
    cal.add(Calendar.YEAR, -minAge);
    Date toDate = cal.getTime();

    try {
      return patientDao.findByDateOfBirthBetween(fromDate, toDate);
    } catch (Exception e) {
      logger.severe("Error getting patients by age range: " + e.getMessage());
      throw new RuntimeException("Failed to get patients by age range", e);
    }
  }

  @Override
  public List<Patient> getPatientsByGender(String gender) {
    if (gender == null || gender.trim().isEmpty()) {
      throw new IllegalArgumentException("Gender cannot be null or empty");
    }

    // Validate gender - legacy approach with hardcoded values
    String normalizedGender = gender.trim().toUpperCase();
    if (
      !normalizedGender.equals("M") &&
      !normalizedGender.equals("F") &&
      !normalizedGender.equals("MALE") &&
      !normalizedGender.equals("FEMALE")
    ) {
      throw new IllegalArgumentException("Invalid gender: " + gender);
    }

    try {
      return patientDao.findByGender(normalizedGender);
    } catch (Exception e) {
      logger.severe("Error getting patients by gender: " + e.getMessage());
      throw new RuntimeException("Failed to get patients by gender", e);
    }
  }

  @Override
  public List<Patient> getPatientsByRegistrationDateRange(
    Date fromDate,
    Date toDate
  ) {
    if (fromDate == null || toDate == null) {
      throw new IllegalArgumentException("Date range cannot be null");
    }

    if (fromDate.after(toDate)) {
      throw new IllegalArgumentException("From date cannot be after to date");
    }

    try {
      return patientDao.findByRegistrationDateBetween(fromDate, toDate);
    } catch (Exception e) {
      logger.severe(
        "Error getting patients by registration date range: " + e.getMessage()
      );
      throw new RuntimeException(
        "Failed to get patients by registration date range",
        e
      );
    }
  }

  @Override
  public boolean validatePatientData(Patient patient) {
    if (patient == null) {
      logger.warning("Patient is null");
      return false;
    }

    // Validate required fields - legacy approach with manual validation
    if (
      patient.getFirstName() == null || patient.getFirstName().trim().isEmpty()
    ) {
      logger.warning("First name is required");
      return false;
    }

    if (
      patient.getLastName() == null || patient.getLastName().trim().isEmpty()
    ) {
      logger.warning("Last name is required");
      return false;
    }

    if (patient.getDateOfBirth() == null) {
      logger.warning("Date of birth is required");
      return false;
    }

    if (patient.getGender() == null || patient.getGender().trim().isEmpty()) {
      logger.warning("Gender is required");
      return false;
    }

    // Validate date of birth is not in future
    if (patient.getDateOfBirth().after(new Date())) {
      logger.warning("Date of birth cannot be in the future");
      return false;
    }

    // Validate email format if provided - basic validation
    if (patient.getEmail() != null && !patient.getEmail().trim().isEmpty()) {
      String email = patient.getEmail().trim();
      if (!email.contains("@") || !email.contains(".")) {
        logger.warning("Invalid email format: " + email);
        return false;
      }
    }

    return true;
  }

  @Override
  public PatientStatistics getPatientStatistics() {
    try {
      PatientStatistics stats = new PatientStatistics();

      // Get basic counts
      stats.setTotalPatients(patientDao.count());
      stats.setActivePatients(patientDao.countActivePatients());
      stats.setInactivePatients(
        stats.getTotalPatients() - stats.getActivePatients()
      );
      stats.setMalePatients(patientDao.countByGender("M"));
      stats.setFemalePatients(patientDao.countByGender("F"));

      // Calculate average age - simplified calculation
      List<Patient> allPatients = patientDao.findAll();
      if (!allPatients.isEmpty()) {
        double totalAge = 0;
        for (Patient patient : allPatients) {
          totalAge += patient.getAge();
        }
        stats.setAverageAge(totalAge / allPatients.size());
      }

      // Get new patients this month and year - simplified calculation
      Calendar cal = Calendar.getInstance();
      cal.set(Calendar.DAY_OF_MONTH, 1);
      cal.set(Calendar.HOUR_OF_DAY, 0);
      cal.set(Calendar.MINUTE, 0);
      cal.set(Calendar.SECOND, 0);
      Date monthStart = cal.getTime();
      Date now = new Date();

      List<Patient> monthlyPatients = patientDao.findByRegistrationDateBetween(
        monthStart,
        now
      );
      stats.setNewPatientsThisMonth(monthlyPatients.size());

      cal.set(Calendar.MONTH, Calendar.JANUARY);
      Date yearStart = cal.getTime();
      List<Patient> yearlyPatients = patientDao.findByRegistrationDateBetween(
        yearStart,
        now
      );
      stats.setNewPatientsThisYear(yearlyPatients.size());

      logger.info("Patient statistics calculated successfully");
      return stats;
    } catch (Exception e) {
      logger.severe("Error calculating patient statistics: " + e.getMessage());
      throw new RuntimeException("Failed to calculate patient statistics", e);
    }
  }

  @Override
  public boolean isNationalIdUnique(String nationalId, Long excludePatientId) {
    if (nationalId == null || nationalId.trim().isEmpty()) {
      return true; // Null/empty national ID is considered unique
    }

    try {
      Patient existingPatient = patientDao.findByNationalId(nationalId.trim());

      if (existingPatient == null) {
        return true; // No patient found with this national ID
      }

      // If excluding a patient ID (for updates), check if it's the same patient
      if (
        excludePatientId != null &&
        existingPatient.getPatientId().equals(excludePatientId)
      ) {
        return true; // Same patient, so national ID is still unique for this patient
      }

      return false; // National ID already exists for a different patient
    } catch (Exception e) {
      logger.severe("Error checking national ID uniqueness: " + e.getMessage());
      throw new RuntimeException("Failed to check national ID uniqueness", e);
    }
  }
}
