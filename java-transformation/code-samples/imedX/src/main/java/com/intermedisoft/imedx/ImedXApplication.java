package com.intermedisoft.imedx;

import com.intermedisoft.imedx.model.Patient;
import com.intermedisoft.imedx.service.PatientService;
import com.intermedisoft.imedx.service.PatientStatistics;
import com.intermedisoft.imedx.service.impl.PatientServiceImpl;
import com.intermedisoft.imedx.util.DatabaseConnection;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.List;
import java.util.Scanner;
import java.util.logging.Logger;

/**
 * ImedX EHR System Main Application - Legacy Java 8 style
 * This represents the main entry point for the legacy EHR system
 * This would be replaced by Spring Boot's @SpringBootApplication
 */
public class ImedXApplication {

  private static final Logger logger = Logger.getLogger(
    ImedXApplication.class.getName()
  );

  // Manual dependency management - would be replaced by Spring's dependency injection
  private static PatientService patientService;
  private static Scanner scanner;
  private static SimpleDateFormat dateFormat = new SimpleDateFormat(
    "yyyy-MM-dd"
  );

  public static void main(String[] args) {
    logger.info("Starting ImedX EHR System...");

    // Initialize system components - legacy approach
    initializeSystem();

    // Start the application
    runApplication();

    logger.info("ImedX EHR System stopped.");
  }

  /**
   * Initialize system components - Legacy style initialization
   * In Spring Boot, this would be handled by auto-configuration
   */
  private static void initializeSystem() {
    try {
      // Test database connection
      logger.info("Testing database connection...");
      if (!DatabaseConnection.testConnection()) {
        logger.severe("Database connection failed. Exiting...");
        System.exit(1);
      }

      // Initialize database schema
      logger.info("Initializing database schema...");
      if (!DatabaseConnection.initializeDatabase()) {
        logger.warning("Database initialization failed, but continuing...");
      }

      // Initialize services - manual dependency injection
      patientService = new PatientServiceImpl();
      scanner = new Scanner(System.in);

      // Create sample data for demo
      createSampleData();

      logger.info("System initialized successfully");
    } catch (Exception e) {
      logger.severe("System initialization failed: " + e.getMessage());
      System.exit(1);
    }
  }

  /**
   * Create sample EHR data for demonstration
   */
  private static void createSampleData() {
    try {
      logger.info("Creating sample EHR data...");

      // Sample patient 1
      Patient patient1 = new Patient();
      patient1.setFirstName("John");
      patient1.setLastName("Doe");
      patient1.setDateOfBirth(parseDate("1985-06-15"));
      patient1.setGender("M");
      patient1.setPhoneNumber("+1-555-0101");
      patient1.setEmail("john.doe@email.com");
      patient1.setAddress("123 Main St, New York, NY 10001");
      patient1.setNationalId("ID001234567");
      patient1.setBloodType("O+");
      patient1.setAllergies("Penicillin");
      patient1.setEmergencyContact("Jane Doe");
      patient1.setEmergencyContactPhone("+1-555-0102");

      // Sample patient 2
      Patient patient2 = new Patient();
      patient2.setFirstName("Sarah");
      patient2.setLastName("Johnson");
      patient2.setDateOfBirth(parseDate("1990-03-22"));
      patient2.setGender("F");
      patient2.setPhoneNumber("+1-555-0201");
      patient2.setEmail("sarah.johnson@email.com");
      patient2.setAddress("456 Oak Ave, Los Angeles, CA 90210");
      patient2.setNationalId("ID001234568");
      patient2.setBloodType("A-");
      patient2.setAllergies("None known");
      patient2.setEmergencyContact("Mike Johnson");
      patient2.setEmergencyContactPhone("+1-555-0202");

      // Sample patient 3
      Patient patient3 = new Patient();
      patient3.setFirstName("Michael");
      patient3.setLastName("Chen");
      patient3.setDateOfBirth(parseDate("1978-11-08"));
      patient3.setGender("M");
      patient3.setPhoneNumber("+1-555-0301");
      patient3.setEmail("michael.chen@email.com");
      patient3.setAddress("789 Pine St, Chicago, IL 60601");
      patient3.setNationalId("ID001234569");
      patient3.setBloodType("B+");
      patient3.setAllergies("Shellfish, Latex");
      patient3.setEmergencyContact("Lisa Chen");
      patient3.setEmergencyContactPhone("+1-555-0302");

      // Register sample patients
      try {
        patientService.registerPatient(patient1);
        patientService.registerPatient(patient2);
        patientService.registerPatient(patient3);
        logger.info("Sample patients created successfully");
      } catch (Exception e) {
        logger.warning(
          "Some sample patients may already exist: " + e.getMessage()
        );
      }
    } catch (Exception e) {
      logger.warning("Failed to create sample data: " + e.getMessage());
    }
  }

  /**
   * Main application loop - Legacy console interface
   * In modern applications, this would be replaced by REST APIs or web interface
   */
  private static void runApplication() {
    boolean running = true;

    while (running) {
      try {
        displayMenu();
        int choice = getMenuChoice();

        switch (choice) {
          case 1:
            registerNewPatient();
            break;
          case 2:
            findPatientById();
            break;
          case 3:
            searchPatientsByName();
            break;
          case 4:
            listAllActivePatients();
            break;
          case 5:
            displayPatientStatistics();
            break;
          case 6:
            updatePatientInformation();
            break;
          case 7:
            deactivatePatient();
            break;
          case 8:
            displaySystemInfo();
            break;
          case 0:
            running = false;
            break;
          default:
            System.out.println("Invalid choice. Please try again.");
        }

        if (running) {
          System.out.println("\nPress Enter to continue...");
          scanner.nextLine();
        }
      } catch (Exception e) {
        logger.severe("Error in main application loop: " + e.getMessage());
        System.out.println("An error occurred: " + e.getMessage());
      }
    }
  }

  /**
   * Display main menu
   */
  private static void displayMenu() {
    System.out.println("\n" + "=".repeat(50));
    System.out.println("     ImedX EHR System - Main Menu");
    System.out.println("=".repeat(50));
    System.out.println("1. Register New Patient");
    System.out.println("2. Find Patient by ID");
    System.out.println("3. Search Patients by Name");
    System.out.println("4. List All Active Patients");
    System.out.println("5. Display Patient Statistics");
    System.out.println("6. Update Patient Information");
    System.out.println("7. Deactivate Patient");
    System.out.println("8. Display System Information");
    System.out.println("0. Exit");
    System.out.println("=".repeat(50));
    System.out.print("Enter your choice: ");
  }

  /**
   * Get menu choice from user
   */
  private static int getMenuChoice() {
    try {
      String input = scanner.nextLine();
      return Integer.parseInt(input);
    } catch (NumberFormatException e) {
      return -1;
    }
  }

  /**
   * Register new patient - Legacy console interface
   */
  private static void registerNewPatient() {
    System.out.println("\n--- Register New Patient ---");

    try {
      Patient patient = new Patient();

      System.out.print("First Name: ");
      patient.setFirstName(scanner.nextLine());

      System.out.print("Last Name: ");
      patient.setLastName(scanner.nextLine());

      System.out.print("Date of Birth (YYYY-MM-DD): ");
      String dobStr = scanner.nextLine();
      patient.setDateOfBirth(parseDate(dobStr));

      System.out.print("Gender (M/F): ");
      patient.setGender(scanner.nextLine().toUpperCase());

      System.out.print("Phone Number: ");
      patient.setPhoneNumber(scanner.nextLine());

      System.out.print("Email: ");
      patient.setEmail(scanner.nextLine());

      System.out.print("Address: ");
      patient.setAddress(scanner.nextLine());

      System.out.print("National ID: ");
      patient.setNationalId(scanner.nextLine());

      System.out.print("Blood Type: ");
      patient.setBloodType(scanner.nextLine());

      System.out.print("Allergies: ");
      patient.setAllergies(scanner.nextLine());

      System.out.print("Emergency Contact: ");
      patient.setEmergencyContact(scanner.nextLine());

      System.out.print("Emergency Contact Phone: ");
      patient.setEmergencyContactPhone(scanner.nextLine());

      Patient registeredPatient = patientService.registerPatient(patient);
      System.out.println("Patient registered successfully!");
      System.out.println("Patient ID: " + registeredPatient.getPatientId());
      System.out.println("Full Name: " + registeredPatient.getFullName());
    } catch (Exception e) {
      System.out.println("Error registering patient: " + e.getMessage());
    }
  }

  /**
   * Find patient by ID
   */
  private static void findPatientById() {
    System.out.println("\n--- Find Patient by ID ---");

    try {
      System.out.print("Enter Patient ID: ");
      String idStr = scanner.nextLine();
      Long patientId = Long.parseLong(idStr);

      Patient patient = patientService.findPatientById(patientId);

      if (patient != null) {
        displayPatientDetails(patient);
      } else {
        System.out.println("Patient not found with ID: " + patientId);
      }
    } catch (NumberFormatException e) {
      System.out.println("Invalid patient ID format");
    } catch (Exception e) {
      System.out.println("Error finding patient: " + e.getMessage());
    }
  }

  /**
   * Search patients by name
   */
  private static void searchPatientsByName() {
    System.out.println("\n--- Search Patients by Name ---");

    try {
      System.out.print("Enter search term: ");
      String searchTerm = scanner.nextLine();

      List<Patient> patients = patientService.searchPatientsByName(searchTerm);

      if (patients.isEmpty()) {
        System.out.println("No patients found matching: " + searchTerm);
      } else {
        System.out.println("Found " + patients.size() + " patient(s):");
        for (Patient patient : patients) {
          System.out.println(
            "ID: " +
            patient.getPatientId() +
            ", Name: " +
            patient.getFullName() +
            ", DOB: " +
            dateFormat.format(patient.getDateOfBirth()) +
            ", Active: " +
            patient.isActive()
          );
        }
      }
    } catch (Exception e) {
      System.out.println("Error searching patients: " + e.getMessage());
    }
  }

  /**
   * List all active patients
   */
  private static void listAllActivePatients() {
    System.out.println("\n--- All Active Patients ---");

    try {
      List<Patient> patients = patientService.getAllActivePatients();

      if (patients.isEmpty()) {
        System.out.println("No active patients found");
      } else {
        System.out.println("Active Patients (" + patients.size() + "):");
        System.out.println("-".repeat(80));
        System.out.printf(
          "%-5s %-20s %-12s %-10s %-15s%n",
          "ID",
          "Name",
          "DOB",
          "Gender",
          "Phone"
        );
        System.out.println("-".repeat(80));

        for (Patient patient : patients) {
          System.out.printf(
            "%-5d %-20s %-12s %-10s %-15s%n",
            patient.getPatientId(),
            patient.getFullName(),
            dateFormat.format(patient.getDateOfBirth()),
            patient.getGender(),
            patient.getPhoneNumber() != null ? patient.getPhoneNumber() : "N/A"
          );
        }
      }
    } catch (Exception e) {
      System.out.println("Error listing patients: " + e.getMessage());
    }
  }

  /**
   * Display patient statistics
   */
  private static void displayPatientStatistics() {
    System.out.println("\n--- Patient Statistics ---");

    try {
      PatientStatistics stats = patientService.getPatientStatistics();

      System.out.println("Total Patients: " + stats.getTotalPatients());
      System.out.println("Active Patients: " + stats.getActivePatients());
      System.out.println("Inactive Patients: " + stats.getInactivePatients());
      System.out.println("Male Patients: " + stats.getMalePatients());
      System.out.println("Female Patients: " + stats.getFemalePatients());
      System.out.printf("Average Age: %.1f years%n", stats.getAverageAge());
      System.out.println(
        "New Patients This Month: " + stats.getNewPatientsThisMonth()
      );
      System.out.println(
        "New Patients This Year: " + stats.getNewPatientsThisYear()
      );
      System.out.printf(
        "Active Patient Percentage: %.1f%%%n",
        stats.getActivePatientPercentage()
      );
    } catch (Exception e) {
      System.out.println("Error displaying statistics: " + e.getMessage());
    }
  }

  /**
   * Update patient information
   */
  private static void updatePatientInformation() {
    System.out.println("\n--- Update Patient Information ---");

    try {
      System.out.print("Enter Patient ID to update: ");
      String idStr = scanner.nextLine();
      Long patientId = Long.parseLong(idStr);

      Patient patient = patientService.findPatientById(patientId);

      if (patient == null) {
        System.out.println("Patient not found with ID: " + patientId);
        return;
      }

      System.out.println("Current patient information:");
      displayPatientDetails(patient);

      System.out.println(
        "\nEnter new information (press Enter to keep current value):"
      );

      System.out.print("Phone Number [" + patient.getPhoneNumber() + "]: ");
      String phone = scanner.nextLine();
      if (!phone.trim().isEmpty()) {
        patient.setPhoneNumber(phone);
      }

      System.out.print("Email [" + patient.getEmail() + "]: ");
      String email = scanner.nextLine();
      if (!email.trim().isEmpty()) {
        patient.setEmail(email);
      }

      System.out.print("Address [" + patient.getAddress() + "]: ");
      String address = scanner.nextLine();
      if (!address.trim().isEmpty()) {
        patient.setAddress(address);
      }

      Patient updatedPatient = patientService.updatePatient(patient);
      System.out.println("Patient updated successfully!");
      displayPatientDetails(updatedPatient);
    } catch (NumberFormatException e) {
      System.out.println("Invalid patient ID format");
    } catch (Exception e) {
      System.out.println("Error updating patient: " + e.getMessage());
    }
  }

  /**
   * Deactivate patient
   */
  private static void deactivatePatient() {
    System.out.println("\n--- Deactivate Patient ---");

    try {
      System.out.print("Enter Patient ID to deactivate: ");
      String idStr = scanner.nextLine();
      Long patientId = Long.parseLong(idStr);

      Patient patient = patientService.findPatientById(patientId);

      if (patient == null) {
        System.out.println("Patient not found with ID: " + patientId);
        return;
      }

      System.out.println("Patient to deactivate:");
      displayPatientDetails(patient);

      System.out.print(
        "Are you sure you want to deactivate this patient? (y/N): "
      );
      String confirmation = scanner.nextLine();

      if (confirmation.toLowerCase().startsWith("y")) {
        boolean success = patientService.deactivatePatient(patientId);
        if (success) {
          System.out.println("Patient deactivated successfully");
        } else {
          System.out.println("Failed to deactivate patient");
        }
      } else {
        System.out.println("Operation cancelled");
      }
    } catch (NumberFormatException e) {
      System.out.println("Invalid patient ID format");
    } catch (Exception e) {
      System.out.println("Error deactivating patient: " + e.getMessage());
    }
  }

  /**
   * Display system information
   */
  private static void displaySystemInfo() {
    System.out.println("\n--- System Information ---");
    System.out.println("Application: ImedX EHR System");
    System.out.println("Version: 1.0.0-LEGACY");
    System.out.println("Java Version: " + System.getProperty("java.version"));
    System.out.println(
      "Active Database Connections: " +
      DatabaseConnection.getActiveConnectionsCount()
    );
    System.out.println("System Time: " + new Date());
  }

  /**
   * Display patient details
   */
  private static void displayPatientDetails(Patient patient) {
    System.out.println("\n--- Patient Details ---");
    System.out.println("Patient ID: " + patient.getPatientId());
    System.out.println("Name: " + patient.getFullName());
    System.out.println(
      "Date of Birth: " + dateFormat.format(patient.getDateOfBirth())
    );
    System.out.println("Age: " + patient.getAge() + " years");
    System.out.println("Gender: " + patient.getGender());
    System.out.println(
      "Phone: " +
      (patient.getPhoneNumber() != null ? patient.getPhoneNumber() : "N/A")
    );
    System.out.println(
      "Email: " + (patient.getEmail() != null ? patient.getEmail() : "N/A")
    );
    System.out.println(
      "Address: " +
      (patient.getAddress() != null ? patient.getAddress() : "N/A")
    );
    System.out.println(
      "National ID: " +
      (patient.getNationalId() != null ? patient.getNationalId() : "N/A")
    );
    System.out.println(
      "Blood Type: " +
      (patient.getBloodType() != null ? patient.getBloodType() : "N/A")
    );
    System.out.println(
      "Allergies: " +
      (patient.getAllergies() != null ? patient.getAllergies() : "None")
    );
    System.out.println(
      "Emergency Contact: " +
      (
        patient.getEmergencyContact() != null
          ? patient.getEmergencyContact()
          : "N/A"
      )
    );
    System.out.println(
      "Emergency Phone: " +
      (
        patient.getEmergencyContactPhone() != null
          ? patient.getEmergencyContactPhone()
          : "N/A"
      )
    );
    System.out.println(
      "Registration Date: " + dateFormat.format(patient.getRegistrationDate())
    );
    System.out.println("Active: " + (patient.isActive() ? "Yes" : "No"));
  }

  /**
   * Parse date string - Legacy approach
   */
  private static Date parseDate(String dateStr) throws ParseException {
    return dateFormat.parse(dateStr);
  }
}
