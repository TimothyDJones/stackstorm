# stackstorm
Repository for tips and learning Stackstorm automation tool

## Stackstorm Setup Using Docker
To start using Stackstorm with Docker.
1. Install [Docker](https://www.docker.com/get-started) according to the standard Docker [installation process](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-20-04). You will need the [Docker Compose](https://docs.docker.com/compose/) utility, as well. In Linux, ensure that your user account is a member of the `docker` group.
2. Clone the Stackstorm Docker repository and change to that directory.
    ```bash
    git clone https://github.com/stackstorm/st2-docker
    cd st2-docker
    ```
    **Note**: On **Windows** hosts, Docker has problems with line endings in the scripts in the **`st2-docker\scripts`** directory. You will need to change them to Unix format (*LF only*). You can do this in [Notepad++](https://notepad-plus-plus.org/) via the *Edit* --> *EOL Conversion* --> *Unix LF* menu option. (Alternately, the [medit](http://mooedit.sourceforge.net/) text editor also supports line-ending editing, as well.)
3. Create a `launch_st2.sh` shell script with the following contents and make it executable.
    ```bash
    #!/usr/bin/env sh
    export ST2_VERSION=3.2.0
    export ST2_EXPOSE_HTTP=127.0.0.1:8080
    docker-compose up -d
    docker-compose exec st2client bash
    ```
4. In the `st2-docker` directory, launch the Stackstorm application.
    ```bash
    launch_st2.sh
    ```
5. Open a web browser to `http:\\localhost:8080` and log in with user ID `st2admin` and password `Ch@ngeMe`.

[Reference 1](https://docs.stackstorm.com/install/docker.html)
[Reference 2](https://github.com/StackStorm/st2-docker/blob/master/README.md)



