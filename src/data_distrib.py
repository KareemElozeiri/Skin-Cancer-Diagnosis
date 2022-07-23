from email.mime import base
import shutil 
import os 

'''
a script to split data with the following counts for each class
train/validate/test : 700/350/350
'''

if __name__ == "__main__":

    base_dir = "../dataset/"

    all_data_dir = os.path.join(base_dir, "all_data")
    train_dir = os.path.join(base_dir, "train")
    test_dir = os.path.join(base_dir, "test")
    validate_dir = os.path.join(base_dir, "validate")
    
    train_benign_dir = os.path.join(train_dir,"benign")
    test_benign_dir = os.path.join(test_dir,"benign")
    validate_benign_dir = os.path.join(validate_dir,"benign")

    train_malignant_dir = os.path.join(train_dir,"malignant")
    test_malignant_dir = os.path.join(test_dir,"malignant")
    validate_malignant_dir = os.path.join(validate_dir,"malignant")



    #training images
    for i in range(1,701):
        src  = os.path.join(all_data_dir,f"benign/{i}.jpg")
        dst = os.path.join(train_benign_dir,f"{i}.jpg")
        shutil.copyfile(src, dst)
    for i in range(1,701):
        src  = os.path.join(all_data_dir,f"malignant/{i}.jpg")
        dst = os.path.join(train_malignant_dir,f"{i}.jpg")
        shutil.copyfile(src, dst)

    # #validation images
    for i in range(701,1051):
        src  = os.path.join(all_data_dir,f"benign/{i}.jpg")
        dst = os.path.join(validate_benign_dir,f"{i}.jpg")
        shutil.copyfile(src, dst)
    
    for i in range(789,1054):
        src  = os.path.join(all_data_dir,f"malignant/{i}.jpg")
        dst = os.path.join(validate_malignant_dir,f"{i-1}.jpg")
        shutil.copyfile(src, dst)

        
    #testing images
    for i in range(1054,1405):
        src  = os.path.join(all_data_dir,f"benign/{i}.jpg")
        dst = os.path.join(test_benign_dir,f"{i-1}.jpg")
        shutil.copyfile(src, dst)
    
    for i in range(1054,1405):
        src  = os.path.join(all_data_dir,f"malignant/{i-1}.jpg")
        dst = os.path.join(test_malignant_dir,f"{i-1}.jpg")
        shutil.copyfile(src, dst)


    print(f"Train Benign Count: {len(os.listdir(train_benign_dir))}")
    print(f"Validate Benign Count: {len(os.listdir(validate_benign_dir))}")
    print(f"Test Benign Count: {len(os.listdir(test_benign_dir))}")

    print(f"Train Malignant Count: {len(os.listdir(train_malignant_dir))}")
    print(f"Validate Malignant Count: {len(os.listdir(validate_malignant_dir))}")
    print(f"Test Malignant Count: {len(os.listdir(test_malignant_dir))}")    
