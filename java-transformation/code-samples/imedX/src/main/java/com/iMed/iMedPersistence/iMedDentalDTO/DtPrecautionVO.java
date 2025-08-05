package com.iMed.iMedPersistence.iMedDentalDTO;

/**
 * <p>Title: Premed/Precaution บนหน้าของ Dental</p>
 * <p>Description: </p>
 * <p>Copyright: Copyright (c) 2559</p>
 * <p>Company: International Medical Software</p>
 * @author Seksit Disaro
 * @version PV
 */

import com.iMed.iMedCore.utility.XPersistent;
import com.iMed.iMedCore.utility.Utility;

public class DtPrecautionVO extends XPersistent
{
  private String precaution_text;
  private String patient_id;
  private String is_active;
  private String create_eid;
  private String create_eid_name;
  private String create_date;
  private String create_time;

  public void setPrecautionText(String precaution_text)
  {
    this.precaution_text = precaution_text;
  }

  public String getPrecautionText()
  {
    return Utility.getStringVO(precaution_text);
  }

  public void setIsActive(String is_active)
  {
    this.is_active = is_active;
  }

  public String getIsActive()
  {
    return Utility.getStringVO(is_active);
  }

  public void setPatientId(String patient_id)
  {
    this.patient_id = patient_id;
  }

  public String getPatientId()
  {
    return Utility.getStringVO(patient_id);
  }

  public void setCreateEid(String create_eid)
  {
    this.create_eid = create_eid;
  }

  public String getCreateEid()
  {
    return Utility.getStringVO(create_eid);
  }

  public void setCreateEidName(String create_eid_name)
  {
    this.create_eid_name = create_eid_name;
  }

  public String getCreateEidName()
  {
    return Utility.getStringVO(create_eid_name);
  }

  public void setCreateDate(String create_date)
  {
    this.create_date = create_date;
  }

  public String getCreateDate()
  {
    return Utility.getStringVO(create_date);
  }

  public void setCreateTime(String create_time)
  {
    this.create_time = create_time;
  }
  
  public String getCreateTime()
  {
    return Utility.getStringVO(create_time);
  }
}