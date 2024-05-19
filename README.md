# Draw rectangles around objects in the images

## Project Description

Function takes images and COCO annotations, and returns folder with images where rectangles are already drawn.

### Technologies used
Python programming language 

Libraries: json, cv2, os

* json - used to read the data from file and load it to python dictionary.
* cv2 - used to process the images.
* os - used for interacting with operating system.

### Code explanation

In this line we are creating a function which takes as an input: initial_folder_with_images, coco_annotations_file and result_folder:
``` def draw_rectangles_around_objects(initial_folder_with_images, coco_annotations_file, result_folder):```.

Next step is to check if our files with initial images and coco annotations are exist. In order to do this ``` os.path.exists ``` function from ``` os.module``` is used.
If path exist it proceed further, otherwise raises ```FileNotFoundError```.

After that we are reading json file and loading it in python dictionary:
``` with open(coco_annotations_file, "r") as f:```
      ``` coco_annotations = json.loads(f) ```.

Next step is to check if result_folder exist or not. If it does not exist it will create it. Otherwise, proceed further: ```os.makedirs(result_folder, exist_ok= True)```.

In next line of code we are creating the full path to each image. For this purpose ``os.listdir`` and ``os.path.join`` functions are used. First to create a list with all files from initial_folder_with_images, second to join image_filename with directory name. We are iterating through a list of files and creating image_path for each image: ``    for image_filename in os.listdir(initial_folder_with_images):
        image_path = os.path.join(initial_folder_with_images, image_filename)``.

After creating image_path it is used to load each image with ``cv2.imread()`` function: ``image = cv2.imread(image_path)``. If image do not exist the function prints "Image not found" and provides its image_path.

Next step is to find image_id which will be used latter-on in order to find right annotations for each image.
* Firstly, list with file_name and id from 'images' list in COCO annotations is created. As filenames in this list have prefix "data/" it is removed with ``removeprefix`` method. The key/value pair reflects to file_name and id. 
* After that the id with respect to image_filename is stored in image_id variable: ```image_id = filename_to_id.get(image_filename)```.
* If image_id is not founded, function will print "No annotation for this image".

Now image_annotations can be found by comparing image_id which is already found from 'images' list and image_id from 'annotations' list:``` image_annotations = [annotation for annotation in annotations["annotations"] if annotation["image_id"] == image_id]```.

Next step is to draw bounding boxes and write category_id in the image. 
* Category_name is found by comparing category_id in image_annotations and 'categories' list in COCO annotations. It creates category_info variable which returns a list with category_id and category_name if category_id is equal to category_id from 'annotations'. In order to do this it uses next() function which returns first match by given condition, or None if condition do not satisfied:   ```        for annotation in image_annotations:
            category_id = annotation["category_id"]
            category_info = next((category for category in annotations["categories"] if category["id"] == category_id), None) 
            category_name = category_info["name"]  ```.
* To draw bounding boxes we extract x, y, width and height values from annotations and use cv2.rectangle() function: ``cv2.rectangle(image, ((x, y), (x+width, y+height)),(0,255,0), 2)``. Here ``(x,y)`` means top-left corner of rectangle and ``(x+width, y+height)`` top-right corner. ``(0,255,0)`` means color in BGR cheme. ``2`` is thickness.
* To print category_name cv2.putText() function is used: ``cv2.putText(image, category_name, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX,  0.5, (0,255,0), 2)``, where ``0.5`` is a font-scale. 

In order to save the result image_filename and result_folder is joint and saved into result_folder_path variable. Using cv2.imwrite() function images with rectangles and category_name on it are saved: ``cv2.imwrite(result_folder_path, image)``.

Last step is paths specifying and function calling. By input() function user provides paths for ``initial_folder_with_images``, ``coco_annotations_file``, ``result_folder`` by entering it from keyboard. 

