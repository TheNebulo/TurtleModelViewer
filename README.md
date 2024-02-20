# Turtle Model Viewer

![Wireframe of sample teapot object](https://i.ibb.co/7JcJkS5/image.png)

Visualises .obj files in 3D space using Turtle GUI.

## Features
- Vertex, Wireframe, and solid views
- Custom .obj file support
- Commented and explained files

## Usage
> Currently no user friendly menus are setup but will be soon. 

Firstly, make sure the dependencies are installed. (These are just math, turtle, and time.)
```bash
pip3 install -r requirements.txt
```

Next run main.py, and you should see the teapot show up.
```bash
python3 main.py
```

## Running custom colours and objects

For colour changes, go to line 7 and line 148 on main.py and change the line with the color wanted.
```python
t.color("colour of your choice")
```

As for object changes, firstly add the new .obj files into the same directory. 
The .obj files must fit the following criteria:
- Each line in the .obj file must start with either o, v, s, or f.
- For context, look at the teapot.obj file.

Then change lines 12 and 13 as follows
```python
verts = obj_interp.read_verts("name of .obj file (i.e. teapot.obj)")
faces = obj_interp.read_faces("name of .obj file (i.e. teapot.obj)")
```
## License

This project is available under the [CC0 license](https://creativecommons.org/publicdomain/zero/1.0/). Feel free to learn from it and incorporate it in your own projects.
