/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.iMed.iMedPersistence.iMedDentalDTO;

import com.iMed.iMedCore.utility.Utility;
import com.iMed.iMedCore.utility.XPersistent;

/**
 *
 * @author Tanawit Aeabsakul
 */
public class BaseDtTreatmentDefaultVO extends XPersistent {

    private String baseDtItemId;
    private String employeeId;

    public BaseDtTreatmentDefaultVO() {
    }

    public String getBaseDtItemId() {
        return Utility.getStringVO(baseDtItemId);
    }

    public void setBaseDtItemId(String baseDtItemId) {
        this.baseDtItemId = baseDtItemId;
    }

    public String getEmployeeId() {
        return Utility.getStringVO(employeeId);
    }

    public void setEmployeeId(String employeeId) {
        this.employeeId = employeeId;
    }

}
