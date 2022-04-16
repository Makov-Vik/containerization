# containerization

## What is it?
The purpose of this work is to learn how to use docker. In this case, I wrote a Dickerfile for 3 different projects, one of which I came up with myself. Here the skills of writing a Dockerfile, running and building a docker project were improved.

## Usage
Шn order to use this code, you need to download this code file or clone this repository:
```
git clone https://github.com/Makov-Vik/containerization.git
```

Also, to run using docker, you must first download it. This can be done on the official [website][1]

### 1 - Python
To create a docker image, use the command:
```
docker build -f Dockerfile.1 -t your_name_image:01 .
```

To run an image:
```
docker run --rm -it -p 8080:8080 your_name_image:01
```

Also, to create an image according to Dockerfile.2, you need to insert it into the command:
```
docker build -f Dockerfile.2 -t your_name_image:02 .
```

To run an image:
```bash
docker run --rm -it -p 8080:8080 your_name_image:02
```

After launching the image, you can go to http://localhost:8080/matrix and verify the implementation of the multiplication of two matrices

### 2 - Go

To create a docker image, use the command:
```bash
docker build -f Dockerfile.1 -t your_name_image:01 .
```

To run an image:
```bash
docker run --rm -it -p 8080:8080 your_name_image:01
```

Just like with the case in python, to create a Dockerfile.2 image, you need to insert it into the command
```bash
docker build -f Dockerfile.2 -t your_name_image:02 .
```
Same with launch:
```bash
docker run --rm -it -p 8080:8080 your_name_image:02
```

In the same way, you can run the image with the third Dockerfile

## 3 - Node.js
In this case, the program can create fake data, which can be useful during the development phase.
If you have Node and npm installed, you can use the following command to run:
```bash
npm i 
node index.js
```

If you prefer to use Docker, then follow these commands:
```bash
docker build -f Dockerfile -t your_name_image:01 .
docker run --rm -it -p 8080:8080 your_name_image:01
```


[1]: https://www.docker.com/products/docker-desktop/