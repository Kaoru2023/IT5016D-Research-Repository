# Help Desk Ticketing System Prototype

## Introduction
This is a prototype of a help desk system for an organisation which allows internal clients to request for assistance.It includes two files: Main.py, for the User Interface, and Ticket.py, for data storage and task execution in Main.py.

## Installation and Usage
1. Install Python (Python 3.x is recommended).   
2. Open the folder where Main.py and Ticket.py are located.
3. Run Main.py to start Help Desk Ticketing System program.  
   => For Windows: Right click the Main.py--> Open with--> Python   

## Project Structure
Main.py : Handles the user interface and interaction.  
Ticket.py : Stores tickets information and perform required tasks.

## How to Use the System
Enter an option from the Help desk Ticketing System Menu:

"Option 1: Submit New Ticket": Choose this option to request assistance. Provide your staffID, name, contact email, and description of the isssue. If you need password change, enter "Password Change" in the description. A New Password will be generated. After submitting a new ticket, a ticket number will be assigned. 

"Option 2: Show All Tickets": Display a list of all tickets with information, including staff ID, creator’s name, contact email address, description of issue, response, and ticket status.

"Option 3: Respond to Ticket by Number": Enter the ticket number and your response message to provide feedback.

"Option 4: Reopen Closed Ticket": Enter the ticket number to reopen a closed ticket.

"Option 5: Show Ticket Statistics": Display the number of Submitted, Resolved, and Open tickets.

"Option 6: Exit": Close the system. 

## Examples
To request assistance, choose Option 1. and provide required information. If you need change password, type "Change Password". A new password and a ticket number will be displayed.

Help Desk Ticketing System Menu:
1. Submit New Ticket
2. Show All Tickets
3. Respond to Ticket by Number
4. Reopen Closed Ticket
5. Show Ticket Statistics
6. Exit
-----------------------------------
Enter your choice 1 - 6: 1  
Enter your staff ID: K1234  
Enter your name: Kaoru  
Enter contact Email: kaoru@gmail.com  
Enter description of issue. To change password, enter 'Password Change': Password Change  
New Password Generated: K1Kao  
Ticket Number: 2001  
-----------------------------------
   
<span style="font-size: 14px;">If you have other issues, type description.</span>
-----------------------------------
Enter your choice 1 - 6: 1  
Enter your staff ID: T3456  
Enter your name: Taro  
Enter contact Email: taro@gmail.com  
Enter description of issue. To change password, enter 'Password Change': PC does not start  
Ticket Submitted Successfully! Ticket Number: 2002  
-----------------------------------

<span style="font-size: 14px;">To respond a ticket, choose Option 3. and specify the ticket number and enter message.</span>
-----------------------------------
Enter your choice 1 - 6: 3  
Enter Ticket Number to Respond: 2002  
Enter Response: Your PC issue resolved  
Response added to the ticket.  
-----------------------------------

<span style="font-size: 14px;">To reopen a closed ticket, choose Option 4. and specify the ticket number.</span>
-----------------------------------
Enter your choice 1 - 6: 4  
Enter Ticket Number to Reopen: 2001  
Ticket reopened.  
-----------------------------------


<span style="font-size: 14px;">To see all ticket information, choose Option2.</span>
-----------------------------------
Enter your choice 1 - 6: 2  
Ticket Number: 2001  
Ticket Creator Name: Kaoru  
Staff ID: K1234  
Contact Email: kaoru@gmail.com  
Description: Password Change  
Response: New Password Generated: K1Kao  
Status: Reopened  
-----------------------------------  
Ticket Number: 2002  
Ticket Creator Name: Taro  
Staff ID: T3456  
Contact Email: taro@gmail.com  
Description: PC does not start  
Response: Your PC issue resolved  
Status: Closed  
-----------------------------------

<span style="font-size: 14px;">To display ticket stats, choose Option 5.</span>
-----------------------------------
Enter your choice 1 - 6: 5    
Submitted Tickets: 2  
Resolved Tickets: 1  
Open Tickets: 1  
-----------------------------------

## Requirements

Python 3.x

## Contact

If you have any questions or feedback, please reach out to me on Github:  
[Kaoru2023] https://github.com/Kaoru2023  


