import itk
import sys
import vtk

def display_images(image_path1, image_path2):
    # Read the two images 
    reader1 = vtk.vtkJPEGReader()
    reader1.SetFileName(image_path1)
    reader2 = vtk.vtkJPEGReader()
    reader2.SetFileName(image_path2)

    # Create image viewers
    image_viewer1 = vtk.vtkImageViewer2()
    image_viewer1.SetInputConnection(reader1.GetOutputPort())
    image_viewer2 = vtk.vtkImageViewer2()
    image_viewer2.SetInputConnection(reader2.GetOutputPort())

    # Set up the rendering window and interactor
    render_window = vtk.vtkRenderWindow()
    interactor = vtk.vtkRenderWindowInteractor()

    # Set the interactor style for interacting with the image viewer
    image_viewer1.SetupInteractor(interactor)
    image_viewer2.SetupInteractor(interactor)

    # Set the position of the second image viewer in the same window
    image_viewer2.SetPosition(image_viewer1.GetPosition()[0] + image_viewer1.GetRenderWindow().GetSize()[0], image_viewer1.GetPosition()[1])

    # Render both images
    image_viewer1.Render()
    image_viewer2.Render()

    # Start the interactor and display the images
    interactor.Start()




if __name__ == "__main__":
    # Security to check the number of arguments
    if len(sys.argv) != 4:
        print("Usage: python script.py input_image output_image radius")
        sys.exit(1)

    # Arguments
    input_filename = sys.argv[1]
    output_filename = sys.argv[2]
    radius = int(sys.argv[3])

    # Read the image
    image = itk.imread(input_filename)

    # Apply median filter
    median = itk.median_image_filter(image, radius=radius)

    # Save the new image
    itk.imwrite(median, output_filename)

    #Display with VTK
    display_images(input_filename, output_filename)

