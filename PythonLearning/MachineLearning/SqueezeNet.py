import tensorflow as tf

class SqueezeNetModel:

    def __init__(self,original_dim,resize_dim,output_size):
        self.original_dim=original_dim
        self.resize_dim= resize_dim
        self.output_size=output_size


    def random_crop_and_flip(self,float_image):
        cropped_im = tf.image.random_crop(float_image,[self.resize_dim,self.resize_dim,1])
        return tf.image.random_flip_left_right(cropped_im)

    def image_preprocessing(self,data,is_training):
        reshaped_image=tf.reshape(data,[3,self.original_dim,self.original_dim])
        transposed_image= tf.transpose(reshaped_image,[1,2,0])
        float_image= tf.cast(transposed_image,tf.float32)
        if is_training:
            updated_image = self.random_crop_and_flip(float_image)
        else:
            updated_image= tf.image.resize_with_crop_or_pad(float_image,self.resize_dim,self.resize_dim)
        standardized_image = tf.image.per_image_standardization(updated_image)
        return standardized_image
