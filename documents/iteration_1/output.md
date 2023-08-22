![ref1]

**Evaluation Only. Created with Aspose.Words. Copyright 2003-2023 Aspose Pty Ltd.**

Available online at www.sciencedirect.com ![](output.002.png)![](output.003.png)![](output.004.png)

![](output.005.png) **ScienceDirect** 

Procedia Computer Science 163 (2019) 85–92 

16th International Learning & Technology Conference 2019 

A Method Of Skin Disease Detection Using Image Processing And Machine Learning 

Nawal Soliman ALKolifi ALEnezi 

*Department of Computer Science and Engineering, Umm AL-Qura University , Makkah , Saudi Arabia ![ref2]*

**Abstract** 

Skin diseases are more common than other diseases. Skin diseases may be caused by fungal infection, bacteria, allergy, or viruses, etc. The advancement of lasers and Photonics based medical technology has made it possible to diagnose the skin diseases  much  more quickly and accurately. But the cost of such diagnosis is still limited and very expensive. So, image processing techniques help to build automated screening system for dermatology at an initial stage. The extraction of features plays a key role in helping to classify skin diseases. Computer vision has a role in the detection of skin diseases in a variety of techniques. Due to deserts and hot weather, skin diseases are common in Saudi Arabia. This work contributes in the research of skin disease detection. We proposed an image processing-based method to detect skin diseases. This method takes the digital image of disease effect skin area, then use image analysis to identify the type of disease. Our proposed approach is simple, fast and does not require expensive equipment other than a camera and a computer. The approach works on the inputs of a color image. Then resize the of the image to extract features using pretrained convolutional neural network. After that classified feature using Multiclass SVM. Finally, the results are shown to the user, including the type of disease, spread, and severity. The system successfully detects 3 different types of skin diseases with an accuracy rate of 100%. 

© 2019 The Authors. Published by Elsevier B.V.

This is an open access article under the CC BY-NC-ND license (https://creativecommons.org/licenses/by-nc-nd/4.0/) Peer-review under responsibility of the scientific committee of the 16th International Learning & Technology Conference 2019.

*Keywords:* Skin diseases; Image Processing; Computer Vision; Machine Learning. ![ref2]

1. **Introduction** 

Skin diseases are more common than other diseases. Skin diseases may be caused by fungal infection, bacteria, allergy, or viruses, etc. A skin disease may change texture or color of the skin. In general, skin diseases are chronic, infectious and sometimes may develop into skin cancer. Therefore, skin diseases must be diagnosed early to reduce 

1877-0509 © 2019 The Authors. Published by Elsevier B.V.

This is an open access article under the CC BY-NC-ND license (https://creativecommons.org/licenses/by-nc-nd/4.0/) Peer-review under responsibility of the scientific committee of the 16th International Learning & Technology Conference 2019. 10.1016/j.procs.2019.12.090

**Created with an evaluation copy of Aspose.Words. To discover the full versions of our APIs please visit: https://products.aspose.com/words/**
![ref3]*Nawal Soliman ALKolifi ALEnezi  / Procedia Computer Science 163 (2019) 85–92*  91

2  *Nawal Soliman ALKolifi ALEnezi/ Procedia Computer Science 00 (2019) 000–000* 

their development and spread. The diagnosis and treatment of a skin disease takes longer time and causes financial and physical cost to the patient. 

In general, most of the common people do not know the type and stage of a skin disease. Some of the skin diseases show symptoms several months later, causing the disease to develop and grow further. This is due to the lack of  medical  knowledge in the public. Sometimes, a  dermatologist (skin specialist doctor) may also find it difficult to diagnose the skin disease and may require expensive laboratory tests to correctly identify the type and stage of the skin disease. The advancement of lasers and photonics based medical technology has made it possible to diagnose the skin diseases much more quickly and accurately. But the cost of such diagnosis is still limited and very expensive. Therefore, we propose an image processing-based approach to diagnose the skin diseases. This method takes the digital image of disease effect skin area then use image analysis  to identify the type of disease. Our proposed approach is simple, fast and does not require expensive equipment's other than a camera and a computer. 

2. **Review of Literature** 

Several researchers have proposed image processing-based techniques to detect the type of skin diseases. Here we briefly review some of the techniques as reported in the literature. 

In [1], a system is proposed for the dissection of skin diseases using color images without the need for doctor intervention. The system consists of two stages, the first the detection of the infected skin by uses color image processing techniques, k-means clustering and color gradient techniques to identify the diseased skin and the second the classification of the disease type using artificial neural networks. The system was tested on six types of skin 

diseases with average accuracy of first stage 95.99% and the second stage 94.016%. 

In the method of [2], extraction of image features is the first step in detection of skin diseases. In this method, the greater number of features extracted from the image, better the accuracy of system. 

The author of [2] applied the method to nine types of skin diseases with accuracy up to 90%. 

Melanoma is type of skin cancer that can cause death, if not diagnose and treat in the early stages. The author of [3], focused on the study of various segmentation techniques that could be applied to detect melanoma using image 

processing. Segmentation process is described that falls on the infected spot boundaries to extract more features. 

The  work  of  [4]  proposed  the  development  of  a  Melanoma  diagnosis  tool  for  dark  skin  using  specialized algorithm databases including images from a variety of Melanoma resources. Similarly, [5] discussed classification of skin diseases such as Melanoma, Basal cell carcinoma (BCC), Nevus and Seborrheic keratosis (SK) by using the 

technique support vector machine (SVM). It yields the best accuracy from a range of other techniques. 

On  the  other  hand,  the  spread  of  chronic  skin  diseases  in  different  regions  may  lead  to  severe  consequences. Therefore, [6] proposed a computer system that automatically detects eczema and determines its severity. The system consists of three stages, the first effective segmentation by detecting the skin, the second extract a set of features, namely color, texture, borders and third determine the severity of eczema using Support Vector Machine 

(SVM). 

In [7], a new approach is proposed to detect skin diseases, which combines computer vision with machine learning. The role of computer vision is to extract the features from the image while the machine learning is used to detect skin diseases. The system was tested on six types of skin diseases with accurately 95%. 

3. **Description of The Dataset** 

`  `We compiled our dataset by collecting images from different websites specific to skin diseases. The database has 80 images of every disease (20 Normal images, 20 Melanoma images, 20 Eczema images and 20 Psoriasis images). Fig 1 shows some of the sample images from our dataset. 

![](output.008.png)

Fig. 1. The first image is eczema, the second Melanoma; the third is psoriasis, and finally healthy skin. 

4. **Methodology** 

In this section, the methodology of the proposed system for detection, extraction and classification of skin diseases images is described. The system will help significantly in the detection of melanoma, Eczema and Psoriasis. The whole architecture can be divided into several modules comprising of preprocessing, feature extraction, and 

classification. The block diagram of the system is shown in Fig 2. 

![](output.009.png)

Fig. 2. The proposed system block diagram. 

1. *Preprocessing:* 

Achieving high performance of skin disease detection system requires overcoming some major difficulties. Such as creating a database and  unifying image dimensions. In the  following section, the  technique  used in  image resizing is explained. 

·  *Image Resizing:* 

To resolve the problem of different image sizes in the database an input image is either increase or decrease in size. Unifying the image size will get the same number of features from all images. Moreover, resizing the image reduces processing time and thus increases system performance. Fig 3 shows the original image of size is 260×325 pixels. Fig 4 shows the resized image with the new size of 227×227 pixels. 

![](output.010.png)

Fig. 3. Example of Original image of Eczema database. 

![](output.011.png)

Fig. 4. Example of resizing image of Eczema database. 

2. *Feature Extraction:* 

At the beginning, Convolutional Neural Network (CNN) is a set of stacked layers involving both nonlinear and linear processes. These layers are learned in a joint manner. The main building blocks of any CNN model are: convolutional layer, pooling layer, nonlinear Rectified Linear Units (ReLU) layer connected to a regular multilayer neural network called fully connected layer, and a loss layer at the backend. CNN has known for its significant performance in applications as the visual tasks and natural language processing [8]. 

![](output.012.png)

Fig. 5. AlexNet block diagram [8]. 

AlexNet is a deep CNN model, developed by Krizhevsky et al. [8], to model the 2012 ImageNet for the Large Scale  Visual  Recognition  Challenge  (ILSVRC-2012).  AlexNet  consists  of  five  convolutional  layers;  where  a nonlinear ReLU layer is stacked after each convolutional layer. In addition, the first, second, and fifth layers contain maxpooling layers, as shown in Figure 5. Moreover, two normalization layers are stacked after the first and the second convolutional layers. Furthermore, two fully connected layers at the top of the model preceded by softmax 

layer. AlexNet was trained using more than 1.2 million images belonging to 1000 classes [8]. 

We proposed feature extraction from a pretrained convolutional neural network. Because it is the easiest and 

robust approach to use the power of pretrained deep learning networks. 

3. *Classification:* 

Classification is a computer vision method. After extracting features, the role of classification is to classy the image via Support Vector Machine (SVM). A SVM can train classifier using extracted features from the training set [9]. 

5. **Result** 

The system is implemented in MATLAB 2018b. We used a platform of Intel Core i3 processor 2.10 GHz with 4- GB RAM. 

The Implementation results are shown in Figure 6. Initially, the input images are preprocessed, then features are extracted using pretrained CNN. Finally, classification is performed using SVM classifier. 

![](output.013.png)

Fig. 6. Result Screen. 

In this study, 100 skin images were used by several dermatological disease patients, also were taken from the Internet. The proposed system can successfully detect 3 different skin diseases with an accuracy of 100%. 

We have used 20 of images for validation purpose and 80 images for training purpose. The system works well. The detection rate of our system is 100%. In the Table 5.1 we can see different detection rate for 3 different diseases. The detection rate of diseases is very high 100%. 

6. **Future Work** 

Jason Fried says, “When is your product or service finished? When should you put it out on the market? When is it safe to let people have it? Probably a lot sooner than you are comfortable with. Once your product does what it 

needs to do, get it out there [10]. 

Just because you have still got a list of things to do does not mean it is not done. Do not hold everything else up because of a few leftovers. You can do them later. And doing them later may mean doing them better, too. [10]. There are many enhancements and extensions which will be added in the future, first, the method of detect skin disease must be on the mobile application developed, then detection the skin lesion in Dermis layer of the skin, finally must detect all the skin disease in the world and degree of disease. 

7. **Conclusion** 

Detection  of  skin  diseases  is  a  very  important  step  to  reduce  death  rates,  disease  transmission  and  the development of the skin disease. Clinical procedures to detect skin diseases are very expensive and time-consuming. Image processing techniques help to build automated screening system for dermatology at an initial stage. The extraction of features plays a key role in helping to classify skin diseases. 

In  this  research  the  method  of  detection  was  designed  by  using  pretrained  convolutional  neural  network (AlexNet) and SVM. In conclusion, we must not forget that this research has an effective role in the detection of skin diseases in Saudi Arabia because it has a very hot weather for the presence of deserts; this indicates that skin diseases are widespread. This research supports medical efficiency in Saudi Arabia. 

Table 1. Disease Detection Rate 

Disease  Sample  Image  Total  Disease  Detection ![](output.014.png)Name  Image  detected  rate % ![](output.015.png)![](output.016.png)![](output.017.png)

Eczema  5  5  100% ![](output.018.png)![](output.019.png)

Melanoma  5  5  100% ![](output.020.png)![](output.021.png)

Psoriasis  5  5  100%![](output.022.png)![](output.023.png)

Healthy  5  5  100% ![](output.024.png)

skin ![](output.025.png)

**Created with an evaluation copy of Aspose.Words. To discover the full versions of our APIs please visit: https://products.aspose.com/words/**
![ref4]  *Nawal Soliman ALKolifi ALEnezi  / Procedia Computer Science 163 (2019) 85–92*

8  *Nawal Soliman ALKolifi ALEnezi/ Procedia Computer Science 00 (2019) 000 000* 

**References** 

1. Arifin, S., Kibria, G., Firoze, A., Amini, A., & Yan, H. (2012) “Dermatological Disease Diagnosis Using Color-Skin Images.” Xian: 

*International Conference on Machine Learning and Cybernetics*. 

2. Yasir, R., Rahman, A., & Ahmed, N. (2014) “Dermatological Disease Detection using Image Processing and Artificial Neural Network. 

“Dhaka*: International Conference on Electrical and Computer Engineering*. 

3. Santy, A., & Joseph, R. (2015) “Segmentation Methods for Computer Aided Melanoma Detection.” *Global Conference on* 

*Communication* *Technologies.* 

4. Zeljkovic, V., Druzgalski, C., Bojic-Minic, S., Tameze, C., & Mayorga, P. (2015) “ Supplemental Melanoma Diagnosis for Darker 

Skin Complexion Gradients.” *Pan American Health Care Exchanges* 

5. Suganya R. (2016) “An Automated Computer Aided Diagnosis of Skin Lesions Detection and Classification for Dermoscopy Images.” *International Conference on Recent Trends in Information Technology*. 
5. Alam, N., Munia, T., Tavakolian, K., Vasefi, V., MacKinnon, N., & Fazel-Rezai, R. (2016) “Automatic Detection and Severity 

Measurement of Eczema Using Image Processing.” *IEEE*. 

7. Kumar, V., Kumar, S., & Saboo, V. (2016) “Dermatological Disease Detection Using Image Processing and Machine Learning.” *IEEE*. 
7. Krizhevsky, A., ILYA, S., & Geoffrey, E. (2012) “ImageNet Classification with Deep Convolutional Neural Networks.” *Advances in* 

*Neural* *Information Processing Systems.* 

9. Cristianini, N., Shawe, J., “Support Vector Machines”, 2000. 
9. SOMMERVILLE, I., “Software Engineering”. 9th .2011. 

**Created with an evaluation copy of Aspose.Words. To discover the full versions of our APIs please visit: https://products.aspose.com/words/**
![ref5]

![](output.028.png)
**Created with an evaluation copy of Aspose.Words. To discover the full versions of our APIs please visit: https://products.aspose.com/words/**

[ref1]: output.001.png
[ref2]: output.006.png
[ref3]: output.007.png
[ref4]: output.026.png
[ref5]: output.027.png
