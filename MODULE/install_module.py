import os


def install_module():
    libs = {"numpy", "tensorflow-gpu", "tensorflow", 'keras', 'pandas'}

    try:
        for lib in libs:
            print("start install {0}".format(lib))
            os.system("pip install " + lib)
            print("{} install successful".format(lib))
        print("All Successful")

    except:
        print("Failed SomeHow")