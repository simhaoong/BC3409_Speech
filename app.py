#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import speech_recognition as sr


# In[2]:


app = Flask(__name__)


# In[ ]:


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        print("File Received")
        filename = secure_filename(file.filename)
        file.save(filename)
        a = sr.AudioFile(filename)
        with a as source:
            a = sr.Recognizer().record(source)
        s = sr.Recognizer().recognize_google(a)
        return(render_template("index.html", result=s))
    else:
        return(render_template("index.html", result="2"))
    
if __name__ == "__main__":
    app.run()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




