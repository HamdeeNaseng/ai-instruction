package com.iMed.iMedPersistence.iMedDentalPersistence;

import com.iMed.iMedPersistence.iMedDentalDTO.DtTreatmentVO;
import javax.ejb.*;

abstract public class DtTreatmentBean implements EntityBean
{
  transient EntityContext entityContext;
  public java.lang.String ejbCreate(java.lang.String dtTreatmentId) throws CreateException {
    setDtTreatmentId(dtTreatmentId);
    return null;
  }
  public java.lang.String ejbCreate(DtTreatmentVO dtTreatmentVO) throws CreateException {
    this.setDtTreatmentId(dtTreatmentVO.getObjectID());
    this.setItemId(dtTreatmentVO.getItemId());
    this.setOrderItemId(dtTreatmentVO.getOrderItemId());
    this.setPatientId(dtTreatmentVO.getPatientId());
    this.setVisitId(dtTreatmentVO.getVisitId());
    this.setFixItemTypeId(dtTreatmentVO.getFixItemTypeId());
    this.setToothNumber(dtTreatmentVO.getToothNumber());
    this.setToothSurface(dtTreatmentVO.getToothSurface());
    this.setToothQuadrant(dtTreatmentVO.getToothQuadrant());
    this.setCourseTreatmentId(dtTreatmentVO.getCourseTreatmentId());
    this.setCoursePriceEstimate(dtTreatmentVO.getCoursePriceEstimate());
    this.setCourseNextTxNote(dtTreatmentVO.getCourseNextTxNote());
    this.setIsCourseCompleted(dtTreatmentVO.getIsCourseCompleted());
    this.setTxNote(dtTreatmentVO.getTxNote());
    this.setDoctorEid(dtTreatmentVO.getDoctorEid());
    this.setTreatmentDate(dtTreatmentVO.getTreatmentDate());
    this.setTreatmentTime(dtTreatmentVO.getTreatmentTime());
    this.setModifyEid(dtTreatmentVO.getModifyEid());
    this.setModifyDate(dtTreatmentVO.getModifyDate());
    this.setModifyTime(dtTreatmentVO.getModifyTime());

    return null;
  }
  public void ejbPostCreate(java.lang.String dtTreatmentId) throws CreateException {
    /**@todo Complete this method*/
  }
  public void ejbPostCreate(DtTreatmentVO dtTreatmentVO) throws CreateException {
    /**@todo Complete this method*/
  }
  public void ejbRemove() throws RemoveException {
    /**@todo Complete this method*/
  }
  public abstract void setDtTreatmentId(java.lang.String dtTreatmentId);
  public abstract void setItemId(java.lang.String itemId);
  public abstract void setOrderItemId(java.lang.String orderItemId);
  public abstract void setFixItemTypeId(java.lang.String fixItemTypeId);
  public abstract void setToothNumber(java.lang.String toothNumber);
  public abstract void setToothSurface(java.lang.String toothSurface);
  public abstract void setCourseTreatmentId(java.lang.String courseTreatmentId);
  public abstract void setIsCourseCompleted(java.lang.String isCourseCompleted);
  public abstract void setCoursePriceEstimate(java.lang.String coursePriceEstimate);
  public abstract void setTxNote(java.lang.String txNote);
  public abstract void setDoctorEid(java.lang.String doctorEid);
  public abstract void setTreatmentDate(java.lang.String treatmentDate);
  public abstract void setTreatmentTime(java.lang.String treatmentTime);
  public abstract void setModifyEid(java.lang.String modifyEid);
  public abstract void setModifyDate(java.lang.String modifyDate);
  public abstract void setModifyTime(java.lang.String modifyTime);
  public abstract void setPatientId(java.lang.String patientId);
  public abstract void setVisitId(java.lang.String visitId);
  public abstract void setCourseNextTxNote(java.lang.String courseNextTxNote);
  public abstract void setToothQuadrant(java.lang.String toothQuadrant);
  public abstract java.lang.String getDtTreatmentId();
  public abstract java.lang.String getItemId();
  public abstract java.lang.String getOrderItemId();
  public abstract java.lang.String getFixItemTypeId();
  public abstract java.lang.String getToothNumber();
  public abstract java.lang.String getToothSurface();
  public abstract java.lang.String getCourseTreatmentId();
  public abstract java.lang.String getIsCourseCompleted();
  public abstract java.lang.String getCoursePriceEstimate();
  public abstract java.lang.String getTxNote();
  public abstract java.lang.String getDoctorEid();
  public abstract java.lang.String getTreatmentDate();
  public abstract java.lang.String getTreatmentTime();
  public abstract java.lang.String getModifyEid();
  public abstract java.lang.String getModifyDate();
  public abstract java.lang.String getModifyTime();
  public abstract java.lang.String getPatientId();
  public abstract java.lang.String getVisitId();
  public abstract java.lang.String getCourseNextTxNote();
  public abstract java.lang.String getToothQuadrant();
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
  public DtTreatmentVO toDTO()
  {
    DtTreatmentVO dtTreatmentVO = new DtTreatmentVO();
    dtTreatmentVO.setObjectID(this.getDtTreatmentId());
    dtTreatmentVO.setItemId(this.getItemId());
    dtTreatmentVO.setOrderItemId(this.getOrderItemId());
    dtTreatmentVO.setPatientId(this.getPatientId());
    dtTreatmentVO.setVisitId(this.getVisitId());
    dtTreatmentVO.setFixItemTypeId(this.getFixItemTypeId());
    dtTreatmentVO.setToothNumber(this.getToothNumber());
    dtTreatmentVO.setToothSurface(this.getToothSurface());
    dtTreatmentVO.setToothQuadrant(this.getToothQuadrant());
    dtTreatmentVO.setCourseTreatmentId(this.getCourseTreatmentId());
    dtTreatmentVO.setCoursePriceEstimate(this.getCoursePriceEstimate());
    dtTreatmentVO.setCourseNextTxNote(this.getCourseNextTxNote());
    dtTreatmentVO.setIsCourseCompleted(this.getIsCourseCompleted());
    dtTreatmentVO.setTxNote(this.getTxNote());
    dtTreatmentVO.setDoctorEid(this.getDoctorEid());
    dtTreatmentVO.setTreatmentDate(this.getTreatmentDate());
    dtTreatmentVO.setTreatmentTime(this.getTreatmentTime());
    dtTreatmentVO.setModifyEid(this.getModifyEid());
    dtTreatmentVO.setModifyDate(this.getModifyDate());
    dtTreatmentVO.setModifyTime(this.getModifyTime());
    return dtTreatmentVO;
  }
}