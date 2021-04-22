# Stackstorm
Repository for tips and learning [Stackstorm](https://stackstorm.com/) automation tool

## Using Docker Toolbox with VirtualBox on AMD CPU on Windows
When running Stackstorm with Docker on Windows with AMD CPU using the *old* [Docker Toolbox](https://github.com/docker/toolbox/releases/) with VirtualBox (instead of the new Docker Desktop), you may run into error when launching the **Docker Quickstart Terminal** tool the first time after installation:
```
Error with pre-create check: "This computer doesn't have VT-X/AMD-v enabled. Enabling it in the BIOS is mandatory"
```
This error occurs even though virtualization support *is* enabled in BIOS. To resolve the problem, open Administrator Powershell prompt and run:
```
docker-machine.exe create default --virtualbox-no-vtx-check
```
This generates the `default` Docker VirtualBox VM, which is used as the "base" for all of the Docker instances. You should now be able to run the Docker Quickstart Terminal or simply run Docker from other command prompt.

[Reference](https://forums.docker.com/t/error-with-pre-create-check-this-computer-doesnt-have-vt-x-amd-v-enabled-enabling-it-in-the-bios-is-mandatory-even-though-its-enabled/79541/3)

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
5. Open a web browser to `http://localhost:8080` and log in with user ID `st2admin` and password `Ch@ngeMe`. Likewise, you can run Stackstorm `st2` commands at the Docker command prompt.
6. To shut down the Docker instance, enter `exit` at the Docker command prompt and then run:
    ```bash
    docker-compose down
    ```

[Reference 1](https://docs.stackstorm.com/install/docker.html)  
[Reference 2](https://github.com/StackStorm/st2-docker/blob/master/README.md)


## Install a New Pack with Python Script Action in Stackstorm
To install a pack in Stackstorm (running in Docker), do the following.
1. Copy (or clone from repository) the pack into the `packs.dev` directory in `st2-docker` directory.
    _Note_: If you prefer to use pack code from another location, such as your "project" directory, you can set the **`ST2_PACKS_DEV`** environment variable to the desired directory path to use.
2. Launch Stackstorm as usual via the `launch_st2.sh` shell script (see above).
3. At the Stackstorm Docker shell prompt, navigate to the new pack directory and run these commands:
    ```bash
    st2 run packs.setup_virtualenv packs='packname' python3=true
    st2 run packs.load packs='packname' register=all
    ```
    Each command will produce some output, the most important of which is **`status: succeeded`**. The first command creates a new [Python virtual environment](https://docs.python.org/3/tutorial/venv.html) specific to Python 3. The second command registers your pack with Stackstorm.
4. To confirm that the new pack is now available, run:
    ```bash
    st2 action list --pack='packname'
    ```
    Stackstorm will display a tabular view of the actions with their descriptions in your new pack.
5. You can now run your new pack at the Docker command prompt or via the web GUI. For example, to execute the Action named [`hello_world_action`](https://github.com/TimothyDJones/stackstorm/blob/main/hello_world/actions/hello_world_action.py) in the [`hello_world`](https://github.com/TimothyDJones/stackstorm/tree/main/hello_world) pack which takes two string parameters `name` and `message`, we might run the following with the corresponding output:
    ```bash
    st2 run hello_world.hello_world_action name="Tim" message="This is a test."
    
    id: 5fa45949e1b2790677f9b699
    action.ref: hello_world.hello_world_action
    context.user: st2admin
    parameters: 
      message: This is a test.
      name: Tim
    status: succeeded
    start_timestamp: Thu, 05 Nov 2020 19:58:01 UTC
    end_timestamp: Thu, 05 Nov 2020 19:58:02 UTC
    result: 
      exit_code: 0
      result: This is a test.
      stderr: ''
      stdout: 'Hello, Tim!
        This is a test.
        '
    ```
    
[Reference](https://docs.stackstorm.com/actions.html)

## Add new user account for Stackstorm
To add new user account to your Stackstorm install, use the standard Linux [`htpasswd`](https://linux.die.net/man/1/htpasswd) utility referencing the Stackstorm `htpasswd` file, which is typically located in `/etc/st2` directory. For example:
```bash
sudo htpasswd -b /etc/st2/htpasswd username password
```



