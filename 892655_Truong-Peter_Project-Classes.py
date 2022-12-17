#Author: Peter Truong
#Version: 1.1
#Project: Classes

#Library used to convert text files into dataframes
import pandas as pd

#df used for reference
df = pd.read_csv("doctors.txt", sep = "_", header = 0)
df = df.rename(columns = {
    'id': 'Id', 'name': 'Name', 'specilist': 'Speciality', 
    'timing': 'Timing', 'qualification': 'Qualification', 'roomNB': 'Room Number'
})

df_facilities = pd.read_csv("facilities.txt", header = 0)

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
        self.ID = ID
        self.Name = Name
        self.Specialization = Specialization
        self.Working_Time = Working_Time
        self.Qualification = Qualification
        self.Room_Number = Room_Number
    
    #format Dr info
    def formatDrInfo(self):
        format_info = f"{self.ID}_{self.Name}_{self.Specialization}_{self.Working_Time}_{self.Qualification}_{self.Room_Number}"
        return format_info

    #input doctor info
    def enterDrInfo(self):
        add_info = []
        self.ID = input("Enter doctorâ€™s ID:\n\n")
        self.Name = input("Enter doctorâ€™s name:\n\n")
        self.Specialization = input("Enter doctorâ€™s specility:\n\n")
        self.Working_Time = input("Enter doctorâ€™s timing (e.g., 7am-10pm):\n\n")
        self.Qualification = input("Enter doctorâ€™s qualification:\n\n")
        self.Room_Number = input("Enter doctorâ€™s room number:\n\n")

        #Add user input into a list
        add_info.append(self.ID, self.Name, self.Specialization,
            self.Working_Time, self.Qualification, self.Room_Number)
        
        #Append list to dataframe
        df = df.append(add_info)
        

    #reads "doctors.txt" file and fills input into a list
    def readDoctorFile(self):

        #Convert text file into dataframe
        df = pd.read_csv("doctors.txt", sep = "_", header = 0)
        df = df.rename(columns = {
            'id': 'Id', 'name': 'Name', 'specilist': 'Speciality', 
            'timing': 'Timing', 'qualification': 'Qualification', 'roomNB': 'Room Number'
        })

        #Store columns values into attributes
        self.ID = df['Id']
        self.Name = df['Name']
        self.Specialization = df['Speciality']
        self.Working_Time = df['Timing']
        self.Qualification = df['Qualification']
        self.Room_Number = df['Room Number']
    
    #Print doctor info based on ID
    def searchDoctorById(self):
        input_id = int(input("Enter the doctor Id:\n\n"))
        if input_id in df["Id"].values:
            print(df[df['Id'] == input_id])
        else:
            print("File does not have that ID.")
    
    #Print doctor info based on name
    def searchDoctorByName(self):
        input_name = int(input("Enter the doctor name:\n\n"))
        if id in df["Name"].values:
            print(df[df['Name'] == input_name])
        else:
            print("File does not have that name.")
    
    #Display doctor info based on option chosen in Doctors menu
    def displayDoctorInfo(self):
        if doctor_menu == 1:
            Doctor.displayDoctorsList()
        elif doctor_menu == 2:
            Doctor.searchDoctorById()
        elif doctor_menu == 3:
            Doctor.searchDoctorByName()

    #Edit doctor info
    def editDoctorInfo(self):
        edit_info = []
        input_id = int(input("Please enter the id of the doctor that you want "
            "to edit their information:\n\n"))
        new_name = input("\nEnter new Name:\n\n")
        new_spec = input("\nEnter new Specilist in:\n\n")
        new_time = input("\nEnter new Timing:\n\n")
        new_qual = input("\nEnter new Qualification:\n\n")
        new_room = int(input("\nEnter new Room number:\n\n"))
        
        #Store edit inputs into list
        edit_info.append(input_id, new_name, new_spec,
            new_time, new_qual, new_room)
        
        #Replace row with list
        df[df['Id'] == input_id] = edit_info
    
    #Display all doctors' info
    def displayDoctorsList(self):
        df2 = df.to_string(index=False) #Show without index
        return df2

class Facility:
    """A class used to create Facility object
        Attribute(s):
            Facility name(str): string that represents the facility name
    """
    #constructor     
    def __init__(self, Facility_name):
        self.Facility_name = Facility_name
    
    #Adds and write faility name to file
    def addFacility(self):
        input_add = input("Enter Facility name:\n\n")
        with open("facilities.txt", "w") as x:
            x.write(f'{input_add}\n')
    
    #Displays the list of facilities
    def displayFacilities(self):
        df_facilities = pd.read_csv("facilities.txt", header = 0)
        df2 = df_facilities.to_string(index=False) #Show without index
        return df2

    #Writes the facilities list to facilities.txt
    def writeListOffacilitiesToFile():
        df_facilities.to_csv('facilities.txt', sep='\t', index=False)

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
    
    def addLabToFile(self):
        pass

    def writeListOfLabsToFile(self):
        pass

    def displayLabsList(self):
        pass

    def formatDrInfo(self):
        pass

    def enterLaboratoryInfo(self):
        pass
    def readLaboratoriesFile(self):
        pass


class Patient:
    """A class used to create Patient object
        Attribute(s):
            pid(int): integer that represents patient id
            name(str):string that represents name of patient
            disease(str): string that represents name of disease
            gender(str): string that represents gender of patient
            age(int): integer that represents age of patient
    """

    #constructor     
    def __init__(self, pid, name, disease, gender, age):
        self.pid = pid
        self.name = name 
        self.disease = disease 
        self.gender = gender 
        self.age = age 
    
    def formatPatientInfo(self):
        pass
    def enterPatientInfo(self):
        pass
    def readPatientFile(self):
        pass
    def searchPatientById(self):
        pass
    def displayPatientInfo(self):
        pass
    def editPatientInfo(self):
        pass
    def displayPatientsList(self):
        pass
    def writeListOfPatientsToFile(self):
        pass
    def addPatientToFile(self):
        pass

class Management:
    """A class used to create Patient object
        Function: DisplayMenu Repeat program until user enters 0
    """
    def DisplayMenu():
        x = input("Enter i")
        main_menu = int(input("Select from the following options, or select 0 to stop:\n"
        "1 - 	Doctors\n"
        "2 - 	Facilities\n"
        "3 - 	Laboratories\n"
        "4 - 	Patients \n\n"))

#Start
while main_menu != 0:
    msg = print("Welcome to Alberta Hospital (AH) Managment system")
    main_menu = int(input("Select from the following options, or select 0 to stop:\n"
    "1 - 	Doctors\n"
    "2 - 	Facilities\n"
    "3 - 	Laboratories\n"
    "4 - 	Patients \n\n"))

    if main_menu == 1:
        while doctor_menu != 6:
            doctor_menu = int(input("Doctors Menu:\n"
                "1 - Display Doctors list\n"
                "2 - Search for doctor by ID\n"
                "3 - Search for doctor by name\n"
                "4 - Add doctor\n"
                "5 - Edit doctor info\n"
                "6 - Back to the Main Menu\n\n"))

            if doctor_menu == 1 :
                Doctor.displayDoctorsList()
            elif doctor_menu == 2:
                Doctor.searchDoctorById()
            elif doctor_menu == 3:
                Doctor.searchDoctorByName()
            elif doctor_menu == 4:
                Doctor.enterDrInfo
            elif doctor_menu == 5:
                Doctor.editDoctorInfo()
            elif doctor_menu == 6:
                pass
            print("\nBack to the prevoius Menu")
        
    if main_menu == 2:
        while facility_menu != 3:
            if facility_menu == 1:
                Facility.displayFacilities()
            elif facility_menu == 2:
                Facility.addFacility
            elif facility_menu == 3:
                pass
            print("\nBack to the prevoius Menu")

    if main_menu == 3:
        while lab_menu != 3:
            if lab_menu == 1:
                Laboratory.displayLabsList()
            elif lab_menu == 2:
                Laboratory.addLabToFile()
            elif lab_menu == 3:
                pass
            print("\nBack to the prevoius Menu")

    if main_menu == 4:
        while patient_menu != 5:
            if patient_menu == 1:
                Patient.displayPatientInfo()
            elif patient_menu == 2:
                Patient.searchPatientById()
            elif patient_menu == 3:
                Patient.addPatientToFile()
            elif patient_menu == 4:
                Patient.editPatientInfo()
            elif patient_menu == 5:
                pass
            print("\nBack to the prevoius Menu")
        pass
    elif main_menu == 0:
        break