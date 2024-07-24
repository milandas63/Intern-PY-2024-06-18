import matplotlib.pyplot as plt

def display_image_with_boxes(image):
    # Convert the image from BGR to RGB for display
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    plt.imshow(image_rgb)
    plt.axis('off')
    plt.show()
