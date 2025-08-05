package com.iMed.iMedPersistence.iMedDentalPersistence;

import javax.ejb.*;
import com.iMed.iMedPersistence.iMedDentalDTO.BaseDtItemVO;

abstract public class BaseDtItemBean implements EntityBean {
  transient EntityContext entityContext;
  public java.lang.String ejbCreate(java.lang.String baseDtItemId, java.lang.String baseDtSymbolId, java.lang.String fixDtActionTypeId, java.lang.String isTreatment, java.lang.String itemId) throws CreateException {
    setBaseDtItemId(baseDtItemId);
    setBaseDtSymbolId(baseDtSymbolId);
    setFixDtActionTypeId(fixDtActionTypeId);
    setIsTreatment(isTreatment);
    setItemId(itemId);
    return null;
  }
  public java.lang.String ejbCreate(BaseDtItemVO baseDtItemVO) throws CreateException {
    System.out.println("objectId : " + baseDtItemVO.getObjectID());
    this.setBaseDtItemId(baseDtItemVO.getObjectID());
    this.setItemId(baseDtItemVO.getItemId());
    this.setBaseDtSymbolId(baseDtItemVO.getBaseDtSymbolId());
    this.setFixDtActionTypeId(baseDtItemVO.getFixDtActionTypeId());
    this.setIsTreatment(baseDtItemVO.getIsTreatment());
    return null;
  }
  public void ejbPostCreate(java.lang.String baseDtItemId, java.lang.String baseDtSymbolId, java.lang.String fixDtActionTypeId, java.lang.String isTreatment, java.lang.String itemId) throws CreateException {
    /**@todo Complete this method*/
  }
  public void ejbPostCreate(BaseDtItemVO baseDtItemVO) throws CreateException {
    /**@todo Complete this method*/
  }
  public void ejbRemove() throws RemoveException {
    /**@todo Complete this method*/
  }
  public abstract void setBaseDtItemId(java.lang.String baseDtItemId);
  public abstract void setBaseDtSymbolId(java.lang.String baseDtSymbolId);
  public abstract void setFixDtActionTypeId(java.lang.String fixDtActionTypeId);
  public abstract void setIsTreatment(java.lang.String isTreatment);
  public abstract void setItemId(java.lang.String itemId);
  public abstract java.lang.String getBaseDtItemId();
  public abstract java.lang.String getBaseDtSymbolId();
  public abstract java.lang.String getFixDtActionTypeId();
  public abstract java.lang.String getIsTreatment();
  public abstract java.lang.String getItemId();
  public void ejbLoad() {
    /**@todo Complete this method*/
  }
  public void ejbStore() {
    /**@todo Complete this method*/
  }
  public void ejbActivate() {
    /**@todo Complete this method*/
  }
  public void ejbPassivate() {
    /**@todo Complete this method*/
  }
  public void unsetEntityContext() {
    this.entityContext = null;
  }
  public void setEntityContext(EntityContext entityContext)
  {
    this.entityContext = entityContext;
  }
}