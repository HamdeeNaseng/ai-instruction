package com.iMed.iMedPersistence.iMedDentalDTO;

/**
 * <p>Title: </p>
 * <p>Description: </p>
 * <p>Copyright: Copyright (c) 2008</p>
 * <p>Company: </p>
 * @author สราวุธ วังอนานนท์
 * @version 1.0
 */

import com.iMed.iMedCore.utility.XPersistent;
import com.iMed.iMedCore.utility.Utility;

public class BaseDtItemVO extends XPersistent
{
  private String item_id;
  private String base_dt_symbol_id;
  private String fix_dt_action_type_id;
  // ใช้สำหรับแสดงผล
  private String item_name;
  // ชื่อ icon ของ symbol ที่ผูกกับ item นั้นๆ
  private String symbol_icon_path;
  // ประเภทของ symbol
  private String fix_dt_symbol_type_id;
  // ประเภทของ item
  private String fix_item_type_id;
  // ประเภทการรักษา ใช้หาตัวช่วยกรอกรายละเอียด Tx
  private String base_dt_tx_type_id;
  //เป็น treatment หรือไม่
  private String is_treatment;
  //note ของ item เอาไปแสดงผล
  private String item_note;
  // ถ้าเลือก item นี้จะเป็น favorite จะมี id นี้
  private String base_dt_treatment_default_id;

  public String getItemNote(){
          return Utility.getStringVO(this.item_note);
  }
  public void setItemNote(String item_note){
          this.item_note = item_note;
  }
  public String getBaseDtSymbolId()
  {
    return Utility.getStringVO(base_dt_symbol_id);
  }
  public void setBaseDtSymbolId(String base_dt_symbol_id)
  {
    this.base_dt_symbol_id = base_dt_symbol_id;
  }
  public String getItemId()
  {
    return Utility.getStringVO(item_id);
  }
  public void setItemId(String item_id)
  {
    this.item_id = item_id;
  }
  public String getFixDtActionTypeId()
  {
    return Utility.getStringVO(fix_dt_action_type_id);
  }
  public void setFixDtActionTypeId(String fix_dt_action_type_id)
  {
    this.fix_dt_action_type_id = fix_dt_action_type_id;
  }

  // ใช้สำหรับแสดงผล
  public String getItemName()
  {
    return Utility.getStringVO(item_name);
  }
  public void setItemName(String item_name)
  {
    this.item_name = item_name;
  }
  public String getSymbolIconPath()
  {
    return Utility.getStringVO(symbol_icon_path);
  }
  public void setSymbolIconPath(String symbol_icon_path)
  {
    this.symbol_icon_path = symbol_icon_path;
  }
  // ประเภทของ symbol
  public String getFixDtSymbolTypeId()
  {
    return Utility.getStringVO(fix_dt_symbol_type_id);
  }
  public void setFixDtSymbolTypeId(String fix_dt_symbol_type_id)
  {
    this.fix_dt_symbol_type_id = fix_dt_symbol_type_id;
  }
  //ประเภทของ item
  public String getFixItemTypeId()
  {
    return Utility.getStringVO(fix_item_type_id);
  }
  public void setFixItemTypeId(String fix_item_type_id)
  {
    this.fix_item_type_id = fix_item_type_id;
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
   //เป็น treatment หรือไม่
   public String getIsTreatment()
   {
     return Utility.getStringVO(is_treatment);
   }
   public void setIsTreatment(String is_treatment)
   {
     this.is_treatment = is_treatment;
   }

   public String getBaseDtTreatmentDefaultId() {
       return Utility.getStringVO(base_dt_treatment_default_id);
   }

   public void setBaseDtTreatmentDefaultId(String base_dt_treatment_default_id) {
       this.base_dt_treatment_default_id = base_dt_treatment_default_id;
   }

}