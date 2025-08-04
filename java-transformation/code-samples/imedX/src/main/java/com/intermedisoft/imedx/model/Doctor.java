package com.intermedisoft.imedx.model;

import java.util.Date;
import java.util.Objects;

/**
 * Doctor Entity - Legacy Java 8 style
 * Represents a doctor in the EHR system
 */
public class Doctor {

  private Long doctorId;
  private String firstName;
  private String lastName;
  private String specialization;
  private String licenseNumber;
  private String email;
  private String phoneNumber;
  private String department;
  private Date hireDate;
  private String qualification;
  private Integer experienceYears;
  private boolean active;
  private String workingHours;
  private Double consultationFee;

  // Default constructor
  public Doctor() {
    this.hireDate = new Date();
    this.active = true;
  }

  // Constructor with essential fields
  public Doctor(
    String firstName,
    String lastName,
    String specialization,
    String licenseNumber
  ) {
    this();
    this.firstName = firstName;
    this.lastName = lastName;
    this.specialization = specialization;
    this.licenseNumber = licenseNumber;
  }

  // Getters and Setters - Legacy Java style
  public Long getDoctorId() {
    return doctorId;
  }

  public void setDoctorId(Long doctorId) {
    this.doctorId = doctorId;
  }

  public String getFirstName() {
    return firstName;
  }

  public void setFirstName(String firstName) {
    this.firstName = firstName;
  }

  public String getLastName() {
    return lastName;
  }

  public void setLastName(String lastName) {
    this.lastName = lastName;
  }

  public String getSpecialization() {
    return specialization;
  }

  public void setSpecialization(String specialization) {
    this.specialization = specialization;
  }

  public String getLicenseNumber() {
    return licenseNumber;
  }

  public void setLicenseNumber(String licenseNumber) {
    this.licenseNumber = licenseNumber;
  }

  public String getEmail() {
    return email;
  }

  public void setEmail(String email) {
    this.email = email;
  }

  public String getPhoneNumber() {
    return phoneNumber;
  }

  public void setPhoneNumber(String phoneNumber) {
    this.phoneNumber = phoneNumber;
  }

  public String getDepartment() {
    return department;
  }

  public void setDepartment(String department) {
    this.department = department;
  }

  public Date getHireDate() {
    return hireDate;
  }

  public void setHireDate(Date hireDate) {
    this.hireDate = hireDate;
  }

  public String getQualification() {
    return qualification;
  }

  public void setQualification(String qualification) {
    this.qualification = qualification;
  }

  public Integer getExperienceYears() {
    return experienceYears;
  }

  public void setExperienceYears(Integer experienceYears) {
    this.experienceYears = experienceYears;
  }

  public boolean isActive() {
    return active;
  }

  public void setActive(boolean active) {
    this.active = active;
  }

  public String getWorkingHours() {
    return workingHours;
  }

  public void setWorkingHours(String workingHours) {
    this.workingHours = workingHours;
  }

  public Double getConsultationFee() {
    return consultationFee;
  }

  public void setConsultationFee(Double consultationFee) {
    this.consultationFee = consultationFee;
  }

  // Business methods
  public String getFullName() {
    return "Dr. " + firstName + " " + lastName;
  }

  public String getDisplayName() {
    return getFullName() + " (" + specialization + ")";
  }

  @Override
  public boolean equals(Object o) {
    if (this == o) return true;
    if (o == null || getClass() != o.getClass()) return false;
    Doctor doctor = (Doctor) o;
    return Objects.equals(doctorId, doctor.doctorId);
  }

  @Override
  public int hashCode() {
    return Objects.hash(doctorId);
  }

  @Override
  public String toString() {
    return (
      "Doctor{" +
      "doctorId=" +
      doctorId +
      ", firstName='" +
      firstName +
      '\'' +
      ", lastName='" +
      lastName +
      '\'' +
      ", specialization='" +
      specialization +
      '\'' +
      ", licenseNumber='" +
      licenseNumber +
      '\'' +
      ", active=" +
      active +
      '}'
    );
  }
}
