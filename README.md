# Fellowuship.AI ResNet18 Challenge 

### Challenge 

Use a pretrained ResNet 18 and train on the Flowers dataset. Use cut-out and discriminative learning rates. Measure its effect on your model's performance.

## Resources

  ### Model
  
  ***ResNet18***

  Main :	https://pytorch.org/docs/stable/torchvision/models.html#torchvision.models.resnet18
  Tutorial :	https://pytorch.org/tutorials/beginner/transfer_learning_tutorial.html

  ### Dataset
  
   ***Flower Dataset***

   Link :	http://www.robots.ox.ac.uk/~vgg/data/flowers/102/

  ### Image Augmentation and Regularization Technique

  Cut-out

  Main : https://paperswithcode.com/method/cutout
  Tutorial : https://github.com/uoguelph-mlrg/Cutout

  Discriminative Learning Rates

  Link : https://www.deeplearningwizard.com/deep_learning/boosting_models_pytorch/lr_scheduling/

## Code
  
  Code Explanation present in notebook 
  
  - To run the model with Cutout use resnet18_cutout.ipynb file
  - To run the mode without Cutout use resnet18.ipynb file

## Results

  ### Base Model
  
  
  
 ![Screenshot](https://github.com/9harshit/fellowshipai-resnet-challenge/blob/main/images/model_basic.png)
  
  ### Model with Discriminative Learning Rates

 ![Screenshot](https://github.com/9harshit/fellowshipai-resnet-challenge/blob/main/images/model_dlr.png)
  
   ### Model with Cut-out

  ![Screenshot](https://github.com/9harshit/fellowshipai-resnet-challenge/blob/main/images/model_cutout.jpg)
  
  ### Model with Cut-out and Discriminative Learning Rates

  ![Screenshot](https://github.com/9harshit/fellowshipai-resnet-challenge/blob/main/images/model_cutout_dlr.png)

