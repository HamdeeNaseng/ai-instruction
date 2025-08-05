package com.iMed.iMedPersistence.iMedDentalPersistence;

import javax.ejb.*;
import java.util.*;
import com.iMed.iMedPersistence.iMedDentalDTO.TemplateDtTxNoteVO;

public interface TemplateDtTxNoteHome extends javax.ejb.EJBLocalHome
{
  public TemplateDtTxNote create(String templateDtTxNoteId) throws CreateException;
  public TemplateDtTxNote create(TemplateDtTxNoteVO templateDtTxNoteVO) throws CreateException;
  public TemplateDtTxNote findByPrimaryKey(String templateDtTxNoteId) throws FinderException;
}