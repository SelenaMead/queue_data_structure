import unittest
from queue_data_structure import Queue, Roller_Coaster_Queue

class TestProgram(unittest.TestCase):
    def test_program(self):

        queue = Queue()
        friends = ['Annabell', 'Bella', 'Carol', 'Danielle', 'Edith']
        for each_friend in friends:
                queue.enqueue(each_friend)

        self.assertEqual(queue.size(), 5)
        self.assertEqual(queue.first_element(), "Annabell")
        self.assertEqual(queue.last_element(), "Edith")
        self.assertEqual(queue.dequeue(), 'Annabell')
        
        
    