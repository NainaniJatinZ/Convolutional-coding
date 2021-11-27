# Convolutional-Coding
Digital Communication Project, abstract: Implementation of  Convolutional Encoder and Decoder  for  2 Memory Unit and 2 Output Unit with a bit rate of 1/2. Also implementation of decoder using Viterbi Algorithm and 2-PAM modulation for bit transmission. 


## How to use

1. Clone the repository on your local device
2. Place the image you want to encode and decode in the "images" folder.
3. Change the ```path``` variable in ```data_handler.py``` to the path of your image and change the ```destination``` variable to where you want the .npy file to be. 
4. Copy this ```destination``` variable and paste it in cell with #CHANGE-THIS in ```conv-code.ipynb```. 
5. Keep on running each cell, and at the end you'll be able to see the result of error correction and accuracy.


## References

[Introduction to Convolution Codes](https://youtu.be/AnyVu5eDhAQ)

[Viterbi Decoding](https://youtu.be/z1MdvYu2ZHk)