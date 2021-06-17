# IT Ticketing System for Small IT Repair Shop
This was my software artefact for my final year project at university. It is an IT Ticketing System targeted for Small IT Repair Shops built using Django, HTML and CSS. During this project I learnt Django from scratch with no experience or support from staff at my university. During my research and my own professional experience I found that ticketing systems didn't provide features that would be beneficial for an IT repair shop or take into considerations scenarios that a small IT repair shop face such as walk in customers. The aim of the project was to build an IT ticketing system for small IT repair shops that would include extra features such as an inventory management system, financial features etc.

Future Work:

Due to circumstances beyond my control certain features were cut or significantly reduced in order to meet my assignement deadline. If someone were to develop this further these are what I would do to improve the software going forward:

Ability to create orders and order forms using the inventory tracking system:
The inventory tracking system ended up being downsized drastically in scope. As a result it’s had limited functionality in the artefact, essentially being an updateable inventory list. I would’ve liked to implement an ordering system through the website. Which could then generate invoices and reports through the report functionality.

Billing for Tickets:
The ability for tickets to be billed and tracked through the application itself. In the current version an invoice for the ticket can be generated which can then be signed and have the price added to it. I would’ve liked to include the ability to bill for tickets with the application and have that linked in.

Report functionality:
The report functionality ended up being cut. I would’ve like to have a dashboard report with graphs highlighting aspects such as number of tickets, billings etc.

Device make and model Django models: 
Originally I had 2 Django models for “device make” and “device model” with the idea being that you could search for “Apple” and then it’ll filter to show only models made by apple. However this ended up getting scrapped due to limitations of my own knowledge of Django and implementing foreign keys.

Ticket filtering:
I would’ve liked to implement a responsive way to filter tickets and allow for searching. This didn’t get implemented due to my limited knowledge of Django. I know this would require the use of filtersets within Django but I don’t have the time and knowledge necessary to have implemented it in this version of the artefact.


