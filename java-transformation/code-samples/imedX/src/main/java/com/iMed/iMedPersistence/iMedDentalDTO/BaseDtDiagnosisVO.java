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

public class BaseDtDiagnosisVO extends XPersistent
{
  private String description;
  private String base_dt_symbol_id;
  private String fix_dt_action_type_id;
  // ชื่อ icon ของ symbol ที่ผูกกับ dx นั้นๆ
  private String symbol_icon_path;
  // ประเภทของ symbol
  private String fix_dt_symbol_type_id;
  private String icd10_code;

  //สำหรับแสดงผล
  private String icd10_description;

  private String base_dt_diagnosis_default_id;

  public BaseDtDiagnosisVO()
  {
  }
  public String getIcd10Description(){
          return Utility.getStringVO(this.icd10_description);
  }
  public void setIcd10Description(String icd10_description){
          this.icd10_description = icd10_description;
  }
  public String getDescription()
  {
    return Utility.getStringVO(description);
  }
  public void setDescription(String description)
  {
    this.description = description;
  }
  public String getBaseDtSymbolId()
  {
    return Utility.getStringVO(base_dt_symbol_id);
  }
  public void setBaseDtSymbolId(String base_dt_symbol_id)
  {
    this.base_dt_symbol_id = base_dt_symbol_id;
  }
  public String getFixDtActionTypeId()
  {
    return Utility.getStringVO(fix_dt_action_type_id);
  }
  public void setFixDtActionTypeId(String fix_dt_action_type_id)
  {
    this.fix_dt_action_type_id = fix_dt_action_type_id;
  }
  // ชื่อ icon ของ symbol ที่ผูกกับ item นั้นๆ
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

  public String getIcd10Code()
  {
    return Utility.getStringVO(icd10_code);
  }
  public void setIcd10Code(String icd10_code)
  {
    this.icd10_code = icd10_code;
  }

  public String getBaseDtDiagnosisDefaultId() {
      return Utility.getStringVO(base_dt_diagnosis_default_id);
  }

  public void setBaseDtDiagnosisDefaultId(String base_dt_diagnosis_default_id) {
      this.base_dt_diagnosis_default_id = base_dt_diagnosis_default_id;
  }

}