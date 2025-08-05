/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.iMed.iMedPersistence.iMedDentalPersistence;

import javax.ejb.EJBLocalObject;

/**
 *
 * @author Tanawit Aeabsakul
 */
public interface BaseDtTreatmentDefault extends EJBLocalObject {

    public String getBaseDtTreatmentDefaultId();

    public String getBaseDtItemId();

    public void setBaseDtItemId(String baseDtItemId);

    public String getEmployeeId();

    public void setEmployeeId(String employeeId);
}
