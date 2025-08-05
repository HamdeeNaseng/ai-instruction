package com.iMed.iMedPersistence.iMedDentalDTO;

import com.iMed.iMedCore.utility.*;
import java.util.*;
import java.io.Serializable;
/**
 * <p>Title: สำหรับเก็บข้อมูลการพิมพ์ใบ dental record / 1 visit / 1 dental doctor</p>
 * <p>Description: </p>
 * <p>Copyright: Copyright (c) 2551</p>
 * <p>Company: International Medical Software</p>
 * @author Kroeksak Lakmuang
 * @version PV
 */

public class DentalRecordPrintVO implements Serializable
{
  private String doctor_eid;
  private String doctor_eid_name;
  private String visit_id;

  private String main_symptom;
  private String current_illness;
  private String fix_discharge_status;
  private String fix_discharge_status_name;

  private List listOrderXrayDentalName;
  private List listOrderDrugName;
  private List listOrderName;

  private List listDtDiagnosisVO;
  private List listDtTreatmentPlanVO;
  private List listDtTreatmentVO;


  public List getListOrderName(){
          return this.listOrderName;
  }
  public void setListOrderName(List listOrderName){
          this.listOrderName = listOrderName;
  }

  /** เพิ่มรายการเข้าไปใน List โดยจะเช็คซ้ำจาก object_id ให้ */
  public boolean addDtDiagnosisVO(DtDiagnosisVO vo){
    if( vo == null ){
      return false;
    }
    if( listDtDiagnosisVO == null ){
      listDtDiagnosisVO = new ArrayList();
    }
    //เช็คซ้ำ
    for(int i=0 ; i < listDtDiagnosisVO.size() ; i++){
      DtDiagnosisVO dataVO = (DtDiagnosisVO)listDtDiagnosisVO.get(i);
      if( dataVO.getObjectID().equals(vo.getObjectID())){
        return false; //แสดงว่าซ้ำ จะไม่เพิ่ม
      }
    }
    listDtDiagnosisVO.add(vo);
    return true;
  }

  /** เพิ่มรายการเข้าไปใน List โดยจะเช็คซ้ำจาก object_id ให้ */
  public boolean addDtTreatmentPlanVO(DtTreatmentPlanVO vo){
    if( vo == null ){
      return false;
    }
    if( listDtTreatmentPlanVO == null ){
      listDtTreatmentPlanVO = new ArrayList();
    }
    //เช็คซ้ำ
    for(int i=0 ; i < listDtTreatmentPlanVO.size() ; i++){
      DtTreatmentPlanVO dataVO = (DtTreatmentPlanVO)listDtTreatmentPlanVO.get(i);
      if( dataVO.getObjectID().equals(vo.getObjectID())){
        return false; //แสดงว่าซ้ำ จะไม่เพิ่ม
      }
    }
    listDtTreatmentPlanVO.add(vo);
    return true;
  }

  /** เพิ่มรายการเข้าไปใน List โดยจะเช็คซ้ำจาก object_id ให้ */
  public boolean addDtTreatmentVO(DtTreatmentVO vo){
    if( vo == null ){
      return false;
    }
    if( listDtTreatmentVO == null ){
      listDtTreatmentVO = new ArrayList();
    }
    //เช็คซ้ำ
    for(int i=0 ; i < listDtTreatmentVO.size() ; i++){
      DtTreatmentVO dataVO = (DtTreatmentVO)listDtTreatmentVO.get(i);
      if( dataVO.getObjectID().equals(vo.getObjectID())){
        return false; //แสดงว่าซ้ำ จะไม่เพิ่ม
      }
    }
    listDtTreatmentVO.add(vo);
    return true;
  }

  public String getFixDischargeStatus(){
          return Utility.getStringVO(this.fix_discharge_status);
  }
  public String getFixDischargeStatusName(){
          return Utility.getStringVO(this.fix_discharge_status_name);
  }
  public void setFixDischargeStatus(String fix_discharge_status){
          this.fix_discharge_status = fix_discharge_status;
  }
  public void setFixDischargeStatusName(String fix_discharge_status_name){
          this.fix_discharge_status_name = fix_discharge_status_name;
  }
  public List getListOrderDrugName(){
          return this.listOrderDrugName;
  }
  public void setListOrderDrugName(List listOrderDrugName){
          this.listOrderDrugName = listOrderDrugName;
  }
  public String getDoctorEid(){
          return Utility.getStringVO(this.doctor_eid);
  }
  public String getDoctorEidName(){
          return Utility.getStringVO(this.doctor_eid_name);
  }
  public String getVisitId(){
          return Utility.getStringVO(this.visit_id);
  }
  public String getMainSymptom(){
          return Utility.getStringVO(this.main_symptom);
  }
  public String getCurrentIllness(){
          return Utility.getStringVO(this.current_illness);
  }
  public List getListOrderXrayDentalName(){
          return this.listOrderXrayDentalName;
  }
  public List getListDtDiagnosisVO(){
          return this.listDtDiagnosisVO;
  }
  public List getListDtTreatmentPlanVO(){
          return this.listDtTreatmentPlanVO;
  }
  public List getListDtTreatmentVO(){
          return this.listDtTreatmentVO;
  }
  public void setDoctorEid(String doctor_eid){
          this.doctor_eid = doctor_eid;
  }
  public void setDoctorEidName(String doctor_eid_name){
          this.doctor_eid_name = doctor_eid_name;
  }
  public void setVisitId(String visit_id){
          this.visit_id = visit_id;
  }
  public void setMainSymptom(String main_symptom){
          this.main_symptom = main_symptom;
  }
  public void setCurrentIllness(String current_illness){
          this.current_illness = current_illness;
  }
  public void setListOrderXrayDentalName(List listOrderXrayDentalName){
          this.listOrderXrayDentalName = listOrderXrayDentalName;
  }
  public void setListDtDiagnosisVO(List listDtDiagnosisVO){
          this.listDtDiagnosisVO = listDtDiagnosisVO;
  }
  public void setListDtTreatmentPlanVO(List listDtTreatmentPlanVO){
          this.listDtTreatmentPlanVO = listDtTreatmentPlanVO;
  }
  public void setListDtTreatmentVO(List listDtTreatmentVO){
          this.listDtTreatmentVO = listDtTreatmentVO;
  }

}