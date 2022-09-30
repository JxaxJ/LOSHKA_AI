import os

try:
    import tensorflow as tf
except:
    os.system('tensorflow==2.10.0')


def install_module():
    libs = {"numpy==1.23.3", 'keras==2.10.0'}
    os.system('pip install --upgrade pip')

    if not tf.config.list_physical_devices('GPU'):
        print('You don`t installed CUDA or CUDNN, installing tensorflow-gpu skipped')
        try:
            for lib in libs:
                print("start install {0}".format(lib))
                os.system(f"pip install {lib}")
                print("{} install successful".format(lib))
            print("All Successful")

        except:
            print("Failed SomeHow")

    else:
        try:
            for lib in libs:
                print("start install {0}".format(lib))
                os.system(f"pip install {lib}")
                print("{} install successful".format(lib))
            os.system('pip install tensorflow-gpu==2.10.0')
            print("All Successful")

        except:
            print("Failed SomeHow")