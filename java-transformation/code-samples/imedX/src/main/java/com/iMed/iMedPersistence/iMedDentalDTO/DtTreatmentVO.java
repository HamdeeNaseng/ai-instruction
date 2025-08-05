package com.iMed.iMedPersistence.iMedDentalDTO;

import com.iMed.iMedCore.utility.XPersistent;
import com.iMed.iMedCore.utility.Utility;
import com.iMed.iMedCore.utility.fix.FixBooleanStatus;
import com.iMed.iMedPersistence.iMedOPDDTO.OrderItemVO;
import com.iMed.iMedPersistence.iMedOPDDTO.VisitVO;
// OPD

import java.util.*;
/**
 * <p>Title: </p>
 * <p>Description: </p>
 * <p>Copyright: Copyright (c) 2551</p>
 * <p>Company: International Medical Software</p>
 * @author Rungsiri Thirawittayanon
 * @version PV
 */

public class DtTreatmentVO extends XPersistent
{
  private String item_id;
  private String order_item_id;
  private String patient_id;
  private String visit_id;
  private String fix_item_type_id;
  private String tooth_number;
  private String tooth_surface;
  private String tooth_quadrant;
  private String tx_note;
  private String course_treatment_id;
  private String course_price_estimate;
  private String course_next_tx_note;
  private String is_course_completed;
  private String doctor_eid;
  private String treatment_date;
  private String treatment_time;
  private String modify_eid;
  private String modify_date;
  private String modify_time;
  // ใช้สำหรับสั่ง order
  private OrderItemVO order_item;
  private VisitVO visit;
  private String fix_order_status_id;
  private String item_name;
  private String doctor_eid_name;
  private String base_dt_symbol_id;
  // ใช้ update symbol ใน teeth chart
  private List listAddedSymbol;
  private List listRemovedSymbol;
  // มีการเปลี่ยนแปลงข้อมูล icd9 หรือไม่
  private boolean is_diagnosis_icd9_updated;
  // เก็บข้อมูลสำหรับให้ GUI ใช้ update Teeth Chart
  private BaseDtItemVO base_dt_item;
  // ใช้สำหรับสั่ง order จาก Tx Plan
  private String dt_treatment_plan_id;
  // เป็น treatment course หรือไม่
  private String is_treatment_course;
  // ค่ารักษาที่จ่ายแล้วสำหรับ treatment course นี้
  private String course_price_paid;
  // Tracking
  private String is_edit;
  private String track_actor;
  private String track_actor_name;
  private String track_date;
  private String track_time;

  public DtTreatmentVO()
  {
  }
  public String getCourseTreatmentId()
  {
    return Utility.getStringVO(course_treatment_id);
  }
  public void setCourseTreatmentId(String course_treatment_id)
  {
    this.course_treatment_id = course_treatment_id;
  }
  public String getCoursePriceEstimate()
  {
    return Utility.getStringVO(course_price_estimate);
  }
  public void setCoursePriceEstimate(String course_price_estimate)
  {
    this.course_price_estimate = course_price_estimate;
  }
  public String getCourseNextTxNote()
  {
    return Utility.getStringVO(course_next_tx_note);
  }
  public void setCourseNextTxNote(String course_next_tx_note)
  {
    this.course_next_tx_note = course_next_tx_note;
  }
  public String getDoctorEid()
  {
    return Utility.getStringVO(doctor_eid);
  }
  public void setDoctorEid(String doctor_eid)
  {
    this.doctor_eid = doctor_eid;
  }
  public String getIsCourseCompleted()
  {
    return Utility.isNotNull(is_course_completed) ? is_course_completed : FixBooleanStatus.FALSE;
  }
  public void setIsCourseCompleted(String is_course_completed)
  {
    this.is_course_completed = is_course_completed;
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
  public String getOrderItemId()
  {
    return Utility.getStringVO(order_item_id);
  }
  public void setOrderItemId(String order_item_id)
  {
    this.order_item_id = order_item_id;
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
  public String getTreatmentDate()
  {
    return Utility.getStringVO(treatment_date);
  }
  public void setTreatmentDate(String treatment_date)
  {
    this.treatment_date = treatment_date;
  }
  public String getTreatmentTime()
  {
    return Utility.getStringVO(treatment_time);
  }
  public void setTreatmentTime(String treatment_time)
  {
    this.treatment_time = treatment_time;
  }
  public String getTxNote()
  {
    return Utility.getStringVO(tx_note);
  }
  public void setTxNote(String tx_note)
  {
    this.tx_note = tx_note;
  }
  public String getPatientId()
  {
    return Utility.getStringVO(patient_id);
  }
  public void setPatientId(String patient_id)
  {
    this.patient_id = patient_id;
  }
  public String getFixItemTypeId()
  {
    return Utility.getStringVO(fix_item_type_id);
  }
  public void setFixItemTypeId(String fix_item_type_id)
  {
    this.fix_item_type_id = fix_item_type_id;
  }
  public String getVisitId()
  {
    return Utility.getStringVO(visit_id);
  }
  public void setVisitId(String visit_id)
  {
    this.visit_id = visit_id;
  }

  // ใช้สำหรับสั่ง order
  public OrderItemVO getOrderItem()
  {
    return order_item;
  }
  public void setOrderItem(OrderItemVO order_item)
  {
    this.order_item = order_item;
  }
  public VisitVO getVisit()
  {
    return visit;
  }
  public void setVisit(VisitVO visit)
  {
    this.visit = visit;
  }
  public String getFixOrderStatusId()
  {
    return Utility.getStringVO(fix_order_status_id);
  }
  public void setFixOrderStatusId(String fix_order_status_id)
  {
    this.fix_order_status_id = fix_order_status_id;
  }
  public String getItemName()
  {
    return Utility.getStringVO(item_name);
  }
  public void setItemName(String item_name)
  {
    this.item_name = item_name;
  }
  public String getDoctorEidName()
  {
    return Utility.getStringVO(doctor_eid_name);
  }
  public void setDoctorEidName(String doctor_eid_name)
  {
    this.doctor_eid_name = doctor_eid_name;
  }
  public String getBaseDtSymbolId()
  {
    return Utility.getStringVO(base_dt_symbol_id);
  }
  public void setBaseDtSymbolId(String base_dt_symbol_id)
  {
    this.base_dt_symbol_id = base_dt_symbol_id;
  }
  // ใช้ update symbol ใน teeth chart
  public List getListAddedSymbol()
  {
    return listAddedSymbol;
  }
  public void setListAddedSymbol(List listAddedSymbol)
  {
    this.listAddedSymbol = listAddedSymbol;
  }
  public List getListRemovedSymbol()
  {
    return listRemovedSymbol;
  }
  public void setListRemovedSymbol(List listRemovedSymbol)
  {
    this.listRemovedSymbol = listRemovedSymbol;
  }
  // มีการเปลี่ยนแปลงข้อมูล icd9 หรือไม่
  public void setIsDiagnosisIcd9Updated(boolean is_diagnosis_icd9_updated)
  {
    this.is_diagnosis_icd9_updated = is_diagnosis_icd9_updated;
  }
  public boolean getIsDiagnosisIcd9Updated()
  {
    return is_diagnosis_icd9_updated;
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
  // ใช้สำหรับสั่ง order จาก Tx Plan
  public String getDtTreatmentPlanId()
  {
    return Utility.getStringVO(dt_treatment_plan_id);
  }
  public void setDtTreatmentPlanId(String dt_treatment_plan_id)
  {
    this.dt_treatment_plan_id = dt_treatment_plan_id;
  }
  // ใช้ตรวจสอบ treatment course
  public String getIsTreatmentCourse()
  {
    return Utility.isNotNull(is_treatment_course) ? is_treatment_course : FixBooleanStatus.FALSE;
  }
  public void setIsTreatmentCourse(String is_treatment_course)
  {
    this.is_treatment_course = is_treatment_course;
  }
  public String getCoursePricePaid()
  {
    return Utility.isNotNull(course_price_paid) ? course_price_paid : "0";
  }
  public void setCoursePricePaid(String course_price_paid)
  {
    this.course_price_paid = course_price_paid;
  }
  // ใช้สำหรับ Tracking
  public String getIsEdit() {
    return this.is_edit;
  }
  public void setIsEdit(String is_edit) {
    this.is_edit = is_edit;
  }
  public void setTrackActor(String track_actor)
  {
    this.track_actor = track_actor;
  }

  public String getTrackActor()
  {
    return Utility.getStringVO(track_actor);
  }

  public void setTrackActorName(String track_actor_name)
  {
    this.track_actor_name = track_actor_name;
  }

  public String getTrackActorName()
  {
    return Utility.getStringVO(track_actor_name);
  }

  public void setTrackDate(String track_date)
  {
    this.track_date = track_date;
  }

  public String getTrackDate()
  {
    return Utility.getStringVO(track_date);
  }

  public void setTrackTime(String track_time)
  {
    this.track_time = track_time;
  }

  public String getTrackTime()
  {
    return Utility.getStringVO(track_time);
  }


}