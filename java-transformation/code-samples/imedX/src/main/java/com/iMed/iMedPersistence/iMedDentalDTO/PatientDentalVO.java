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

public class PatientDentalVO implements Serializable
{
  // Teeth chart
  private List listTeethChart;
  // รายการ Order ของ visit ปัจจุบัน
  private List listOrder;
  // รายการ Symbol ใน Teeth Chart ของผู้ป่วย
  private List listDtSymbol;
  // รายการตรวจร่างกาย
  private List listDentalExamination;
  // ข้อมูลตรวจร่างกายของ visit ที่ระบุ
  private DentalExaminationVO dental_examination;
  // แผนการรักษา และการรักษาต่อเนื่อง
  private List listTreatmentPlan;
  // ประวัติการให้การรักษา
  private Hashtable treatment_history;
  // ยอดที่เหลือของการรักษาแบบ course
  private String course_remain_cost;
  // ข้อความ Dental Precaution อันปัจจุบัน
  private DtPrecautionVO currentDentalPrecaution;
  // ข้อมูลการตรวจสภาพฟัน
  private List listTeethChartExam;
  // ข้อมูลสภาพฟันแบบรวม
  private List listTeethChartOverall;

  public PatientDentalVO()
  {
  }

  public List getListTeethChart()
  {
    return listTeethChart;
  }
  public void setListTeethChart(List listTeethChart)
  {
    this.listTeethChart = listTeethChart;
  }
  public List getListOrder()
  {
    return listOrder;
  }
  public void setListOrder(List listOrder)
  {
    this.listOrder = listOrder;
  }
  public List getListDtSymbol()
  {
    return listDtSymbol;
  }
  public void setListDtSymbol(List listDtSymbol)
  {
    this.listDtSymbol = listDtSymbol;
  }
  public List getListDentalExamination()
  {
    return listDentalExamination;
  }
  public void setListDentalExamination(List listDentalExamination)
  {
    this.listDentalExamination = listDentalExamination;
  }
  public DentalExaminationVO getDentalExamination()
  {
    return dental_examination;
  }
  public void setDentalExamination(DentalExaminationVO dental_examination)
  {
    this.dental_examination = dental_examination;
  }
  public List getListTreatmentPlan()
  {
    return listTreatmentPlan;
  }
  public void setListTreatmentPlan(List listTreatmentPlan)
  {
    this.listTreatmentPlan = listTreatmentPlan;
  }
  public Hashtable getTreatmentHistory()
  {
    return treatment_history;
  }
  public void setTreatmentHistory(Hashtable treatment_history)
  {
    this.treatment_history = treatment_history;
  }
  // ยอดที่เหลือของการรักษาแบบ course
  public String getCourseRemainCost()
  {
    return Utility.isNotNull(course_remain_cost) ? course_remain_cost : "0.00";
  }
  public void setCourseRemainCost(String course_remain_cost)
  {
    this.course_remain_cost = course_remain_cost;
  }
  // Precaution ครั้งที่ใช้งานอยู่สำหรับ Patient คนนี้
  public DtPrecautionVO getCurrentDentalPrecaution() {
    return this.currentDentalPrecaution;
  }
  public void setCurrentDentalPrecaution(DtPrecautionVO dtPrecautionVO) {
    this.currentDentalPrecaution = dtPrecautionVO;
  }
  
  public List getListTeethChartExam()
  {
    return listTeethChartExam;
  }
  public void setListTeethChartExam(List listTeethChartExam)
  {
    this.listTeethChartExam = listTeethChartExam;
  }
    
  public List getListTeethChartOverall()
  {
    return listTeethChartOverall;
  }
  public void setListTeethChartOverall(List listTeethChartOverall)
  {
    this.listTeethChartOverall = listTeethChartOverall;
  }
}