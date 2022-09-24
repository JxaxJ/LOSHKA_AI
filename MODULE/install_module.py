import os


def install_module():
    libs = {'--upgrade pip', "numpy==1.23.3", "tensorflow-gpu==2.9.1", "tensorflow==2.9.1", 'keras==2.9.0'}

    try:
        for lib in libs:
            print("start install {0}".format(lib))
            os.system(f"pip install {lib}")
            print("{} install successful".format(lib))
        print("All Successful")

    except:
        print("Failed SomeHow")
