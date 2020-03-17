# FoodBot

A Raspbery Pi microprocessor was implemented with a machine learning model utilising Convolutional Neural Networks to classify a set of food products and use the outputs in a range of practical functionalities, such as keeping track of inventory.

List and content of files:

1) train_model.ipynb - Jupyter Notebook containing CNN model training procedure.
2) FoodBot.py - Python script demonstrating all implemented functionalities.
3) scan.py - Python script initiating video recording on Raspberry Pi (initiated in FoodBot.py).
4) categories.txt - text file containing food product classes recognisable by the model.
5) inventory.txt - text file containing current product inventory.
6) target_inv.txt text file containing target inventory levels.
7) food_model3.h5 - pre-trained Keras model.
8) avocado.mp4 - test film of avocado (initiated in FoodBot.py).
9) potato.mp4 - test film of potato (initiated in FoodBot.py).

The scripts are fully implemented and ready to run with or without the use of a Raspberry Pi.
In order to run the scripts on either devices the following libraries are required (at minimum):
- Tensorflow
- OpenCV
- NumPy
- Matplotlib
- skimage
- picamera (if using with Raspberry Pi)

To experience full functionality load files 2-9 onto a Raspberry Pi fitted with a camera attachment
ensuring that they are all saved to the same directory as run FoodBot.py. The program will prompt
you for inputs, for example:

Hi! What would you like to do?
1 - Add product to inventory.
2 - Access shopping list.
3 - Clear inventory.

If you want to for example add a product to the inventory you would type the number 1 when prompted
and submit with 'Enter'.

Note: The training/validation datasets are not included because they are very large files, so if the
notebook (file 1) is re-run it might output a 'No such file in directory.' error. However, the
scrips are very general (see Report), so changing the 'data_path' variable at the top to a path containing
folders with images is sufficient to run (and re-train) the model. The notebook is submitted in a fully run
format.
