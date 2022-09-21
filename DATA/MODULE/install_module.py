import os


def install_module():
    libs = {'--upgrade pip', "numpy", "tensorflow-gpu", "tensorflow", 'keras'}

    try:
        for lib in libs:
            print("start install {0}".format(lib))
            os.system(f"pip install {lib}")
            print("{} install successful".format(lib))
        print("All Successful")

    except:
        print("Failed SomeHow")