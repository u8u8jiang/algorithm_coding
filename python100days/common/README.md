
1. function.py   
    * def identity_function(x)    
    * def step_function(x)    
    * def sigmoid(x)    
    * def sigmoid_grad(x)    
    * def relu(x)    
    * def relu_grad(x)    
    * def softmax(x)    
    * def sum_squared_error(y, t)    
    * def cross_entropy_error(y, t)    
    * def softmax_loss(X, t)    

2. gradient.py   
    * def _numerical_gradient_1d(f, x)
    * def numerical_gradient_2d(f, X)
    * def numerical_gradient(f, x)

3. layers.py
    * class Relu    
    * class Sigmoid     
    * class Affine     
    * class SoftmaxWithLoss    
    * class Dropout    
    * class BatchNormalization     
    * class Convolution    
    * class Pooling    
* multi_layer_net.py   
* multi_layer_net_extend.py    

4. optimizer.py    
    * class SGD  
    * class Momentum  
    * class Nesterov  
    * class AdaGrad  
    * class RMSprop  
    * class Adam  
* trainer.py

5. util.py  
    * def smooth_curve(x)   
    * def shuffle_dataset(x, t)   
    * def conv_output_size(input_size, filter_size, stride=1, pad=0)   
    * def im2col(input_data, filter_h, filter_w, stride=1, pad=0)   
    