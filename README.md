

### Secutiry Inspection System for Terrorist Images

We conducted research on the security detection of violent and terrorist images on the internet, and developed a deep learning-based security review system for such images. Our system employs algorithms and solutions from four different perspectives, including **deep learning model detection**, **analysis of image text content**, **recognition of the faces of leaders of violent and terrorist groups**, and **detection of specific targets associated with violent and terrorist activities**. Finally, we adopted a multi-solution joint mechanism to improve the limitations and detection rate of existing solutions.



* **Environment**
  * Django >= 3.0
  * wagtail >= 2.9
* **Run System**
  * `python manage.py makemigrations`
  * `python manage.py migrate`
  * `python manage.py runserver`
  * open browser and visit `127.0.0.1:8000/home`