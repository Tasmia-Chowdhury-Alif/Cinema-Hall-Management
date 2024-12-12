class Star_Cinema:
    __hall_list = []

    @classmethod
    def entry_hall(cls, a):
        cls.__hall_list.append(a)

class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no):
        self.__seats = {}  # it's a dictionary of seat's matrix information 
        self.__show_list = []
        self.__rows = rows
        self.__cols = cols
        self.__hall_no = hall_no

        self.entry_hall(self)  # inserting the object to the Star_Cinema class attribute hall_list
        
    def entry_show(self, show_id, movie_name, time):
        self.__show_list.append((show_id, movie_name, time))

        seat_matrix = []
        for r in range(self.__rows):
            ro = []
            for c in range(self.__cols):
                ro.append(0)
            seat_matrix.append(ro)

        self.__seats[show_id] = seat_matrix  # seats is allocated with id and the seat_matrix

    def book_seats(self, show_id, seat_position):
        # Checking if the id is valid
        if show_id not in [s[0] for s in self.__show_list]:
            print()
            print("Invalid Show Id. Please provide a valid Show Id.")
            print()
            return
        
        # Checking if seat_position is valid
        row, col = seat_position
        if row < 0 or row >= self.__rows or col < 0 or col >= self.__cols:
            print()
            print("Invalid Seat position. Please provide a valid row and column.")
            print()
            return

        # Checking if the seat is already booked 
        if self.__seats[show_id][row][col] == 1:
            print()
            print(f"The seat ({row}, {col}) is already booked!!!")
            print()
            return
        
        # Book the seat
        self.__seats[show_id][row][col] = 1

        matrix = self.__seats[show_id]
        
        print("\n")
        for i in matrix:
            print(i)
        
        print("\n")

        print("Congrats!! You have successfully booked your seat.\n")

    def view_show_list(self):
        for i in self.__show_list:
            print("Show id: ", i[0], ". Movie Name: ", i[1], ". Time: ", i[2])
        
    def view_available_seats(self, show_id):
        # Checking if the id is valid
        if show_id not in [s[0] for s in self.__show_list]:
            print()
            print("Invalid Show Id. Please provide a valid Show Id.")
            print()
            return
        
        matrix = self.__seats[show_id]
        
        print("\n")
        for i in matrix:
            print(i)
        
        print("\n")


Hall_a = Hall(7, 7, 8)

Hall_a.entry_show(111, "The Batman", "28 December 2024 at 02:30 PM")
Hall_a.entry_show(222, "Boyka Undisputed 3", "28 December 2024 at 06:00 PM")
Hall_a.entry_show(333, "Jawan", "28 December 2024 at 10:00 AM")
Hall_a.entry_show(444, "Doraimon", "28 December 2024 at 05:45 PM")


while True:
    print("1. View All Show Today")
    print("2. View Available Seats")
    print("3. Book Ticket")
    print("4. Exit")
    op = int(input("Enter Your Option: "))

    if op == 1:
        Hall_a.view_show_list()
    elif op == 2:
        s = int(input("Enter Show Id: "))
        Hall_a.view_available_seats(s)
    elif op == 3:
        s = int(input("Enter Show Id: "))
        r = int(input("Enter Row no: ")) - 1 # making 0 base index
        c = int(input("Enter Column: ")) - 1 # making 0 base index
        Hall_a.book_seats(s, (r, c))
    else:
        break













# class Star_Cinema :
#     hall_list = []

#     @classmethod
#     def entry_hall(cls,a):
#         cls.hall_list.append(a)

# class Hall(Star_Cinema) :
#     def __init__(self , rows , cols , hall_no):
#         self.seats = {} # it's a dictionary of seat's matrix information 
#         self.show_list = []
#         self.rows = rows
#         self.cols = cols
#         self.hall_no = hall_no
#         # self.available_seat = {}

#         self.entry_hall(self) # inserting the object to the Star_Cinema class attribute hall_list
        
#         # seats which is an dictionary of seats information
#         # show_list which is an list of tuples
#         # rows which is the row of the seats in that hall
#         # cols which is the column of the seats in that hall
#         # hall_no which is the unique no. of that hall

#     def entry_show(self , show_id , movie_name , time):

#         self.show_list.append((show_id , movie_name , time))

#         seat_matrix = []
#         for r in range(self.rows) :
#             ro = []
#             for c in range(self.cols) :
#                 ro.append(0)
#             seat_matrix.append(ro)

#         self.seats[show_id] = seat_matrix # seats is allocated with id and the seat_metrix
#         # self.available_seat[show_id] = (self.rows * self.cols)


#     def book_seats(self , show_id , seat_position):
#         if(show_id not in [s[0] for s in self.show_list]):
#             print()
#             print("Invalid Show Id . Please provide a valis Show Id .")
#             print()
#             return
        
#         # Check if seat_position is valid
#         row, col = seat_position
#         if row < 0 or row >= self.rows or col < 0 or col >= self.cols:
#             print()
#             print("Invalid Seat position. Please provide a valid row and column.")
#             print()
#             return

#         if self.seats[show_id][row][col] == 1:
#             print()
#             print(f"The seat ({row}, {col}) is already booked!!!")
#             print()
#             return
        
#         # Book the seat
#         self.seats[show_id][row][col] = 1

#         matrix = self.seats[show_id]
        
#         print("\n")
#         for i in matrix :
#             print(i)
        
#         print("\n")

#         print("Congrats !! You have successfull booked your seat .\n")

#     def view_show_list(self ):
#         for i in self.show_list :
#             print("Show id : " ,i[0],". Movie Name : ",i[1], ". Time :", i[2])
        
    
#     def view_available_seats(self,show_id):
#         # print(f"Available seats for the Show_id {show_id} is : {self.available_seat[show_id]}")
#         matrix = self.seats[show_id]
        
#         print("\n")
#         for i in matrix :
#             print(i)
        
#         print("\n")


# Hall_a = Hall(7,7,8)
# # dsf = Hall(5,6,3)

# Hall_a.entry_show(111,"The Batman", "28 December 2024 at 02:30 PM")
# Hall_a.entry_show(222,"Boyka Undisputed 3", "28 December 2024 at 06:00 PM")
# Hall_a.entry_show(333,"Jawan ", "28 December 2024 at 10:00 AM")
# Hall_a.entry_show(444,"Doraimon", "28 December 2024 at 05:45 PM")

# # for i in dsf.show_list :
# #     print("Hall id : " ,i[0],".\nMovie Name : ",i[1], ".\nTime :", i[2])

# # print(dsf.seats[78])

# # print(Star_Cinema.hall_list[0].hall_no)
# # print(Star_Cinema.hall_list[1].hall_no)


# while True:
#     print("1. View All Show Today ")
#     print("2. View Available Seats ")
#     print("3. Book Ticket ")
#     print("4. Exit ")
#     op = int(input("Enter Your Option : "))

#     if op == 1 :
#         Hall_a.view_show_list()
#     elif op == 2 :
#         s = int(input("Enter Show Id : "))
#         Hall_a.view_available_seats(s)
#     elif op == 3 :
#         s = int(input("Enter Show Id : "))
#         r = int(input("Enter Row no : "))-1
#         c = int(input("Enter Column : "))-1
#         Hall_a.book_seats(s,(r,c))
#     else :
#         break