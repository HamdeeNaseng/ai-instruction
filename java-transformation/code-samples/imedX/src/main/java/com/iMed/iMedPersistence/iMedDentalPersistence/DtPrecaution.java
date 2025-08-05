package com.iMed.iMedPersistence.iMedDentalPersistence;

import javax.ejb.*;
import java.util.*;

public interface DtPrecaution extends javax.ejb.EJBLocalObject
{
  public String getDtPrecautionId();
  public void setPatientId(String patientId);
  public String getPatientId();
  public void setPrecautionText(String precautionText);
  public String getPrecautionText();
  public void setIsActive(String isActive);
  public String getIsActive();
  public void setCreateEid(String createEid);
  public String getCreateEid();
  public void setCreateDate(String createDate);
  public String getCreateDate();
  public void setCreateTime(String createTime);
  public String getCreateTime();
}