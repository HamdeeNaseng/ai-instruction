package com.iMed.iMedPersistence.iMedDentalPersistence;

import javax.ejb.*;
import com.iMed.iMedPersistence.iMedDentalDTO.TeethChartVO;

abstract public class DtTeethChartBean implements EntityBean
{
  transient EntityContext entityContext;
  public java.lang.String ejbCreate(java.lang.String dtTeethChartId) throws CreateException {
    setDtTeethChartId(dtTeethChartId);
    return null;
  }
  public java.lang.String ejbCreate(TeethChartVO teethChartVO) throws CreateException {
    setDtTeethChartId(teethChartVO.getObjectID());
    setPatientId(teethChartVO.getPatientId());
    setToothNumber(teethChartVO.getToothNumber());
    setFixDtToothTypeId(teethChartVO.getFixDtToothTypeId());
    setIsMissingTooth(teethChartVO.getIsMissingTooth());
    setModifyDate(teethChartVO.getModifyDate());
    setModifyTime(teethChartVO.getModifyTime());
    setModifyEid(teethChartVO.getModifyEid());
    return null;
  }
  public void ejbPostCreate(java.lang.String dtTeethChartId) throws CreateException {
    /**@todo Complete this method*/
  }
  public void ejbPostCreate(TeethChartVO teethChartVO) throws CreateException {
    /**@todo Complete this method*/
  }
  public void ejbRemove() throws RemoveException {
    /**@todo Complete this method*/
  }
  public abstract void setDtTeethChartId(java.lang.String dtTeethChartId);
  public abstract void setPatientId(java.lang.String patientId);
  public abstract void setToothNumber(java.lang.String toothNumber);
  public abstract void setFixDtToothTypeId(java.lang.String fixDtToothTypeId);
  public abstract void setIsMissingTooth(java.lang.String isMissingTooth);
  public abstract void setModifyDate(java.lang.String modifyDate);
  public abstract void setModifyTime(java.lang.String modifyTime);
  public abstract void setModifyEid(java.lang.String modifyEid);
  public abstract java.lang.String getDtTeethChartId();
  public abstract java.lang.String getPatientId();
  public abstract java.lang.String getToothNumber();
  public abstract java.lang.String getFixDtToothTypeId();
  public abstract java.lang.String getIsMissingTooth();
  public abstract java.lang.String getModifyDate();
  public abstract java.lang.String getModifyTime();
  public abstract java.lang.String getModifyEid();
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
  public void updateDtTeethChart(TeethChartVO teethChartVO)
  {
    setPatientId(teethChartVO.getPatientId());
    setToothNumber(teethChartVO.getToothNumber());
    setFixDtToothTypeId(teethChartVO.getFixDtToothTypeId());
    setIsMissingTooth(teethChartVO.getIsMissingTooth());
    setModifyDate(teethChartVO.getModifyDate());
    setModifyTime(teethChartVO.getModifyTime());
    setModifyEid(teethChartVO.getModifyEid());
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