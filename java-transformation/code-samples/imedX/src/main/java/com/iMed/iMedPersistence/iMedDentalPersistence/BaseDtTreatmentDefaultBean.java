/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.iMed.iMedPersistence.iMedDentalPersistence;

import com.iMed.iMedPersistence.iMedDentalDTO.BaseDtTreatmentDefaultVO;
import javax.ejb.CreateException;
import javax.ejb.EntityBean;
import javax.ejb.EntityContext;

/**
 *
 * @author Tanawit Aeabsakul
 */
abstract public class BaseDtTreatmentDefaultBean implements EntityBean {

    transient EntityContext entityContext;

    public String ejbCreate(String baseDtTreatmentDefaultId) throws CreateException {
        setBaseDtTreatmentDefaultId(baseDtTreatmentDefaultId);
        return null;
    }

    public String ejbCreate(BaseDtTreatmentDefaultVO baseDtTreatmentDefaultVO) throws CreateException {
        setBaseDtTreatmentDefaultId(baseDtTreatmentDefaultVO.getObjectID());
        setBaseDtItemId(baseDtTreatmentDefaultVO.getBaseDtItemId());
        setEmployeeId(baseDtTreatmentDefaultVO.getEmployeeId());
        return null;
    }

    public void ejbPostCreate(String baseDtTreatmentDefaultId) throws CreateException {
    }

    public void ejbPostCreate(BaseDtTreatmentDefaultVO baseDtTreatmentDefaultVO) throws CreateException {
    }

    @Override
    public void ejbRemove() {
    }

    public abstract void setBaseDtTreatmentDefaultId(String baseDtTreatmentDefaultId);

    public abstract void setBaseDtItemId(String baseDtItemId);

    public abstract void setEmployeeId(String employeeId);

    public abstract String getBaseDtTreatmentDefaultId();

    public abstract String getBaseDtItemId();

    public abstract String getEmployeeId();

    @Override
    public void unsetEntityContext() {
        entityContext = null;
    }

    @Override
    public void setEntityContext(EntityContext entityContext) {
        this.entityContext = entityContext;
    }

    @Override
    public void ejbStore() {
    }

    @Override
    public void ejbLoad() {
    }

    @Override
    public void ejbPassivate() {
    }

    @Override
    public void ejbActivate() {
    }

}
