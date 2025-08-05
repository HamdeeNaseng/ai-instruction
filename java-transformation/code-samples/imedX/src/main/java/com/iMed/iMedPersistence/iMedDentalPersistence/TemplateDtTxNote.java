package com.iMed.iMedPersistence.iMedDentalPersistence;

import javax.ejb.*;
import java.util.*;

public interface TemplateDtTxNote extends javax.ejb.EJBLocalObject
{
  public String getTemplateDtTxNoteId();
  public void setCode(String code);
  public String getCode();
  public void setDescription(String description);
  public String getDescription();
  public void setEmployeeId(String employeeId);
  public String getEmployeeId();
  public void setBaseDtTxTypeId(String baseDtTxTypeId);
  public String getBaseDtTxTypeId();
}