package com.intermedisoft.imedx.service;

import com.intermedisoft.imedx.model.Patient;
import java.util.Date;
import java.util.List;

/**
 * Patient Service Interface - Legacy Java 8 style
 * Defines business logic operations for patient management
 */
public interface PatientService {
  /**
   * Register a new patient
   * @param patient Patient to register
   * @return Registered patient with ID
   * @throws IllegalArgumentException if patient data is invalid
   */
  Patient registerPatient(Patient patient);

  /**
   * Update existing patient information
   * @param patient Patient with updated information
   * @return Updated patient
   * @throws IllegalArgumentException if patient not found or data invalid
   */
  Patient updatePatient(Patient patient);

  /**
   * Find patient by ID
   * @param patientId Patient ID
   * @return Patient or null if not found
   */
  Patient findPatientById(Long patientId);

  /**
   * Find patient by national ID
   * @param nationalId National ID
   * @return Patient or null if not found
   */
  Patient findPatientByNationalId(String nationalId);

  /**
   * Search patients by name (partial match)
   * @param searchTerm Search term for name
   * @return List of matching patients
   */
  List<Patient> searchPatientsByName(String searchTerm);

  /**
   * Get all active patients
   * @return List of active patients
   */
  List<Patient> getAllActivePatients();

  /**
   * Get all patients (active and inactive)
   * @return List of all patients
   */
  List<Patient> getAllPatients();

  /**
   * Deactivate patient (soft delete)
   * @param patientId Patient ID
   * @return true if deactivated successfully
   */
  boolean deactivatePatient(Long patientId);

  /**
   * Reactivate patient
   * @param patientId Patient ID
   * @return true if reactivated successfully
   */
  boolean reactivatePatient(Long patientId);

  /**
   * Get patients by age range
   * @param minAge Minimum age
   * @param maxAge Maximum age
   * @return List of patients in age range
   */
  List<Patient> getPatientsByAgeRange(int minAge, int maxAge);

  /**
   * Get patients by gender
   * @param gender Gender (M/F)
   * @return List of patients with specified gender
   */
  List<Patient> getPatientsByGender(String gender);

  /**
   * Get patients registered within date range
   * @param fromDate Start date
   * @param toDate End date
   * @return List of patients registered in date range
   */
  List<Patient> getPatientsByRegistrationDateRange(Date fromDate, Date toDate);

  /**
   * Validate patient data
   * @param patient Patient to validate
   * @return true if valid, false otherwise
   */
  boolean validatePatientData(Patient patient);

  /**
   * Get patient statistics
   * @return Map of patient statistics
   */
  PatientStatistics getPatientStatistics();

  /**
   * Check if national ID is unique
   * @param nationalId National ID to check
   * @param excludePatientId Patient ID to exclude from check (for updates)
   * @return true if unique, false if already exists
   */
  boolean isNationalIdUnique(String nationalId, Long excludePatientId);
}
