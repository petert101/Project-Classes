#Author: Peter Truong
#Version: 1.2
#Project: Classes

#Library used to convert text files into dataframes
import pandas as pd

#Initialized values
main_menu = -1
doctor_menu = -1
facility_menu = -1
lab_menu = -1
patient_menu = -1

### Classes ###
class Doctor:
    """A class used to create Doctor object
        Attributes:
            ID(int): integer that represents the doctor id
            Name(str): string that represents doctor name
            Specialization(str): string that represents doctor specialization
            Working Time(str): string that represents the working time
            Qualification(str):string that represents qualification
            Room Number(int): integer that represents the room number
    """

    #constructor     
    def __init__(self, ID, Name, Specialization, Working_Time, Qualification, Room_Number):
        self.__ID = ID
        self.__Name = Name
        self.Specialization = Specialization
        self.Working_Time = Working_Time
        self.Qualification = Qualification
        self.Room_Number = Room_Number

#Getters
    def get_id(self):
        return self.__ID
    def get_name(self):
        return self.__Name
    def get_specialization(self):
        return self.Specialization
    def get_working_time(self):
        return self.Working_Time
    def get_qualification(self):
        return self.Qualification
    def get_room_Number(self):
        return self.Room_Number

    #Setters
    def set_id(self, ID):
        self.__ID = ID
    def set_name(self, Name):
        self.__Name = Name
    def set_specialization(self, Specialization):
        self.Specialization = Specialization
    def set_working_time(self, Working_Time):
        self.Working_Time = Working_Time
    def set_qualification(self, Qualification):
        self.Qualification = Qualification
    def set_room_Number(self, Room_Number):
        self.Room_Number = Room_Number
    
    #Doctor table info
    global df_doctor, df_doctor2
    df_doctor = pd.read_csv("doctors.txt", sep = "_", header = 0)
    df_doctor = df_doctor.rename(columns = {
        'id': 'Id', 'name': 'Name', 'specilist': 'Speciality', 
        'timing': 'Timing', 'qualification': 'Qualification', 'roomNB': 'Room Number'
    })
    df_doctor2 = df_doctor.to_string(index=False) #Show without index

    ### Methods ###
    #Format doctor info with _ separator
    def FormatDrInfo(self):
        global add_doctor
        add_doctor = '_'.join(doctor_info) 

    #input and write doctor info into text file
    def enterDrInfo():
        global doctor_info
        doctor_info = []
        doctor_id = input("Enter doctorâ€™s ID:\n\n")
        doctor_name = input("Enter doctorâ€™s name:\n\n")
        doctor_specialization = input("Enter doctorâ€™s specility:\n\n")
        doctor_working_time = input("Enter doctorâ€™s timing (e.g., 7am-10pm):\n\n")
        doctor_qualification = input("Enter doctorâ€™s qualification:\n\n")
        doctor_room_number = input("Enter doctorâ€™s room number:\n\n")

        #put inputs into a list and add _ as a separator using the format function
        doctor_info.append(doctor_id)
        doctor_info.append(doctor_name)
        doctor_info.append(doctor_specialization)
        doctor_info.append(doctor_working_time)
        doctor_info.append(doctor_qualification)
        doctor_info.append(doctor_room_number)
        Doctor.FormatDrInfo(doctor_info) 
        
        #add list to the text file 
        with open("doctors.txt", "a") as doctor_file:
            doctor_file.write("\n")
            doctor_file.write(add_doctor)

    #Read doctor file and store doctor objects into a list
    def readDoctorsFile():
        with open("doctors.txt", "r") as doctor_file:
                global doctor_list
                doctor_list = doctor_file.readlines()[1:] #Ignores column titles and reads from 2nd line
    
    #Search doctor info based on ID
    def searchDoctorById():
        input_id = int(input("Enter the doctor Id:\n\n"))
        if input_id in df_doctor["Id"].values:
            print(df_doctor[df_doctor['Id'] == input_id])
        else:
            print("Can't find the doctor with the same ID on the system\n")

    #Search doctor info based on name
    def searchDoctorByName():
        input_name = input("Enter the doctor name:\n\n")
        if input_name in df_doctor["Name"].values:
            print(df_doctor[df_doctor["Name"] == input_name])
        else:
            print("Can't find the doctor with the same name on the system\n")
    
    #Display doctor info as a list
    def displayDoctorInfo():
        print(doctor_list)
    
    #Edit doctor info
    def editDoctorInfo():
        global edit_doctor
        edit_doctor = []
        input_id = int(input("Please enter the id of the doctor that you want "
            "to edit their information:\n\n"))
        new_name = input("\nEnter new Name:\n\n")
        new_spec = input("\nEnter new Specilist in:\n\n")
        new_time = input("\nEnter new Timing:\n\n")
        new_qual = input("\nEnter new Qualification:\n\n")
        new_room = int(input("\nEnter new Room number:\n\n"))
        
        #Store edit inputs into list
        edit_doctor.append(input_id)
        edit_doctor.append(new_name)
        edit_doctor.append(new_spec)
        edit_doctor.append(new_time)
        edit_doctor.append(new_qual)
        edit_doctor.append(new_room)
        
        #Replace row with list
        df_doctor[df_doctor['Id'] == input_id] = edit_doctor

    #Print all doctors' info
    def displayDoctorsList():
        print(df_doctor2)

class Facility:
    """A class used to create Facility object
        Attribute(s):
            Facility name(str): string that represents the facility name
    """

    #Constructor
    def __init__(self, Facility_name):
        self.Facility_name = Facility_name
        
    #Getter(s)
    def get_Facility_name(self):
        return self.Facility_name

    #Setter(s)
    def set_Facility_name(self, Facility_name):
        self.Facility_name = Facility_name

    global facility_list
    facility_list = []

    #Methods
    #Add and write facility name to file
    def addFacility():
        global add_facility
        add_facility = (input("Enter the name of the facility: \n\n"))
        Facility.writeListOffacilitiesToFile()
        
    #Displays the list of facilities
    def displayFacilities():
        with open("facilities.txt", "r") as f:
            print(f.read())
        
    #Write the facilities list to a facilities.txt
    def writeListOffacilitiesToFile():
        with open("facilities.txt", "a") as facility_file:
            facility_file.write("\n")
            facility_file.write(add_facility)

class Laboratory:
    """A class used to create Laboratory object
        Attribute(s):
            Lab name(str): string that represents the Lab name
            cost(int):integer that represents cost of lab
    """

    #constructor     
    def __init__(self, Laboratory_name, cost):
        self.Laboratory_name = Laboratory_name
        self.cost = cost 
    
    #Setters
    def get_Lab_name(self):
        return self.__Lab_name
    def get_cost(self):
        return self.__cost  
    
    #Getters
    def set_Lab_name(self, Lab_name):
        self.__Lab_name = Lab_name
    def set_cost(self, cost):
        self.__cost = cost

    #Doctor table info
    global df_lab, df_lab2
    df_lab = pd.read_csv("laboratories.txt", sep = "_", header = 0)
    df_lab2 = df_lab.to_string(index=False) #Show without index

    #Methods
    #Adds and writes lab name to the file with _ separator
    def addLabToFile(self):
        #add list to text file 
        with open("laboratories.txt", "a") as lab_file:
            lab_file.write("\n")
            lab_file.write(add_lab)
        
    #Write list of labs to laboratories.txt
    def writeListOfLabsToFile():
        with open('laboratoriess.txt', 'w') as write_file:
            write_file.writelines(lab_list)

    #Display list of labs
    def displayLabsList():
        print(df_lab2)
        
    #Format lab list with _ separator
    def formatLabInfo(self):
        global add_lab
        add_lab = '_'.join(lab_info) 
        
    #Enter lab info
    def enterLaboratoryInfo():
        global lab_info
        lab_info = []
        lab_name = input("Enter Laboratory facility:\n\n")
        lab_cost = input("Enter Laboratory cost:\n\n")

        #put inputs into a list and add _ as a separator using the format function
        lab_info.append(lab_name)
        lab_info.append(lab_cost)
        Laboratory.formatLabInfo(lab_info) 
        
        #Add list to lab file
        Laboratory.addLabToFile(add_lab)
    
    #Read lab file and store lab objects into a list
    def readLaboratoriesFile():
        with open("laboratories.txt", "r") as lab_file: 
            global lab_list
            lab_list = lab_file.readlines()[1:] #Ignores column titles and read from 2nd line

class Patient:
    """A class used to create Patient object
        Attribute(s):
            pid(int): integer that represents patient id
            name(str):string that represents name of patient
            disease(str): string that represents name of disease
            gender(str): string that represents gender of patient
            age(int): integer that represents age of patient
    """

    #Constructor
    def __init__(self, pid, name, disease, gender, age):
        self.pid = pid
        self.name = name
        self.disease = disease
        self.gender = gender
        self.age = age

    #Getters
    def get_pid(self):
        return self.__pid
    def get_name(self):
        return self.__name
    def get_disease(self):
        return self.__disease 
    def get_gender(self):
        return self.__gender  
    def get_age(self):
        return self.__age

    #Setters
    def set_pid(self, pid):
        self.__pid = pid
    def set_cost(self, name):
        self.__name = name
    def set_Lab_name(self, disease):
        self.__disease = disease
    def set_gender(self, gender):
        self.__gender = gender
    def set_age(self, age):
        self.__age = age

    #Patients table info
    global df_patient, df_patient2
    df_patient = pd.read_csv("patients.txt", sep = "_", header = 0)
    df_patient2 = df_patient.to_string(index=False) #Show without index

    #Methods
    #Format lab list with _ separator
    def formatPatientInfo(self):
        global add_patient
        add_patient = '_'.join(patient_info) 

    def enterPatientInfo():
        global patient_info
        patient_info = []
        patient_id = input("Enter Patient id:\n\n")
        patient_name = input("Enter Patient name:\n\n")
        patient_disease = input("Enter Patient disease:\n\n")
        patient_gender = input("Enter Patient gender:\n\n")
        patient_age = input("Enter Patient age:\n\n")

        #put inputs into a list and add _ as a separator using the format function
        patient_info.append(patient_id)
        patient_info.append(patient_name)
        patient_info.append(patient_disease)
        patient_info.append(patient_gender)
        patient_info.append(patient_age)
        Patient.formatPatientInfo(patient_info) 
        
        #Add list to lab file
        Patient.addPatientToFile(add_patient)

    #Read patient file and store patient objects into a list
    def readPatientFile():
        with open("patients.txt", "r") as patient_file: 
            global patient_list
            patient_list = patient_file.readlines()[1:] #Ignores column titles and read from 2nd line

    #Search patient info based on ID 
    def searchPatientById():
        input_id = int(input("Enter the patient Id:\n\n"))
        if input_id in df_patient["id"].values:
            print(df_patient[df_patient['id'] == input_id])
        else:
            print("Can't find the patient with the same ID on the system\n")
    
    #Display patients' info
    def displayPatientInfo():
        print(patient_list)
    
    #Edit patient info
    def editPatientInfo():
        global edit_patient
        edit_patient = []
        input_id = int(input("Please enter the id of the Patient that you want "
            "to edit their information:\n\n"))
        new_name = input("\nEnter new Name:\n\n")
        new_disease = input("\nEnter new disease in:\n\n")
        new_gender = input("\nEnter new gender:\n\n")
        new_age = input("\nEnter new age:\n\n")

        #Store edit inputs into list
        edit_patient.append(input_id)
        edit_patient.append(new_name)
        edit_patient.append(new_disease)
        edit_patient.append(new_gender)
        edit_patient.append(new_age)

        #Replace row with list
        df_patient[df_patient['id'] == input_id] = edit_patient  

    def displayPatientsList():
        print(df_patient2)
    
    #Write list of labs to patients.txt
    def writeListOfPatientsToFile():
        with open('patients.txt', 'w') as write_file:
            write_file.writelines(patient_list)

    #Adds and writes patient name to the file with _ separator
    def addPatientToFile(self):
        #add list to text file 
        with open("patients.txt", "a") as patient_file:
            patient_file.write("\n")
            patient_file.write(add_patient)
    
class Management:
    """ A class used to create the Managment object
    Purpose of this class is to display the different menus
        - main menu         - doctor menu       - facility menu
        - laboratory menu   - patient menu      
    """

    def StartMessage(self):
        msg = print("Welcome to Alberta Hospital (AH) Managment system")
    def DisplayMenu(self):
        global main_menu
        while main_menu != 0:
            main_menu = int(input("Select from the following options, or select 0 to stop:\n"
                "1 - 	Doctors\n"
                "2 - 	Facilities\n"
                "3 - 	Laboratories\n"
                "4 - 	Patients \n\n"))
            if main_menu == 1:
                Management.DoctorMenu()
            elif main_menu == 2:
                Management.FacilityMenu()
            elif main_menu == 3:
                Management.LaboratoryMenu()
            elif main_menu == 4:
                Management.PatientMenu()
    
    def DoctorMenu():
        global doctor_menu
        while doctor_menu != 6:
            doctor_menu = int(input("Doctors Menu:\n"
                "1 - Display Doctors list\n"
                "2 - Search for doctor by ID\n"
                "3 - Search for doctor by name\n"
                "4 - Add doctor\n"
                "5 - Edit doctor info\n"
                "6 - Back to the Main Menu\n\n"))
            
            #Display doctor list
            if doctor_menu == 1:
                Doctor.displayDoctorsList()
            
            #Search for doctor by ID
            elif doctor_menu == 2:
                Doctor.searchDoctorById()
            
            #Search for doctor by name
            elif doctor_menu == 3:
                Doctor.searchDoctorByName()

            #Add doctor 
            elif doctor_menu == 4:
                Doctor.enterDrInfo()
            
            #Edit doctor info
            elif doctor_menu == 5:
                Doctor.editDoctorInfo()
                pass  
            print("\nBack to the prevoius Menu")

    def FacilityMenu():
        global facility_menu
        while facility_menu != 3:
            facility_menu = int(input("Facilities Menu:\n"
                "1 - Display Facilities list\n"
                "2 - Add Facility\n"
                "3 - Back to the Main Menu\n\n"))

            #Display facilities list
            if facility_menu == 1:
                Facility.displayFacilities()
            
            #Add facility to list
            elif facility_menu == 2:
                Facility.addFacility()
            print("\nBack to the prevoius Menu")
    
    def LaboratoryMenu():
        global lab_menu
        while lab_menu != 3:
            lab_menu = int(input("Laboratories Menu:\n"
                "1 - Display laboratories list\n"
                "2 - Add laboratory\n"
                "3 - Back to the Main Menu\n\n"))
            
            #Display lab list
            if lab_menu == 1:
                Laboratory.displayLabsList()

            #Add lab to list
            elif lab_menu == 2:
                Laboratory.enterLaboratoryInfo()
            print("\nBack to the prevoius Menu")
    
    def PatientMenu():
        global patient_menu
        while patient_menu != 5:
            patient_menu = int(input("Patients Menu:\n"
                "1 - Display patients list\n"
                "2 - Search for patient by ID\n"
                "3 - Add patient\n"
                "4 - Edit patient info\n"
                "5 - Back to the Main Menu\n\n"))
            
            #Display patient list
            if patient_menu == 1:
                Patient.displayPatientsList()

            #Search for patient by ID
            elif patient_menu == 2:
                Patient.searchPatientById()

            #Add patient
            if patient_menu == 3:
                Patient.enterPatientInfo()

            #Edit patient info
            if patient_menu == 4:
                Patient.editPatientInfo()
            print("\nBack to the prevoius Menu")

#Reference Management class to use functions
start = Management()

#Start program
start.StartMessage()
start.DisplayMenu()