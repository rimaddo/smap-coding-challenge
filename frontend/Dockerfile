FROM node:9

# set working directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# copy package.json into container
COPY package.json /usr/src/app/package.json

# add node modules bin to path
ENV PATH /usr/src/app/node_modules/.bin:$PATH

# install dependencies
RUN npm install
