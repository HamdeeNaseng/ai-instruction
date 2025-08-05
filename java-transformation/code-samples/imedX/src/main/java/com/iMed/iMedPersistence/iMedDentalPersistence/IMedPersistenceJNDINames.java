package com.iMed.iMedPersistence.iMedDentalPersistence;

/**
 * <p>Title: </p>
 * <p>Description: </p>
 * <p>Copyright: Copyright (c) 2005</p>
 * <p>Company: </p>
 * @author สราวุธ วังอนานนท์
 * @version 1.0
 */

public class IMedPersistenceJNDINames
{
  // Teeth chart ของผู้ป่วย
  public final static String DT_TEETH_CHART = "java:app/iMedPersistence/DtTeethChart!com.iMed.iMedPersistence.iMedDentalPersistence.DtTeethChartHome";
  // การรักษาทางทันตกรรม (order)
  public final static String DT_TREATMENT = "java:app/iMedPersistence/DtTreatment!com.iMed.iMedPersistence.iMedDentalPersistence.DtTreatmentHome";
  // การวินิจฉัยทางทันตกรรม
  public final static String DT_DIAGNOSIS = "java:app/iMedPersistence/DtDiagnosis!com.iMed.iMedPersistence.iMedDentalPersistence.DtDiagnosisHome";
  // วางแผนการรักษาทางทันตกรรม
  public final static String DT_TREATMENT_PLAN = "java:app/iMedPersistence/DtTreatmentPlan!com.iMed.iMedPersistence.iMedDentalPersistence.DtTreatmentPlanHome";
  // การตรวจรักษาทางทันตกรรม (set up)
  public final static String BASE_DT_ITEM = "java:app/iMedPersistence/BaseDtItem!com.iMed.iMedPersistence.iMedDentalPersistence.BaseDtItemHome";
  // การวินิจฉัยของแทพย์ (set up)
  public final static String BASE_DT_DIAGNOSIS_DEFAULT = "java:app/iMedPersistence/BaseDtDiagnosisDefault!com.iMed.iMedPersistence.iMedDentalPersistence.BaseDtDiagnosisDefaultHome";
  // Precaution ในหน้า Treatment (Today)
  public final static String DT_PRECAUTION = "java:app/iMedPersistence/DtPrecaution!com.iMed.iMedPersistence.iMedDentalPersistence.DtPrecautionHome";
  // TemplateDtTreatmentNote
  public final static String TEMPLATE_DT_TX_NOTE = "java:app/iMedPersistence/TemplateDtTxNote!com.iMed.iMedPersistence.iMedDentalPersistence.TemplateDtTxNoteHome";
  // Favorite treatment item
  public final static String BASE_DT_TREATMENT_DEFAULT = "java:app/iMedPersistence/BaseDtTreatmentDefault!com.iMed.iMedPersistence.iMedDentalPersistence.BaseDtTreatmentDefaultHome";
}
