import matplotlib.pyplot as plt




    
def colorize_single_image(image_path, colorizator):
    
    image = plt.imread(image_path)
    colorizator.set_image(image, 576, True, 25)
    colorization=colorizator.colorize()
    # plt.imsave(save_path, colorization)
    
    return  colorization
    