# First_Exercise : Image Processing 

## Short Description about the exercise

This python script uses <strong>"itk"</strong> library to apply a filter to an image. Then, it is possible to see the two images (the original image and the filtered one) with the <strong>"vtk"</strong> library.

## Preparation

Before you start, you have to clone the git repository with this command : 

```
git clone https://github.com/FlorianDAVAUX/First_Exercise.git
```
Then, you have ton install the two librairies :

```
pip3 install itk vtk
```

## Use

To run the code you have to write this line in the terminal :

```
python3 exercise.py input_image output_image radius
```
- input_image : the path to the image you want to filter
- output_image : the path to save the image filtered
- radius : the radius if the median filter

## How it works

### Image Processing 
1. First, the script read the image with <strong>"itk.imread()"</strong>
2. Then, it applies the median filter with <strong>"itk.median_image_filter()"</strong>
3. Finally, it saves the new image with <strong>"itk.imwrite()"</strong>

### Image Visualization
Thanks to the function <strong>"display_images(image_path1, image_path2)"</strong> with the two images path arguments
1. First, it reads the two images with <strong>"vtkJPEGReader()"</strong>
2. Then, it creates image viewers with <strong>"vtk.vtkImageViewer2()"</strong> to visualise the image
3. It sets up the rendering window and interactor with <strong>"vtk.vtkRenderWindow()"</strong> and <strong>"vtk.vtkRenderWindowInteractor()"</strong>
4. Then, set the interactor style for interacting with the image viewer
5. Set the position of the second image viewer in the same window
6. Render both images
7. Start the interactor and display the images

