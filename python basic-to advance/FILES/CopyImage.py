#Program for Copying an Image (Binary File--denoated by a letter b)
#CopyImage.py
def imagecopyex():
    with open("D:\\KVR\\kvr.png","rb") as rp:
        with open("pythonfac.png","wb") as wp:
            imgdata=rp.read() # Read the Data from Souce File (Image)
            wp.write(imgdata) # write image data to Dest File
            print("Image Copied--verify")

#Main Program
imagecopyex() # Function Call


