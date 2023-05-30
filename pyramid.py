import cv2

# Load the input image
# تصویر خود را بارگزاری میکنیم
image = cv2.imread('Image/DanialbartehNewProfile.Png')

# You can load another image
# شما میتوانید تصاویر دیگر رو اضافه بفرمائید
# image = cv2.imread('Image/Car.png')

# Define the scale factor for each level of the pyramid
# اسکیل فکتور را برای هر لول تعیین میکنیم
scale_factor = 0.8

# Initialize the list of pyramid images
# تصاویر را طبقه بندی میکنیم
pyramid_images = [image]

# We go to different levels and implement the pyramid
# در سطح های مختلف میرویم و پیرامید را پیاده سازی میکنیم
for i in range(1, 10):
    # Resize the previous level image
    # اندازه تصویر قبلی را تغییر میدهیم
    previous_level = pyramid_images[i - 1]
    new_size = (int(previous_level.shape[1] * scale_factor), int(previous_level.shape[0] * scale_factor))
    resized = cv2.resize(previous_level, new_size)

    # Add the resized image to the pyramid
    # اندازه تصویر را به پیرامید اضافه میکنیم
    pyramid_images.append(resized)

    # Display the current level of the pyramid (In Title)
    # لول پیرامید را به کاربر نمایش میدهیم (در Title)
    cv2.imshow(f'Level {i}', resized)
    cv2.waitKey(0)

cv2.destroyAllWindows()
