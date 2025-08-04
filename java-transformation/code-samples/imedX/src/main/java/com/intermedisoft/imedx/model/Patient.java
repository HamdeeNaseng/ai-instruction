package com.intermedisoft.imedx.model;

import java.util.Date;
import java.util.Objects;

/**
 * Patient Entity - Legacy Java 8 style
 * Represents a patient in the EHR system
 */
public class Patient {

  private Long patientId;
  private String firstName;
  private String lastName;
  private Date dateOfBirth;
  private String gender;
  private String phoneNumber;
  private String email;
  private String address;
  private String nationalId;
  private Date registrationDate;
  private String emergencyContact;
  private String emergencyContactPhone;
  private String bloodType;
  private String allergies;
  private boolean active;

  // Default constructor
  public Patient() {
    this.registrationDate = new Date();
    this.active = true;
  }

  // Constructor with essential fields
  public Patient(
    String firstName,
    String lastName,
    Date dateOfBirth,
    String gender
  ) {
    this();
    this.firstName = firstName;
    this.lastName = lastName;
    this.dateOfBirth = dateOfBirth;
    this.gender = gender;
  }

  // Getters and Setters - Legacy Java style (verbose)
  public Long getPatientId() {
    return patientId;
  }

  public void setPatientId(Long patientId) {
    this.patientId = patientId;
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

  public Date getDateOfBirth() {
    return dateOfBirth;
  }

  public void setDateOfBirth(Date dateOfBirth) {
    this.dateOfBirth = dateOfBirth;
  }

  public String getGender() {
    return gender;
  }

  public void setGender(String gender) {
    this.gender = gender;
  }

  public String getPhoneNumber() {
    return phoneNumber;
  }

  public void setPhoneNumber(String phoneNumber) {
    this.phoneNumber = phoneNumber;
  }

  public String getEmail() {
    return email;
  }

  public void setEmail(String email) {
    this.email = email;
  }

  public String getAddress() {
    return address;
  }

  public void setAddress(String address) {
    this.address = address;
  }

  public String getNationalId() {
    return nationalId;
  }

  public void setNationalId(String nationalId) {
    this.nationalId = nationalId;
  }

  public Date getRegistrationDate() {
    return registrationDate;
  }

  public void setRegistrationDate(Date registrationDate) {
    this.registrationDate = registrationDate;
  }

  public String getEmergencyContact() {
    return emergencyContact;
  }

  public void setEmergencyContact(String emergencyContact) {
    this.emergencyContact = emergencyContact;
  }

  public String getEmergencyContactPhone() {
    return emergencyContactPhone;
  }

  public void setEmergencyContactPhone(String emergencyContactPhone) {
    this.emergencyContactPhone = emergencyContactPhone;
  }

  public String getBloodType() {
    return bloodType;
  }

  public void setBloodType(String bloodType) {
    this.bloodType = bloodType;
  }

  public String getAllergies() {
    return allergies;
  }

  public void setAllergies(String allergies) {
    this.allergies = allergies;
  }

  public boolean isActive() {
    return active;
  }

  public void setActive(boolean active) {
    this.active = active;
  }

  // Business methods
  public String getFullName() {
    return firstName + " " + lastName;
  }

  public int getAge() {
    if (dateOfBirth == null) {
      return 0;
    }
    Date now = new Date();
    long diff = now.getTime() - dateOfBirth.getTime();
    return (int) (diff / (365.25 * 24 * 60 * 60 * 1000));
  }

  // equals and hashCode - Legacy Java style
  @Override
  public boolean equals(Object o) {
    if (this == o) return true;
    if (o == null || getClass() != o.getClass()) return false;
    Patient patient = (Patient) o;
    return Objects.equals(patientId, patient.patientId);
  }

  @Override
  public int hashCode() {
    return Objects.hash(patientId);
  }

  @Override
  public String toString() {
    return (
      "Patient{" +
      "patientId=" +
      patientId +
      ", firstName='" +
      firstName +
      '\'' +
      ", lastName='" +
      lastName +
      '\'' +
      ", dateOfBirth=" +
      dateOfBirth +
      ", gender='" +
      gender +
      '\'' +
      ", active=" +
      active +
      '}'
    );
  }
}
