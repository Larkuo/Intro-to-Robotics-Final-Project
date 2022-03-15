**CS 353: Introduction to Robotics &amp; AI**

**Final Project: Option 3 || Implementation of Object Detection**

**Larkuo Wilson-Tetteh**

**14-12-2021**

In this project the objective was to implement object detection for all pairs of spectacles in an image frame. Some useful things to note are:

- _Loss function_: the difference between a model&#39;s prediction and the true value which is useful for model optimization during model training.
- _Common Objects in Context (COCO)_: a public large-scale dataset useful for object detection, segmentation and captioning.
- _RetinaNet_: an object detection architecture whose design is based on neural networks and has better precision than the widely known YOLO (you only look once).
- _resnet50\_coco\_v2.h5_: a RetinaNet based model pretrained on the COCO dataset.

To begin the project, 358 images were scrapped from Google Images with the search terms &#39;glasses&#39;, &#39;eyewear&#39;, &#39;medicated glasses&#39;, &#39;spectacles&#39; and &#39;spectacle frames&#39; using python selenium and a geckodriver for Firefox browser.

Following the data collection, the images were resized to 400x400 pixels each using a python script where OpenCV was used. After obtaining the resized images, the dataset was split into a 70%:30% ratio for training and testing respectively. Each image in the training set was then annotated with labels using LabelImg; a python-based graphical image annotation application which outputs xml files named similarly to the corresponding image files.

The processed and labelled data was then uploaded to Google Drive and imported into Google Colabs where it was visualized, reorganized into csv files and additional folders for model training.

After seeing a sample of the images with bound boxes and setting up folders, RetinaNet was cloned and installed. Then, the resnet50\_coco\_v2.h5 model was downloaded and model training began.

Four models were trained, saved, loaded and tested separately because Google Colabs&#39; free version had limits on GPU usage. For each model, it was trained based on an existing model with varying number of batch-size, number of steps and number of epochs which resulted in different loss values after each training session.

| **Model no.** | **Batch-size** | **Steps** | **Epochs** | **Pretrained Model** | **Loss** |
| --- | --- | --- | --- | --- | --- |
| Model 1 | 5 | 5 | 100 | resnet50\_coco\_v2.h5 | 1.4490 |
| Model 2 | 3 | 15 | 30 | model1.h5 | 0.4797 |
| Model 3 | 5 | 30 | 10 | model2.h5 | 0.2181 |
| Model 4 | 2 | 40 | 20 | model3.h5 | 0.1176 |

Overall, all four models were able to fairly accurately predict the values of the bound boxes if the image contained only one pair of spectacles at a time. However, the models did not work properly when predicting the bound boxes for images that had more than one pair of spectacles in frame.

_Google Colabs Notebook Link_: [Here](https://colab.research.google.com/drive/1AyVa0XAHdMetgbGakHl4ZJp0IY7YmFIV?usp=sharing)

_Google Drive Link to Training Data (Images, CSV & Models)_: [Here](https://drive.google.com/drive/folders/1sCGbrnmPyGrnh9lvIrmTCKG5NA8mTQUB?usp=sharing)