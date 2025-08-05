package com.iMed.iMedPersistence.iMedDentalPersistence;

import com.iMed.iMedPersistence.iMedDentalDTO.*;
import javax.ejb.*;

abstract public class DtDiagnosisBean implements EntityBean
{
  transient EntityContext entityContext;
  public java.lang.String ejbCreate(java.lang.String dtDiagnosisId) throws CreateException {
    setDtDiagnosisId(dtDiagnosisId);
    return null;
  }
  public java.lang.String ejbCreate(DtDiagnosisVO dtDiagnosisVO) throws CreateException {
    this.setDtDiagnosisId(dtDiagnosisVO.getObjectID());
    this.setVisitId(dtDiagnosisVO.getVisitId());
    this.setPatientId(dtDiagnosisVO.getPatientId());
    this.setVitalSignExtendId(dtDiagnosisVO.getVitalSignExtendId());
    this.setDiagnosis(dtDiagnosisVO.getDiagnosis());
    this.setToothNumber(dtDiagnosisVO.getToothNumber());
    this.setToothSurface(dtDiagnosisVO.getToothSurface());
    this.setToothQuadrant(dtDiagnosisVO.getToothQuadrant());
    this.setDxNote(dtDiagnosisVO.getDxNote());
    this.setDoctorEid(dtDiagnosisVO.getDoctorEid());
    this.setDiagnosisDate(dtDiagnosisVO.getDiagnosisDate());
    this.setDiagnosisTime(dtDiagnosisVO.getDiagnosisTime());
    this.setIcd10Code(dtDiagnosisVO.getIcd10Code());
    this.setIcd10Description(dtDiagnosisVO.getIcd10Description());
    this.setFixDiagnosisTypeId(dtDiagnosisVO.getFixDiagnosisTypeId());
    return null;
  }
  public void ejbPostCreate(java.lang.String dtDiagnosisId) throws CreateException {
    /**@todo Complete this method*/
  }
  public void ejbPostCreate(DtDiagnosisVO dtDiagnosisVO) throws CreateException {
    /**@todo Complete this method*/
  }
  public void ejbRemove() throws RemoveException {
    /**@todo Complete this method*/
  }
  public abstract void setDtDiagnosisId(java.lang.String dtDiagnosisId);
  public abstract void setVisitId(java.lang.String visitId);
  public abstract void setPatientId(java.lang.String patientId);
  public abstract void setVitalSignExtendId(java.lang.String vitalSignExtendId);
  public abstract void setDiagnosis(java.lang.String diagnosis);
  public abstract void setToothNumber(java.lang.String toothNumber);
  public abstract void setToothSurface(java.lang.String toothSurface);
  public abstract void setDxNote(java.lang.String dxNote);
  public abstract void setDoctorEid(java.lang.String doctorEid);
  public abstract void setDiagnosisDate(java.lang.String diagnosisDate);
  public abstract void setDiagnosisTime(java.lang.String diagnosisTime);
  public abstract void setIcd10Code(java.lang.String icd10Code);
  public abstract void setIcd10Description(java.lang.String icd10Description);
  public abstract void setToothQuadrant(java.lang.String toothQuadrant);
  public abstract void setFixDiagnosisTypeId(java.lang.String fixDiagnosisTypeId);
  public abstract java.lang.String getDtDiagnosisId();
  public abstract java.lang.String getVisitId();
  public abstract java.lang.String getPatientId();
  public abstract java.lang.String getVitalSignExtendId();
  public abstract java.lang.String getDiagnosis();
  public abstract java.lang.String getToothNumber();
  public abstract java.lang.String getToothSurface();
  public abstract java.lang.String getDxNote();
  public abstract java.lang.String getDoctorEid();
  public abstract java.lang.String getDiagnosisDate();
  public abstract java.lang.String getDiagnosisTime();
  public abstract java.lang.String getIcd10Code();
  public abstract java.lang.String getIcd10Description();
  public abstract java.lang.String getToothQuadrant();
  public abstract java.lang.String getFixDiagnosisTypeId();
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