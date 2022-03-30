# Movie-Ticket-Booking
Algorithm for movie seat allocation to fulfill reservation request, maximize customer satisfaction and customer safety.
For the purpose of public safety, buffer of three seats is kept (Covid-19 public safety)
# Design
### Functional Requirements:
* Input file 
* System displays the movie name with one screen
* The system makes sure that no two reservation numbers can be booked
* The system makes sure that no two customers can be allocated the same seat
### Non-Functional Requirements:
* Customer satisfaction with the priority to allocate the seats together. Users should enjoy seamless experience
### Sample Input File Format
##### data1.txt<br />
<Reservation_Identifier No_of_seats><br />
R001 2<br />
R002 1
### Sample Output File Format
##### output_data1.txt<br />

R001 E1 E2 <br />
R002 J1<br />
##### Sample seat allocation<br />

<img width="1183" alt="Output" src="https://user-images.githubusercontent.com/30931914/160734847-63b6f493-3ca6-4314-919a-3c0f0fcb865d.png">

# Assumptions:
1. The theater cannot reserve seats for a group if the requested number of seats is greater than the available seats. In that case, the customers are informed about the insufficient number of available seats.
2. The reservation identifier will be in the format R###
3. For the purpose of public safety, group member can sit together, different group need to keep 3 seats distance in a row.
4. All seats are assumed to be empty during the start.
5. The theater comprises of only one class of seats.
# Customer Satisfaction:
1. Since customers are reserving seats for groups, they would prefer sitting togather. So the first priority will be to allocate seats for the group in a single row.
# Maximum Theater Utilization:
1. Allocation of seat is according to priority. If in any case a group can't be allocated in single row, they will be allocated in the seats available to ensure maximum theater utilization.
# The algorithm follows following rules:
1. First come first serve. Customers that comes first will be allocated seats first.
2. Each seat number must be in the range of 1 and the number of columns in this theater.
3. Each group will be allocated seats in a single row. If the group number is larger than the available number of seats in each row, split the group and allocate as many seats available in that row for few members and for others allocate in the other rows.
4. If the numbers of requested seats are not available in the theater then, inform the customer about insufficient seats.
## Steps for running the code
python main.py inputFile.txt
## Steps for running pytest
pytest filename.py
# Activity Diagram
<img width="833" alt="Activity Diagram" src="https://user-images.githubusercontent.com/30931914/160735249-a0d57813-471f-4b2f-867b-48fafe807905.png">
