package com.iMed.iMedPersistence.iMedDentalPersistence;

import com.iMed.iMedPersistence.iMedDentalDTO.DtTreatmentPlanVO;
import javax.ejb.*;
import java.util.*;

public interface DtTreatmentPlanHome extends javax.ejb.EJBLocalHome
{
  public DtTreatmentPlan create(String dtTreatmentPlanId) throws CreateException;
  public DtTreatmentPlan create(DtTreatmentPlanVO dtTxPlanVO) throws CreateException;
  public DtTreatmentPlan findByPrimaryKey(String dtTreatmentPlanId) throws FinderException;
}