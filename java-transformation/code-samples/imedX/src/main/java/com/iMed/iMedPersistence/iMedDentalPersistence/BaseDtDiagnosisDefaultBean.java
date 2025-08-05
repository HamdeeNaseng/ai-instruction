package com.iMed.iMedPersistence.iMedDentalPersistence;

import javax.ejb.*;
import com.iMed.iMedPersistence.iMedDentalDTO.BaseDtDiagnosisDefaultVO;

abstract public class BaseDtDiagnosisDefaultBean implements EntityBean
{
  transient EntityContext entityContext;
  public java.lang.String ejbCreate(java.lang.String baseDtDiagnosisDefaultId) throws CreateException {
    setBaseDtDiagnosisDefaultId(baseDtDiagnosisDefaultId);
    return null;
  }
  public java.lang.String ejbCreate(BaseDtDiagnosisDefaultVO baseDtDiagnosisDefaultVO) throws CreateException {
    this.setBaseDtDiagnosisDefaultId(baseDtDiagnosisDefaultVO.getObjectID());
    this.setBaseDtDiagnosisId(baseDtDiagnosisDefaultVO.getBaseDtDiagnosisId());
    this.setEmployeeId(baseDtDiagnosisDefaultVO.getEmployeeId());
    return null;
  }
  public void ejbPostCreate(java.lang.String baseDtDiagnosisDefaultId) throws CreateException {
    /**@todo Complete this method*/
  }
  public void ejbPostCreate(BaseDtDiagnosisDefaultVO baseDtDiagnosisDefaultVO) throws CreateException {
    /**@todo Complete this method*/
  }
  public void ejbRemove() throws RemoveException {
    /**@todo Complete this method*/
  }
  public abstract void setBaseDtDiagnosisDefaultId(java.lang.String baseDtDiagnosisDefaultId);
  public abstract void setBaseDtDiagnosisId(java.lang.String baseDtDiagnosisId);
  public abstract void setEmployeeId(java.lang.String employeeId);
  public abstract java.lang.String getBaseDtDiagnosisDefaultId();
  public abstract java.lang.String getBaseDtDiagnosisId();
  public abstract java.lang.String getEmployeeId();
  public void ejbLoad()
  {
    /**@todo Complete this method*/
  }
  public void ejbStore()
  {
    /**@todo Complete this method*/
  }
  public void ejbActivate()
  {
    /**@todo Complete this method*/
  }
  public void ejbPassivate()
  {
    /**@todo Complete this method*/
  }
  public void unsetEntityContext()
  {
    this.entityContext = null;
  }
  public void setEntityContext(EntityContext entityContext)
  {
    this.entityContext = entityContext;
  }
}