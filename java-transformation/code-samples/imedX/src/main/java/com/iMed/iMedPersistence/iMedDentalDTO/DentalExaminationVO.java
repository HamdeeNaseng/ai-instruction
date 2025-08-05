package com.iMed.iMedPersistence.iMedDentalDTO;

import com.iMed.iMedCore.utility.*;
import java.util.*;
import java.io.Serializable;

/**
 * <p>Title: </p>
 * <p>Description: </p>
 * <p>Copyright: Copyright (c) 2551</p>
 * <p>Company: International Medical Software</p>
 * @author Rungsiri Thirawittayanon
 * @version PV
 */

public class DentalExaminationVO implements Serializable
{
  private String visit_id;
  private String vital_sign_extend_id;
  private String main_symptom;
  private String current_illness;
  private String doctor_eid;
  private String doctor_eid_name;
  private String examine_date;
  private String examine_time;
  private String modify_eid;
  private String modify_date;
  private String modify_time;
  // ตารางที่เกี่ยวข้อง
  private List listDtDiagnosis;
  // ข้อมูลเพิ่มเติม
  private String patient_id;
  // template_id กรณีที่ลงข้อมูลผ่าน guideline custom form
  private String base_custom_template_doctor_id;

  public DentalExaminationVO()
  {
  }
  public String getCurrentIllness()
  {
    return Utility.getStringVO(current_illness);
  }
  public void setCurrentIllness(String current_illness)
  {
    this.current_illness = current_illness;
  }
  public String getDoctorEid()
  {
    return Utility.getStringVO(doctor_eid);
  }
  public void setDoctorEid(String doctor_eid)
  {
    this.doctor_eid = doctor_eid;
  }
  public String getDoctorEidName()
  {
    return Utility.getStringVO(doctor_eid_name);
  }
  public void setDoctorEidName(String doctor_eid_name)
  {
    this.doctor_eid_name = doctor_eid_name;
  }
  public String getExamineDate()
  {
    return Utility.getStringVO(examine_date);
  }
  public void setExamineDate(String examine_date)
  {
    this.examine_date = examine_date;
  }
  public String getExamineTime()
  {
    return Utility.getStringVO(examine_time);
  }
  public void setExamineTime(String examine_time)
  {
    this.examine_time = examine_time;
  }
  public String getMainSymptom()
  {
    return Utility.getStringVO(main_symptom);
  }
  public void setMainSymptom(String main_symptom)
  {
    this.main_symptom = main_symptom;
  }
  public String getModifyDate()
  {
    return Utility.getStringVO(modify_date);
  }
  public void setModifyDate(String modify_date)
  {
    this.modify_date = modify_date;
  }
  public String getModifyEid()
  {
    return Utility.getStringVO(modify_eid);
  }
  public void setModifyEid(String modify_eid)
  {
    this.modify_eid = modify_eid;
  }
  public String getModifyTime()
  {
    return Utility.getStringVO(modify_time);
  }
  public void setModifyTime(String modify_time)
  {
    this.modify_time = modify_time;
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
  // ตารางที่เกี่ยวข้อง
  public List getListDtDiagnosis()
  {
    return listDtDiagnosis;
  }
  public void setListDtDiagnosis(List listDtDiagnosis)
  {
    this.listDtDiagnosis = listDtDiagnosis;
  }
  // ข้อมูลเพิ่มเติม
  public String getPatientId()
  {
    return Utility.getStringVO(patient_id);
  }
  public void setPatientId(String patient_id)
  {
    this.patient_id = patient_id;
  }
  // template_id กรณีที่ลงข้อมูลผ่าน guideline custom form
  public String getBaseCustomTemplateDoctorId()
  {
    return Utility.getStringVO(base_custom_template_doctor_id);
  }
  public void setBaseCustomTemplateDoctorId(String base_custom_template_doctor_id)
  {
    this.base_custom_template_doctor_id = base_custom_template_doctor_id;
  }
}