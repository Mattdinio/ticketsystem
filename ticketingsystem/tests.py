from datetime import datetime
from django.test import TestCase, Client
from django.urls import reverse, resolve
from django.contrib.auth.models import User
from ticketingsystem.views import *
from ticketingsystem.models import *
from ticketingsystem.forms import *

# This class tests the URL routing gets resolved correctly
class TestURLS(TestCase):

    def test_home_resolves(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func, home)

    def test_dashboard_resolves(self):
        url = reverse('Dashboard')
        self.assertEquals(resolve(url).func, dashboard)

    def test_create_ticket_resolves(self):
        url = reverse('create-ticket')
        self.assertEquals(resolve(url).func, createTicket)
    
    def test_ticket_detail_resolves(self):
        url = reverse('Ticket_Detail', args=[1])
        self.assertEquals(resolve(url).func, ticket_detail)

    def test_my_tickets_resolves(self):
        url = reverse('my-tickets')
        self.assertEquals(resolve(url).func, myTickets)

    def test_customer_list_resolves(self):
        url = reverse('Customer_List')
        self.assertEquals(resolve(url).func, customerList)

    def test_create_customer_resolves(self):
        url = reverse('create_customer')
        self.assertEquals(resolve(url).func, createCustomer)

    def test_stock_list_resolves(self):
        url = reverse('stock-list')
        self.assertEquals(resolve(url).func, stockList)

    def test_create_stock_resolves(self):
        url = reverse('create_stock')
        self.assertEquals(resolve(url).func, createStock)

    def test_stock_edit_resolves(self):
        url = reverse('stock_edit', args=[1])
        self.assertEquals(resolve(url).func, editStock)

# This class tests that the views are used correctly and the right template is rendered
class testViews(TestCase):

    def setUp(self):
        self.client = Client()
        #creates a user for the testing
        user = User.objects.create_user(username = 'testUser', email = 'test@tester.com')
        user.set_password('hjok34ASDshuio*4')
        user.save()
        self.login = self.client.login(username = 'testUser', password = 'hjok34ASDshuio*4')
        #testCustomer created to create a test ticket
        testCustomer = Customer.objects.create(firstName = 'Tester', lastName = 'McTest', 
        number = '07468524732', email = '', address = '')
        #test Ticket created to test ticket detail page
        testTicket = Ticket.objects.create(ticketName = 'HELP', deviceMake = 'HP', deviceModel = 'Tester', 
        deviceType = 'Laptop', customer = testCustomer, assigned = user, ticketStatus = 'Open', ticketDescription = 'This is a test Ticket' )
        #testStock created to test stock detail page
        testStock = inventoryItem.objects.create(itemName = 'Test Item', itemType = 'Tablet', 
        quantityInStock = 1, price = 1.00, orderLink = '')
        self.homeURL = reverse('home')
        self.dashURL = reverse('Dashboard')
        self.ticketDetailURL = reverse('Ticket_Detail', args=[1])
        self.createTicketURL = reverse('create-ticket')
        self.myticketsURL = reverse('my-tickets')
        self.customerListURL = reverse('Customer_List')
        self.createCustomerURL = reverse('create_customer')
        self.stockListURL = reverse('stock-list')
        self.createStockURL = reverse('create_stock')
        self.stockEditURL = reverse('stock_edit', args=[1])


    def test_home_get(self):
        response = self.client.get(self.homeURL)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def test_dashboard_GET(self):
        response = self.client.get(self.dashURL)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'dashboard.html')
    
    def test_ticketDetail_GET(self):
        response = self.client.get(self.ticketDetailURL)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ticket_detail.html')

    def test_create_ticket_GET(self):
        response = self.client.get(self.createTicketURL)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'create-ticket.html')

    def test_my_tickets_GET(self):
        response = self.client.get(self.myticketsURL)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'my_tickets.html')

    def test_customer_list_GET(self):
        response = self.client.get(self.customerListURL)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'customer_list.html')

    def test_create_customer_GET(self):
        response = self.client.get(self.createCustomerURL)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'create_customer.html')

    def test_stock_list_GET(self):
        response = self.client.get(self.stockListURL)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'stock_list.html')

    def test_create_stock_GET(self):
        response = self.client.get(self.createStockURL)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'create_stock.html')

    def test_stock_edit_GET(self):
        response = self.client.get(self.stockEditURL)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'stock_edit.html')

# This class tests the model methods
class testModels(TestCase):

    def setUp(self):
        self.client = Client()
        #creates a user for the testing
        user = User.objects.create_user(username = 'testUser', email = 'test@tester.com')
        user.set_password('hjok34ASDshuio*4')
        user.save()
        self.login = self.client.login(username = 'testUser', password = 'hjok34ASDshuio*4')
        #testCustomer created to create a test ticket
        testCustomer = Customer.objects.create(firstName = 'Tester', lastName = 'McTest', 
        number = '07468524732', email = '', address = '')
        #test Ticket created to test ticket detail page
        testTicket = Ticket.objects.create(ticketName = 'HELP', deviceMake = 'HP', deviceModel = 'Tester', 
        deviceType = 'Laptop', customer = testCustomer, assigned = user, ticketStatus = 'Open', ticketDescription = 'This is a test Ticket' )
        #testStock created to test stock detail page
        testStock = inventoryItem.objects.create(itemName = 'Test Item', itemType = 'Tablet',  quantityInStock = 1, price = 1.00, orderLink = '')

    def testCustomerModel(self):
        newtestCustomer = Customer.objects.create(firstName = 'Testy', lastName = 'McTest', 
        number = '07468524732', email = '', address = '')
        #tests the __str__ method
        self.assertEqual(str(newtestCustomer),'Testy McTest')

    def testTicketModel(self):
        testCustomer = Customer.objects.create(firstName = 'Tester', lastName = 'McTest',
        number = '07468524732', email = '', address = '')
        user = User.objects.get(id=1) 
        testTicket = Ticket.objects.create(ticketName = 'HELP ME', deviceMake = 'HP', deviceModel = 'Tester', 
        deviceType = 'Laptop', customer = testCustomer, assigned = user, ticketStatus = 'Open', ticketDescription = 'This is a test Ticket' )
        #tests the __str__ method
        self.assertEqual(str(testTicket),'HELP ME')
        #test the get assigned method
        self.assertEqual(testTicket.assigned, user)

    def testInventoryModel(self):
        testStock = inventoryItem.objects.create(itemName = 'Test Item', itemType = 'Tablet',  quantityInStock = 1, price = 1.00, orderLink = '')
        #tests the __str__ method
        self.assertEqual(str(testStock),'Test Item(Tablet)')

'''
FORM METHOD UNIT TESTS BELOW
'''

#This class tests the customer form's validation
class testCustomerModelForm(TestCase):
    
    def testValidData(self):
        form = customerForm(data = {
            'firstName': 'Test',
            'lastName': 'Test',
            'number' : '07468524732',
            'email' : 'test@tester.com',
            'address' : '123 fake street, Portsmouth, PO1 1NL'
        })
        self.assertTrue(form.is_valid())
    #Test No Data provided
    def testNoData(self):
        form = customerForm(data = {
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 3)

    def testFirstNameRequired(self):
        form = customerForm(data = {
            'firstName': '',
            'lastName': 'Test',
            'number' : '07468524732',
            'email' : 'test@tester.com',
            'address' : '123 fake street, Portsmouth, PO1 1NL'
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 1)

    def testFirstNameLength(self):
        form = customerForm(data = {
            'firstName': 'MyNameIsJohnBrownIHavemorethanahundredcharactersinmynamewhichshouldtriggerthelengthofthistesthopefully',
            'lastName': 'Test',
            'number' : '07468524732',
            'email' : 'test@tester.com',
            'address' : '123 fake street, Portsmouth, PO1 1NL'
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 1)

    def testLastNameRequired(self):
        form = customerForm(data = {
            'firstName': 'Test',
            'lastName': '',
            'number' : '07468524732',
            'email' : 'test@tester.com',
            'address' : '123 fake street, Portsmouth, PO1 1NL'
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 1)

    def testLastNameLength(self):
        form = customerForm(data = {
            'firstName': 'Test',
            'lastName': 'MyNameIsJohnBrownIHavemorethanahundredcharactersinmynamewhichshouldtriggerthelengthofthistesthopefully',
            'number' : '07468524732',
            'email' : 'test@tester.com',
            'address' : '123 fake street, Portsmouth, PO1 1NL'
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 1)

    def testNumberRequired(self):
        form = customerForm(data = {
            'firstName': 'Test',
            'lastName': 'Test',
            'number' : '',
            'email' : 'test@tester.com',
            'address' : '123 fake street, Portsmouth, PO1 1NL'
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 1)

    def testNumberLengthLong(self):
        form = customerForm(data = {
            'firstName': 'Test',
            'lastName': 'Test',
            'number' : '15150151051510500150',
            'email' : 'test@tester.com',
            'address' : '123 fake street, Portsmouth, PO1 1NL'
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 1)

    def testNumberLengthShort(self):
        form = customerForm(data = {
            'firstName': 'Test',
            'lastName': 'Test',
            'number' : '0154510',
            'email' : 'test@tester.com',
            'address' : '123 fake street, Portsmouth, PO1 1NL'
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 1)

    def testLettersInNumber(self):
        form = customerForm(data = {
            'firstName': 'Test',
            'lastName': 'Test',
            'number' : '023926138H5',
            'email' : 'test@tester.com',
            'address' : '123 fake street, Portsmouth, PO1 1NL'
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 1)

    #Test Email
    def testNoEmail(self):
        form = customerForm(data = {
            'firstName': 'Test',
            'lastName': 'Test',
            'number' : '07468524732',
            'email' : '',
            'address' : '123 fake street, Portsmouth, PO1 1NL'
        })
        self.assertTrue(form.is_valid())

    def testEmailFormat(self):
        form = customerForm(data = {
            'firstName': 'Test',
            'lastName': 'Test',
            'number' : '07468524732',
            'email' : 'hello',
            'address' : '123 fake street, Portsmouth, PO1 1NL'
        })
        self.assertFalse(form.is_valid())

    def testEmailLength(self):
        form = customerForm(data = {
            'firstName': 'Test',
            'lastName': 'Test',
            'number' : '07468524732',
            'email' : 'thisissuperlongemailthatismorethan254characterstotessdasdasdasdasdasdasdasdasdtheemaillengththisissuperlongemailthatismorethan254characterstotestheemaillengththisissuperlongemailthatismorethan254characterstotestheemaillength@testercodedemailneedingtobemorethan254characters.com',
            'address' : '123 fake street, Portsmouth, PO1 1NL'
        })
        self.assertFalse(form.is_valid())

    #Test blank address
    def testNoAddress(self):
        form = customerForm(data = {
            'firstName': 'Test',
            'lastName': 'Test',
            'number' : '07468524732',
            'email' : 'test@tester.com',
            'address' : ''
        })
        self.assertTrue(form.is_valid())

    def testNoEmailORAddress(self):
        form = customerForm(data = {
            'firstName': 'Test',
            'lastName': 'Test',
            'number' : '07468524732',
            'email' : '',
            'address' : ''
        })
        self.assertTrue(form.is_valid())

#This class tests the Ticket form's validation
class testTicketModelForm(TestCase):

    def setUp(self):
        self.client = Client()
        #creates a user to act as the technician assigned / ticket creator
        user = User.objects.create_user(username = 'testUser', email = 'test@tester.com')
        user.set_password('hjok34ASDshuio*4')
        user.save()
        self.login = self.client.login(username = 'testUser', password = 'hjok34ASDshuio*4')
        #testCustomer created to customer for the test ticket
        testCustomer = Customer.objects.create(firstName = 'Tester', lastName = 'McTest', 
        number = '07468524732', email = '', address = '')

    def testValidData(self):
        user = User.objects.get(id=1) 
        customer = Customer.objects.get(id=1) 
        form = ticketForm(data = {
            'ticketName': 'Test Ticket',
            'deviceMake': 'HP',
            'deviceModel' : 'Test Mark 2',
            'deviceType' : 'Tablet',
            'customer' : customer,
            'assigned' : user,
            'ticketStatus' : 'Open',
            'ticketDescription' : 'Help me'
        })
        self.assertTrue(form.is_valid())

    def testnoData(self):
        user = User.objects.get(id=1) 
        customer = Customer.objects.get(id=1) 
        form = ticketForm(data = {
        })
        self.assertFalse(form.is_valid())

    def testNameRequired(self):
        user = User.objects.get(id=1) 
        customer = Customer.objects.get(id=1) 
        form = ticketForm(data = {
            'ticketName': '',
            'deviceMake': 'HP',
            'deviceModel' : 'Test Mark 2',
            'deviceType' : 'Tablet',
            'customer' : customer,
            'assigned' : user,
            'ticketStatus' : 'Open',
            'ticketDescription' : 'Help me'
        })
        self.assertFalse(form.is_valid())

    def testNameLength(self):
        user = User.objects.get(id=1) 
        customer = Customer.objects.get(id=1) 
        form = ticketForm(data = {
            'ticketName': 'Help me my computer has caught fire and I dont think it works any more, also please help me please now please I really need this computer to work!!',
            'deviceMake': 'HP',
            'deviceModel' : 'Test Mark 2',
            'deviceType' : 'Tablet',
            'customer' : customer,
            'assigned' : user,
            'ticketStatus' : 'Open',
            'ticketDescription' : 'Help me'
        })
        self.assertFalse(form.is_valid())

    def testDeviceMakeRequired(self):
        user = User.objects.get(id=1) 
        customer = Customer.objects.get(id=1) 
        form = ticketForm(data = {
            'ticketName': 'Test',
            'deviceMake': '',
            'deviceModel' : 'Test Mark 2',
            'deviceType' : 'Tablet',
            'customer' : customer,
            'assigned' : user,
            'ticketStatus' : 'Open',
            'ticketDescription' : 'Help me'
        })
        self.assertFalse(form.is_valid())

    def testDeviceMakeLength(self):
        user = User.objects.get(id=1) 
        customer = Customer.objects.get(id=1) 
        form = ticketForm(data = {
            'ticketName': 'Test',
            'deviceMake': 'Super Mega Awesome Company with super leet skills building computer hardware yo',
            'deviceModel' : 'Test Mark 2',
            'deviceType' : 'Tablet',
            'customer' : customer,
            'assigned' : user,
            'ticketStatus' : 'Open',
            'ticketDescription' : 'Help me'
        })
        self.assertFalse(form.is_valid())

    def testDeviceModelRequired(self):
        user = User.objects.get(id=1) 
        customer = Customer.objects.get(id=1) 
        form = ticketForm(data = {
            'ticketName': 'Test',
            'deviceMake': 'HP',
            'deviceModel' : '',
            'deviceType' : 'Tablet',
            'customer' : customer,
            'assigned' : user,
            'ticketStatus' : 'Open',
            'ticketDescription' : 'Help me'
        })
        self.assertFalse(form.is_valid())

    def testDeviceModelLength(self):
        user = User.objects.get(id=1) 
        customer = Customer.objects.get(id=1) 
        form = ticketForm(data = {
            'ticketName': 'Test',
            'deviceMake': 'HP',
            'deviceModel' : 'Super Cool Awesome Mega Fantastic Fast Computer that is totally real',
            'deviceType' : 'Tablet',
            'customer' : customer,
            'assigned' : user,
            'ticketStatus' : 'Open',
            'ticketDescription' : 'Help me'
        })
        self.assertFalse(form.is_valid())

    def testDeviceTypeRequired(self):
        user = User.objects.get(id=1) 
        customer = Customer.objects.get(id=1) 
        form = ticketForm(data = {
            'ticketName': 'Test',
            'deviceMake': 'HP',
            'deviceModel' : 'Test',
            'deviceType' : '',
            'customer' : customer,
            'assigned' : user,
            'ticketStatus' : 'Open',
            'ticketDescription' : 'Help me'
        })
        self.assertFalse(form.is_valid())

    def testDeviceTypeNonOption(self):
        user = User.objects.get(id=1) 
        customer = Customer.objects.get(id=1) 
        form = ticketForm(data = {
            'ticketName': 'Test',
            'deviceMake': 'HP',
            'deviceModel' : 'Test',
            'deviceType' : 'Awesome',
            'customer' : customer,
            'assigned' : user,
            'ticketStatus' : 'Open',
            'ticketDescription' : 'Help me'
        })
        self.assertFalse(form.is_valid())

    def testNoCustomer(self):
        user = User.objects.get(id=1) 
        customer = Customer.objects.get(id=1) 
        form = ticketForm(data = {
            'ticketName': 'Test',
            'deviceMake': 'HP',
            'deviceModel' : 'Test',
            'deviceType' : 'Tablet',
            'customer' : '',
            'assigned' : user,
            'ticketStatus' : 'Open',
            'ticketDescription' : 'Help me'
        })
        self.assertFalse(form.is_valid())

    def testNoTechnicianAssigned(self):
        user = User.objects.get(id=1) 
        customer = Customer.objects.get(id=1) 
        form = ticketForm(data = {
            'ticketName': 'Test',
            'deviceMake': 'HP',
            'deviceModel' : 'Omen',
            'deviceType' : 'Tablet',
            'customer' : customer,
            'assigned' : '',
            'ticketStatus' : 'Open',
            'ticketDescription' : 'Help me'
        })
        self.assertTrue(form.is_valid())

    # Whilst Null is allowed in the Technician Model, Null shouldn't be a valid option within the form. This test checks that.
    def testNULLTechnicianAssigned(self):
        user = User.objects.get(id=1) 
        customer = Customer.objects.get(id=1) 
        form = ticketForm(data = {
            'ticketName': 'Test',
            'deviceMake': 'HP',
            'deviceModel' : 'Omen',
            'deviceType' : 'Tablet',
            'customer' : customer,
            'assigned' : 'NULL',
            'ticketStatus' : 'Open',
            'ticketDescription' : 'Help me'
        })
        self.assertFalse(form.is_valid())

    def testNonStatusOption(self):
        user = User.objects.get(id=1) 
        customer = Customer.objects.get(id=1) 
        form = ticketForm(data = {
            'ticketName': 'Test',
            'deviceMake': 'HP',
            'deviceModel' : 'Omen',
            'deviceType' : 'Tablet',
            'customer' : customer,
            'assigned' : user,
            'ticketStatus' : 'Awesome',
            'ticketDescription' : 'Help me'
        })
        self.assertFalse(form.is_valid())

    def testNoStatusProvided(self):
        user = User.objects.get(id=1) 
        customer = Customer.objects.get(id=1) 
        form = ticketForm(data = {
            'ticketName': 'Test',
            'deviceMake': 'HP',
            'deviceModel' : 'Omen',
            'deviceType' : 'Tablet',
            'customer' : customer,
            'assigned' : user,
            'ticketStatus' : '',
            'ticketDescription' : 'Help me'
        })
        self.assertFalse(form.is_valid())

    def testStatusLength(self):
        user = User.objects.get(id=1) 
        customer = Customer.objects.get(id=1) 
        form = ticketForm(data = {
            'ticketName': 'Test',
            'deviceMake': 'HP',
            'deviceModel' : 'Omen',
            'deviceType' : 'Tablet',
            'customer' : customer,
            'assigned' : user,
            'ticketStatus' : 'Waiting on Customer',
            'ticketDescription' : 'Help me'
        })
        self.assertTrue(form.is_valid())

    def testDescriptionRequired(self):
        user = User.objects.get(id=1) 
        customer = Customer.objects.get(id=1) 
        form = ticketForm(data = {
            'ticketName': 'Test',
            'deviceMake': 'HP',
            'deviceModel' : 'Omen',
            'deviceType' : 'Tablet',
            'customer' : customer,
            'assigned' : user,
            'ticketStatus' : 'Waiting on Customer',
            'ticketDescription' : ''
        })
        self.assertFalse(form.is_valid())

#This class tests the Inventory form's validation
class testInventoryModelForm(TestCase):

    def testValidData(self):
        form = inventoryForm(data = {
            'itemName': 'Test Item',
            'itemType': 'Tablet',
            'quantityInStock' : 1,
            'price' : 1.99, 
            'orderLink' : 'http://www.google.com',
        })
        self.assertTrue(form.is_valid())

    def testNoData(self):
        form = inventoryForm(data = {
        })
        self.assertFalse(form.is_valid())

    def testNameRequired(self):
        form = inventoryForm(data = {
            'itemName': '',
            'itemType': 'Tablet',
            'quantityInStock' : 1,
            'price' : 1.99,
            'orderLink' : 'http://www.google.com',
        })
        self.assertFalse(form.is_valid())

    def testNameLength(self):
        form = inventoryForm(data = {
            'itemName': 'super coool mega awesome item of awesomeness you would never believe how good this item is really it will blown your freaking mind how cool it is really it is so cool that people would would pay billions and billions of pounds for it',
            'itemType': 'Tablet',
            'quantityInStock' : 1,
            'price' : 1.99,
            'orderLink' : 'http://www.google.com',
        })
        self.assertFalse(form.is_valid())

    def testNoType(self):
        form = inventoryForm(data = {
            'itemName': 'Test Item',
            'itemType': '',
            'quantityInStock' : 1,
            'price' : 1.99,
            'orderLink' : 'http://www.google.com',
        })
        self.assertFalse(form.is_valid())
    
    def testNonTypeSelected(self):
        form = inventoryForm(data = {
            'itemName': 'Test Item',
            'itemType': 'Cool Thing',
            'quantityInStock' : 1,
            'price' : 1.99,
            'orderLink' : 'http://www.google.com',
        })
        self.assertFalse(form.is_valid())

    def testlongestType(self):
        form = inventoryForm(data = {
            'itemName': 'Test Item',
            'itemType': 'Mobile Phone',
            'quantityInStock' : 1,
            'price' : 1.99,
            'orderLink' : 'http://www.google.com',
        })
        self.assertTrue(form.is_valid())

    def testNegativeQuantity(self):
        form = inventoryForm(data = {
            'itemName': 'Test Item',
            'itemType': 'Tablet',
            'quantityInStock' : -1,
            'price' : 1.99,
            'orderLink' : 'http://www.google.com',
        })
        self.assertFalse(form.is_valid())

    def testZeroQuantity(self):
        form = inventoryForm(data = {
            'itemName': 'Test Item',
            'itemType': 'Tablet',
            'quantityInStock' : 0,
            'price' : 1.99,
            'orderLink' : 'http://www.google.com',
        })
        self.assertTrue(form.is_valid())

    def testLargeQuantity(self):
        form = inventoryForm(data = {
            'itemName': 'Test Item',
            'itemType': 'Tablet',
            'quantityInStock' : 100000000000000,
            'price' : 1.99,
            'orderLink' : 'http://www.google.com',
        })
        self.assertTrue(form.is_valid())

    def testNegativePrice(self):
        form = inventoryForm(data = {
            'itemName': 'Test Item',
            'itemType': 'Tablet',
            'quantityInStock' : 1,
            'price' : -1.99,
            'orderLink' : 'http://www.google.com',
        })
        self.assertFalse(form.is_valid())

    def testPriceWithMoreDecimalPlaces(self):
        form = inventoryForm(data = {
            'itemName': 'Test Item',
            'itemType': 'Tablet',
            'quantityInStock' : 1,
            'price' : 1.01516513150,
            'orderLink' : 'http://www.google.com',
        })
        self.assertFalse(form.is_valid())

    def testBigPrice(self):
        form = inventoryForm(data = {
            'itemName': 'Test Item',
            'itemType': 'Tablet',
            'quantityInStock' : 1,
            'price' : 999999999999999.00,
            'orderLink' : 'http://www.google.com',
        })
        self.assertFalse(form.is_valid())

    def testOrderLinkNotRequired(self):
        form = inventoryForm(data = {
            'itemName': 'Test Item',
            'itemType': 'Tablet',
            'quantityInStock' : 1,
            'price' : 999999999999999.00,
            'orderLink' : '',
        })
        self.assertFalse(form.is_valid())

    
    def testLinkStructure(self):
        form = inventoryForm(data = {
            'itemName': 'Test Item',
            'itemType': 'Tablet',
            'quantityInStock' : 1,
            'price' : 999999999999999.00,
            'orderLink' : 'hello',
        })
        self.assertFalse(form.is_valid())

    def testhttpsLink(self):
        form = inventoryForm(data = {
            'itemName': 'Test Item',
            'itemType': 'Tablet',
            'quantityInStock' : 1,
            'price' : 1.00,
            'orderLink' : 'https://www.google.com',
        })
        self.assertTrue(form.is_valid())

    def testNewDomains(self):
        form = inventoryForm(data = {
            'itemName': 'Test Item',
            'itemType': 'Tablet',
            'quantityInStock' : 1,
            'price' : 1.00,
            'orderLink' : 'http://www.get.shop',
        })
        self.assertTrue(form.is_valid())

    def testNonURL(self):
        form = inventoryForm(data = {
            'itemName': 'Test Item',
            'itemType': 'Tablet',
            'quantityInStock' : 1,
            'price' : 1.00,
            'orderLink' : 'test',
        })
        self.assertFalse(form.is_valid())

    def testNoHTMLURL(self):
        form = inventoryForm(data = {
            'itemName': 'Test Item',
            'itemType': 'Tablet',
            'quantityInStock' : 1,
            'price' : 1.00,
            'orderLink' : 'www.google.com',
        })
        self.assertTrue(form.is_valid())

