import unittest


def find_rectangular_overlap(rect1, rect2):

    # Calculate the overlap between the two rectangles
    x2a=rect1['left_x']+rect1['width']
    x2b=rect2['left_x']+rect2['width']
    y2a=rect1['bottom_y']+rect1['height']
    y2b=rect2['bottom_y']+rect2['height']
    xr=max(rect1['left_x'],rect2['left_x'])
    yr=max(rect1['bottom_y'],rect2['bottom_y'])
    width=min(x2a,x2b)-xr
    height=min(y2a,y2b)-yr
    if((x2a<=rect2['left_x'] and y2a<=rect2['bottom_y']) 
        or ((y2a or rect1['bottom_y'])==rect2['bottom_y'])
        or (x2a or rect1['left_x'] )==rect2['left_x']):
        return{
            'left_x': None,
            'bottom_y': None,
            'width': None,
            'height': None,
        }

    return {
            'left_x': xr,
            'bottom_y': yr,
            'width': width,
            'height': height,
        }


















# Tests

class Test(unittest.TestCase):

    def test_overlap_along_both_axes(self):
        rect1 = {
            'left_x': 1,
            'bottom_y': 1,
            'width': 6,
            'height': 3,
        }
        rect2 = {
            'left_x': 5,
            'bottom_y': 2,
            'width': 3,
            'height': 6,
        }
        expected = {
            'left_x': 5,
            'bottom_y': 2,
            'width': 2,
            'height': 2,
        }
        actual = find_rectangular_overlap(rect1, rect2)
        self.assertEqual(actual, expected)


    def test_one_rectangle_inside_another(self):
        rect1 = {
            'left_x': 1,
            'bottom_y': 1,
            'width': 6,
            'height': 6,
        }
        rect2 = {
            'left_x': 3,
            'bottom_y': 3,
            'width': 2,
            'height': 2,
        }
        expected = {
            'left_x': 3,
            'bottom_y': 3,
            'width': 2,
            'height': 2,
        }
        actual = find_rectangular_overlap(rect1, rect2)
        self.assertEqual(actual, expected)

    def test_both_rectangles_the_same(self):
        rect1 = {
            'left_x': 2,
            'bottom_y': 2,
            'width': 4,
            'height': 4,
        }
        rect2 = {
            'left_x': 2,
            'bottom_y': 2,
            'width': 4,
            'height': 4,
        }
        expected = {
            'left_x': 2,
            'bottom_y': 2,
            'width': 4,
            'height': 4,
        }
        actual = find_rectangular_overlap(rect1, rect2)
        self.assertEqual(actual, expected)

    def test_touch_on_horizontal_edge(self):
        rect1 = {
            'left_x': 1,
            'bottom_y': 2,
            'width': 3,
            'height': 4,
        }
        rect2 = {
            'left_x': 2,
            'bottom_y': 6,
            'width': 2,
            'height': 2,
        }
        expected = {
            'left_x': None,
            'bottom_y': None,
            'width': None,
            'height': None,
        }
        actual = find_rectangular_overlap(rect1, rect2)
        self.assertEqual(actual, expected)

    def test_touch_on_vertical_edge(self):
        rect1 = {
            'left_x': 1,
            'bottom_y': 2,
            'width': 3,
            'height': 4,
        }
        rect2 = {
            'left_x': 4,
            'bottom_y': 3,
            'width': 2,
            'height': 2,
        }
        expected = {
            'left_x': None,
            'bottom_y': None,
            'width': None,
            'height': None,
        }
        actual = find_rectangular_overlap(rect1, rect2)
        self.assertEqual(actual, expected)

    def test_touch_at_a_corner(self):
        rect1 = {
            'left_x': 1,
            'bottom_y': 1,
            'width': 2,
            'height': 2,
        }
        rect2 = {
            'left_x': 3,
            'bottom_y': 3,
            'width': 2,
            'height': 2,
        }
        expected = {
            'left_x': None,
            'bottom_y': None,
            'width': None,
            'height': None,
        }
        actual = find_rectangular_overlap(rect1, rect2)
        self.assertEqual(actual, expected)

    def test_no_overlap(self):
        rect1 = {
            'left_x': 1,
            'bottom_y': 1,
            'width': 2,
            'height': 2,
        }
        rect2 = {
            'left_x': 4,
            'bottom_y': 6,
            'width': 3,
            'height': 6,
        }
        expected = {
            'left_x': None,
            'bottom_y': None,
            'width': None,
            'height': None,
        }
        actual = find_rectangular_overlap(rect1, rect2)
        self.assertEqual(actual, expected)
    def test_touch_on_horizontal_edge(self):
       rect1 = {
           'left_x': 1,
           'bottom_y': 0,
           'width': 5,
           'height': 4,
       }
       rect2 = {
           'left_x': 2,
           'bottom_y': 3,
           'width': 3,
           'height': 4,
       }
       expected = {
           'left_x': 2,
           'bottom_y': 3,
           'width': 3,
           'height': 1,
       }
       actual = find_rectangular_overlap(rect1, rect2)
       self.assertEqual(actual, expected)


unittest.main(verbosity=2)