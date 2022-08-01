#


### allowed_file
```python
.allowed_file(
   filename
)
```

---
Checks if the file has allowed extension.


**Args**

* **filename** (str) : The name of the file uploaded.


**Returns**

* **bool**  : True if the file is supported, false otherwise.


----


### get_faces
```python
.get_faces(
   img_path
)
```

---
Gets the lits of faces detected by MTCNN detector.


**Args**

* **img_path** (str) : The path to the image.


**Returns**

* **list**  : The list of faces bounding box coordinates.

