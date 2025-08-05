package com.iMed.iMedPersistence.iMedDentalPersistence;

import com.iMed.iMedPersistence.iMedDentalDTO.DtTreatmentPlanVO;
import javax.ejb.*;

abstract public class DtTreatmentPlanBean implements EntityBean
{
  transient EntityContext entityContext;
  public java.lang.String ejbCreate(java.lang.String dtTreatmentPlanId) throws CreateException {
    setDtTreatmentPlanId(dtTreatmentPlanId);
    return null;
  }
  public java.lang.String ejbCreate(DtTreatmentPlanVO dtTxPlanVO) throws CreateException {
    this.setDtTreatmentPlanId(dtTxPlanVO.getObjectID());
    this.setItemId(dtTxPlanVO.getItemId());
    this.setPatientId(dtTxPlanVO.getPatientId());
    this.setVisitId(dtTxPlanVO.getVisitId());
    this.setPlanNo(dtTxPlanVO.getPlanNo());
    this.setToothNumber(dtTxPlanVO.getToothNumber());
    this.setToothSurface(dtTxPlanVO.getToothSurface());
    this.setTxNote(dtTxPlanVO.getTxNote());
    this.setDoctorEid(dtTxPlanVO.getDoctorEid());
    this.setModifyEid(dtTxPlanVO.getModifyEid());
    this.setModifyDate(dtTxPlanVO.getModifyDate());
    this.setModifyTime(dtTxPlanVO.getModifyTime());
    this.setIsArchive(dtTxPlanVO.getIsArchive());
    this.setArchiveDoctorEid(dtTxPlanVO.getArchiveDoctorEid());
    this.setArchiveDate(dtTxPlanVO.getArchiveDate());
    this.setArchiveTime(dtTxPlanVO.getArchiveTime());
    this.setIsApplied(dtTxPlanVO.getIsApplied());
    this.setToothQuadrant(dtTxPlanVO.getToothQuadrant());
    return null;
  }
  public void ejbPostCreate(java.lang.String dtTreatmentPlanId) throws CreateException {
    /**@todo Complete this method*/
  }
  public void ejbPostCreate(DtTreatmentPlanVO dtTxPlanVO) throws CreateException {
    /**@todo Complete this method*/
  }
  public void ejbRemove() throws RemoveException {
    /**@todo Complete this method*/
  }
  public abstract void setDtTreatmentPlanId(java.lang.String dtTreatmentPlanId);
  public abstract void setItemId(java.lang.String itemId);
  public abstract void setPatientId(java.lang.String patientId);
  public abstract void setVisitId(java.lang.String visitId);
  public abstract void setPlanNo(java.lang.String planNo);
  public abstract void setToothNumber(java.lang.String toothNumber);
  public abstract void setToothSurface(java.lang.String toothSurface);
  public abstract void setTxNote(java.lang.String txNote);
  public abstract void setDoctorEid(java.lang.String doctorEid);
  public abstract void setModifyEid(java.lang.String modifyEid);
  public abstract void setModifyDate(java.lang.String modifyDate);
  public abstract void setModifyTime(java.lang.String modifyTime);
  public abstract void setIsArchive(java.lang.String isArchive);
  public abstract void setArchiveDoctorEid(java.lang.String archiveDoctorEid);
  public abstract void setArchiveDate(java.lang.String archiveDate);
  public abstract void setArchiveTime(java.lang.String archiveTime);
  public abstract void setIsApplied(java.lang.String isApplied);
  public abstract void setToothQuadrant(java.lang.String toothQuadrant);
  public abstract java.lang.String getDtTreatmentPlanId();
  public abstract java.lang.String getItemId();
  public abstract java.lang.String getPatientId();
  public abstract java.lang.String getVisitId();
  public abstract java.lang.String getPlanNo();
  public abstract java.lang.String getToothNumber();
  public abstract java.lang.String getToothSurface();
  public abstract java.lang.String getTxNote();
  public abstract java.lang.String getDoctorEid();
  public abstract java.lang.String getModifyEid();
  public abstract java.lang.String getModifyDate();
  public abstract java.lang.String getModifyTime();
  public abstract java.lang.String getIsArchive();
  public abstract java.lang.String getArchiveDoctorEid();
  public abstract java.lang.String getArchiveDate();
  public abstract java.lang.String getArchiveTime();
  public abstract java.lang.String getIsApplied();
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
}