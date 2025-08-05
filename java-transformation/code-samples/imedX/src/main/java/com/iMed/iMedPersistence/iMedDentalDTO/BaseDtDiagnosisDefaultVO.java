package com.iMed.iMedPersistence.iMedDentalDTO;

import com.iMed.iMedCore.utility.XPersistent;
import com.iMed.iMedCore.utility.Utility;

/**
 * <p>Title: </p>
 * <p>Description: </p>
 * <p>Copyright: Copyright (c) 2552</p>
 * <p>Company: International Medical Software</p>
 * @author Surachai Boonum
 * @version PV
 */

public class BaseDtDiagnosisDefaultVO extends XPersistent
{
  private String base_dt_diagnosis_id;
  private String employee_id;

  //เพิ่มเติมชื่อเรียก diagnosis
  private String description;

  //เพิ่มเติมจากตาราง employee
  private String prename;
  private String firstname;
  private String lastname;

  public BaseDtDiagnosisDefaultVO()
  {
  }

  public String getBaseDtDiagnosisId()
  {
    return Utility.getStringVO(this.base_dt_diagnosis_id);
  }
  public void setBaseDtDiagnosisId(String base_dt_diagnosis_id)
  {
    this.base_dt_diagnosis_id = base_dt_diagnosis_id;
  }

  public String getEmployeeId()
  {
    return Utility.getStringVO(this.employee_id);
  }
  public void setEmployeeId(String employee_id)
  {
    this.employee_id = employee_id;
  }

//เพิ่มเติมชื่อเรียก diagnosis
  public String getDescription()
  {
    return Utility.getStringVO(this.description);
  }

  public void setDescription(String description)
  {
    this.description = description;
  }

//เพิ่มเติมจากตาราง employee
  public String getPrename()
  {
    return Utility.getStringVO(this.prename);
  }
  public void setPrename(String prename)
  {
    this.prename = prename;
  }
  public String getFirstname()
  {
    return Utility.getStringVO(this.firstname);
  }
  public void setFirstname(String firstname)
  {
    this.firstname = firstname;
  }
  public String getLastname()
  {
    return Utility.getStringVO(this.lastname);
  }
  public void setLastname(String lastname)
  {
    this.lastname = lastname;
  }

}