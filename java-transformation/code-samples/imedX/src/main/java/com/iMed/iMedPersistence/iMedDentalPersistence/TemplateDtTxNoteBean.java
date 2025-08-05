package com.iMed.iMedPersistence.iMedDentalPersistence;

import javax.ejb.*;
import com.iMed.iMedPersistence.iMedDentalDTO.TemplateDtTxNoteVO;

abstract public class TemplateDtTxNoteBean implements EntityBean
{
  transient EntityContext entityContext;
  public java.lang.String ejbCreate(java.lang.String templateDtTxNoteId) throws CreateException {
    setTemplateDtTxNoteId(templateDtTxNoteId);
    return null;
  }
  public java.lang.String ejbCreate(TemplateDtTxNoteVO templateDtTxNoteVO) throws CreateException {
    this.setTemplateDtTxNoteId(templateDtTxNoteVO.getObjectID());
    this.setCode(templateDtTxNoteVO.getCode());
    this.setDescription(templateDtTxNoteVO.getDescription());
    this.setEmployeeId(templateDtTxNoteVO.getEmployeeId());
    this.setBaseDtTxTypeId(templateDtTxNoteVO.getBaseDtTxTypeId());
    return null;
  }
  public void ejbPostCreate(java.lang.String templateDtTxNoteId) throws CreateException {
    /**@todo Complete this method*/
  }
  public void ejbPostCreate(TemplateDtTxNoteVO templateDtTxNoteVO) throws CreateException {
    /**@todo Complete this method*/
  }
  public void ejbRemove() throws RemoveException {
    /**@todo Complete this method*/
  }
  public abstract void setTemplateDtTxNoteId(java.lang.String templateDtTxNoteId);
  public abstract void setCode(java.lang.String code);
  public abstract void setDescription(java.lang.String description);
  public abstract void setEmployeeId(java.lang.String employeeId);
  public abstract void setBaseDtTxTypeId(java.lang.String baseDtTxTypeId);
  public abstract java.lang.String getTemplateDtTxNoteId();
  public abstract java.lang.String getCode();
  public abstract java.lang.String getDescription();
  public abstract java.lang.String getEmployeeId();
  public abstract java.lang.String getBaseDtTxTypeId();
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