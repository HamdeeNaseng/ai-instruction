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

public class TeethChartVO extends XPersistent
{
  private String fix_dt_tooth_type_id;
  private String is_missing_tooth;
  private String patient_id;
  private String tooth_number;
  private String modify_date;
  private String modify_time;
  private String modify_eid;
  private int tooth_id;

  public String getFixDtToothTypeId()
  {
    return Utility.getStringVO(fix_dt_tooth_type_id);
  }
  public void setFixDtToothTypeId(String fix_dt_tooth_type_id)
  {
    this.fix_dt_tooth_type_id = fix_dt_tooth_type_id;
  }
  public String getIsMissingTooth()
  {
    return Utility.getStringVO(is_missing_tooth);
  }
  public void setIsMissingTooth(String is_missing_tooth)
  {
    this.is_missing_tooth = is_missing_tooth;
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
  public int getToothId()
  {
    return tooth_id;
  }
  public void setToothId(int tooth_id)
  {
    this.tooth_id = tooth_id;
  }
  public String getModifyDate()
  {
    return Utility.getStringVO(modify_date);
  }
  public void setModifyDate(String modify_date)
  {
    this.modify_date = modify_date;
  }
  public String getModifyTime()
  {
    return Utility.getStringVO(modify_time);
  }
  public void setModifyTime(String modidy_time)
  {
    this.modify_time = modidy_time;
  }
  public String getModifyEid()
  {
    return Utility.getStringVO(modify_eid);
  }
  public void setModifyEid(String modify_eid)
  {
    this.modify_eid = modify_eid;
  }
}