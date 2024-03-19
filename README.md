![Romarin Board Banner Image](/base_static/global/images/Githeader.jpg)
<h2 align='center'>Romarin</h2>

This project is a functional web applicaction in Python and Django. In this project there is a website where people can search for recipes by category or name of the recipe. Futhermore, there is a dashboard where we can add a recipe, update and/or delete them, that only will be published after consent of the administrators of the website


### Romarin Main Page
![Romarin main Image](/base_static/global/images/romarin_home.png)

### Romarin single recipe Page
![Romarin single_recipe Image](/base_static/global/images/single_recipe.png)

### Romarin dashboard Page
![Romarin dashboard Image](/base_static/global/images/romarin_dashboard.png)

### Usage

1. After cloning this repository, create a virtual environment and install the requirements listed in the 'requirements.txt' file:

```
pip install -r requirements.txt
```

2. In the file setting.py, configure the database settings.
3. Execute below commands:

```
python manage.py makemigrations
python manage.py migrate
```

4. Create superuser for admin access and follow instructions:

```
python manage.py createsuperuser
```

5. Running the tests
   
```
python manage.py runserver
```

### Tools
+ Django
+ Laragon
+ MySQL
+ Python
+ Html
+ CSS

### References
+ Images: unsplash.com
+ Recipes: allrecipes.com

