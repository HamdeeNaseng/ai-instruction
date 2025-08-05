package com.iMed.iMedPersistence.iMedDentalDTO;

import com.iMed.iMedCore.utility.XPersistent;
import com.iMed.iMedCore.utility.Utility;

/**
 * <p>Title: </p>
 * <p>Description: </p>
 * <p>Copyright: Copyright (c) 2551</p>
 * <p>Company: International Medical Software</p>
 * @author Rungsiri Thirawittayanon
 * @version PV
 */

public class DtDiagnosisVO extends XPersistent
{
  private String visit_id;
  private String patient_id;
  private String vital_sign_extend_id;
  private String diagnosis;
  private String tooth_number;
  private String tooth_surface;
  private String tooth_quadrant;
  private String dx_note;
  private String doctor_eid;
  private String diagnosis_date;
  private String diagnosis_time;
  private String icd10_code;
  private String icd10_description;
  // สำหรับตรวจสอบ TC
  private BaseDtDiagnosisVO base_dt_diagnosis;
  private String fix_diagnosis_type_id;

  public DtDiagnosisVO()
  {
  }
  public String getDiagnosis()
  {
    return Utility.getStringVO(diagnosis);
  }
  public void setDiagnosis(String diagnosis)
  {
    this.diagnosis = diagnosis;
  }
  public String getDiagnosisDate()
  {
    return Utility.getStringVO(diagnosis_date);
  }
  public void setDiagnosisDate(String diagnosis_date)
  {
    this.diagnosis_date = diagnosis_date;
  }
  public String getDiagnosisTime()
  {
    return Utility.getStringVO(diagnosis_time);
  }
  public void setDiagnosisTime(String diagnosis_time)
  {
    this.diagnosis_time = diagnosis_time;
  }
  public String getDoctorEid()
  {
    return Utility.getStringVO(doctor_eid);
  }
  public void setDoctorEid(String doctor_eid)
  {
    this.doctor_eid = doctor_eid;
  }
  public String getDxNote()
  {
    return Utility.getStringVO(dx_note);
  }
  public void setDxNote(String dx_note)
  {
    this.dx_note = dx_note;
  }
  public String getPatientId()
  {
    return Utility.getStringVO(patient_id);
  }
  public void setPatientId(String patient_id)
  {
    this.patient_id = patient_id;
  }
  public String getToothNumber()
  {
    return Utility.getStringVO(tooth_number);
  }
  public void setToothNumber(String tooth_number)
  {
    this.tooth_number = tooth_number;
  }
  public String getToothSurface()
  {
    return Utility.getStringVO(tooth_surface);
  }
  public void setToothSurface(String tooth_surface)
  {
    this.tooth_surface = tooth_surface;
  }
  public String getToothQuadrant()
  {
    return Utility.getStringVO(tooth_quadrant);
  }
  public void setToothQuadrant(String tooth_quadrant)
  {
    this.tooth_quadrant = tooth_quadrant;
  }
  public String getVisitId()
  {
    return Utility.getStringVO(visit_id);
  }
  public void setVisitId(String visit_id)
  {
    this.visit_id = visit_id;
  }
  public String getVitalSignExtendId()
  {
    return Utility.getStringVO(vital_sign_extend_id);
  }
  public void setVitalSignExtendId(String vital_sign_extend_id)
  {
    this.vital_sign_extend_id = vital_sign_extend_id;
  }

  public String getIcd10Code()
  {
    return Utility.getStringVO(icd10_code);
  }
  public void setIcd10Code(String icd10_code)
  {
    this.icd10_code = icd10_code;
  }

  public String getIcd10Description()
  {
    return Utility.getStringVO(icd10_description);
  }
  public void setIcd10Description(String icd10_description)
  {
    this.icd10_description = icd10_description;
  }

  // สำหรับตรวจสอบ TC
  public BaseDtDiagnosisVO getBaseDtDiagnosis()
  {
    return base_dt_diagnosis;
  }
  public void setBaseDtDiagnosis(BaseDtDiagnosisVO base_dt_diagnosis)
  {
    this.base_dt_diagnosis = base_dt_diagnosis;
  }
  public String getFixDiagnosisTypeId()
  {
    return Utility.getStringVO(fix_diagnosis_type_id);
  }
  public void setFixDiagnosisTypeId(String fix_diagnosis_type_id)
  {
    this.fix_diagnosis_type_id = fix_diagnosis_type_id;
  }
}