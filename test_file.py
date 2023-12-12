import unittest
from DRDViz import DRDViz
from node import Node
from edge import Edge

class TestDRDViz(unittest.TestCase):

    def setUp(self):
        self.visualizer = DRDViz()

    def test_init(self):
        self.assertEqual(len(self.visualizer.nodes), 0)
        self.assertEqual(len(self.visualizer.edges), 0)
        self.assertEqual(len(self.visualizer.nodeIndex), 0)
        self.assertEqual(len(self.visualizer.markedNodes), 0)
        self.assertEqual(len(self.visualizer.markedEdges), 0)

    def test_loadGraphFromFile(self):
        # Which is the 'test1.txt' contains the correct format as specified
        self.visualizer.loadGraphFromFile('test1.txt')
        # Check if nodes and edges are loaded correctly
        self.assertNotEqual(len(self.visualizer.nodes), 0)
        self.assertNotEqual(len(self.visualizer.edges), 0)

    def test_reset(self):
        # Load graph and mark some nodes and edges
        self.visualizer.loadGraphFromFile('test1.txt')
        self.visualizer.markedNodes.append(self.visualizer.nodes[0])
        self.visualizer.markedEdges.append(self.visualizer.edges[0])
        self.visualizer.reset()
        # After reset, marked nodes and edges should be empty
        self.assertEqual(len(self.visualizer.markedNodes), 0)
        self.assertEqual(len(self.visualizer.markedEdges), 0)

    def test_save(self):
        # Load graph and save the plot to a file
        self.visualizer.loadGraphFromFile('test1.txt')
        output_file = 'test_output.png'
        self.visualizer.save(output_file)
        # Check if the file is created
        self.assertTrue(os.path.isfile(output_file))
        # Clean up the file after test
        os.remove(output_file)

    def test_markStart(self):
        # Assign a start label
        start_label = 'A'  
        self.visualizer.markStart(start_label)
        self.assertIn(start_label, self.visualizer.nodeStyles)
        self.assertEqual(self.visualizer.nodeStyles[start_label], ('D', 'c'))

    def test_markGoal(self):
        # Assign a goal label
        goal_label = 'B' 
        self.visualizer.markGoal(goal_label)
        self.assertIn(goal_label, self.visualizer.nodeStyles)
        self.assertEqual(self.visualizer.nodeStyles[goal_label], ('D', 'r'))
        # Add more assertions here if necessary

if __name__ == '__main__':
    unittest.main()
