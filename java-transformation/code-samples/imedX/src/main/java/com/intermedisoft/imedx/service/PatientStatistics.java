package com.intermedisoft.imedx.service;

/**
 * Patient Statistics DTO - Legacy Java 8 style
 * Data Transfer Object for patient statistics
 */
public class PatientStatistics {

  private long totalPatients;
  private long activePatients;
  private long inactivePatients;
  private long malePatients;
  private long femalePatients;
  private double averageAge;
  private long newPatientsThisMonth;
  private long newPatientsThisYear;

  // Default constructor
  public PatientStatistics() {}

  // Constructor with all fields
  public PatientStatistics(
    long totalPatients,
    long activePatients,
    long inactivePatients,
    long malePatients,
    long femalePatients,
    double averageAge,
    long newPatientsThisMonth,
    long newPatientsThisYear
  ) {
    this.totalPatients = totalPatients;
    this.activePatients = activePatients;
    this.inactivePatients = inactivePatients;
    this.malePatients = malePatients;
    this.femalePatients = femalePatients;
    this.averageAge = averageAge;
    this.newPatientsThisMonth = newPatientsThisMonth;
    this.newPatientsThisYear = newPatientsThisYear;
  }

  // Getters and Setters - Legacy Java style
  public long getTotalPatients() {
    return totalPatients;
  }

  public void setTotalPatients(long totalPatients) {
    this.totalPatients = totalPatients;
  }

  public long getActivePatients() {
    return activePatients;
  }

  public void setActivePatients(long activePatients) {
    this.activePatients = activePatients;
  }

  public long getInactivePatients() {
    return inactivePatients;
  }

  public void setInactivePatients(long inactivePatients) {
    this.inactivePatients = inactivePatients;
  }

  public long getMalePatients() {
    return malePatients;
  }

  public void setMalePatients(long malePatients) {
    this.malePatients = malePatients;
  }

  public long getFemalePatients() {
    return femalePatients;
  }

  public void setFemalePatients(long femalePatients) {
    this.femalePatients = femalePatients;
  }

  public double getAverageAge() {
    return averageAge;
  }

  public void setAverageAge(double averageAge) {
    this.averageAge = averageAge;
  }

  public long getNewPatientsThisMonth() {
    return newPatientsThisMonth;
  }

  public void setNewPatientsThisMonth(long newPatientsThisMonth) {
    this.newPatientsThisMonth = newPatientsThisMonth;
  }

  public long getNewPatientsThisYear() {
    return newPatientsThisYear;
  }

  public void setNewPatientsThisYear(long newPatientsThisYear) {
    this.newPatientsThisYear = newPatientsThisYear;
  }

  // Business methods
  public double getActivePatientPercentage() {
    if (totalPatients == 0) return 0.0;
    return (double) activePatients / totalPatients * 100.0;
  }

  public double getMalePatientPercentage() {
    if (totalPatients == 0) return 0.0;
    return (double) malePatients / totalPatients * 100.0;
  }

  public double getFemalePatientPercentage() {
    if (totalPatients == 0) return 0.0;
    return (double) femalePatients / totalPatients * 100.0;
  }

  @Override
  public String toString() {
    return (
      "PatientStatistics{" +
      "totalPatients=" +
      totalPatients +
      ", activePatients=" +
      activePatients +
      ", inactivePatients=" +
      inactivePatients +
      ", malePatients=" +
      malePatients +
      ", femalePatients=" +
      femalePatients +
      ", averageAge=" +
      averageAge +
      ", newPatientsThisMonth=" +
      newPatientsThisMonth +
      ", newPatientsThisYear=" +
      newPatientsThisYear +
      '}'
    );
  }
}
