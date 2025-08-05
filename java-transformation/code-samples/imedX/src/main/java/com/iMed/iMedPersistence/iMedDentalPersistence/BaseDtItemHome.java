package com.iMed.iMedPersistence.iMedDentalPersistence;

import javax.ejb.*;
import java.util.*;
import com.iMed.iMedPersistence.iMedDentalDTO.BaseDtItemVO;

public interface BaseDtItemHome extends javax.ejb.EJBLocalHome {
  public BaseDtItem create(String baseDtItemId, String baseDtSymbolId, String fixDtActionTypeId, String isTreatment, String itemId) throws CreateException;
  public BaseDtItem create(BaseDtItemVO baseDtItemVO) throws CreateException;
  public Collection findByItemId(String itemId) throws FinderException;
  public BaseDtItem findByPrimaryKey(String baseDtItemId) throws FinderException;
}