# README

### REQUIREMENTS:
1. Makefile
1. Docker
1. Dockercompose

### HOW TO START:
1. ```cd <project_root>```
1. ```make run```
1. ```make shell-django```
  1. ```python manage.py migrate```
  1. ```python manage.py runserver 0:8080```
  1. ```python manage.py createsuperuser```
1. In browser go to **localhost:8080/admin/** and create some **students** and **courses**

# API:
1. ```GET``` ```/report/<student_id>``` - return student report
1. ```GET``` ```/course/``` - return courses list
1. ```DELETE``` ```/patricipant/<student_id>```unassign student
1.```POST``` ```/create/```  assign  student

{
  course: number,
  student: number,
  completed: boolean(default=false)
}
```
