package com.iMed.iMedPersistence.iMedDentalPersistence;

import javax.ejb.*;
import java.util.*;

public interface DtTreatmentPlan extends javax.ejb.EJBLocalObject
{
  public String getDtTreatmentPlanId();
  public void setItemId(String itemId);
  public String getItemId();
  public void setPatientId(String patientId);
  public String getPatientId();
  public void setVisitId(String visitId);
  public String getVisitId();
  public void setPlanNo(String planNo);
  public String getPlanNo();
  public void setToothNumber(String toothNumber);
  public String getToothNumber();
  public void setToothSurface(String toothSurface);
  public String getToothSurface();
  public void setTxNote(String txNote);
  public String getTxNote();
  public void setDoctorEid(String doctorEid);
  public String getDoctorEid();
  public void setModifyEid(String modifyEid);
  public String getModifyEid();
  public void setModifyDate(String modifyDate);
  public String getModifyDate();
  public void setModifyTime(String modifyTime);
  public String getModifyTime();
  public void setIsArchive(String isArchive);
  public String getIsArchive();
  public void setArchiveDoctorEid(String archiveDoctorEid);
  public String getArchiveDoctorEid();
  public void setArchiveDate(String archiveDate);
  public String getArchiveDate();
  public void setArchiveTime(String archiveTime);
  public String getArchiveTime();
  public void setIsApplied(String isApplied);
  public String getIsApplied();
  public void setToothQuadrant(String toothQuadrant);
  public String getToothQuadrant();
}