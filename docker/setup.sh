#!/bin/bash

# clone spyddder-man to be moved to its final location by docker builder
git clone https://github.com/hysds/spyddder-man.git

# clone slcp2pm to be moved to its final location by docker builder
git clone https://${GIT_OAUTH_TOKEN}@github.jpl.nasa.gov/aria-hysds/slcp2pm.git
