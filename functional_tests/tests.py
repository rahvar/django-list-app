from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from django.test import LiveServerTestCase

class NewVisitorTest(LiveServerTestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()

	def tearDown(self):
		
		self.browser.quit()

	def check_for_row_in_list_table(self, row_text):
	 	table = self.browser.find_element_by_id('id_list_table')
	 	rows = table.find_elements_by_tag_name('tr')
	 	self.assertIn(row_text, [row.text for row in rows])


	def test_can_start_a_list_and_retrieve_it_later(self):
	 	# Edith has heard about a .....
	 	# checkout its homepage
	 	self.browser.get(self.live_server_url)

	 	#she notices the page title and header mention to-do lists
	 	self.assertIn('To-Do', self.browser.title)
	 	header_text = self.browser.find_element_by_tag_name('h1').text
	 	self.assertIn('To-Do',header_text)
	
	 	# She is invited to enter a to-do item straight away
	 	inputbox = self.browser.find_element_by_id('id_new_item')
	 	self.assertEqual(
	 		inputbox.get_attribute('placeholder'),
	 		'Enter a to-do item'
	 		)

	 	# She types "Buy peacock feathers"
	 	# is tying fly-fishing lures
	 	inputbox.send_keys('Buy peacock feathers')

	 	# When she hits enter, the page updates and the page lists
	 	# "1: Buy peacock feathers" as an item in the to-do list table
	 	inputbox.send_keys(Keys.ENTER)
	 	
	 	self.check_for_row_in_list_table('1: Buy peacock feathers')

	 	# There is still a text box inviting her to add another item. She 
	 	# enters "Use peacock feathers to make a fly" (Edith is very 
	 	# methodical)
	 
	 	inputbox = self.browser.find_element_by_id('id_new_item')
	 	inputbox.send_keys('Use peacock feathers to make a fly')
	 	inputbox.send_keys(Keys.ENTER)

	 	# The page updates again,and now shows both items on her list
	 	self.check_for_row_in_list_table('1: Buy peacock feathers')
	 	self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')
	 	
	 	#Now a new user comes to the site
	 	## Use a new browser session to make sure no info of 
	 	## of Edith comes through from the cookies etc #
	 	self.fail('Finish the test')

	  

    # She visits that URL - her to-do list is still there.           
