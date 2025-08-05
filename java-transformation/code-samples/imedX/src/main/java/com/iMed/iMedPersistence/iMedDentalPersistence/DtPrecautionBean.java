package com.iMed.iMedPersistence.iMedDentalPersistence;

import javax.ejb.*;
import com.iMed.iMedPersistence.iMedDentalDTO.DtPrecautionVO;

abstract public class DtPrecautionBean implements EntityBean
{
  transient EntityContext entityContext;
  public java.lang.String ejbCreate(java.lang.String dtPrecautionId) throws CreateException {
    setDtPrecautionId(dtPrecautionId);
    return null;
  }
  public java.lang.String ejbCreate(DtPrecautionVO dtPrecautionVO) throws CreateException {
    this.setDtPrecautionId(dtPrecautionVO.getObjectID());
    this.setPrecautionText(dtPrecautionVO.getPrecautionText());
    this.setPatientId(dtPrecautionVO.getPatientId());
    this.setIsActive(dtPrecautionVO.getIsActive());
    this.setCreateEid(dtPrecautionVO.getCreateEid());
    this.setCreateDate(dtPrecautionVO.getCreateDate());
    this.setCreateTime(dtPrecautionVO.getCreateTime());
    return null;
  }
  public void ejbPostCreate(java.lang.String dtPrecautionId) throws CreateException {
    /**@todo Complete this method*/
  }
  public void ejbPostCreate(DtPrecautionVO dtPrecautionVO) throws CreateException {
    /**@todo Complete this method*/
  }
  public void ejbRemove() throws RemoveException {
    /**@todo Complete this method*/
  }
  public abstract void setDtPrecautionId(java.lang.String dtPrecautionId);
  public abstract void setPatientId(java.lang.String patientId);
  public abstract void setPrecautionText(java.lang.String precautionText);
  public abstract void setIsActive(java.lang.String isActive);
  public abstract void setCreateEid(java.lang.String createEid);
  public abstract void setCreateDate(java.lang.String createDate);
  public abstract void setCreateTime(java.lang.String createTime);
  public abstract java.lang.String getDtPrecautionId();
  public abstract java.lang.String getPatientId();
  public abstract java.lang.String getPrecautionText();
  public abstract java.lang.String getIsActive();
  public abstract java.lang.String getCreateEid();
  public abstract java.lang.String getCreateDate();
  public abstract java.lang.String getCreateTime();
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