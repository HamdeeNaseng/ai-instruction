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

public class TemplateDtTxNoteVO extends XPersistent
{
  private String code;
  private String description;
  private String employee_id;
  private String employee_name;
  private String base_dt_tx_type_id;
  private String base_dt_tx_type_description;

  public TemplateDtTxNoteVO()
  {
  }
  public String getBaseDtTxTypeId()
  {
    return Utility.getStringVO(base_dt_tx_type_id);
  }
  public void setBaseDtTxTypeId(String base_dt_tx_type_id)
  {
    this.base_dt_tx_type_id = base_dt_tx_type_id;
  }
  public String getCode()
  {
    return Utility.getStringVO(code);
  }
  public void setCode(String code)
  {
    this.code = code;
  }
  public String getDescription()
  {
    return Utility.getStringVO(description);
  }
  public void setDescription(String description)
  {
    this.description = description;
  }
  public String getEmployeeId()
  {
    return Utility.getStringVO(employee_id);
  }
  public void setEmployeeId(String employee_id)
  {
    this.employee_id = employee_id;
  }
  public String getEmployeeName() {
    return employee_name;
  }
  public void setEmployeeName(String employee_name)
  {
    this.employee_name = employee_name;
  }
  public String getBaseDtTxTypeDescription() {
    return this.base_dt_tx_type_description;
  }
  public void setBaseDtTxTypeDescription(String base_dt_tx_type_description)  {
        this.base_dt_tx_type_description = base_dt_tx_type_description;
  }
}