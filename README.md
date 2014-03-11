[![Build Status](https://travis-ci.org/gordio/gordio-site.png?branch=master)](https://travis-ci.org/gordio/gordio-site)


Installing
==========

```
fab build
fab 'manage:loaddata flatpages.json'
```


Development environment required
=======

 * python-3.3
 * virtualenv
 * fabric


Usage
=====

0. Configure `settings_local.py` exmpl: `cp ./project_name/settings_local{_example,}.py`
1. `fab build` - build site environment
2. `fab run` or `fab run:0.0.0.0:8080` - run dev server
3. `fab manage:shell`, `fab manage:'dbshell -h'`, `fab manage:shell\ -h`, etc...
