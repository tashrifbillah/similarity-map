This Python application takes user input for a region of interest (ROI) over an image and 
searches the whole image for regions similar to that of the ROI. Upon finding similar 
regions, it draws contours around them according to a user defined parameter.



## Installation

> pip install opencv-python scikit-image matplotlib

## Run

    git clone https://github.com/tashrifbillah/similarity-map.git
    cd similarity-map
    python app.py /path/to/image.jpg

An example image is provided with this repository. You can use that as:

    python app.py img/coins.jpg

Once the image is rendered in a window:

* draw a box around a coin by clicking and holding your mouse left button
* start drawing at top-left and finish at bottom-right
* after releasing the left button, press `q` for the computation to start
* follow instructions on the command line

## Workflow

The `app.py` comprises the following:

* `draw_box.py`: opens the given image, lets the user draw a bounding box around their 
region of interest (ROI), implemented via *opencv-python*.

* `sim_map.py`: the ROI is searched in the given image through a histogram matching algorithm, 
implemented via *scikit-image* and *matplotlib*

* `find_contours.py`: contours are drawn around the similarity map, implemented via *scikit-image* and *matplotlib*.
In addition, centers of the contours are saved in [centers.txt](measures/centers.txt) file.


## Configuration

The `app.py` accepts only one configurable parameter `level` (`[0,1]`) as in [here](https://scikit-image.org/docs/dev/api/skimage.measure.html#find-contours).
It renders a new set of contours for each new threshold provided on the command line.


## TODO

In this initial implementation, emphasis was given on runnability rather than accuracy. Moving forward, the following 
enhancement could be done:

* Draw contours satisfying some area criterion
* Devise a more robust matching method
* Make the Python app an web application

