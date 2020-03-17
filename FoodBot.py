from tensorflow.python.keras.models import load_model
import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage.transform import resize
import os
import glob
import sys

#Load pretrained model.
model = load_model('food_model3.h5')

#Specify inventory paths.
items = [line.strip() for line in open('categories.txt')]
inv_path = 'inventory.txt'
target_path = 'target_inv.txt'

class FoodBot:

    def __init__(self, inventory = inv_path, target = target_path, items = items):
        self.img = []
        self.inv = inventory
        self.target_level = target
        self.items = items

    def getFrame(self, sec):
        #Check if more frames left and import frame image.
        self.vidcap.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
        hasFrames, image = self.vidcap.read()

        if hasFrames:
            #Resize and store frame image.
            image = resize(image, output_shape = (100, 100,1))
            self.img.append(image)
        return hasFrames

    def vid_to_frame(self, path):
        #Import video file.
        self.vidcap = cv2.VideoCapture(path)

        #Video specifications
        fps = 25
        sec = 0
        frameRate = 1/fps
        count = 1

        #Check for frames.
        success = self.getFrame(sec)
        while success:
            count = count + 1
            sec = sec + frameRate
            sec = round(sec, 2)
            success = self.getFrame(sec)

    def add_item(self, path):
        #Convert film to frames.
        self.vid_to_frame(path)

        #Predict class probabilities for input images.
        data = np.asarray(self.img)
        prediction = model.predict(data)

        #Get mean probability for each class.
        mean_pred = np.mean(prediction, axis = 0)

        #Print all product probabilities.
        for i in range (len(self.items)):
            print('{}: {:.2f}%'.format(self.items[i], mean_pred[i]*100))

        #Get most probable item label.
        item_index = np.argmax(mean_pred)

        #Write item to inventory file.
        inv = open(self.inv, 'a')
        inv.write(str(item_index))
        inv.close()

        return item_index


    def shopping_list(self):
        #Examine inventories.
        inv = [int(line.strip()) for line in open(self.inv)]
        target = []
        for item in open(self.target_level).readlines():
            target.append(int(item.strip('\n')[0]))

        #Check inventory levels and compare to target.
        curr_level = np.asarray([inv.count(i) for i in range (len(self.items))])
        target = np.asarray(target)
        deficit = target - curr_level

        #Print shopping list to terminal.
        print('Shopping list: \n--------------')
        for i in range (len(deficit)):
            if deficit[i] > 0:
                print('{} {}s'.format(deficit[i], self.items[i]))
            else:
                pass

    def clear_inv(self):
        #Take user input.
        print('Are you sure you want to clear the inventory?')
        print('y - Yes.')
        print('n - No.')
        option = input()

        #Check if input is correct.
        assert option == 'y' or option == 'n', \
        'Please select one of the above options!'

        if option == 'y':
            #Clear inventory file.
            open(self.inv, 'w').close()
        else:
            pass



def main():

    film_path = 'test/'
    bot = FoodBot()

    print('Hi! What would you like to do? \n')
    print('1 - Add product to inventory.')
    print('2 - Access shopping list.')
    print('3 - Clear inventory.')

    option = int(input())

    assert option == 1 or option == 2 or option == 3, \
    'Please select one of the above options!'

    if option == 1:
        print('Great! Would you like to: \n')
        print('1 - Scan in new product (Raspberry Pi Camera required).')
        print('2 - Run test for avocado.')
        print('3 - Run test for potato.')

        option = int(input())

        assert option == 1 or option == 2 or option == 3, \
        'Please select one of the above options!'

        if option == 1:
            import scan
            added_item = bot.add_item('scan.mp4')
            print('Added {} to inventory.'.format(items[added_item]))

        elif option == 2:
            print('Please wait...')
            added_item = bot.add_item('avocado.mp4')
            print('Added {} to inventory.'.format(items[added_item]))

        else:
            print('Please wait...')
            added_item = bot.add_item('potato.mp4')
            print('Added {} to inventory.'.format(items[added_item]))

    elif option == 2:
        bot.shopping_list()

    else:
        bot.clear_inv()


main()
