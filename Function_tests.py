import unittest

from draw_rectangles_around_objects import draw_rectangles_around_objects

class TestClass(unittest.TestCase):
    def test_initial_folder_with_images_not_found(self):
        with self.assertRaises(FileNotFoundError):
            draw_rectangles_around_objects('not_existed_folder_with_images', 'coco_annotations_file', 'result_folder')

    def test_coco_annotations_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            draw_rectangles_around_objects('initial_folder_with_images', 'not_existed_coco_annotations_file',
                                           'result_folder')

    # {test which checks if coco_annotations_file is opening correctly}
    # {test to check if the result_folder is created}
    # {test to check if path to images are created}
    # {test to check if image is exist and loaded}
    # {test to check if image_id is found correctly with respect to filename}
    # {test to check if annotations for each image is found}
    # {test to check if bounding boxes drawn correctly and text is written}
    # {test to check if result_folder_path created}
    # {test to check if result is saved}

