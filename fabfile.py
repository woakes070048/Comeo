from fabric.api import run, env


env.host_string = "root@comeo.org.md"


def deploy():
    stop()
    pull()
    build()
    start()


def pull():
    # Pull updates from the central repo
    run("cd /home/comeo_lab_env/comeo_project/ && git fetch --all && git reset --hard origin/lab_droplet")


def start():
    # start all docker-compose services
    # migrations will be applied before django starts up
    run("cd /home/comeo_lab_env/comeo_project/Docker/lab && make run-detached")


def build():
    # Rebuild django container, to install there new pip reqs
    run("cd /home/comeo_lab_env/comeo_project/Docker/lab && make build")


def stop():
    # Stop running containers
    run("cd /home/comeo_lab_env/comeo_project/Docker/lab && make stop")
