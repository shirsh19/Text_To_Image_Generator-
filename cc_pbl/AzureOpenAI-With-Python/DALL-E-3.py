import os
import httpx
from openai import AzureOpenAI
from PIL import Image
import os

client = AzureOpenAI(
    api_version="2024-02-01",  
    api_key= "D4rpkVYXR4zT09sV2nOBIrwrTU0tyR92L1ej1gBVjfTgbq52AYHeJQQJ99BDACfhMk5XJ3w3AAAAACOG99ga",  
    azure_endpoint="https://rajsh-m9on6bbo-swedencentral.cognitiveservices.azure.com/openai/deployments/dall-e-3/images/generations?api-version=2024-02-01"
)
            
result = client.images.generate(
    model="dalle3", # the name of your DALL-E 3 deployment
    prompt="Students gpomg to a collage named bharti vidyapeeth",
    n=1
 )
            
# Set the directory for the stored image
image_dir = os.path.join(os.curdir, 'images')
            
# If the directory doesn't exist, create it
if not os.path.isdir(image_dir):
    os.mkdir(image_dir)
            
# Initialize the image path (note the filetype should be png)
image_path = os.path.join(image_dir, 'generated_image.png')
           
# Retrieve the generated image
image_url = result.data[0].url  # extract image URL from response
generated_image = httpx.get(image_url).content  # download the image
with open(image_path, "wb") as image_file:
    image_file.write(generated_image)
            
# Display the image in the default image viewer
image = Image.open(image_path)
image.show()