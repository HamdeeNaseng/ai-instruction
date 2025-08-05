package com.iMed.iMedPersistence.iMedDentalPersistence;

import javax.ejb.*;
import java.util.*;
import com.iMed.iMedPersistence.iMedDentalDTO.DtPrecautionVO;

public interface DtPrecautionHome extends javax.ejb.EJBLocalHome
{
  public DtPrecaution create(String dtPrecautionId) throws CreateException;
  public DtPrecaution create(DtPrecautionVO dtPrecautionVO) throws CreateException;
  public DtPrecaution findByPatientId(String patientId) throws FinderException;
  public Collection findPrecautionByPatientIdAndActiveState(String patientId, String activeState) throws FinderException;
  public DtPrecaution findByPrimaryKey(String dtPrecautionId) throws FinderException;
}