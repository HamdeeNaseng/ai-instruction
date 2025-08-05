package com.iMed.iMedPersistence.iMedDentalPersistence;

import javax.ejb.*;
import java.util.*;
import com.iMed.iMedPersistence.iMedDentalDTO.*;

public interface DtTeethChart extends javax.ejb.EJBLocalObject
{
  public String getDtTeethChartId();
  public void setPatientId(String patientId);
  public String getPatientId();
  public void setToothNumber(String toothNumber);
  public String getToothNumber();
  public void setFixDtToothTypeId(String fixDtToothTypeId);
  public String getFixDtToothTypeId();
  public void setIsMissingTooth(String isMissingTooth);
  public String getIsMissingTooth();
  public void setModifyDate(String modifyDate);
  public String getModifyDate();
  public void setModifyTime(String modifyTime);
  public String getModifyTime();
  public void setModifyEid(String modifyEid);
  public String getModifyEid();
  public void updateDtTeethChart(TeethChartVO teethChartVO);
}