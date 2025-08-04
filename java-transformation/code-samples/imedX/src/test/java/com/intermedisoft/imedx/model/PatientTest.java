package com.intermedisoft.imedx.model;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertNotNull;
import static org.junit.Assert.assertTrue;

import java.util.Calendar;
import java.util.Date;
import org.junit.Test;

/**
 * Patient Model Test - Legacy JUnit 4 style
 * This represents the old-style unit testing that would be modernized
 * with JUnit 5, AssertJ, and better test structure in Spring Boot
 */
public class PatientTest {

  @Test
  public void testPatientConstructorWithDefaults() {
    Patient patient = new Patient();

    assertNotNull(
      "Registration date should not be null",
      patient.getRegistrationDate()
    );
    assertTrue("Patient should be active by default", patient.isActive());
  }

  @Test
  public void testPatientConstructorWithEssentialFields() {
    Date dateOfBirth = new Date();
    Patient patient = new Patient("John", "Doe", dateOfBirth, "M");

    assertEquals("First name should match", "John", patient.getFirstName());
    assertEquals("Last name should match", "Doe", patient.getLastName());
    assertEquals(
      "Date of birth should match",
      dateOfBirth,
      patient.getDateOfBirth()
    );
    assertEquals("Gender should match", "M", patient.getGender());
    assertNotNull(
      "Registration date should not be null",
      patient.getRegistrationDate()
    );
    assertTrue("Patient should be active by default", patient.isActive());
  }

  @Test
  public void testGetFullName() {
    Patient patient = new Patient("John", "Doe", new Date(), "M");

    assertEquals(
      "Full name should be concatenated",
      "John Doe",
      patient.getFullName()
    );
  }

  @Test
  public void testGetAge() {
    // Create a patient born 25 years ago
    Calendar cal = Calendar.getInstance();
    cal.add(Calendar.YEAR, -25);
    Date dateOfBirth = cal.getTime();

    Patient patient = new Patient("John", "Doe", dateOfBirth, "M");

    int age = patient.getAge();
    assertTrue("Age should be around 25", age >= 24 && age <= 26); // Allow for date calculations
  }

  @Test
  public void testGetAgeWithNullBirthDate() {
    Patient patient = new Patient();
    patient.setDateOfBirth(null);

    assertEquals("Age should be 0 for null birth date", 0, patient.getAge());
  }

  @Test
  public void testEqualsAndHashCode() {
    Patient patient1 = new Patient("John", "Doe", new Date(), "M");
    patient1.setPatientId(1L);

    Patient patient2 = new Patient("Jane", "Smith", new Date(), "F");
    patient2.setPatientId(1L);

    Patient patient3 = new Patient("John", "Doe", new Date(), "M");
    patient3.setPatientId(2L);

    // Same ID should be equal
    assertTrue(
      "Patients with same ID should be equal",
      patient1.equals(patient2)
    );
    assertEquals(
      "Patients with same ID should have same hash code",
      patient1.hashCode(),
      patient2.hashCode()
    );

    // Different ID should not be equal
    assertFalse(
      "Patients with different ID should not be equal",
      patient1.equals(patient3)
    );
  }

  @Test
  public void testToString() {
    Patient patient = new Patient("John", "Doe", new Date(), "M");
    patient.setPatientId(1L);

    String toString = patient.toString();

    assertTrue(
      "ToString should contain patient ID",
      toString.contains("patientId=1")
    );
    assertTrue(
      "ToString should contain first name",
      toString.contains("firstName='John'")
    );
    assertTrue(
      "ToString should contain last name",
      toString.contains("lastName='Doe'")
    );
    assertTrue(
      "ToString should contain gender",
      toString.contains("gender='M'")
    );
    assertTrue(
      "ToString should contain active status",
      toString.contains("active=true")
    );
  }

  @Test
  public void testSettersAndGetters() {
    Patient patient = new Patient();

    // Test all setters and getters
    patient.setPatientId(123L);
    assertEquals(
      "Patient ID should match",
      Long.valueOf(123L),
      patient.getPatientId()
    );

    patient.setFirstName("John");
    assertEquals("First name should match", "John", patient.getFirstName());

    patient.setLastName("Doe");
    assertEquals("Last name should match", "Doe", patient.getLastName());

    Date dob = new Date();
    patient.setDateOfBirth(dob);
    assertEquals("Date of birth should match", dob, patient.getDateOfBirth());

    patient.setGender("M");
    assertEquals("Gender should match", "M", patient.getGender());

    patient.setPhoneNumber("+1-555-0123");
    assertEquals(
      "Phone number should match",
      "+1-555-0123",
      patient.getPhoneNumber()
    );

    patient.setEmail("john.doe@email.com");
    assertEquals(
      "Email should match",
      "john.doe@email.com",
      patient.getEmail()
    );

    patient.setAddress("123 Main St");
    assertEquals("Address should match", "123 Main St", patient.getAddress());

    patient.setNationalId("ID123456789");
    assertEquals(
      "National ID should match",
      "ID123456789",
      patient.getNationalId()
    );

    Date regDate = new Date();
    patient.setRegistrationDate(regDate);
    assertEquals(
      "Registration date should match",
      regDate,
      patient.getRegistrationDate()
    );

    patient.setEmergencyContact("Jane Doe");
    assertEquals(
      "Emergency contact should match",
      "Jane Doe",
      patient.getEmergencyContact()
    );

    patient.setEmergencyContactPhone("+1-555-0124");
    assertEquals(
      "Emergency contact phone should match",
      "+1-555-0124",
      patient.getEmergencyContactPhone()
    );

    patient.setBloodType("O+");
    assertEquals("Blood type should match", "O+", patient.getBloodType());

    patient.setAllergies("Penicillin");
    assertEquals(
      "Allergies should match",
      "Penicillin",
      patient.getAllergies()
    );

    patient.setActive(false);
    assertFalse("Active status should be false", patient.isActive());
  }
}
