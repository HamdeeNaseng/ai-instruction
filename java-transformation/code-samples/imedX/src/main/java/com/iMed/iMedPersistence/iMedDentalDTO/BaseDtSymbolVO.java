package com.iMed.iMedPersistence.iMedDentalDTO;

import com.iMed.iMedCore.utility.XPersistent;
import com.iMed.iMedCore.utility.Utility;
import java.util.*;
/**
 * <p>Title: </p>
 * <p>Description: </p>
 * <p>Copyright: Copyright (c) 2551</p>
 * <p>Company: International Medical Software</p>
 * @author Rungsiri Thirawittayanon
 * @version PV
 */

public class BaseDtSymbolVO extends XPersistent
{
  private String fix_dt_symbol_type_id;
  // ใช้สำหรับแสดงข้อมูล
  private String tooth_number;
  private String tooth_surface;
  private String tooth_surface_id;
  private String tooth_quadrant;
  // อ้างอิง FixDtSymbolType.getSymbolPath
  private Hashtable symbol_path;
  // ใช้ตรวจสอบ symbol dx ใน TC
  private String check_date;
  private String check_time;
  // ใช้ดูว่าเป็น Treatment หรือ Diagnosis
  private String fix_dt_teeth_chart_render_type_id;

  public BaseDtSymbolVO()
  {
  }

  public String getFixDtSymbolTypeId()
  {
    return Utility.getStringVO(fix_dt_symbol_type_id);
  }
  public void setFixDtSymbolTypeId(String fix_dt_symbol_type_id)
  {
    this.fix_dt_symbol_type_id = fix_dt_symbol_type_id;
  }
  // ใช้สำหรับแสดงข้อมูล
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
  public String getToothSurfaceId()
  {
    return Utility.getStringVO(tooth_surface_id);
  }
  public void setToothSurfaceId(String tooth_surface_id)
  {
    this.tooth_surface_id = tooth_surface_id;
  }
  public String getToothQuadrant()
  {
    return Utility.getStringVO(tooth_quadrant);
  }
  public void setToothQuadrant(String tooth_quadrant)
  {
    this.tooth_quadrant = tooth_quadrant;
  }
  public Hashtable getSymbolPath()
  {
    return symbol_path;
  }
  public void setSymbolPath(Hashtable symbol_path)
  {
    this.symbol_path = symbol_path;
  }
  // ใช้ตรวจสอบ symbol dx ใน TC
  public String getCheckDate()
  {
    return Utility.getStringVO(check_date);
  }
  public void setCheckDate(String check_date)
  {
    this.check_date = check_date;
  }
  public String getCheckTime()
  {
    return Utility.getStringVO(check_time);
  }
  public void setCheckTime(String check_time)
  {
    this.check_time = check_time;
  }
  // ใช้ดูว่าเป็น Dx หรือ Tx ใน TC
  public String getFixDtTeethChartRenderTypeId() {
    return Utility.getStringVO(fix_dt_teeth_chart_render_type_id);
  }
  public void setFixDtTeethChartRenderTypeId(String fix_dt_teeth_chart_render_type_id) {
    this.fix_dt_teeth_chart_render_type_id = fix_dt_teeth_chart_render_type_id;
  }
}