'''
-Add another method in the Course class that prints the head office location:
 Cape Town.
-Create a subclass of the Course class named OOPCourse.
-Create a constructor that initialises the following attributes with default values:

description = “OOP Fundamentals”
trainer = "Mr Anon A. Mouse"

Create a method in the OOPCourse subclass named trainer_details that prints
what the course is about and the name of the trainer by using the description
and trainer attributes.
Create a method in the OOPCourse subclass named show_course_id that prints the ID number of the course: #12345
Create an object of the OOPCourse subclass called course_1 and call following methods 
-contact_details()
-trainer_details()
-show_course_id()
These methods should all print out the correct information to the terminal.
'''

# Parent class


class Course:
    '''
    Class representing a course.

    Attributes:
    name = name of course
    contact websire = website address
    location = where Head Office is situated.

    '''

    # Class attribute for the course name
    name = "Fundamentals of Computer Science"

    # Class attribute for the contact website
    contact_website = "www.hyperiondev.com"

    # Class attribute for head office location
    location = "Cape Town"

    # Method to display contact details
    def contact_details(self):
        '''
        Creating function to display contact details.
        '''
        print("Please contact us by visiting", self.contact_website)

        # Method to show location of head office
    def head_office_loc(self):
        '''
        Function to display location of head office.
        '''
        print("Our head Office is situated in", self.location)

# Sub class


class OOPCourse(Course):
    '''
Subclass created of Course.
Initializing within constructor the following attributes:
- description = information on course offered
- trainer = name of trainer

    '''
    def __init__(self, description="OOP Fundamentals",
                 trainer="Mr. Anon A. Mouse"):
        self.description = description
        self.trainer = trainer

    def trainer_details(self):
        '''
        Display trainer details.

        '''
        print(f"This is a course on {self.description} and is lead by the trainer {self.trainer}.")

    def show_course_id(self, id="12345"):
        '''
        Method created under subclass OOPCourse displaying ID)
        '''
        self.id = id
        print(f"The ID number of the course is {self.id}")

# Create an OOPCourse object


course_1 = OOPCourse()

# Call the methods
course_1.contact_details()     # Inhertied from the course
course_1.trainer_details()     # Defined in OOPCourse
course_1.show_course_id()      # Defind in OOPCourse

# Example usage:
# Create an instance of the Course class
course = Course()

# Call head_office_loc method to display info
course.head_office_loc()
