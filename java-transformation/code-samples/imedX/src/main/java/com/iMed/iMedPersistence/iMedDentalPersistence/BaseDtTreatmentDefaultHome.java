/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.iMed.iMedPersistence.iMedDentalPersistence;

import com.iMed.iMedPersistence.iMedDentalDTO.BaseDtTreatmentDefaultVO;
import javax.ejb.CreateException;
import javax.ejb.EJBLocalHome;
import javax.ejb.FinderException;

/**
 *
 * @author Tanawit Aeabsakul
 */
public interface BaseDtTreatmentDefaultHome extends EJBLocalHome {

    public BaseDtTreatmentDefault create(String baseDtTreatmentDefaultId) throws CreateException;

    public BaseDtTreatmentDefault create(BaseDtTreatmentDefaultVO baseDtTreatmentDefaultVO) throws CreateException;

    public BaseDtTreatmentDefault findByPrimaryKey(String baseDtTreatmentDefaultId) throws FinderException;
}
