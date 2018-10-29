# Set the base image to the base image
FROM hmlandregistry/dev_base_python_flask:3

RUN yum install -y geos

# ----
# Put your app-specific stuff here (extra yum installs etc).
# Any unique environment variables your config.py needs should also be added as ENV entries here

ENV APP_NAME=validation-api \
    SCHEMA_RELATIVE_DIRECTORY=schema \
    SCHEMA_FILENAME=local-land-charge.json \
    MAX_HEALTH_CASCADE=6 \
    MAX_NO_OF_EXTENTS=500 \
    SCHEMA_VERSIONS=v1_0,v2_0,v3_0,v4_0,v5_0,v6_0,v7_0

# ----

# The command to run the app is inherited from lr_base_python_flask

# Get the python environment ready.
# Have this at the end so if the files change, all the other steps don't need to be rerun. Same reason why _test is
# first. This ensures the container always has just what is in the requirements files as it will rerun this in a
# clean image.
ADD requirements_test.txt requirements_test.txt
ADD requirements.txt requirements.txt
RUN pip3 install -r requirements.txt && \
  pip3 install -q -r requirements_test.txt
