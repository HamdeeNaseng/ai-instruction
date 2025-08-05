package com.iMed.iMedPersistence.iMedDentalPersistence;

import com.iMed.iMedPersistence.iMedDentalDTO.*;
import javax.ejb.*;
import java.util.*;

public interface DtDiagnosisHome extends javax.ejb.EJBLocalHome
{
  public DtDiagnosis create(String dtDiagnosisId) throws CreateException;
  public DtDiagnosis create(DtDiagnosisVO dtDiagnosisVO) throws CreateException;
  public Collection findByVitalSignExtendId(String vsExtendId) throws FinderException;
  public Collection findByVisitId(String visitId) throws FinderException;
  public DtDiagnosis findByPrimaryKey(String dtDiagnosisId) throws FinderException;
}