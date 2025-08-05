package com.iMed.iMedPersistence.iMedDentalPersistence;

import javax.ejb.*;
import java.util.*;

public interface BaseDtItem extends javax.ejb.EJBLocalObject {
  public String getBaseDtItemId();
  public void setBaseDtSymbolId(String baseDtSymbolId);
  public String getBaseDtSymbolId();
  public void setFixDtActionTypeId(String fixDtActionTypeId);
  public String getFixDtActionTypeId();
  public void setIsTreatment(String isTreatment);
  public String getIsTreatment();
  public void setItemId(String itemId);
  public String getItemId();
}