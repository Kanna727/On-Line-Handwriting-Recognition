# On-Line Handwriting Recognition
Recognizing what user writes on screen using SVM and scikit-learn

> _A minor project being done by a team from NIT Patna._

This Project aims towords online character recognition, using machine learning, for the most widely
used Indic script-Devanagari. It focuses on GUI development for input, its pre-processing and feature
extraction. The input characters are fed by the users, using finger or stylus, in an application of hand-held
smart devices like mobile phones and tablets, which operate on Android as the interface. The recognition
model is made compatible with Android with use of TensorFlow. Each coordinate of the screen touched
the user is captured. These coordinates undergo several pre-processing techniques after which the
recognition process starts. Each input is identified as a combination of several strokes. Each stroke is
further divided into local areas called zones. Each zone comes out with its values of several features for
the input coordinates lying in that zone. The dataset is prepared for training the machine learning model
based on these feature values.

#### TEAM:
- [Prasanth Kanna](chitturiprasanth13797@gmail.com)
- [Shruti Mary](smary25dec@gmail.com)
- [Karthik Thakur](iamkarthik08@gmail.com)
- [Priyusha Reddy](priyusha825@gmail.com)

#### COORDINATOR:
- Prof. Rajib Ghosh
