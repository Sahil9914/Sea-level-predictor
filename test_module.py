import unittest
import sea_level_predictor

class SeaLevelPredictorTestCase(unittest.TestCase):
    def test_draw_plot(self):
        ax = sea_level_predictor.draw_plot()
        self.assertEqual(ax.get_xlabel(), 'Year')
        self.assertEqual(ax.get_ylabel(), 'Sea Level (inches)')
        self.assertEqual(ax.get_title(), 'Rise in Sea Level')

if __name__ == "__main__":
    unittest.main()
