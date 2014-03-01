django-goskell (Go Skeleton, Go)
========

Django skeleton (based on 1.7a2) with:

 - django-pipeline
 - cssmin
 - jsmin


Development environment required
=======

 * python-3.3
 * virtualenv
 * fabric


Usage
=====

0. `django-admin.py startproject --template=https://github.com/gordio/django-goskel/zipball/master my_project`

0. Configure `settings_local.py` exmpl: `cp ./project_name/settings_local.py{_example,}`
1. `fab build` - build site environment
2. `fab run` or `fab run:0.0.0.0:8080` - run dev server
3. `fab manage:shell`, `fab manage:'dbshell -h'`, `fab manage:shell\ -h`, etc...


Tips & Tricks
=============

 * Install in venv - `./venv/bin/pip install <packet_name>`
 * Create locale file - `fab 'manage:makemessages -i venv -l ru'`
 * Update locale file - `fab 'manage:makemessages -i venv -a'`

 * Add local exclude (gitignore) patterns to .git/info/exclude OS's tmp files:

```
.DS_Store
.DS_Store?
.Spotlight-V100
.Trashes
ehthumbs.db
Thumbs.db
```
