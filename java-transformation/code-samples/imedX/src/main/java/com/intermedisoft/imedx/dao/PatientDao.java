package com.intermedisoft.imedx.dao;

import com.intermedisoft.imedx.model.Patient;
import java.util.Date;
import java.util.List;

/**
 * Patient DAO interface - Legacy Java 8 style
 * Extends GenericDao with Patient-specific methods
 */
public interface PatientDao extends GenericDao<Patient, Long> {
  /**
   * Find patients by first name and last name
   * @param firstName First name
   * @param lastName Last name
   * @return List of matching patients
   */
  List<Patient> findByName(String firstName, String lastName);

  /**
   * Find patient by national ID
   * @param nationalId National ID
   * @return Patient or null if not found
   */
  Patient findByNationalId(String nationalId);

  /**
   * Find patients by date of birth range
   * @param fromDate Start date
   * @param toDate End date
   * @return List of patients in date range
   */
  List<Patient> findByDateOfBirthBetween(Date fromDate, Date toDate);

  /**
   * Find patients by gender
   * @param gender Gender (M/F)
   * @return List of patients with specified gender
   */
  List<Patient> findByGender(String gender);

  /**
   * Find active patients
   * @param active Active status
   * @return List of active/inactive patients
   */
  List<Patient> findByActiveStatus(boolean active);

  /**
   * Search patients by partial name match
   * @param searchTerm Search term for name matching
   * @return List of matching patients
   */
  List<Patient> searchByName(String searchTerm);

  /**
   * Find patients registered within date range
   * @param fromDate Start date
   * @param toDate End date
   * @return List of patients registered in date range
   */
  List<Patient> findByRegistrationDateBetween(Date fromDate, Date toDate);

  /**
   * Find patients by blood type
   * @param bloodType Blood type (A+, B+, O-, etc.)
   * @return List of patients with specified blood type
   */
  List<Patient> findByBloodType(String bloodType);

  /**
   * Count patients by gender
   * @param gender Gender
   * @return Count of patients
   */
  long countByGender(String gender);

  /**
   * Count active patients
   * @return Count of active patients
   */
  long countActivePatients();
}
