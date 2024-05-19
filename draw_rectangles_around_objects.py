import json
import cv2
import os

def draw_rectangles_around_objects(initial_folder_with_images, coco_annotations_file, result_folder):
    if not os.path.exists(initial_folder_with_images):
        raise FileNotFoundError(initial_folder_with_images)
    if not os.path.exists(coco_annotations_file):
        raise FileNotFoundError(coco_annotations_file)

    # loading coco_annotations from the JSON file
    with open(coco_annotations_file, "r") as f:
        coco_annotations = json.load(f)

    # checking if result_folder_path exist or not
    # if it does not exist we will create it with os.makedirs function
    # if it exists the error will not be raised
    os.makedirs(result_folder, exist_ok=True)

    # creating a path to images
    # os.listdir returns a list with all files from initial_folder_with_images
    # os.path.join joins directory path of an item with its filename
    for image_filename in os.listdir(initial_folder_with_images):
        image_path = os.path.join(initial_folder_with_images, image_filename)

        # loading image with cv2.imread() function
        image = cv2.imread(image_path)
        if image is None:
            print(f"Image is not founded: {image_path}")
            continue

        # looking for image_id in COCO annotations by image_filename
        # the dictionary with file_names and respective ids from 'images' list in COCO annotations is created
        # image_id returns value of respective key which contain image_filename
        filename_to_id = {image_info['file_name'].removeprefix("data/"): image_info['id'] for image_info in coco_annotations['images']}
        image_id = filename_to_id.get(image_filename)
        if image_id is None:
            print(f"No annotation for this image: {image_filename}")
            continue
        # looking for respective annotation by image_id
        image_annotations = [annotation for annotation in coco_annotations["annotations"] if annotation["image_id"] == image_id]

        # drawing bounding boxes on the image and printing respective category_name
        # category_name is found by comparing category_id in image_annotations and in 'categories' list in COCO annotations
        for annotation in image_annotations:
            category_id = annotation["category_id"]
            category_info = next((category for category in coco_annotations["categories"] if category["id"] == category_id), None) # next() returns first match
            category_name = category_info["name"]
            bbox = annotation["bbox"]
            x, y, width, height = bbox
            print(f"Category: {category_name}, Bbox: {bbox}")
            # (x, y) is top-left corner of rectangle
            # (x+width, y+height) is top-right corner
            # (0,255,0) - color BGR, and 2 is thickness
            cv2.rectangle(image, (int(x), int(y)), (int(x + width), int(y + height)), (0, 255, 0), 2)
            cv2.putText(image, category_name, (int(x), int(y) - 5), cv2.FONT_HERSHEY_SIMPLEX,  0.5, (0, 255, 0), 2)

        # creating result_folder_path by concatenating image_filename and result_folder
        result_folder_path = os.path.join(result_folder, image_filename)
        # saving an image to a result_folder
        cv2.imwrite(result_folder_path, image)

# specifying the paths by input() function
initial_folder_with_images = input( "Provide the path to the folder with images")
coco_annotations_file = input("Provide the path to the JSON file with COCO annotations")
result_folder = input("Provide the path to the folder where final results should be saved or create the name of the folder to save results there")
# calling the function
draw_rectangles_around_objects(initial_folder_with_images, coco_annotations_file, result_folder)







