package com.iMed.iMedPersistence.iMedDentalPersistence;

import javax.ejb.*;
import java.util.*;
import com.iMed.iMedPersistence.iMedDentalDTO.*;

public interface DtTreatment extends javax.ejb.EJBLocalObject
{
  public String getDtTreatmentId();
  public void setItemId(String itemId);
  public String getItemId();
  public void setOrderItemId(String orderItemId);
  public String getOrderItemId();
  public void setFixItemTypeId(String fixItemTypeId);
  public String getFixItemTypeId();
  public void setToothNumber(String toothNumber);
  public String getToothNumber();
  public void setToothSurface(String toothSurface);
  public String getToothSurface();
  public void setCourseTreatmentId(String courseTreatmentId);
  public String getCourseTreatmentId();
  public void setIsCourseCompleted(String isCourseCompleted);
  public String getIsCourseCompleted();
  public void setCoursePriceEstimate(String coursePriceEstimate);
  public String getCoursePriceEstimate();
  public void setTxNote(String txNote);
  public String getTxNote();
  public void setDoctorEid(String doctorEid);
  public String getDoctorEid();
  public void setTreatmentDate(String treatmentDate);
  public String getTreatmentDate();
  public void setTreatmentTime(String treatmentTime);
  public String getTreatmentTime();
  public void setModifyEid(String modifyEid);
  public String getModifyEid();
  public void setModifyDate(String modifyDate);
  public String getModifyDate();
  public void setModifyTime(String modifyTime);
  public String getModifyTime();
  public void setPatientId(String patientId);
  public String getPatientId();
  public void setVisitId(String visitId);
  public String getVisitId();
  public void setCourseNextTxNote(String courseNextTxNote);
  public String getCourseNextTxNote();
  public void setToothQuadrant(String toothQuadrant);
  public String getToothQuadrant();
  public DtTreatmentVO toDTO();
}