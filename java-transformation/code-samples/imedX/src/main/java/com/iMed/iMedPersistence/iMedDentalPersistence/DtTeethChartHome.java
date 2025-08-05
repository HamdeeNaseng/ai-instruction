package com.iMed.iMedPersistence.iMedDentalPersistence;

import javax.ejb.*;
import java.util.*;
import com.iMed.iMedPersistence.iMedDentalDTO.*;

public interface DtTeethChartHome extends javax.ejb.EJBLocalHome
{
  public DtTeethChart create(String dtTeethChartId) throws CreateException;
  public DtTeethChart create(TeethChartVO teethChartVO) throws CreateException;
  public DtTeethChart findByPrimaryKey(String dtTeethChartId) throws FinderException;
}