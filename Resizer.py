# import the necessary packages
def HeightMatters():

    import cv2

    image = cv2.imread("ttt\\2_Words.png")

    h,w,c = image.shape

    #how Xs
    times = 1 #(2* image.shape[1])/ image.shape[1] # r = the ratio of the new width to the old width
    dim = (int(times* image.shape[1]), int(image.shape[0] * times)) # image.shape[1] = width


    resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
    cv2.imwrite("ttt\\d_complex_one_15.png", resized)
