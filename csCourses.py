from constraintSatisfaction import *
# a list of courses that a computer science major has to take.
# Features
# prerequisite courses
# Domain: the semesters you can take that class
courses = { 'CSCI 125': [3, [''], [1, 2]],
                'CSCI 155': [3, [''], [2, 3, 4, 5, 6, 7, 8]],
                'CSCI 185': [3, ['CSCI 125'], [3]],
                'CSCI 235': [3, ['MATH 170', 'CSCI 185'], [3, 4, 5, 6, 7, 8]],
                'CSCI 260': [3, ['MATH 170', 'CSCI 185'], [4]],
                'CSCI 270': [3, ['CSCI 235', 'MATH 180'], [5, 6, 7, 8]],
                'CSCI 312': [3, ['CSCI 235'], [5, 6, 7]],
                'CSCI 318': [3, ['CSCI 260'], [5, 6, 7]],
                'CSCI 330': [3, ['CSCI 260', 'CSCI 185'], [4, 5]],
                'CSCI 335': [3, ['CSCI 260'], [6, 7, 8]],
                'CSCI 345': [3, ['CSCI 330'], [6, 7, 8]],
                'CSCI 380': [3, ['CSCI 260'], [6, 7, 8]],
                'CSCI 455': [3, [''], [7, 8]],
                'MATH 170': [4, [''], [1]],
                'MATH 180': [4, ['MATH 170'], [2, 3]],
                'MATH 310': [3, ['MATH 180'], [3, 4, 5, 6, 7, 8]],
                'FCWR 101': [3, [''], [1, 2]],
                'FCWR 151': [3, ['FCWR 101'], [1, 2, 3, 4]],
                'FCSP 105': [3, [''], [1, 2, 3, 4]],
                'FCSC 101': [3, [''], [1, 2, 3, 4]],
                'FCIQ 101': [3, [''], [1, 2]],
                'Career Discovery': [2, [''], [1]],
                'ETCS 108': [3, [''], [1, 2, 3, 4, 5, 6, 7, 8]],
                'FCWR 304': [3, ['FCIQ 101', 'FCSP 105', 'FCSC 101', 'FCWR 151'], [3, 4, 5, 6, 7, 8]],
                'Natural Science I': [4, [''], [1]],
                'Natural Science I - Lab': [0, [''], [1]],
                'Natural Science II - Lab': [0, [''], [2]],
                'Natural Science II': [4, ['Natural Science I'], [2]],
                'Natural Science Elective': [3, [''], [3, 4, 5, 6, 7, 8]],
                'Math/Science Elective I': [3, [''], [3, 4, 5, 6, 7, 8]],
                'Math/Science Elective II': [3, [''], [3, 4, 5, 6, 7, 8]],
                'Literature': [3, ['FCIQ 101', 'FCSP 105', 'FCSC 101', 'FCWR 151'], [5, 6, 7, 8]],
                'Behavioral Science': [3, ['FCIQ 101', 'FCSP 105', 'FCSC 101', 'FCWR 151'], [5, 6, 7, 8]],
                'Philosophy': [3, ['FCIQ 101', 'FCSP 105', 'FCSC 101', 'FCWR 151'], [5, 6, 7, 8]],
                'ICSS 309': [3, ['FCIQ 101', 'FCSP 105', 'FCSC 101', 'FCWR 151'], [7, 8]],
                'CS Elective I': [3, [''], [2, 3, 4, 5, 6, 7, 8]],
                'CS Elective II': [3, [''], [2, 3, 4, 5, 6, 7, 8]],
                'CS Elective III': [3, [''], [2, 3, 4, 5, 6, 7, 8]],
                'CS Elective IV': [3, [''], [2, 3, 4, 5, 6, 7, 8]],
                'CS Elective V': [3, [''], [2, 3, 4, 5, 6, 7, 8]],
                'CS Elective VI': [3, [''], [2, 3, 4, 5, 6, 7, 8]],
                'General Elective': [3, [''], [2, 3, 4, 5, 6, 7, 8]]
               }

class CSPGraphCourses(CSPGraph):
    def __init__(self):
        # call parent constructor
        CSPGraph.__init__(self)

    def objectiveFunction(self):
        value = CSPGraph.objectiveFunction(self)
        credit_value = 0
        s1_credit = 0
        s2_credit = 0
        s3_credit = 0
        s4_credit = 0
        s5_credit = 0
        s6_credit = 0
        s7_credit = 0
        s8_credit = 0
        for feature in self.features:
            if feature.value == 1:
                s1_credit += courses[feature.name][0]

            elif feature.value == 2:
                s2_credit += courses[feature.name][0]

            elif feature.value == 3:
                s3_credit += courses[feature.name][0]

            elif feature.value == 4:
                s4_credit += courses[feature.name][0]

            elif feature.value == 5:
                s5_credit += courses[feature.name][0]

            elif feature.value == 6:
                s6_credit += courses[feature.name][0]

            elif feature.value == 7:
                s7_credit += courses[feature.name][0]

            elif feature.value == 8:
                s8_credit += courses[feature.name][0]

        if s1_credit >= 12 and s1_credit <= 18:
            credit_value += 1

        if s2_credit >= 12 and s2_credit <= 18:
            credit_value += 1

        if s3_credit >= 12 and s3_credit <= 18:
            credit_value += 1

        if s4_credit >= 12 and s4_credit <= 18:
            credit_value += 1

        if s5_credit >= 12 and s5_credit <= 18:
            credit_value += 1

        if s6_credit >= 12 and s6_credit <= 18:
            credit_value += 1

        if s7_credit >= 12 and s7_credit <= 18:
            credit_value += 1

        if s8_credit >= 12 and s8_credit <= 18:
            credit_value += 1

        total = credit_value + value

        return total

    def allConstraintsSatisfied(self):
        """
        This function tests all the features against all of the constraints. It
        returns true if the current set of feature assignments does not violate any
        of the constraints.
        """
        for constraint in self.constraints:
        # if any of the constraints are not satisfied, then return False
            if (not constraint.satisfied(constraint.tail.value, constraint.head.value)):
                return False

        #
        # Add code to check other constraints (like the semester credit limits) here.
        # If any of those constraints are violated (e.g., a semester only has 11 credits,
        # return False
        #
        # no violations, so return true
        return True


class CSPConstraintCorequisite(CSPConstraint):
    def __init__(self, ftrTail, strConstraint, ftrHead):
        CSPConstraint.__init__(self, ftrTail, strConstraint, ftrHead)

    def satisfied(self, tailValue, headValue):
        """
        returns true if constraint is satisfied and false if it is not
        """
        # if the head value or tail value is unassigned then it returns True
        if tailValue == "none" or headValue == "none":
            return True
        # are the tailValue and headValue the same
        if (tailValue == 1) and (headValue == 1):
            return True
        if (tailValue == 2) and (headValue == 2):
            return True
        if (tailValue == 3) and (headValue == 3):
            return True
        if (tailValue == 4) and (headValue == 4):
            return True
        if (tailValue == 5) and (headValue == 5):
            return True
        if (tailValue == 6) and (headValue == 6):
            return True
        if (tailValue == 7) and (headValue == 7):
            return True
        if (tailValue == 8) and (headValue == 8):
            return True

        # otherwise, constraint is not satisfied so return false
        return False

def course_map():
    csp_graph = CSPGraphCourses()

    # The features for the graph are the number of credits for each course and the semester
    for key in courses:
        csp_graph.addFeature(key, courses[key][2])

    # a list of the courses with prerequisite courses
    constraint_list = [('FCWR 151', 'FCWR 101'), ('FCWR 304', 'FCWR 101'), ('FCWR 304', 'FCWR 151'), ('MATH 180', 'MATH 170'), ('MATH 310', 'MATH 180'),
                      ('CSCI 155', 'CSCI 125'), ('CSCI 155', 'MATH 170'), ('CSCI 185', 'CSCI 125'),('CSCI 235', 'CSCI 185'), ('CSCI 235', 'MATH 170'),
                      ('CSCI 260', 'MATH 170'),('CSCI 260', 'CSCI 185'), ('CSCI 270', 'MATH 180'), ('CSCI 270', 'CSCI 235'), ('CSCI 312', 'CSCI 235'),
                      ('CSCI 318', 'CSCI 260'),('CSCI 330', 'CSCI 260'), ('CSCI 330', 'CSCI 185'), ('CSCI 335', 'CSCI 260'), ('CSCI 345', 'CSCI 330'),
                      ('CSCI 380', 'CSCI 260'), ('Natural Science II', 'Natural Science I'), ('Literature', 'FCIQ 101'), ('Literature', 'FCSP 105'),
                      ('Literature', 'FCSC 101'), ('Literature', 'FCWR 151'), ('Behavioral Science', 'FCIQ 101'), ('Behavioral Science', 'FCSP 105'),
                      ('Behavioral Science', 'FCSC 101'), ('Behavioral Science', 'FCWR 151'), ('Philosophy', 'FCIQ 101'), ('Philosophy', 'FCSP 105'),
                      ('Philosophy', 'FCSC 101'), ('Philosophy', 'FCWR 151'), ('Philosophy', 'Literature'), ('ICSS 309', 'FCIQ 101'), ('ICSS 309', 'FCSP 105'),
                      ('ICSS 309', 'FCSC 101'), ('ICSS 309', 'FCWR 151'), ('CS Elective I', 'CS Elective II')]

    for con_tuple in constraint_list:
        tail = con_tuple[0]
        head = con_tuple[1]
        strConstraint = '>'
        # create a new constraint object from tail to head
        newConstraint = CSPConstraintNotEqual(csp_graph.getFeature(tail), strConstraint, csp_graph.getFeature(head))
        # put the new constraint in the graph's list of constraints
        csp_graph.constraints.append(newConstraint)
        # create a new constraint object from head to tail
        newConstraint = CSPConstraintNotEqual(csp_graph.getFeature(head), strConstraint, csp_graph.getFeature(tail))
        # put the new constraint in the graph's list of constraints
        csp_graph.constraints.append(newConstraint)


    constraint_list2 = [('Natural Science I', 'Natural Science I - Lab'), ('Natural Science II', 'Natural Science II - Lab'),
                        ('CSCI 312', 'CSCI 318'), ('CSCI 330', 'CSCI 260'), ('CSCI 330', 'CSCI 185')]

    for con_tuple in constraint_list2:
        tail = con_tuple[0]
        head = con_tuple[1]
        strConstraint = '='
        newConstraint = CSPConstraintCorequisite(csp_graph.getFeature(tail), strConstraint, csp_graph.getFeature(head))
        # put the new constraint in the graph's list of constraints
        csp_graph.constraints.append(newConstraint)
        # create a new constraint object from head to tail
        newConstraint = CSPConstraintCorequisite(csp_graph.getFeature(head), strConstraint, csp_graph.getFeature(tail))
        # put the new constraint in the graph's list of constraints
        csp_graph.constraints.append(newConstraint)



    hillClimbingSearch(csp_graph)


course_map()