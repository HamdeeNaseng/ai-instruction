package com.iMed.iMedPersistence.iMedDentalDTO;

import com.iMed.iMedCore.utility.XPersistent;
import com.iMed.iMedCore.utility.Utility;
import com.iMed.iMedCore.utility.fix.FixDtTxCategory;

/**
 * <p>Title: </p>
 * <p>Description: </p>
 * <p>Copyright: Copyright (c) 2551</p>
 * <p>Company: International Medical Software</p>
 * @author Rungsiri Thirawittayanon
 * @version PV
 */

public class DtTreatmentPlanVO extends XPersistent
{
  private String item_id;
  private String patient_id;
  private String visit_id;
  private String plan_no;
  private String tooth_number;
  private String tooth_surface;
  private String tooth_quadrant;
  private String tx_note;
  private String doctor_eid;
  private String modify_eid;
  private String modify_date;
  private String modify_time;
  // ใช้แสดงข้อมูล
  private String item_name;
  private String fix_item_type_id;
  private String doctor_eid_name;
  private String archive_doctor_eid_name;
  // ประเภทการรักษา ใช้หาตัวช่วยกรอกรายละเอียด Tx
  private String base_dt_tx_type_id;
  // ให้ GUI ใช้ตรวจสอบประเภท tx ในตาราง Tx Plan ว่าเป็น แผน / การรักษาต่อเนื่อง
  private String fix_dt_tx_category_id;
  // ใช้เก็บข้อมูล treatment course
  private DtTreatmentVO treatment_course;
  // ใช้เก็บข้อมูลเรื่อง Archive แผนการรักษา
  private String is_archive;
  private String archive_doctor_eid;
  private String archive_date;
  private String archive_time;
  // ใช้เก็บข้อมูลมาร์กว่าทำเสร็จรึยัง
  private String is_applied;
  // เก็บข้อมูลสำหรับให้ GUI ใช้ update Teeth Chart
  private BaseDtItemVO base_dt_item;

  public DtTreatmentPlanVO()
  {
  }
  public String getDoctorEid()
  {
    return Utility.getStringVO(doctor_eid);
  }
  public void setDoctorEid(String doctor_eid)
  {
    this.doctor_eid = doctor_eid;
  }
  public String getItemId()
  {
    return Utility.getStringVO(item_id);
  }
  public void setItemId(String item_id)
  {
    this.item_id = item_id;
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
  public String getPatientId()
  {
    return Utility.getStringVO(patient_id);
  }
  public void setPatientId(String patient_id)
  {
    this.patient_id = patient_id;
  }
  public String getPlanNo()
  {
    return Utility.getStringVO(plan_no);
  }
  public void setPlanNo(String plan_no)
  {
    this.plan_no = plan_no;
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
  public String getTxNote()
  {
    return Utility.getStringVO(tx_note);
  }
  public void setTxNote(String tx_note)
  {
    this.tx_note = tx_note;
  }
  public String getVisitId()
  {
    return Utility.getStringVO(visit_id);
  }
  public void setVisitId(String visit_id)
  {
    this.visit_id = visit_id;
  }
  // ใช้แสดงข้อมูล
  public String getItemName()
  {
    return Utility.getStringVO(item_name);
  }
  public void setItemName(String item_name)
  {
    this.item_name = item_name;
  }
  public String getFixItemTypeId()
  {
    return Utility.getStringVO(fix_item_type_id);
  }
  public void setFixItemTypeId(String fix_item_type_id)
  {
    this.fix_item_type_id = fix_item_type_id;
  }
  public String getDoctorEidName()
  {
    return Utility.getStringVO(doctor_eid_name);
  }
  public void setDoctorEidName(String doctor_eid_name)
  {
    this.doctor_eid_name = doctor_eid_name;
  }
  public String getArchiveDoctorEidName()
  {
    return Utility.getStringVO(archive_doctor_eid_name);
  }
  public void setArchiveDoctorEidName(String archive_doctor_eid_name)
  {
    this.archive_doctor_eid_name = archive_doctor_eid_name;
  }

  // ประเภทการรักษาทางทันตกรรม
  public String getBaseDtTxTypeId()
  {
    return Utility.getStringVO(base_dt_tx_type_id);
  }
  public void setBaseDtTxTypeId(String base_dt_tx_type_id)
  {
    this.base_dt_tx_type_id = base_dt_tx_type_id;
  }
  // ให้ GUI ใช้ตรวจสอบประเภท tx ในตาราง Tx Plan ว่าเป็น แผน / การรักษาต่อเนื่อง
  public String getFixDtTxCategoryId()
  {
    return Utility.isNotNull(fix_dt_tx_category_id) ? fix_dt_tx_category_id : FixDtTxCategory.PLAN;
  }
  public void setFixDtTxCategoryId(String fix_dt_tx_category_id)
  {
    this.fix_dt_tx_category_id = fix_dt_tx_category_id;
  }
  // ใช้เก็บข้อมูล treatment course
  public DtTreatmentVO getTreatmentCourse()
  {
    return treatment_course;
  }
  public void setTreatmentCourse(DtTreatmentVO treatment_course)
  {
    this.treatment_course = treatment_course;
  }
  public String getIsArchive() {
    return Utility.getStringVO(is_archive);
  }
  public void setIsArchieve(String is_archive) {
    this.is_archive = is_archive;
  }
  public String getArchiveDoctorEid()  {
    return Utility.getStringVO(archive_doctor_eid);
  }
  public void setArchiveDoctorEid(String archive_doctor_eid)  {
    this.archive_doctor_eid = archive_doctor_eid;
  }
  public String getArchiveDate()  {
    return Utility.getStringVO(archive_date);
  }
  public void setArchiveDate(String archive_date)  {
    this.archive_date = archive_date;
  }
  public String getArchiveTime()  {
    return Utility.getStringVO(archive_time);
  }
  public void setArchiveTime(String archive_time)  {
    this.archive_time = archive_time;
  }
  public String getIsApplied() {
    return Utility.getStringVO(is_applied);
  }
  public void setIsApplied(String is_applied) {
    this.is_applied = is_applied;
  }
  // เก็บข้อมูลสำหรับให้ GUI ใช้ update Teeth Chart
  public void setBaseDtItem(BaseDtItemVO base_dt_item)
  {
    this.base_dt_item = base_dt_item;
  }
  public BaseDtItemVO getBaseDtItem()
  {
    return base_dt_item;
  }
}