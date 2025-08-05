package com.iMed.iMedPersistence.iMedDentalPersistence;

import javax.ejb.*;
import java.util.*;

public interface DtDiagnosis extends javax.ejb.EJBLocalObject
{
  public String getDtDiagnosisId();
  public void setVisitId(String visitId);
  public String getVisitId();
  public void setPatientId(String patientId);
  public String getPatientId();
  public void setVitalSignExtendId(String vitalSignExtendId);
  public String getVitalSignExtendId();
  public void setDiagnosis(String diagnosis);
  public String getDiagnosis();
  public void setToothNumber(String toothNumber);
  public String getToothNumber();
  public void setToothSurface(String toothSurface);
  public String getToothSurface();
  public void setDxNote(String dxNote);
  public String getDxNote();
  public void setDoctorEid(String doctorEid);
  public String getDoctorEid();
  public void setDiagnosisDate(String diagnosisDate);
  public String getDiagnosisDate();
  public void setDiagnosisTime(String diagnosisTime);
  public String getDiagnosisTime();
  public void setIcd10Code(String icd10Code);
  public String getIcd10Code();
  public void setIcd10Description(String icd10Description);
  public String getIcd10Description();
  public void setToothQuadrant(String toothQuadrant);
  public String getToothQuadrant();
  public void setFixDiagnosisTypeId(String fixDiagnosisTypeId);
  public String getFixDiagnosisTypeId();
}