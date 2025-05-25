#Dictionary Course Program
#Brianna Zaffina
#12/11/2023

MY_NAME = "Brianna Zaffina"

def main():
    print("Dictionary Course Program -", MY_NAME)
    print()

    #dictionaries:
    rooms = {'CS101':3004, 'CS102':4501, 'CS103':6755, 'NT110':1244, 'CM241':1411}
    instructors = {'CS101':"Haynes", 'CS102':"Alvarado", 'CS103':"Rich", 'NT110':"Burke", 'CM241':"Lee"}
    times = {'CS101':"8:00 a.m.", 'CS102':"9:00 a.m.", 'CS103':"10:00 a.m.", 'NT110':"11:00 a.m.", 'CM241':"1:00 p.m."}

    #prompting user:
    course_num = input("Enter the course number: ")
    course_num = course_num.upper();
    print()

    #if else statement:
    if course_num in rooms:
        print("The course information for course #", course_num, "is as follows:")
        room_num = rooms[course_num]
        print("Room #:", room_num)
        instructor = instructors[course_num]
        print("Instructor:", instructor)
        time = times[course_num]
        print("Time:", time)
        print()

    else:
        print("Course not found.")
        print()
    
    print("Program terminated normally.")
              
main()
