def read_file(file_name):    
    request_array = []
    try:

        with open(file_name) as f:
            lines = f.readlines() #reading line by line
            for line in lines:
                request_array.append(line.split())
    except FileNotFoundError:
        print("Sorry, the file does not exist")
    return request_array
    
def write_file(file_name, content):
    with open(file_name, 'w') as f:
        if isinstance(content, str): 
            f.write(content)
            f.write('\n')
        elif isinstance(content, list): 
            for line in content:
                f.write(line) 
                f.write('\n')
        else:
            pass


def seat_map(number): 
    return chr((ord(str(number)) + 17)) 



class Theater:
    def __init__(self, file_name, rows=10, columns=20, buffer_seats=3):
        self.rows = rows
        self.columns = columns
        self.number_of_seats = self.rows * self.columns
        self.file_name = file_name
        self.remain_seats = [self.columns for _ in range(self.rows)] 
        self.write_file_name = 'output_' + self.file_name
        self.mat_file_name  = 'output_mat' + self.file_name
        self.buffer_seats = buffer_seats
        self.safe_row = 1

    def seatReservation(self):
        request_array = read_file(self.file_name)
        output = []
        mat = [['s']*20 for i in range(10)]
        dict_seat = {'A':9,'B':8,'C':7,'D':6, 'E':5, 'F':4, 'G':3, 'H':2, 'I':1, 'J':0 } 
        dupset = set()
      
        for request in request_array:
            line = ''
            reservationIdentifier, noOfSeats = request[0], int(request[1])

            if noOfSeats <= 0:
                line = 'Error: ' + reservationIdentifier + ' ' + 'seat number should be a positive number:' + str(noOfSeats)
            elif noOfSeats > self.number_of_seats:
                line = 'Error: ' + reservationIdentifier + ' ' + 'Not enough seats left'
            elif noOfSeats > self.columns:
                line = 'Error: ' + reservationIdentifier + ' ' + 'Number of seats should be less than or equal to 20'
            elif reservationIdentifier[0] != 'R':
                line = 'Error: ' + reservationIdentifier + ' ' + 'Reservation Identifier should start with R'
            elif reservationIdentifier in dupset:
                line = 'Error: ' + reservationIdentifier + ' ' + 'Reservation number already exits'
            else:
                dupset.add(reservationIdentifier)
                seat_alloc = self.seatAllocation(reservationIdentifier, noOfSeats)[:-1] 
                line = reservationIdentifier + ' ' + seat_alloc  
                seats = seat_alloc.split(',')
                
                for j in seats:
                    mat[dict_seat[j[0]]][int(j[1:])-1] = reservationIdentifier
                
            output.append(line)

      
        rows, cols = (10, 20)
        arr=[]
        for i in range(rows):
            col = []
            for j in range(cols):
                col.append(reservationIdentifier)
            arr.append(col)

        
        
        row = dict_seat.keys()
        row = sorted(row)
        mat_final=[]
        mat_final.append("-----------------------------------------------------------------------------------------------------")
        mat_final.append("======================================All eyes this side============================================= ")
        mat_final.append("-----------------------------------------------------------------------------------------------------")
        mat_final.append("----------------------------------Displaying Movie : THE BATMAN -------------------------------------")
        mat_final.append("\nEXIT\n\n\n")
        write_file(self.write_file_name, output)
        mat = mat[::-1]
        
        for i in range(10):
            mat_final.append( str(row[i] +" "+ str(  mat[i])))
        
        mat_final.append("\n\nEXIT")
        
        write_file(self.mat_file_name, mat_final)
        print('Output file in:' + self.write_file_name + '\nMatrix file in: ' + self.mat_file_name)
        return self.write_file_name
        #return 'Output file in:' + self.write_file_name + '\nMatrix file in: ' + self.mat_file_name

    def seatAllocation(self, reservationIdentifier, noOfSeats): # identifier:R001 noOfSeats:5
        row = self.rows // 2 - 1 #starting from mid row; row = 4
        up = True
        counter = self.safe_row
        res = ''

        while 0 <= row < self.rows:
            if noOfSeats <= self.remain_seats[row]: 
                for i in range(self.columns - self.remain_seats[row] + 1,
                               self.columns - self.remain_seats[row] + 1 + noOfSeats): 
                    res += seat_map(row) + str(i) + ',' 
                seats = min(noOfSeats + self.buffer_seats, self.remain_seats[row]) 
                self.remain_seats[row] -= seats 
                self.number_of_seats -= seats

                return res

            if up:
                row += counter
                counter += self.safe_row
                up = False
            else:
                row -= counter
                counter += self.safe_row
                up = True

        # if this group have to be seatAllocationd in different rows
        row = self.rows // 2 - 1
        up = True
        counter = self.safe_row
        res = ''
        while noOfSeats > 0:
            if self.remain_seats[row] > 0:
                start = self.columns - self.remain_seats[row] + 1
                for i in range(start, self.columns + 1):
                    if noOfSeats > 0:
                        res += seat_map(row) + str(i) + ','
                        noOfSeats -= 1
                        self.remain_seats[row] -= 1
                        self.number_of_seats -= 1
            if self.remain_seats[row] != 0:
                self.number_of_seats -= min(self.remain_seats[row], self.buffer_seats)
                self.remain_seats[row] -= min(self.remain_seats[row], self.buffer_seats)

            if up:
                row += counter
                counter += self.safe_row
                up = False
            else:
                row -= counter
                counter += self.safe_row
                up = True
        return res


