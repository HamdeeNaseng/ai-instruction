package com.iMed.iMedPersistence.iMedDentalPersistence;

import javax.ejb.*;
import java.util.*;
import com.iMed.iMedPersistence.iMedDentalDTO.BaseDtDiagnosisDefaultVO;

public interface BaseDtDiagnosisDefaultHome extends javax.ejb.EJBLocalHome
{
  public BaseDtDiagnosisDefault create(String baseDtDiagnosisDefaultId) throws CreateException;
  public BaseDtDiagnosisDefault create(BaseDtDiagnosisDefaultVO baseDtDiagnosisDefaultVO) throws CreateException;
  public Collection findByBaseDtDiagnosisId(String baseDtDiagnosisId) throws FinderException;
  public BaseDtDiagnosisDefault findByPrimaryKey(String baseDtDiagnosisDefaultId) throws FinderException;
}