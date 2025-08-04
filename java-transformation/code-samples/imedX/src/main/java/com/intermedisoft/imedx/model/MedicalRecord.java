package com.intermedisoft.imedx.model;

import java.util.Date;
import java.util.Objects;

/**
 * Medical Record Entity - Legacy Java 8 style
 * Represents a medical record/visit in the EHR system
 */
public class MedicalRecord {

  private Long recordId;
  private Long patientId;
  private Long doctorId;
  private Date visitDate;
  private String chiefComplaint;
  private String presentIllness;
  private String physicalExamination;
  private String diagnosis;
  private String treatment;
  private String medications;
  private String notes;
  private String recordType; // CONSULTATION, EMERGENCY, FOLLOW_UP, etc.
  private Double temperature;
  private Integer bloodPressureSystolic;
  private Integer bloodPressureDiastolic;
  private Integer heartRate;
  private Double weight;
  private Double height;
  private Date createdDate;
  private Date updatedDate;
  private String status; // DRAFT, COMPLETED, REVIEWED, ARCHIVED

  // Default constructor
  public MedicalRecord() {
    this.visitDate = new Date();
    this.createdDate = new Date();
    this.status = "DRAFT";
  }

  // Constructor with essential fields
  public MedicalRecord(Long patientId, Long doctorId, String chiefComplaint) {
    this();
    this.patientId = patientId;
    this.doctorId = doctorId;
    this.chiefComplaint = chiefComplaint;
  }

  // Getters and Setters - Legacy Java style
  public Long getRecordId() {
    return recordId;
  }

  public void setRecordId(Long recordId) {
    this.recordId = recordId;
  }

  public Long getPatientId() {
    return patientId;
  }

  public void setPatientId(Long patientId) {
    this.patientId = patientId;
  }

  public Long getDoctorId() {
    return doctorId;
  }

  public void setDoctorId(Long doctorId) {
    this.doctorId = doctorId;
  }

  public Date getVisitDate() {
    return visitDate;
  }

  public void setVisitDate(Date visitDate) {
    this.visitDate = visitDate;
  }

  public String getChiefComplaint() {
    return chiefComplaint;
  }

  public void setChiefComplaint(String chiefComplaint) {
    this.chiefComplaint = chiefComplaint;
  }

  public String getPresentIllness() {
    return presentIllness;
  }

  public void setPresentIllness(String presentIllness) {
    this.presentIllness = presentIllness;
  }

  public String getPhysicalExamination() {
    return physicalExamination;
  }

  public void setPhysicalExamination(String physicalExamination) {
    this.physicalExamination = physicalExamination;
  }

  public String getDiagnosis() {
    return diagnosis;
  }

  public void setDiagnosis(String diagnosis) {
    this.diagnosis = diagnosis;
  }

  public String getTreatment() {
    return treatment;
  }

  public void setTreatment(String treatment) {
    this.treatment = treatment;
  }

  public String getMedications() {
    return medications;
  }

  public void setMedications(String medications) {
    this.medications = medications;
  }

  public String getNotes() {
    return notes;
  }

  public void setNotes(String notes) {
    this.notes = notes;
  }

  public String getRecordType() {
    return recordType;
  }

  public void setRecordType(String recordType) {
    this.recordType = recordType;
  }

  public Double getTemperature() {
    return temperature;
  }

  public void setTemperature(Double temperature) {
    this.temperature = temperature;
  }

  public Integer getBloodPressureSystolic() {
    return bloodPressureSystolic;
  }

  public void setBloodPressureSystolic(Integer bloodPressureSystolic) {
    this.bloodPressureSystolic = bloodPressureSystolic;
  }

  public Integer getBloodPressureDiastolic() {
    return bloodPressureDiastolic;
  }

  public void setBloodPressureDiastolic(Integer bloodPressureDiastolic) {
    this.bloodPressureDiastolic = bloodPressureDiastolic;
  }

  public Integer getHeartRate() {
    return heartRate;
  }

  public void setHeartRate(Integer heartRate) {
    this.heartRate = heartRate;
  }

  public Double getWeight() {
    return weight;
  }

  public void setWeight(Double weight) {
    this.weight = weight;
  }

  public Double getHeight() {
    return height;
  }

  public void setHeight(Double height) {
    this.height = height;
  }

  public Date getCreatedDate() {
    return createdDate;
  }

  public void setCreatedDate(Date createdDate) {
    this.createdDate = createdDate;
  }

  public Date getUpdatedDate() {
    return updatedDate;
  }

  public void setUpdatedDate(Date updatedDate) {
    this.updatedDate = updatedDate;
  }

  public String getStatus() {
    return status;
  }

  public void setStatus(String status) {
    this.status = status;
  }

  // Business methods
  public String getBloodPressure() {
    if (bloodPressureSystolic != null && bloodPressureDiastolic != null) {
      return bloodPressureSystolic + "/" + bloodPressureDiastolic;
    }
    return null;
  }

  public Double getBMI() {
    if (weight != null && height != null && height > 0) {
      double heightInMeters = height / 100; // Convert cm to meters
      return weight / (heightInMeters * heightInMeters);
    }
    return null;
  }

  public boolean isVitalSignsComplete() {
    return (
      temperature != null &&
      bloodPressureSystolic != null &&
      bloodPressureDiastolic != null &&
      heartRate != null
    );
  }

  @Override
  public boolean equals(Object o) {
    if (this == o) return true;
    if (o == null || getClass() != o.getClass()) return false;
    MedicalRecord that = (MedicalRecord) o;
    return Objects.equals(recordId, that.recordId);
  }

  @Override
  public int hashCode() {
    return Objects.hash(recordId);
  }

  @Override
  public String toString() {
    return (
      "MedicalRecord{" +
      "recordId=" +
      recordId +
      ", patientId=" +
      patientId +
      ", doctorId=" +
      doctorId +
      ", visitDate=" +
      visitDate +
      ", chiefComplaint='" +
      chiefComplaint +
      '\'' +
      ", status='" +
      status +
      '\'' +
      '}'
    );
  }
}
