import tensorflow as tf
from keras import Model
from keras.layers import SeparableConv2D,Conv2D, MaxPooling2D, Dropout
from keras.layers import Conv2DTranspose, concatenate
from keras.layers import Input

#======================================================================================

# Encoder
# Work as Feature Extractor
def conv2d_block(input_tensor, n_filters, kernel_size=3):
    # 2 Convs 
    x = input_tensor
    for i in range(2):
        x = Conv2D(filters=n_filters, kernel_size=kernel_size,
                   kernel_initializer='he_normal', activation='relu', padding='same')(x)
    return x
 
def encoder_layer(inputs, n_filters=64, pool_size=(2,2)):
    # Encoder of 1 Layer     
    conv = conv2d_block(inputs, n_filters)
    pull = MaxPooling2D(pool_size=pool_size)(conv)
    pull = Dropout(0.2)(pull)
 
    return conv, pull
 
def encoder(inputs):
    # # Full Encoder    
    # conv1, pull1 = encoder_layer(inputs, n_filters=64)
    # conv2, pull2 = encoder_layer(pull1, n_filters=128)
    # conv3, pull3 = encoder_layer(pull2, n_filters=256)
    # conv4, pull4 = encoder_layer(pull3, n_filters=512)
 
    # return pull4, (conv1, conv2, conv3, conv4)
    
    conv1, pull1 = encoder_layer(inputs, n_filters=64)
    conv2, pull2 = encoder_layer(pull1, n_filters=128)
    conv3, pull3 = encoder_layer(pull2, n_filters=256)
 
    return pull3, (conv1, conv2, conv3)

#======================================================================================

# BottleNeck
def bottleneck(inputs):
    # bottle_neck = conv2d_block(inputs, n_filters=1024)
    # return bottle_neck
    
    bottle_neck = conv2d_block(inputs, n_filters=512)
    return bottle_neck

#======================================================================================

# Decoder(Skip Connection)
# Work as Segmentation
def decoder_layer(inputs, conv_output, n_filters=64, kernel_size=3, strides=3):
    # Decoder of 1 Layer
    # Transpose Convolution(Up Convolution)
    upconv = Conv2DTranspose(n_filters, kernel_size, strides, padding='same')(inputs)
    conv = concatenate([upconv, conv_output])
    conv = Dropout(0.2)(conv)
    conv = conv2d_block(conv, n_filters)
 
    return conv

def decoder(inputs, convs, output_channels):
    # # Full Decoder 
    # conv1, conv2, conv3, conv4 = convs
    
    # conv6 = decoder_layer(inputs, conv4, n_filters=512, kernel_size=3, strides=2)
    # conv7 = decoder_layer(conv6,  conv3, n_filters=256, kernel_size=3, strides=2)
    # conv8 = decoder_layer(conv7,  conv2, n_filters=128, kernel_size=3, strides=2)
    # conv9 = decoder_layer(conv8,  conv1, n_filters=64,  kernel_size=3, strides=2)

    # outputs = tf.keras.layers.Conv2D(output_channels, 1, activation='softmax')(conv9)
 
    # return outputs
    
    conv1, conv2, conv3 = convs
    
    conv7 = decoder_layer(inputs, conv3, n_filters=256, kernel_size=3, strides=2)
    conv8 = decoder_layer(conv7,  conv2, n_filters=128, kernel_size=3, strides=2)
    conv9 = decoder_layer(conv8,  conv1, n_filters=64,  kernel_size=3, strides=2)

    outputs = tf.keras.layers.Conv2D(output_channels, 1, activation='softmax')(conv9)
 
    return outputs

#======================================================================================

# putting it all together 
def UNet(img_size, OUTPUT_CHANNEL):
    # Full UNet 
    inputs = Input(shape=(img_size[0],img_size[1],3,))
 
    encoder_output, convs = encoder(inputs)
    bottle_neck = bottleneck(encoder_output)
    outputs = decoder(bottle_neck, convs, OUTPUT_CHANNEL)
 
    model = Model(inputs, outputs)
    model.summary()
 
    return model