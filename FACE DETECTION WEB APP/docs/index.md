# FACE DETECTION WEB APP

### Table of contents

- [1. Overview](#1-overview) <!-- omit in toc -->
  - [1.1. About the project](#11-about-the-project)
  - [1.2. Key features](#12-key-features)
  - [1.3. Technologies](#13-technologies)
  - [1.4. Properties](#14-properties)
- [2. Application](#2-application)
  - [2.1. Requirements](#21-requirements)
  - [2.2. Run the application](#22-run-the-application)
- [3. Documentation](#3-documentation)

### 1. Overview
#### 1.1. About the project

<p>This application allows multiple users simultaneously to upload images for face detection performed by MTCNN model. The system outputs the predicted faces by sending JSON message from the server to the client with bounding boxes coordinates. Operations are asynchronous without the need to reload the webpage. </p>


#### 1.2. Key features

- uploading images for face detection
- accessing the list of uploaded images
- removing the specified entry from the list
- managing multiple users
- displaying images with detected faces
- counting detected faces
- displaying the real-time active users count

#### 1.3. Technologies

|  |  |
| --- | --- |
| Flask | Flask-SocketIO, Flask-RESTful |
| Python 3.8.6 | MTCNN, Matplotlib Pyplot |
| JavaScript | |
| AJAX | |
| HTML5 | |
| Jinja2 ||
| CSS |
| Bootstrap |

#### 1.4. Properties

This application was developed according to REST (Representational state transfer) software architectural style.

Main properties implemented:
- client-server architecture
- resources specific identification
- unified interface
- use of self-decribing messages
- stateless interaction

The specific URI (URL) consists of a set of parameters which are transfered to the resource. This application is based on MIME type application/json resource representation.

HTTP protocol methods used: GET, POST, DELETE.



### 2. Application
#### 2.1. Requirements

Pipfile content:
[[source]]
- url = "https://pypi.org/simple"
- verify_ssl = true
- name = "pypi"

[packages]
- flask = "*"
- mtcnn = "*"
- matplotlib = "*"
- flask-restful = "*"
- flask-socketio = "*"

[dev-packages]
- mkdocs = "*"

[requires]
- python_version = "3.8.6"


#### 2.2. Run the application

The application can be run from the FACE DETECTION WEB APP/app.py file and navigating to the http://127.0.0.1:5000 in the browser.

Recommended browsers: Opera, Chrome.

### 3. Documentation

The project documentation can be accessed by
navigating to the project's root directory (\FACE DETECTION WEB APP) and in the command line running:

`mkdocs serve`

The documentation should be available here: http://127.0.0.1:8000