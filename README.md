# Fellowuship.AI ResNet18 Challenge 

### Challenge 

Use a pretrained ResNet 18 and train on the Flowers dataset. Use cut-out and discriminative learning rates. Measure its effect on your model's performance.

## Resources

  ### Model
  
  ***ResNet18***

  <p>Main :	https://pytorch.org/docs/stable/torchvision/models.html#torchvision.models.resnet18 </p>
  <p>Tutorial :	https://pytorch.org/tutorials/beginner/transfer_learning_tutorial.html </p>

  ### Dataset
  
   ***Flower Dataset***

   Link :	http://www.robots.ox.ac.uk/~vgg/data/flowers/102/

  ### Image Augmentation and Regularization Technique

  ***Cut-out***

  <p>Main : https://paperswithcode.com/method/cutout </p>
  <p>Tutorial : https://github.com/uoguelph-mlrg/Cutout </p>

  ***Discriminative Learning Rates***

  Link : https://www.deeplearningwizard.com/deep_learning/boosting_models_pytorch/lr_scheduling/
 

## Model Description 

  - ResNet18 is shallow enough that it does'nt have any issue durnig training, but is deep enoguh to learn complex features.
  - ResNet model have architecture that allows the network to skip training for the layers that are not useful and do not add value in overall accuracy
  - Resnet18 model pretrained on Imagenet dataset.
  - Frozen pretrained layers.
  - Training of model only occurs in custom layer.
  - Custom output dense layer added with 102 output nodes.

## Code
  
  Code Explanation present in notebook and .py files
  
  - After downloadling dataset run dataset_handling.py file to place images in folders based on their class and folder type (Image used in training and of class 1 will      placed in train/1 folder)
  - To run the model with Cutout use resnet18_cutout.ipynb file
  - To run the mode without Cutout use resnet18.ipynb file

## Results and Conclusion

  - All the models are trained for 100 epochs

  ### Base Model
  
  - Cutout and DLR methods were not used to train and test this model.
  - Out of 4 models the base model has the highest accuracy.
  - It also converged in least number of epochs.
  
  Best Validation Accuracy : 86.56% 
  Best Validation Loss : 0.65 (Apporox)
  
 ![Screenshot](https://github.com/9harshit/fellowshipai-resnet-challenge/blob/main/images/model_basic.png)
  
  ### Model with Discriminative Learning Rates
  
  - DLR method is used to train and test this model.
  - Changes in accuracy and loss became stagnant after 40th epoch due to the weight decay.
  - However validation loss is still quite low
  
  Best Validation Accuracy : 83.23% 
  Best Validation Loss : 0.66 (Apporox)

 ![Screenshot](https://github.com/9harshit/fellowshipai-resnet-challenge/blob/main/images/model_dlr.png)
  
   ### Model with Cut-out
   
  - Cutout method is used to train and test this model.
  - Model Accuracy and loss are competitve.
  - Model keepting converging throughout the training, which leads to the conclusion that cutout method did force the model to keep learning new features from the images every epoch.
  - Trainig the model on more number of epochs could lead to high accuracy. 
  
  Best Validation Accuracy : 82% 
  Best Validation Loss : 0.82 (Apporox)

  ![Screenshot](https://github.com/9harshit/fellowshipai-resnet-challenge/blob/main/images/model_cutout.jpg)
  
  ### Model with Cut-out and Discriminative Learning Rates
  
  - Cut-Out and DLR methods were both used to train and test this model.
  - Least accurate model.
  - Highest validatoin loss.
  - Convergence halted after 20th epoch due to less image data and weight decay,
  
  Best Validation Accuracy : 79% 
  Best Validation Loss : 0.91 (Apporox)

  ![Screenshot](https://github.com/9harshit/fellowshipai-resnet-challenge/blob/main/images/model_cutout_dlr.png)
  
  
  ### Obeservations
  
  - Though cutout method theretical and practically does force the model to learn different features of the data and not just the main features, hgiher accuracy of base model proves that giving information rich data to model will always provide better results. 
  - Discriminative learning rates  should not used in initial part of trainig since at later stages of the training learning rate is reduced dramatically and due to which model does not learn in later epochs. However the DLR should be programmed to activated after 60-70% of the training is completed to avoid overfitting but still allwoing the model to keep and learning and discover new features special in transfer learning.

