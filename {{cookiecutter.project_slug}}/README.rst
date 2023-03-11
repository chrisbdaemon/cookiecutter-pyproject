{% set is_open_source = cookiecutter.open_source_license != 'Not open source' -%}
{% for _ in cookiecutter.project_name %}={% endfor %}
{{ cookiecutter.project_name }}
{% for _ in cookiecutter.project_name %}={% endfor %}
{%- if cookiecutter.repo_host|lower == 'github.com' %}
{% set repo_name = "GitHub" %}
{%- else %}
{% set repo_name = "GitLab" %}
{%- endif %}

{% if is_open_source %}
.. image:: https://img.shields.io/pypi/v/{{ cookiecutter.project_slug }}.svg
        :target: https://pypi.python.org/pypi/{{ cookiecutter.project_slug }}

.. image:: https://img.shields.io/travis/{{ cookiecutter.repo_username }}/{{ cookiecutter.project_slug }}.svg
        :target: https://travis-ci.com/{{ cookiecutter.repo_username }}/{{ cookiecutter.project_slug }}

.. image:: https://readthedocs.org/projects/{{ cookiecutter.project_slug | replace("_", "-") }}/badge/?version=latest
        :target: https://{{ cookiecutter.project_slug | replace("_", "-") }}.readthedocs.io/en/latest/?version=latest
        :alt: Documentation Status
{%- endif %}

{% if cookiecutter.add_pyup_badge == 'y' %}
.. image:: https://pyup.io/repos/{{ repo_name|lower }}/{{ cookiecutter.repo_username }}/{{ cookiecutter.project_slug }}/shield.svg
     :target: https://pyup.io/repos/{{ repo_name|lower }}/{{ cookiecutter.repo_username }}/{{ cookiecutter.project_slug }}/
     :alt: Updates
{% endif %}


{{ cookiecutter.project_short_description }}

{% if is_open_source %}
* Free software: {{ cookiecutter.open_source_license }}
* Documentation: https://{{ cookiecutter.project_slug | replace("_", "-") }}.readthedocs.io.
{% endif %}

Features
--------

* TODO

Credits
-------

This package was created with Cookiecutter_ and the `chrisbdaemon/cookiecutter-pypackage`_ project template
which was derived from the `audreyr/cookiecutter-pypackage` template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`chrisbdaemon/cookiecutter-pypackage`: https://github.com/chrisbdaemon/cookiecutter-pypackage
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
