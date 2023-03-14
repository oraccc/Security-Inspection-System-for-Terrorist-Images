

### Secutiry Inspection System for Terrorist Images

We conducted research on the security detection of violent and terrorist images on the internet, and developed a deep learning-based security review system for such images. Our system employs algorithms and solutions from four different perspectives, including **deep learning model detection**, **analysis of image text content**, **recognition of the faces of leaders of violent and terrorist groups**, and **detection of specific targets associated with violent and terrorist activities**. Finally, we adopted a multi-solution joint mechanism to improve the limitations and detection rate of existing solutions.

#### Innovations

Our innovations are as follows: 

- [x] Our system has a comprehensive range of functions, including classification of violent and terrorist levels and scenes, analysis of text and images related to violent and terrorist activities, recognition of leaders of violent and terrorist groups, and detection of specific targets such as guns and flags. This makes our system the most comprehensive among current platforms for detecting violent and terrorist images. 
- [x] Compared to traditional single algorithms, we use a joint detection algorithm that achieves higher accuracy and expands the range of functions while improving the detection accuracy. 
- [x] We have established corresponding datasets of violent and terrorist text and images, and have expanded these datasets using GAN networks and other technologies. This not only supports data training but also provides ideas for improving algorithms. 
- [x] We have designed a user-friendly interface that supports both separate and joint detection of violent and terrorist images, as well as queries for single images or datasets.

#### Usage

* **Environment**
  * Django >= 3.0
  * wagtail >= 2.9
* **Run System**
  * `python manage.py makemigrations`
  * `python manage.py migrate`
  * `python manage.py runserver`
  * open browser and visit `127.0.0.1:8000/home`