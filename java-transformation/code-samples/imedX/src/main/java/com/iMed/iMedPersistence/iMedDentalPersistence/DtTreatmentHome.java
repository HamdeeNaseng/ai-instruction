package com.iMed.iMedPersistence.iMedDentalPersistence;

import com.iMed.iMedPersistence.iMedDentalDTO.*;
import javax.ejb.*;
import java.util.*;

public interface DtTreatmentHome extends javax.ejb.EJBLocalHome
{
  public DtTreatment create(String dtTreatmentId) throws CreateException;
  public DtTreatment create(DtTreatmentVO dtTreatmentVO) throws CreateException;
  public Collection findByOrderItemId(String orderItemId) throws FinderException;
  public Collection findByCourseTreatmentId(String patientId, String courseTreatmentId) throws FinderException;
  public DtTreatment findByPrimaryKey(String dtTreatmentId) throws FinderException;
}