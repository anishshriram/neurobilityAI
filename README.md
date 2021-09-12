# neurobilityAI

### Inspiration
I love working with AI and neural networks, but there is no real application for them if people are not able to easily reap their benefits. The AbilityHacks hackathon, one designed to promote innovations that support people with disabilities, provided the push to develop an application that incorporated AI. 

I have a lot of close relationships with people with learning disablities, and as such I wanted to create someething to help them. The goal of this project was to write a neural network that would benefit either an individual with a learning disability (most specifically dysgraphia or dyslexia), or an educator working with people with learning disabilities, and create a web app based on that.

### Overview
NeurobilityAI uses a basic deep neural network trained off of the MNIST dataset to recognize handwritten digits. Essentially, my web app can take in a 'png' image of a handwritten digit, and then predict what that digit is. 

There are two pathways I see this assisting those with disabilities. 

1. Many people with dyslexia and dysgraphia find an issue with non-uniformity in text and other writing materials. Though it is not the perfect solution, converting handwritten learning materials into uniform, computer generated, digits would help in understanding material.
2. Educators working with people who have dysgraphia can find analyzing work and providing feedback difficult. By converting unclear handwritten information into clear computer generated text can help teachers with this issue.

### How it works
I used TensorFlow and Keras libraries to assist me with my deep learning model. The actual model is quite simple:

```python
model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(512, activation=tf.nn.relu),
    tf.keras.layers.Dense(10, activation=tf.nn.softmax)
])
```
I also used Flask to host both my web app and my web service.

- Flask - Microframework for python (a very minimal web application framework, or software that supports web app development)

###### Web App vs Web Service
Web application (the web page) gets data, then it sends the data to the web service (backend), which then uses that information for whatever processes it needs to complete, then it sends it back to the frontend application.

### Challenges Faced, What's Next, What Did I Learn?
First of all, I think it is important to know that prior to this experience, I had NO experience constructing web applications, flask, HTTP, or anything of the sort. I think it is impressive how much I got done and learned in the short period I did this project (only took around 4, 5 hours).
I had a LOT of challenges getting the model to actually take in the images, and preprocessing them. I had quite a bit of challenges figuring out flask. I give a lot of credit to their documentation page, reading up helped me a lot.

I think what I created was impressive given the circumstances...but I have a lot to work on. 
1. Creating a more friendly UI/UX would be top of my list...the site is veryyy basic
2. Incorporating some of my more complicated neural networks would also be a good thing to do. Because of the short time I only did a very simple one. 
3. Creating more functionality to make my site more inclusive for a wider range of people. I am sure I can create something to help people with a wider range of learning disabilities, and I hope to do so soon!

### Important Notes
My code is HEAVILY commented. Feel free to go through everything and learn more in detail about what I did. A video description will be attached on my devpost project submission.
