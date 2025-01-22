import cv2
import pytesseract
from PIL import Image

# Load image
image_path = "/Users/bhavjotsingh/Desktop/test-question.png"
img = cv2.imread(image_path)

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply thresholding
_, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)

# Save preprocessed image
processed_image_path = "processed_test_question.png"
cv2.imwrite(processed_image_path, thresh)

# Run OCR again
extracted_text = pytesseract.image_to_string(Image.open(processed_image_path))

print("Extracted Text:")
print(extracted_text)
